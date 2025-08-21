"""
Ollama provider implementation for local AI models.
"""

import requests
from typing import List, Dict, Any
from .base_provider import BaseProvider
from ..config import settings

class OllamaProvider(BaseProvider):
    """Provider for local Ollama models."""

    def __init__(self, base_url: str = None):
        self.base_url = base_url or settings.ollama_base_url
        self.timeout = settings.ollama_request_timeout

    def chat_completion(self, messages: List[Dict[str, str]], model: str, **kwargs) -> str:
        url = f"{self.base_url}/api/chat"
        payload = {
            "model": model,
            "messages": messages,
            "stream": False,
            "options": kwargs.get("options", {})
        }

        try:
            response = requests.post(url, json=payload, timeout=self.timeout)
            response.raise_for_status()
            return response.json()["message"]["content"]
        except requests.exceptions.ConnectionError:
            raise ConnectionError("Could not connect to Ollama. Is it running?")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Ollama API request failed: {e}")

    def list_models(self) -> List[str]:
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=10)
            response.raise_for_status()
            models_data = response.json().get("models", [])
            return [model["name"] for model in models_data]
        except requests.exceptions.RequestException:
            return []  # Return empty list if Ollama isn't running

    def is_available(self) -> bool:
        """Check if Ollama is running and accessible."""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False