"""
Tool system for Sam AI's agent mode.
"""

from src.sam_ai.tools.example_tools import calculator, get_current_time, read_file

# Registry of available tools
TOOL_REGISTRY = {
    "calculator": {
        "function": calculator,
        "description": "Perform mathematical calculations. Input should be a mathematical expression as a string."
    },
    "get_current_time": {
        "function": get_current_time,
        "description": "Get the current date and time."
    },
    "read_file": {
        "function": read_file,
        "description": "Read the contents of a text file. Input should be the file path."
    }
}

__all__ = ['TOOL_REGISTRY', 'calculator', 'get_current_time', 'read_file']