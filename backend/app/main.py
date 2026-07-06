"""ProspectPilot AI — Main FastAPI Application.

Entry point for the backend server. Configures routes, middleware,
and the LangGraph agent pipeline.
"""

from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import loguru

from app.config import settings
from app.database import init_db, close_db
from app.agents import AgentPipeline, AgentContext
from app.agents.lead_discovery import LeadDiscoveryAgent
from app.agents.research import ResearchAgent
from app.agents.personalization import PersonalizationAgent
from app.agents.outreach import OutreachAgent
from app.agents.conversation import ConversationAgent
from app.agents.calendar import CalendarAgent
from app.agents.crm import CrmAgent
from app.agents.analytics import AnalyticsAgent

logger = loguru.logger


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    """Application lifespan — startup and shutdown."""
    logger.info(f"Starting {settings.APP_NAME} v{settings.APP_VERSION}")
    await init_db()
    # Build the agent pipeline
    app.state.pipeline = (
        AgentPipeline()
        .add_agent(LeadDiscoveryAgent())
        .add_agent(ResearchAgent())
        .add_agent(PersonalizationAgent())
        .add_agent(OutreachAgent())
        .add_agent(ConversationAgent())
        .add_agent(CalendarAgent())
        .add_agent(CrmAgent())
        .add_agent(AnalyticsAgent())
    )
    logger.info(f"Agent pipeline initialized with 8 agents")
    yield
    await close_db()
    logger.info("Application shutdown complete")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
)

# CORS — allow frontend during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---- Health Check ----
@app.get("/health")
async def health_check():
    return {"status": "ok", "version": settings.APP_VERSION, "service": settings.APP_NAME}


# ---- Error Handler ----
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception on {request.url}: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "An internal server error occurred."},
    )


# ---- Import and include routers ----
from app.api import customers, campaigns, prospects, meetings  # noqa: E402

app.include_router(customers.router, prefix="/api/v1/customers", tags=["Customers"])
app.include_router(campaigns.router, prefix="/api/v1/campaigns", tags=["Campaigns"])
app.include_router(prospects.router, prefix="/api/v1/prospects", tags=["Prospects"])
app.include_router(meetings.router, prefix="/api/v1/meetings", tags=["Meetings"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)