# This is a critical module. We'll use Pydantic for data validation and settings management, which is the modern standard. It will handle loading settings from environment variables and a .env file, with a focus on security for API keys.

"""
Configuration management for Sam AI using Pydantic settings.
Handles loading settings from environment variables and a .env file securely.
"""

import os
from typing import Literal, Optional
from pathlib import Path

from pydantic import BaseSettings, Field, validator
from pydantic.types import SecretStr
import keyring

# Default service name for storing secrets in the system keyring
KEYRING_SERVICE_NAME = "sam-ai"

class Settings(BaseSettings):
    """
    Main settings class for Sam AI.
    Settings can be set via environment variables (case-insensitive) or a .env file.
    """

    # --- Application Settings ---
    app_name: str = "Sam AI"
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"

    # --- AI Provider Selection ---
    default_provider: Literal["ollama", "openai"] = "ollama"
    default_model: str = "phi3"

    # --- Ollama Settings ---
    ollama_base_url: str = "http://localhost:11434"
    ollama_request_timeout: int = 300  # 5 minutes for long responses

    # --- OpenAI Settings ---
    # These are loaded from the keyring by default for security
    openai_api_key: Optional[SecretStr] = Field(default=None, env="OPENAI_API_KEY")
    openai_base_url: str = "https://api.openai.com/v1"  # Allows for custom endpoints
    openai_default_model: str = "gpt-4o"

    # --- Memory & Context Settings ---
    max_chat_history: int = 20  # Number of messages to keep in immediate context
    memory_persistence_path: Path = Path.home() / ".sam_ai" / "memory"

    class Config:
        # Look for a .env file in the project root
        env_file = ".env"
        env_file_encoding = 'utf-8'
        # Allow extra environment variables (like API keys from the system)
        extra = 'allow'

    @validator("memory_persistence_path")
    def ensure_memory_path_exists(cls, v: Path) -> Path:
        """Ensure the directory for storing memory exists."""
        v.mkdir(parents=True, exist_ok=True)
        return v

    @validator("openai_api_key", pre=True, always=True)
    def get_openai_api_key_from_keyring(cls, v, values) -> Optional[SecretStr]:
        """
        Priority for loading OpenAI API Key:
        1. Explicitly set via environment variable (OPENAI_API_KEY)
        2. Loaded from the system's keyring
        3. None (user will have to set it in the UI)
        """
        # If it was already set by the env variable, use that.
        if v is not None:
            # If v is already a SecretStr, return it. If it's a string, convert it.
            return v if isinstance(v, SecretStr) else SecretStr(v)

        # Try to get the key from the system keyring
        try:
            stored_key = keyring.get_password(KEYRING_SERVICE_NAME, "openai_api_key")
            if stored_key:
                return SecretStr(stored_key)
        except keyring.errors.KeyringError:
            # Keyring might not be available (e.g., in a container)
            # Silently fail and return None
            pass

        return None  # No key found

    def save_openai_api_key_to_keyring(self, api_key: str) -> None:
        """Securely save the OpenAI API key to the system keyring."""
        try:
            keyring.set_password(KEYRING_SERVICE_NAME, "openai_api_key", api_key)
            # Update the current settings object
            self.openai_api_key = SecretStr(api_key)
        except keyring.errors.KeyringError as e:
            raise Exception(f"Could not save API key to keyring: {e}")

    def delete_openai_api_key_from_keyring(self) -> None:
        """Remove the OpenAI API key from the system keyring."""
        try:
            keyring.delete_password(KEYRING_SERVICE_NAME, "openai_api_key")
            self.openai_api_key = None
        except keyring.errors.PasswordDeleteError:
            # Password didn't exist, that's fine.
            pass
        except keyring.errors.KeyringError as e:
            raise Exception(f"Could not delete API key from keyring: {e}")


# Create a global settings object that can be imported throughout the application
settings = Settings()

def load_config() -> Settings:
    """
    Helper function to load and return the configuration.
    This is useful if you need to reload settings at runtime.
    """
    global settings
    settings = Settings()
    return settings
