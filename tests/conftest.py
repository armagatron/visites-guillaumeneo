import fakeredis
import pytest
from fastapi.testclient import TestClient

from app import main


@pytest.fixture
def client(monkeypatch):
    """Client de test branché sur un faux Redis en mémoire (aucun Docker requis)."""
    fake = fakeredis.FakeRedis(decode_responses=True)
    monkeypatch.setattr(main, "r", fake)
    return TestClient(main.app)
