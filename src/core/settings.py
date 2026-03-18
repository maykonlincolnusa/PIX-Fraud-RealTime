from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import field_validator


class Settings(BaseSettings):

    APP_NAME: str = "FMB System Anti-Fraud"

    VERSION: str = "1.0.0"

    DEBUG: bool = False

    DATABASE_URL: str = "sqlite:///./data/fraud_master_bank.db"
    TIMESCALE_ENABLED: bool = True

    REDIS_URL: str = "redis://localhost:6379"

    EVENT_STORE_TABLE: str = "events"

    FEATURE_STORE_TABLE: str = "features"

    GRAPH_DB_URL: str = "bolt://localhost:7687"

    API_PREFIX: str = "/api/v1"

    # Kafka / streaming
    KAFKA_BOOTSTRAP_SERVERS: str = "redpanda:9092"
    KAFKA_PIX_TOPIC: str = "pix.transactions"
    KAFKA_ALERT_TOPIC: str = "pix.alerts"
    KAFKA_GROUP_ID: str = "pix-fraud-consumers"

    # Zero-trust
    PIX_API_KEY: str = "change-this-api-key"
    ZERO_TRUST_ALLOWED_SERVICES: str = "pix-gateway,sovereign-platform,ops-console"
    ZERO_TRUST_REQUIRE_SIGNATURE: bool = False
    ZERO_TRUST_HMAC_SECRET: str = "change-hmac-secret"

    # SELS immutable ledger
    SELS_SALT: str = "change-sels-salt"

    # Alerting
    TELEGRAM_BOT_TOKEN: str = ""
    TELEGRAM_CHAT_ID: str = ""
    WHATSAPP_API_URL: str = ""
    WHATSAPP_TOKEN: str = ""
    WHATSAPP_TO: str = ""

    # Sovereign platform
    SOVEREIGN_PLATFORM_WEBHOOK: str = ""
    SOVEREIGN_PLATFORM_TOKEN: str = ""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @field_validator("DEBUG", mode="before")
    @classmethod
    def _parse_debug(cls, value):
        if isinstance(value, str):
            lowered = value.strip().lower()
            if lowered in {"release", "prod", "production"}:
                return False
        return value

    def allowed_services(self) -> list[str]:
        return [
            item.strip()
            for item in self.ZERO_TRUST_ALLOWED_SERVICES.split(",")
            if item.strip()
        ]


settings = Settings()
