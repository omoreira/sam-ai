"""
Example tools for Sam AI's agent mode.
"""

import datetime
from pathlib import Path
from typing import Dict, Any

def calculator(expression: str) -> Dict[str, Any]:
    """
    Evaluate a mathematical expression safely.
    
    Args:
        expression: Mathematical expression as string
        
    Returns:
        Dictionary with result or error
    """
    try:
        # Very basic safe evaluation - in production, use a proper safe eval library
        allowed_chars = set('0123456789+-*/(). ')
        if not all(c in allowed_chars for c in expression):
            return {"error": "Invalid characters in expression"}
            
        result = eval(expression, {"__builtins__": {}}, {})
        return {"result": result, "expression": expression}
        
    except Exception as e:
        return {"error": f"Calculation error: {str(e)}"}

def get_current_time() -> Dict[str, Any]:
    """Get the current date and time."""
    now = datetime.datetime.now()
    return {
        "current_time": now.isoformat(),
        "formatted": now.strftime("%Y-%m-%d %H:%M:%S")
    }

def read_file(file_path: str) -> Dict[str, Any]:
    """
    Read the contents of a text file.
    
    Args:
        file_path: Path to the file to read
        
    Returns:
        Dictionary with file content or error
    """
    try:
        path = Path(file_path)
        if not path.exists():
            return {"error": f"File not found: {file_path}"}
            
        if not path.is_file():
            return {"error": f"Path is not a file: {file_path}"}
            
        content = path.read_text(encoding='utf-8')
        return {"content": content, "file_path": str(path)}
        
    except Exception as e:
        return {"error": f"Error reading file: {str(e)}"}