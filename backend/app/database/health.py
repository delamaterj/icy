from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.extensions import db


def check_database_health() -> bool:
    """
    Executes a lightweight query to verify database connectivity.
    Returns True if the database is reachable, otherwise False.
    """

    try:
        db.session.execute(text("SELECT 1"))
        return True

    except SQLAlchemyError:
        return False