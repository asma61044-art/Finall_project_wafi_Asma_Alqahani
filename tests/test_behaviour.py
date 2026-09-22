import json
from pathlib import Path
from wafi.domain.models import Ticket
from wafi.domain.policy import decide

def test_invariance():
    a=decide(Ticket("1","VPN is slow")); b=decide(Ticket("2","vpn IS SLOW"))
    assert (a.team,a.urgency)==(b.team,b.urgency)

def test_directional():
    normal=decide(Ticket("1","minor delay"))
    outage=decide(Ticket("2","All users cannot access the service"))
    assert outage.urgency.value=="urgent"
    assert outage.urgency != normal.urgency

def test_golden():
    cases=json.loads(Path("tests/golden.json").read_text())
    actual=[]
    for x in cases:
        d=decide(Ticket(x["ticket_id"],x["text"]))
        actual.append({"ticket_id":x["ticket_id"],"text":x["text"],"team":d.team,"urgency":d.urgency.value})
    assert actual==cases
