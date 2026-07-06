"""Campaign API routes."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_campaigns(customer_id: str | None = None):
    """List campaigns, optionally filtered by customer."""
    return {"campaigns": []}


@router.post("/")
async def create_campaign():
    """Create a new outreach campaign."""
    return {"message": "Not yet implemented"}


@router.get("/{campaign_id}")
async def get_campaign(campaign_id: str):
    """Get a campaign by ID."""
    return {"campaign_id": campaign_id}


@router.put("/{campaign_id}")
async def update_campaign(campaign_id: str):
    """Update a campaign."""
    return {"campaign_id": campaign_id}


@router.post("/{campaign_id}/activate")
async def activate_campaign(campaign_id: str):
    """Activate a campaign to start the agent pipeline."""
    return {"campaign_id": campaign_id, "status": "activating"}


@router.post("/{campaign_id}/pause")
async def pause_campaign(campaign_id: str):
    """Pause an active campaign."""
    return {"campaign_id": campaign_id, "status": "pausing"}