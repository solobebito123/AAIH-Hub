"""
Configuration — AAIH (Apex Agentic & Intelligence Hub)

Environment-based configuration for all service keys and endpoints.
"""

import os


# --- Emergent Universal LLM Gateway ---
EMERGENT_LLM_KEY = os.environ.get("EMERGENT_LLM_KEY", "")
EMERGENT_LLM_BASE_URL = os.environ.get("EMERGENT_LLM_BASE_URL", "https://integrations.emergentagent.com/llm")

# --- Aisure AI Engine ---
AISURE_API_KEY = os.environ.get("AISURE_API_KEY", "")
AISURE_BASE_URL = os.environ.get("AISURE_BASE_URL", "https://api.aisure.dev/v1")

# --- xAI / Grok ---
XAI_API_KEY = os.environ.get("XAI_API_KEY", "")
XAI_BASE_URL = os.environ.get("XAI_BASE_URL", "https://api.x.ai/v1")

# --- Anthropic (direct) ---
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")

# --- ScrapingBee ---
SCRAPINGBEE_API_KEY = os.environ.get("SCRAPINGBEE_API_KEY", "")

# --- Twilio SMS ---
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID", "")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN", "")
TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER", "")
TWILIO_API_KEY_SID = os.environ.get("TWILIO_API_KEY_SID", "")
TWILIO_API_KEY_SECRET = os.environ.get("TWILIO_API_KEY_SECRET", "")

# --- Flask / App ---
FLASK_SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "aaih-dev-secret-key")
FLASK_PORT = int(os.environ.get("FLASK_PORT", "5000"))

# --- Brain Source Configuration ---
# Valid sources: "Aisure", "Grok", "Emergent"
DEFAULT_BRAIN_SOURCE = os.environ.get("DEFAULT_BRAIN_SOURCE", "Emergent")
BRAIN_SOURCES_PRIORITY = ["Emergent", "Aisure", "Grok"]

# --- Model Defaults ---
EMERGENT_DEFAULT_MODEL = "claude-sonnet-4-5"
EMERGENT_TECHNICAL_MODEL = "claude-sonnet-4-5"
EMERGENT_GENERAL_MODEL = "gpt-4o"
