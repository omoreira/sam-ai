"""
Tests for AI providers.
"""

import pytest
from unittest.mock import patch, MagicMock
from src.sam_ai.providers.ollama_provider import OllamaProvider
from src.sam_ai.providers.openai_provider import OpenAIProvider

class TestOllamaProvider:
    """Test Ollama provider functionality."""
    
    @patch('requests.post')
    def test_chat_completion_success(self, mock_post):
        """Test successful chat completion."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "message": {"content": "Hello, I'm an AI assistant."}
        }
        mock_post.return_value = mock_response
        
        provider = OllamaProvider(base_url="http://localhost:11434")
        messages = [{"role": "user", "content": "Hello"}]
        
        response = provider.chat_completion(messages, "phi3")
        
        assert response == "Hello, I'm an AI assistant."
        mock_post.assert_called_once()
    
    @patch('requests.post')
    def test_chat_completion_failure(self, mock_post):
        """Test chat completion failure."""
        mock_post.side_effect = ConnectionError("Connection failed")
        
        provider = OllamaProvider(base_url="http://localhost:11434")
        messages = [{"role": "user", "content": "Hello"}]
        
        with pytest.raises(ConnectionError):
            provider.chat_completion(messages, "phi3")

class TestOpenAIProvider:
    """Test OpenAI provider functionality."""
    
    def test_initialization_without_key(self):
        """Test initialization without API key."""
        provider = OpenAIProvider(api_key=None)
        assert not provider.is_available()
    
    @patch('openai.OpenAI')
    def test_chat_completion_success(self, mock_openai):
        """Test successful chat completion."""
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = "Hello from OpenAI"
        mock_client.chat.completions.create.return_value = mock_response
        mock_openai.return_value = mock_client
        
        provider = OpenAIProvider(api_key="test-key")
        messages = [{"role": "user", "content": "Hello"}]
        
        response = provider.chat_completion(messages, "gpt-4")
        
        assert response == "Hello from OpenAI"
        mock_client.chat.completions.create.assert_called_once()