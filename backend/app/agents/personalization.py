"""Personalization Agent — crafts unique outreach messages."""

from typing import Any, Dict
from app.agents import AgentContext, BaseAgent


class PersonalizationAgent(BaseAgent):
    """Writes personalized outreach messages for each prospect using LLM."""

    name = "personalization"

    async def run(self, ctx: AgentContext, input_data: Dict[str, Any]) -> Dict[str, Any]:
        ctx.log("Personalizing outreach messages...")
        researched = input_data.get("researched_prospects", [])
        personalized = []

        for prospect in researched:
            # TODO: Call LLM to generate personalized message
            ctx.log(f"Personalized message for: {prospect.get('company_name')}")

        return {"personalized_prospects": personalized, "personalization_complete": True}