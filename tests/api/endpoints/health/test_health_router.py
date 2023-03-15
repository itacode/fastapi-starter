from app.api.endpoints.health.health_router import get_health


class TestHealthRouter:
    def test_get_health(self):
        assert get_health() == "OK"
