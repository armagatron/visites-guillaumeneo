import redis


def test_root_incremente_le_compteur(client):
    assert client.get("/").json() == {"visites": 1}
    assert client.get("/").json() == {"visites": 2}


def test_health_ok(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_health_redis_down(client, monkeypatch):
    from app import main

    def panne():
        raise redis.exceptions.ConnectionError("simulée")

    monkeypatch.setattr(main.r, "ping", panne)
    response = client.get("/health")
    assert response.status_code == 503


def test_metrics_expose_les_compteurs(client):
    client.get("/")
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "http_requests_total" in response.text
    assert "http_request_duration_seconds" in response.text
