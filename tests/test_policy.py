from wafi.domain.models import Ticket, Urgency
from wafi.domain.policy import decide


def test_low():
    r = decide(Ticket("1", "Need a new monitor"))
    assert r.team == "hardware" and r.urgency == Urgency.LOW


def test_medium():
    r = decide(Ticket("2", "VPN is slow"))
    assert r.team == "network" and r.urgency == Urgency.MEDIUM


def test_outage():
    r = decide(Ticket("3", "All users cannot access the service"))
    assert r.urgency == Urgency.URGENT


def test_unknown():
    assert decide(Ticket("4", "Please advise")).team == "service-desk"
