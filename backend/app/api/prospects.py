"""Prospect API routes."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_prospects(campaign_id: str | None = None, status: str | None = None):
    """List prospects, optionally filtered."""
    return {"prospects": []}


@router.get("/{prospect_id}")
async def get_prospect(prospect_id: str):
    """Get a prospect by ID."""
    return {"prospect_id": prospect_id}


@router.post("/{prospect_id}/enrich")
async def enrich_prospect(prospect_id: str):
    """Trigger AI enrichment/research for a prospect."""
    return {"prospect_id": prospect_id, "status": "enriching"}


@router.post("/{prospect_id}/disqualify")
async def disqualify_prospect(prospect_id: str):
    """Disqualify a prospect."""
    return {"prospect_id": prospect_id, "status": "disqualified"}