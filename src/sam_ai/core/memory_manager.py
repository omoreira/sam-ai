"""
Memory management for Sam AI.
Handles conversation history and context management.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any
from ..config import settings

class MemoryManager:
    """Manages conversation memory and context."""
    
    def __init__(self):
        self.conversation_history: List[Dict] = []
        self.memory_file = settings.memory_persistence_path / "conversation_memory.json"
        self._ensure_memory_directory()
        self._load_memory()
    
    def _ensure_memory_directory(self):
        """Ensure the memory directory exists."""
        settings.memory_persistence_path.mkdir(parents=True, exist_ok=True)
    
    def _load_memory(self):
        """Load conversation memory from file."""
        try:
            if self.memory_file.exists():
                with open(self.memory_file, 'r') as f:
                    self.conversation_history = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            self.conversation_history = []
    
    def _save_memory(self):
        """Save conversation memory to file."""
        try:
            with open(self.memory_file, 'w') as f:
                json.dump(self.conversation_history, f, indent=2)
        except IOError as e:
            print(f"Error saving memory: {e}")
    
    def add_interaction(self, user_message: str, ai_response: str):
        """Add a new interaction to memory."""
        interaction = {
            "timestamp": datetime.now().isoformat(),
            "user": user_message,
            "assistant": ai_response
        }
        
        self.conversation_history.append(interaction)
        
        # Keep only the most recent messages
        if len(self.conversation_history) > settings.max_chat_history:
            self.conversation_history = self.conversation_history[-settings.max_chat_history:]
        
        self._save_memory()
    
    def get_context(self, current_message: str) -> List[Dict]:
        """
        Get relevant context for the current message.
        
        Args:
            current_message: The current user message
            
        Returns:
            List of message dictionaries for context
        """
        # Simple implementation: return recent history
        # This could be enhanced with semantic search later
        context_messages = []
        
        for interaction in self.conversation_history[-5:]:  # Last 5 interactions
            context_messages.append({"role": "user", "content": interaction["user"]})
            context_messages.append({"role": "assistant", "content": interaction["assistant"]})
        
        return context_messages
    
    def clear(self):
        """Clear all conversation memory."""
        self.conversation_history = []
        try:
            if self.memory_file.exists():
                self.memory_file.unlink()
        except OSError:
            pass
    
    def export_memory(self, file_path: Path):
        """Export memory to a specified file."""
        try:
            with open(file_path, 'w') as f:
                json.dump(self.conversation_history, f, indent=2)
        except IOError as e:
            print(f"Error exporting memory: {e}")