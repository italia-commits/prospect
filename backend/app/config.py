"""ProspectPilot AI — Configuration.

All environment-based configuration for the application.
Uses pydantic-settings for type-safe env var loading.
"""

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # Application
    APP_NAME: str = "ProspectPilot AI"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = False

    # Database
    DATABASE_URL: str = "postgresql+asyncpg://prospectpilot:prospectpilot_dev@localhost:5432/prospectpilot"

    # Redis / Celery
    REDIS_URL: str = "redis://localhost:6379/0"

    # OpenAI
    OPENAI_API_KEY: Optional[str] = None
    OPENAI_MODEL: str = "gpt-4o"

    # Anthropic
    ANTHROPIC_API_KEY: Optional[str] = None
    ANTHROPIC_MODEL: str = "claude-3-5-sonnet-20240620"

    # Stripe
    STRIPE_SECRET_KEY: Optional[str] = None
    STRIPE_WEBHOOK_SECRET: Optional[str] = None

    # SendGrid (email)
    SENDGRID_API_KEY: Optional[str] = None
    SENDGRID_FROM_EMAIL: str = "hello@prospectpilot.ai"

    # Auth
    SECRET_KEY: str = "change-me-in-production"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours

    # Agent settings
    AGENT_MAX_ITERATIONS: int = 25
    AGENT_TEMPERATURE: float = 0.3
    AGENT_MAX_CONCURRENT: int = 5

    # Outreach defaults
    DEFAULT_OUTREACH_LIMIT_PER_DAY: int = 50
    DEFAULT_FOLLOW_UP_DELAY_HOURS: int = 48

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()