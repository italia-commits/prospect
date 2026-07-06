"""LangGraph Agent Orchestration Framework for ProspectPilot AI.

Defines the base agent class and the orchestrator that chains agents
together into an autonomous SDR pipeline.

Agent Pipeline Flow:
1. LeadDiscoveryAgent → finds matching prospects
2. ResearchAgent → researches each prospect
3. PersonalizationAgent → crafts unique outreach
4. OutreachAgent → sends multi-channel messages
5. ConversationAgent → handles replies/objections
6. CalendarAgent → books meetings when prospect agrees
7. CrmAgent → updates records throughout
8. AnalyticsAgent → measures and reports performance
"""

import uuid
from datetime import datetime
from typing import Any, Dict, List, Optional, Protocol

import loguru

logger = loguru.logger


class AgentContext:
    """Shared context passed through the agent pipeline."""

    def __init__(self, customer_id: uuid.UUID, campaign_id: Optional[uuid.UUID] = None):
        self.customer_id = customer_id
        self.campaign_id = campaign_id
        self.correlation_id: str = str(uuid.uuid4())
        self.started_at: datetime = datetime.utcnow()
        self.state: Dict[str, Any] = {}
        self.errors: List[str] = []

    def log(self, message: str) -> None:
        logger.info(f"[{self.correlation_id}] {message}")


class BaseAgent(Protocol):
    """Protocol for all agents in the pipeline."""

    name: str

    async def run(self, ctx: AgentContext, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the agent's logic with the given context and input data."""
        ...


class AgentPipeline:
    """Orchestrator that runs the full agent pipeline in sequence."""

    def __init__(self):
        self._agents: List[BaseAgent] = []

    def add_agent(self, agent: BaseAgent) -> "AgentPipeline":
        self._agents.append(agent)
        return self

    async def execute(self, ctx: AgentContext, initial_data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the pipeline, passing results from one agent to the next."""
        ctx.log(f"Starting pipeline with {len(self._agents)} agents")
        current_data = initial_data

        for agent in self._agents:
            ctx.log(f"Running agent: {agent.name}")
            try:
                result = await agent.run(ctx, current_data)
                current_data.update(result)
                ctx.state[agent.name] = result
            except Exception as e:
                ctx.errors.append(f"{agent.name}: {str(e)}")
                ctx.log(f"Agent {agent.name} failed: {e}")
                # Continue with next agent unless critical
                continue

        ctx.log(f"Pipeline completed with {len(ctx.errors)} errors")
        return current_data