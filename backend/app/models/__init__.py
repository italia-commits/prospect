"""SQLAlchemy ORM models for ProspectPilot AI.

All domain entities mapped to PostgreSQL tables.
"""

from app.models.customer import Customer, CustomerPlan
from app.models.campaign import Campaign, CampaignStatus
from app.models.prospect import Prospect, ProspectStatus
from app.models.interaction import Interaction, InteractionDirection, InteractionType
from app.models.meeting import Meeting, MeetingStatus

__all__ = [
    "Customer",
    "CustomerPlan",
    "Campaign",
    "CampaignStatus",
    "Prospect",
    "ProspectStatus",
    "Interaction",
    "InteractionDirection",
    "InteractionType",
    "Meeting",
    "MeetingStatus",
]