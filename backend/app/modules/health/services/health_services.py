from datetime import datetime, timezone
from app.database.health import check_database_health


class HealthService:

    def get_health(self):

        database_connected = check_database_health()

        return {
           "status": "healthy" if database_connected else "degraded",
            "database": "connected" if database_connected else "disconnected",
            "version": "0.1.0",
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }