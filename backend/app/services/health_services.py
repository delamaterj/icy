from datetime import datetime, timezone


class HealthService:

    def get_health(self):

        return {
            "status": "healthy",
            "service": "ICY Backend",
            "version": "0.1.0",
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }