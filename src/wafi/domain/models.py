from dataclasses import dataclass
from enum import Enum


class Urgency(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    URGENT = "urgent"


@dataclass(frozen=True)
class Ticket:
    ticket_id: str
    text: str


@dataclass(frozen=True)
class Decision:
    team: str
    urgency: Urgency
    reason: str
