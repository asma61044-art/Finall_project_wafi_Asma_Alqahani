import logging
from contextlib import asynccontextmanager
from uuid import uuid4
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from wafi.adapters.model import RuleBasedTicketModel
from wafi.api.logging import configure
from wafi.api.schemas import PredictRequest, PredictResponse, response
from wafi.api.settings import Settings
from wafi.domain.models import Ticket
from wafi.service.predict import PredictionService

settings = Settings()
configure(settings.log_level)
logger = logging.getLogger("wafi")
model = RuleBasedTicketModel()
service = PredictionService(model)

@asynccontextmanager
async def lifespan(_: FastAPI):
    model.warmup()
    yield

app = FastAPI(title="Wafi", version="1.0.0", lifespan=lifespan)

@app.middleware("http")
async def trace(request: Request, call_next):
    tid = request.headers.get("X-Trace-ID") or str(uuid4())
    request.state.trace_id = tid
    result = await call_next(request)
    result.headers["X-Trace-ID"] = tid
    return result

@app.get("/health")
def health() -> dict[str,str]:
    return {"status":"alive"}

@app.get("/ready")
def ready():
    if not model.ready:
        return JSONResponse(status_code=503, content={"status":"not_ready"})
    return {"status":"ready"}

@app.post("/v1/predict", response_model=PredictResponse)
def predict(request: Request, payload: PredictRequest) -> PredictResponse:
    tid = request.state.trace_id
    d = service.predict(Ticket(payload.ticket_id, payload.text))
    logger.info("prediction_created", extra={"trace_id":tid})
    return response(tid, payload.ticket_id, d)
