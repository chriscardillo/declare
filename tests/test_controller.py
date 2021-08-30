import pytest
import uuid
from declare import Controller

@pytest.fixture
def controller():
    return Controller("app")

def test_controller_name(controller):
    assert controller.name == "app"

def test_controller_has_uuid(controller):
    assert isinstance(controller.uuid, uuid.UUID)
