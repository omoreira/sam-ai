"""
Tests for the main orchestration engine.
"""

import pytest
from unittest.mock import patch, MagicMock
from src.sam_ai.core.engine import Orchestrator
from src.sam_ai.core.memory_manager import MemoryManager

class TestOrchestrator:
    """Test the main orchestrator functionality."""
    
    @patch('src.sam_ai.core.engine.get_provider')
    def test_initialization(self, mock_get_provider):
        """Test orchestrator initialization."""
        mock_provider = MagicMock()
        mock_get_provider.return_value = mock_provider
        
        orchestrator = Orchestrator()
        
        assert orchestrator.current_mode == "chat"
        assert orchestrator.provider == mock_provider
        mock_get_provider.assert_called_once()
    
    @patch('src.sam_ai.core.engine.get_provider')
    @patch.object(MemoryManager, 'get_context')
    @patch.object(MemoryManager, 'add_interaction')
    def test_process_message(self, mock_add, mock_get_context, mock_get_provider):
        """Test message processing."""
        mock_provider = MagicMock()
        mock_provider.chat_completion.return_value = "Test response"
        mock_get_provider.return_value = mock_provider
        
        mock_get_context.return_value = []
        
        orchestrator = Orchestrator()
        response = orchestrator.process_message("Hello", "chat")
        
        assert response == "Test response"
        mock_provider.chat_completion.assert_called_once()
        mock_add.assert_called_once()