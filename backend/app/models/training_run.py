from __future__ import annotations
import uuid
from datetime import datetime
from sqlalchemy import (
    UUID,
    DateTime,
    Enum as SQLEnum,
    ForeignKey,
    Text,
    Float,
    Integer
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.extensions import db
from app.enums.training_run_status import TrainingRunStatus


class TrainingRun(db.Model):

    __tablename__ = "training_runs"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    experiment_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("experiments.id"),
        nullable=False
    )

    status: Mapped[TrainingRunStatus] = mapped_column(
        SQLEnum(TrainingRunStatus),
        nullable=False,
        default=TrainingRunStatus.CREATED
    )

    started_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    error_message: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )

    test_size: Mapped[float] = mapped_column(
        Float,
        nullable=False,
        default=0.20
    )
    
    random_seed: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=42
    )

    experiment = relationship(
        "Experiment",
        back_populates="training_runs"
    )

    result = relationship(
    "TrainingRunResult",
    back_populates="training_run",
    uselist=False
)