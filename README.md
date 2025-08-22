# Sam AI

<p align="center">
  <img src="assets/SamAIlogo.png" alt="Sam AI Logo" width="100"/>
</p>

A Modular, Portable, and Trauma-Informed AI Personal Assistant.
<<<<<<< HEAD

=======
>>>>>>> 59a69730eb9fb0c1cfce71d9763d49c51c11b4e3
Named in loving memory of Sam Lee Catson (2007-2022).

## In Memoriam: Sam Lee Catson

**Date:** May 4, 2022

> Goodbye, Sam! We will miss you immensely.
>
> Thank you for staying with us for over 14 years! Thank you for all the happy moments we spent together!
>
> To those who got to meet Sam in person, who knew Sam: You know that Sam wasn't an ordinary cat. He had a unique, strong personality. He was one of a kind.
>
> Sam was fearless, smart, chatty, hyperactive, friendly and very sweet. He was a force of nature and a spoiled brat. He lived life to the fullest.
>
> Sam was stubborn, never knew when to give up. Unfortunately, his body did. His genetics betrayed him. First, his kidneys. Then, his liver. Then, his heart. One by one, his organs began shutting down while his mind was forever present, awaken. We did everything we could. Dr. Boctor and his team at the St. Catharines Animal Hospital provided the best care, the best treatment. Sam fought as hard as he could, but nature always wins in the end.
>
> Sam spent the last moments of his life at home with us. He passed away in our arms last night, knowing that we love him dearly.
>
> Wherever you are, Sam. Remember (like we always told you whenever we had to go away for a while, whenever we had to leave you at the hospital):
>
> *"Don't worry, kitty! We will come back for you. We will always will!"*

See you in Valhalla,

Olga M.

---

 **Status: Early Development - Testing Phase**

> **Note:** This is currently in active testing. The next major release will include secure private data handling for personal context, mental health support, and career guidance modules. Use with caution in production environments.

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

##  Current Status
-  Core AI engine with Ollama integration
-  Streamlit web interface prototype
-  Basic memory management
-  Multi-provider support (Ollama/OpenAI)
- **Coming Soon:** Secure private data modules
- **Coming Soon:** Mental health support tools
- **Coming Soon:** Career and writing assistant features

## Features

- **Provider-Agnostic**: Choose your AI engine. Run powerful models locally for free with **Ollama** (e.g., Llama 3, Phi-3) or connect to premium APIs like **OpenAI** for maximum capability.
- **Portable Memory**: Your context, history, and preferences stay with you across devices and sessions.
- **Modular Tools**: Extend Sam's capabilities with custom tools for document analysis, workflow automation, and more.
- **Dual-Mode Operation**:
  - **Chat Mode**: For natural, supportive conversation.
  - **Agent Mode**: For multi-step reasoning and task execution.
- **Privacy-First**: Defaults to local execution. Your data never leaves your machine unless you explicitly choose a cloud API.

## Quick Start

### Prerequisites

1. **Python 3.9+**
2. **Ollama**: [Installation Guide](https://ollama.com)

### Installation & Setup

```bash
# Clone the repository
git clone https://github.com/your-username/sam-ai.git
cd sam-ai

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Linux/macOS:
source venv/bin/activate
# On Windows (Command Prompt):
.\venv\Scripts\activate.bat
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Pull a language model (e.g., the efficient Phi-3 model)
ollama pull phi3
```
### Important: Pydantic 2.x Required

Sam AI currently requires **Pydantic 2.x** or later, which needs the `pydantic-settings` package:

```bash
# This will install all required dependencies including pydantic-settings
pip install -r requirements.txt
```
Note: Backward compatibility with Pydantic 1.x is planned for a future release. If you need to use an older Python environment, please check the project issues for compatibility updates.

### Running the Prototype

```bash
# Make sure Ollama is running in one terminal
ollama serve

# Run the application using the dedicated launcher
python run_sam.py
```

The launcher will automatically open your browser to the Sam AI interface (usually http://localhost:8501).

## Troubleshooting & Debugging Tools

Sam AI includes several helper scripts to diagnose and resolve common issues:

### `test_sam.py` - Quick Setup Verification
**When to use:** After installation to verify everything is working correctly.
```bash
python test_sam.py
```
**Expected output:** `All basic tests passed!`

### `debug_imports.py` - Detailed Import Diagnostics
**When to use:** When you see `ModuleNotFoundError` or other import issues.
```bash
python debug_imports.py
```
**Provides:** Detailed error messages, file existence checks, and path information.

### `run_sam.py` - Recommended Application Launcher
**When to use:** Always use this to start Sam AI - it handles the complex setup for you.
```bash
python run_sam.py
```

## Common Issues & Solutions

| Symptom | Solution |
|---------|----------|
| `ModuleNotFoundError` | Use `python run_sam.py` or run `pip install -e .` |
| Ollama connection issues | Ensure `ollama serve` is running in another terminal |
| Streamlit import errors | Use the provided launcher scripts |

## Project Roadmap

- **Phase 1:** Core Engine & CLI
- **Phase 2:** Streamlit UI Prototype (Current)
- **Phase 3:** Robust Desktop App (In Progress)
- **Phase 4:** Mobile Client & Advanced Integrations
- **Future:** Secure private data modules, mental health support tools, career assistant features

## For Developers

We welcome contributions! Please read our:
- [Architecture Overview](./docs/ARCHITECTURE.md)
- [Contributing Guidelines](./docs/CONTRIBUTING.md)
- [Setup Guide](./docs/SETUP.md)

## License

This project is licensed under the GNU Affero General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Disclaimer

**Sam AI is not a licensed mental health professional.** The trauma-informed features are designed for supportive self-reflection and should not be used as a substitute for therapy or professional medical advice.

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](./docs/CONTRIBUTING.md) for details.

## Bug Reports

Found a bug? Please [open an issue](https://github.com/your-username/sam-ai/issues) with detailed information about the problem.
