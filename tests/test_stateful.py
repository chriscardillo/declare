import pytest
import uuid
from declare import Stateful

@pytest.fixture
def stateful():
    return Stateful("app")

def test_stateful_name(stateful):
    assert stateful.name == "app"

def test_controller_has_uuid(stateful):
    assert isinstance(stateful.uuid, uuid.UUID)
