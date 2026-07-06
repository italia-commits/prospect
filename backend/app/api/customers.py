"""Customer API routes."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_customers():
    """List all customers."""
    return {"customers": []}


@router.post("/")
async def create_customer():
    """Create a new customer."""
    return {"message": "Not yet implemented"}


@router.get("/{customer_id}")
async def get_customer(customer_id: str):
    """Get a customer by ID."""
    return {"customer_id": customer_id}


@router.put("/{customer_id}")
async def update_customer(customer_id: str):
    """Update a customer."""
    return {"customer_id": customer_id}


@router.delete("/{customer_id}")
async def delete_customer(customer_id: str):
    """Delete a customer."""
    return {"customer_id": customer_id}