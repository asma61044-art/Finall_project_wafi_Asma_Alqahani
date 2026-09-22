from wafi.adapters.model import TicketModel
from wafi.domain.models import Decision, Ticket

class PredictionService:
    def __init__(self, model: TicketModel) -> None:
        self.model = model
    def predict(self, ticket: Ticket) -> Decision:
        return self.model.predict(ticket)
