"""Tests contre un vrai Redis. Lancer avec : pytest -m integration"""

import pytest
from fastapi.testclient import TestClient

from app import main

pytestmark = pytest.mark.integration


def test_compteur_avec_vrai_redis():
    main.r.delete("visites")
    client = TestClient(main.app)
    assert client.get("/").json() == {"visites": 1}
    assert client.get("/health").status_code == 200
