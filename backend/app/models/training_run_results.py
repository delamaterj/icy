from __future__ import annotations
import uuid
from datetime import datetime
from sqlalchemy import UUID, DateTime, Float, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.extensions import db

class TrainingRunResult(db.Model):

    __tablename__ = "training_run_results"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    training_run_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("training_runs.id"),
        nullable=False,
        unique=True
    )

    accuracy: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    precision: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    recall: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    f1_score: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    confusion_matrix: Mapped[list] = mapped_column(
        JSON,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )

    training_run = relationship(
        "TrainingRun",
        back_populates="result"
    )