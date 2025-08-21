"""
AI Provider abstractions for Sam AI.
"""

from .base_provider import BaseProvider
from .ollama_provider import OllamaProvider
from .openai_provider import OpenAIProvider

__all__ = ['BaseProvider', 'OllamaProvider', 'OpenAIProvider']

def get_provider(provider_name: str) -> BaseProvider:
    """
    Factory function to get the appropriate provider.
    
    Args:
        provider_name: Name of the provider ('ollama' or 'openai')
        
    Returns:
        An instance of the requested provider
        
    Raises:
        ValueError: If the provider name is not recognized
    """
    provider_name = provider_name.lower()
    
    if provider_name == 'ollama':
        return OllamaProvider()
    elif provider_name == 'openai':
        return OpenAIProvider()
    else:
        raise ValueError(f"Unknown provider: {provider_name}")