#!/usr/bin/env python3
# debug_imports.py - Debug the import issues
import os
import sys

print("=== DEBUG IMPORT ISSUES ===")
print(f"Current directory: {os.getcwd()}")
print(f"Python path: {sys.path}")

# Test if we can find the modules
try:
    # Add project root to path
    project_root = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, project_root)
    print(f"Added to path: {project_root}")

    # Test config import
    from src.sam_ai.config import settings
    print("✓ Config import successful")

    # Test engine import
    from src.sam_ai.core.engine import Orchestrator
    print("✓ Engine import successful")

    # Test provider import
    from src.sam_ai.providers.ollama_provider import OllamaProvider
    print("✓ Provider import successful")

    print("All imports working! The issue is with Streamlit execution.")

except ImportError as e:
    print(f"Import failed: {e}")
    print("Trying to find the files...")

    # Check if files exist
    config_path = os.path.join(project_root, 'src', 'sam_ai', 'config.py')
    print(f"Config file exists: {os.path.exists(config_path)}")

    engine_path = os.path.join(project_root, 'src', 'sam_ai', 'core', 'engine.py')
    print(f"Engine file exists: {os.path.exists(engine_path)}")
