from __future__ import annotations
import uuid
from datetime import datetime
from sqlalchemy import UUID, DateTime, String, Enum as SQLEnum, ForeignKey, Text, Float, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column
from app.extensions import db
from app.enums.experiment_status import ExperimentStatus
from app.enums.experiment_model import ExperimentModel

class Experiment(db.Model):

    __tablename__ = "experiments"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    dataset_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("datasets.id"),
        nullable=False
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    status: Mapped[ExperimentStatus] = mapped_column(
        SQLEnum(ExperimentStatus),
        nullable=False,
        default=ExperimentStatus.CREATED
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )

    model: Mapped[ExperimentModel] = mapped_column(
        SQLEnum(ExperimentModel),
        nullable=False
    )

    target_column: Mapped[str] = mapped_column(
        String(255),
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

    dataset = relationship(
        "Dataset",
        back_populates="experiments"
    )