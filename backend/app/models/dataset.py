from __future__ import annotations
import uuid
from datetime import datetime, timezone
from sqlalchemy import UUID, DateTime, Integer, String, BigInteger, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column
from app.extensions import db
from app.enums.dataset_status import DatasetStatus
from app.enums.file_type import FileType


class Dataset(db.Model):
    __tablename__ = "datasets"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    original_filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    stored_filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    file_path: Mapped[str] = mapped_column(
        String(512),
        nullable=False
    )

    file_size_bytes: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False
    )
    checksum: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
        unique=True
    )   
    file_type: Mapped[FileType] = mapped_column(
        SQLEnum(FileType),
        nullable=False
    )

    row_count: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )
    column_count: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    status: Mapped[DatasetStatus] = mapped_column(
        SQLEnum(DatasetStatus),
        nullable=False,
        default=DatasetStatus.UPLOADED
    )

    version: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=1
    )

    uploaded_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc)
    )