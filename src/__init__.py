# This file tells Python that the sam_ai directory is a package.
# It's often used to define the public interface of the package—what gets imported when someone does import sam_ai.

"""
Sam AI - A Modular, Portable, and Trauma-Informed AI Personal Assistant.
"""

__version__ = "0.1.0-alpha"
__author__ = "Your Name <your.email@example.com>"

# This import allows for a cleaner import structure for users/other modules.
# Instead of `from sam_ai.core.engine import Orchestrator`, they can do:
# `from sam_ai import Orchestrator` (if we uncomment the lines below).

# Import key classes for easier access
# from .core.engine import Orchestrator
# from .providers.ollama_provider import OllamaProvider
# from .providers.openai_provider import OpenAIProvider
# from .config import load_config, Settings

# Alternatively, you can define __all__ to explicitly state what is public.
# __all__ = ["Orchestrator", "OllamaProvider", "OpenAIProvider", "load_config", "Settings"]

# For now, we'll keep it simple. The above lines are commented out as an example
# for future expansion when the package structure is more stable.
