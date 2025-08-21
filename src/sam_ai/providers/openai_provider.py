"""
OpenAI provider implementation for cloud-based AI models.
"""

import openai
from typing import List, Dict, Any
from .base_provider import BaseProvider
from ..config import settings

class OpenAIProvider(BaseProvider):
    """Provider for OpenAI API models."""

    def __init__(self, api_key: str = None, base_url: str = None):
        self.api_key = api_key or (settings.openai_api_key.get_secret_value() 
                                  if settings.openai_api_key else None)
        self.base_url = base_url or settings.openai_base_url
        self.client = None
        
        if self.api_key:
            self._initialize_client()

    def _initialize_client(self):
        """Initialize the OpenAI client."""
        self.client = openai.OpenAI(
            api_key=self.api_key,
            base_url=self.base_url
        )

    def chat_completion(self, messages: List[Dict[str, str]], model: str, **kwargs) -> str:
        if not self.client:
            raise ValueError("OpenAI client not initialized. Please provide an API key.")
        
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                **kwargs
            )
            return response.choices[0].message.content
        except openai.APIConnectionError as e:
            raise ConnectionError(f"Failed to connect to OpenAI API: {e}")
        except openai.APIError as e:
            raise Exception(f"OpenAI API returned an error: {e}")
        except openai.AuthenticationError as e:
            raise ValueError(f"OpenAI API authentication failed: {e}")

    def list_models(self) -> List[str]:
        # For OpenAI, we return some common models since listing all requires special permissions
        return [
            "gpt-4o",
            "gpt-4-turbo",
            "gpt-4",
            "gpt-3.5-turbo",
        ]

    def is_available(self) -> bool:
        """Check if OpenAI is configured properly."""
        return self.api_key is not None and self.client is not None

    def update_api_key(self, api_key: str):
        """Update the API key and reinitialize the client."""
        self.api_key = api_key
        self._initialize_client()