"""Research Agent — researches prospects and gathers intelligence."""

from typing import Any, Dict
from app.agents import AgentContext, BaseAgent


class ResearchAgent(BaseAgent):
    """Researches each prospect: company, tech stack, recent news, funding, etc."""

    name = "research"

    async def run(self, ctx: AgentContext, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Research all discovered prospects."""
        ctx.log("Researching prospects...")

        prospects = input_data.get("discovered_prospects", [])
        researched = []

        for prospect in prospects:
            # TODO: Implement web research (company website, LinkedIn, Crunchbase)
            ctx.log(f"Researched: {prospect.get('company_name')}")

        return {"researched_prospects": researched, "research_complete": True}