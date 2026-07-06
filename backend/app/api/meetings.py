"""Meeting API routes."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_meetings(customer_id: str | None = None, status: str | None = None):
    """List booked meetings, optionally filtered."""
    return {"meetings": []}


@router.get("/{meeting_id}")
async def get_meeting(meeting_id: str):
    """Get a meeting by ID."""
    return {"meeting_id": meeting_id}


@router.post("/{meeting_id}/confirm")
async def confirm_meeting(meeting_id: str):
    """Confirm a scheduled meeting."""
    return {"meeting_id": meeting_id, "status": "confirmed"}


@router.post("/{meeting_id}/cancel")
async def cancel_meeting(meeting_id: str):
    """Cancel a scheduled meeting."""
    return {"meeting_id": meeting_id, "status": "cancelled"}