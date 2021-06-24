def test_ping(test_app):
    responce = test_app.get("/debug/ping")
    assert responce.status_code == 200
    assert responce.json() == {"ping": "pong!"}
