# Sam AI

A Modular, Portable, and Trauma-Informed AI Personal Assistant.

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

<p align="center">
  <img src="https://via.placeholder.com/800x400.png?text=Sam+AI+Interface+Preview" alt="Sam AI Preview" />
</p>

## ✨ Features

- **🤖 Provider-Agnostic**: Choose your AI engine. Run powerful models locally for free with **Ollama** (e.g., Llama 3, Phi-3) or connect to premium APIs like **OpenAI** for maximum capability.
- **🧠 Portable Memory**: Your context, history, and preferences stay with you across devices and sessions.
- **🛠️ Modular Tools**: Extend Sam's capabilities with custom tools for document analysis, workflow automation, and more.
- **⚙️ Dual-Mode Operation**:
  - **Chat Mode**: For natural, supportive conversation.
  - **Agent Mode**: For multi-step reasoning and task execution.
- **🔒 Privacy-First**: Defaults to local execution. Your data never leaves your machine unless you explicitly choose a cloud API.
- **❤️ Trauma-Informed**: Designed with mental health support principles in mind.

## 🚀 Quick Start

### Prerequisites

1. **Python 3.9+**
2. **Ollama** (for local models): [Installation Guide](https://ollama.com)

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/sam-ai.git
cd sam-ai

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

### Running the Prototype
```bash
# Make sure Ollama is running
ollama serve

# Pull a model (if you haven't already)
ollama pull phi3

# Run the Streamlit UI
streamlit run prototypes/streamlit_app.py
```
Open your browser to the provided URL (usually http://localhost:8501).

### Project Roadmap
See our detailed Project Proposal for the full vision.

Phase 1: Core Engine & CLI

Phase 2: Streamlit UI Prototype (Current)

Phase 3: Robust Desktop App (In Progress)

Phase 4: Mobile Client & Advanced Integrations

### For Developers
We welcome contributions! Please read our:

Architecture Overview

Contributing Guidelines

Setup Guide

### Documentation
Architecture - System design and components

Contributing - How to contribute to the project

Setup - Development environment setup

### License
This project is licensed under the GNU Affero General Public License v3.0 - see the LICENSE file for details.

### Disclaimer
Sam AI is not a licensed mental health professional. The trauma-informed features are designed for supportive self-reflection and should not be used as a substitute for therapy or professional medical advice.

### Contributing
We welcome contributions! Please see our Contributing Guidelines for details.

### Bug Reports
Found a bug? Please open an issue with detailed information about the problem.

