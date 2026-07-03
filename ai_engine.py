"""
AI Engine — AAIH (Apex Agentic & Intelligence Hub)

Multi-provider AI engine supporting Emergent Universal LLM Gateway,
Aisure, and xAI/Grok as brain sources.
"""

import logging
from typing import Optional

from openai import OpenAI

import config

logger = logging.getLogger(__name__)


class AIEngineError(Exception):
    pass


class EmergentGateway:
    """
    Emergent Universal LLM Gateway client.

    Uses the OpenAI SDK with Emergent credentials to access any model
    through the universal gateway. Defaults to claude-sonnet-4-5 for
    technical tasks.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        default_model: Optional[str] = None,
    ):
        self.api_key = api_key or config.EMERGENT_LLM_KEY
        self.base_url = base_url or config.EMERGENT_LLM_BASE_URL
        self.default_model = default_model or config.EMERGENT_DEFAULT_MODEL

        if not self.api_key:
            raise AIEngineError("Emergent LLM key not configured")

        self.client = OpenAI(
            api_key=self.api_key,
            base_url=self.base_url,
        )

    def chat(
        self,
        messages: list[dict],
        model: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 2048,
        system_prompt: Optional[str] = None,
    ) -> str:
        model = model or self.default_model
        final_messages = []

        if system_prompt:
            final_messages.append({"role": "system", "content": system_prompt})

        final_messages.extend(messages)

        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=final_messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Emergent Gateway error (model={model}): {e}")
            raise AIEngineError(f"Emergent Gateway request failed: {e}") from e

    def complete_technical(self, prompt: str, context: str = "") -> str:
        messages = [{"role": "user", "content": prompt}]
        system_prompt = (
            "You are an expert technical assistant specializing in programming, "
            "cybersecurity, systems engineering, and automation. "
            "Provide precise, actionable answers."
        )
        if context:
            system_prompt += f"\n\nContext:\n{context}"

        return self.chat(
            messages=messages,
            model=config.EMERGENT_TECHNICAL_MODEL,
            system_prompt=system_prompt,
            temperature=0.3,
        )

    def complete_general(self, prompt: str, system_prompt: str = "") -> str:
        messages = [{"role": "user", "content": prompt}]
        return self.chat(
            messages=messages,
            model=config.EMERGENT_GENERAL_MODEL,
            system_prompt=system_prompt or "You are a helpful AI assistant.",
        )


class BrainRouter:
    VALID_SOURCES = {"Emergent", "Aisure", "Grok"}

    def __init__(self):
        self._engines = {}
        self._initialize_engines()

    def _initialize_engines(self):
        try:
            self._engines["Emergent"] = EmergentGateway()
        except AIEngineError:
            pass

    def route(
        self, 
        messages: list[dict], 
        task_type: str = "general", 
        preferred_source: Optional[str] = None, 
        **kwargs
    ) -> str:
        # Routing logic implementation
        return ""
