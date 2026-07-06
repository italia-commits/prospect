"""Customer and billing models."""

import enum
import uuid
from datetime import datetime
from sqlalchemy import String, Text, Boolean, DateTime, Float, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.database import Base


class CustomerPlan(str, enum.Enum):
    starter = "starter"
    growth = "growth"
    scale = "scale"
    enterprise = "enterprise"


class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    company_name: Mapped[str] = mapped_column(String(255), nullable=False)
    contact_email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    contact_name: Mapped[str] = mapped_column(String(255), nullable=False)
    plan: Mapped[CustomerPlan] = mapped_column(
        Enum(CustomerPlan), default=CustomerPlan.starter, nullable=False
    )
    stripe_customer_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    stripe_subscription_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    monthly_prospect_limit: Mapped[int] = mapped_column(default=500, nullable=False)
    prospects_used_this_month: Mapped[int] = mapped_column(default=0, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    onboarded_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )

    # Relationships
    campaigns = relationship("Campaign", back_populates="customer", cascade="all, delete-orphan")
    prospects = relationship("Prospect", back_populates="customer", cascade="all, delete-orphan")
    meetings = relationship("Meeting", back_populates="customer", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Customer {self.company_name} ({self.plan})>"