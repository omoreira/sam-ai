"""
Main orchestration engine for Sam AI.
Handles the flow between providers, memory, and tools.
"""

import logging
from typing import Dict, List, Any, Optional
from ..config import settings
from ..providers import get_provider
from .memory_manager import MemoryManager

logger = logging.getLogger(__name__)

class Orchestrator:
    """Main orchestrator that manages the AI conversation flow."""
    
    def __init__(self):
        self.memory = MemoryManager()
        self.provider = get_provider(settings.default_provider)
        self.current_mode = "chat"  # 'chat' or 'agent'
        
    def process_message(self, message: str, mode: str = "chat") -> str:
        """
        Process a user message and return the AI response.
        
        Args:
            message: The user's input message
            mode: The operation mode ('chat' or 'agent')
            
        Returns:
            The AI's response
        """
        self.current_mode = mode
        
        # Get relevant context from memory
        context = self.memory.get_context(message)
        
        # Prepare messages for the AI provider
        messages = self._prepare_messages(message, context)
        
        try:
            # Get response from the provider
            response = self.provider.chat_completion(
                messages=messages,
                model=settings.default_model,
                mode=mode
            )
            
            # Update memory with this interaction
            self.memory.add_interaction(message, response)
            
            return response
            
        except Exception as e:
            logger.error(f"Error processing message: {e}")
            return f"I encountered an error: {str(e)}. Please check if Ollama is running."
    
    def _prepare_messages(self, message: str, context: List[Dict]) -> List[Dict]:
        """Prepare the messages array for the AI provider."""
        messages = []
        
        # Add system prompt based on mode
        if self.current_mode == "agent":
            system_prompt = self._get_agent_system_prompt()
        else:
            system_prompt = self._get_chat_system_prompt()
            
        messages.append({"role": "system", "content": system_prompt})
        
        # Add context from memory
        messages.extend(context)
        
        # Add current message
        messages.append({"role": "user", "content": message})
        
        return messages
    
    def _get_chat_system_prompt(self) -> str:
        """Get the system prompt for chat mode."""
        return """You are Sam, a helpful, kind, and trauma-informed AI assistant.
        Be supportive, empathetic, and professional in your responses.
        Focus on being helpful while maintaining appropriate boundaries."""
    
    def _get_agent_system_prompt(self) -> str:
        """Get the system prompt for agent mode."""
        return """You are Sam in Agent Mode. You can help with multi-step tasks.
        Think step by step and break down complex problems.
        You have access to various tools - let me know if you need to use any."""
    
    def switch_provider(self, provider_name: str):
        """Switch to a different AI provider."""
        self.provider = get_provider(provider_name)
        logger.info(f"Switched to provider: {provider_name}")
    
    def clear_memory(self):
        """Clear the conversation memory."""
        self.memory.clear()
        logger.info("Conversation memory cleared")