"""
Abstract base class for all AI providers.
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any

class BaseProvider(ABC):
    """Abstract base class for all AI providers."""

    @abstractmethod
    def chat_completion(self, messages: List[Dict[str, str]], model: str, **kwargs) -> str:
        """
        Send a list of messages to the provider and return the response.

        Args:
            messages: List of dicts with 'role' and 'content'.
            model: The model identifier to use.
            **kwargs: Additional provider-specific arguments.

        Returns:
            The generated response as a string.
        """
        pass

    @abstractmethod
    def list_models(self) -> List[str]:
        """Return a list of available model names for this provider."""
        pass

    @abstractmethod
    def is_available(self) -> bool:
        """Check if the provider is available and configured properly."""
        pass