from pydantic import BaseModel, ConfigDict, Field

from wafi.domain.models import Decision


class PredictRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    ticket_id: str = Field(min_length=1, max_length=64)
    text: str = Field(min_length=3, max_length=1000)


class PredictResponse(BaseModel):
    trace_id: str
    ticket_id: str
    team: str
    urgency: str
    reason: str


def response(trace_id: str, ticket_id: str, d: Decision) -> PredictResponse:
    return PredictResponse(
        trace_id=trace_id,
        ticket_id=ticket_id,
        team=d.team,
        urgency=d.urgency.value,
        reason=d.reason,
    )
