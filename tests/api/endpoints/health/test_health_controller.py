from app.api.endpoints.health.health_router import read_health


class TestHealthRouter:
    def test_read_health(self):
        assert read_health() == "OK"
