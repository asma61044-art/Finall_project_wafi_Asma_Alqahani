from typing import Protocol

from wafi.domain.models import Decision, Ticket
from wafi.domain.policy import decide


class TicketModel(Protocol):
    def warmup(self) -> None: ...
    def predict(self, ticket: Ticket) -> Decision: ...


class RuleBasedTicketModel:
    def __init__(self) -> None:
        self.ready = False

    def warmup(self) -> None:
        self.ready = True

    def predict(self, ticket: Ticket) -> Decision:
        if not self.ready:
            raise RuntimeError("model is not warmed up")
        return decide(ticket)
