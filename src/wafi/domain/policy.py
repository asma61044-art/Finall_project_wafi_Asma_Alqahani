from wafi.domain.models import Decision, Ticket, Urgency

TEAM_KEYWORDS = {
    "network": ("vpn","network","wifi","internet","dns","router"),
    "identity": ("password","login","account","mfa","authentication"),
    "application": ("application","app","portal","software","error"),
    "hardware": ("laptop","monitor","keyboard","mouse","printer"),
}
OUTAGE = ("full service outage","service is down for everyone","all users cannot access","everyone cannot access")

def decide(ticket: Ticket) -> Decision:
    text = ticket.text.strip().lower()
    team = _team(text)
    if any(x in text for x in OUTAGE):
        return Decision(team, Urgency.URGENT, "full-service outage indicator detected")
    if any(x in text for x in ("urgent","critical","blocked")):
        urgency = Urgency.URGENT
    elif any(x in text for x in ("slow","intermittent","delay")):
        urgency = Urgency.MEDIUM
    else:
        urgency = Urgency.LOW
    return Decision(team, urgency, "standard keyword policy")

def _team(text: str) -> str:
    for team, words in TEAM_KEYWORDS.items():
        if any(w in text for w in words):
            return team
    return "service-desk"
