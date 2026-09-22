import pytest
from wafi.adapters.model import RuleBasedTicketModel
from wafi.domain.models import Ticket

def test_requires_warmup():
    with pytest.raises(RuntimeError):
        RuleBasedTicketModel().predict(Ticket("1","wifi issue"))

def test_after_warmup():
    m=RuleBasedTicketModel(); m.warmup()
    assert m.predict(Ticket("1","wifi issue")).team=="network"
