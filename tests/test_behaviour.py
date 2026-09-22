import json
from pathlib import Path

from wafi.adapters.model import RuleBasedTicketModel
from wafi.domain.models import Ticket, Urgency


def real_model() -> RuleBasedTicketModel:
    model = RuleBasedTicketModel()
    model.warmup()
    return model


def test_invariance_real_model():
    model = real_model()
    a = model.predict(Ticket("1", "VPN is slow"))
    b = model.predict(Ticket("2", "vpn IS SLOW"))
    assert (a.team, a.urgency) == (b.team, b.urgency)


def test_directional_real_model():
    model = real_model()
    normal = model.predict(Ticket("1", "minor delay"))
    outage = model.predict(Ticket("2", "All users cannot access the service"))
    assert outage.urgency is Urgency.URGENT
    assert outage.urgency != normal.urgency


def test_golden_reference_real_model():
    model = real_model()
    cases = json.loads(Path(__file__).with_name("golden.json").read_text())
    actual = []
    for case in cases:
        d = model.predict(Ticket(case["ticket_id"], case["text"]))
        actual.append(
            {
                "ticket_id": case["ticket_id"],
                "text": case["text"],
                "team": d.team,
                "urgency": d.urgency.value,
            }
        )
    assert actual == cases
