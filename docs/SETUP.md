# Development Environment Setup

This guide will help you set up a local development environment for Sam AI on your machine (Linux, macOS, or WSL).

## Prerequisites

1.  **Python 3.9 or higher**
    *   Check your version: `python3 --version`
    *   Download from [python.org](https://python.org) or use your system's package manager (e.g., `sudo apt install python3 python3-pip` on Ubuntu).

2.  **Ollama**
    *   **Installation:** Follow the official guide at [https://ollama.com](https://ollama.com).
    *   **Linux one-liner:**
        ```bash
        curl -fsSL https://ollama.com/install.sh | sh
        ```
    *   **Verify installation:** Run `ollama serve` in a terminal. Keep it running.
    *   **Pull a test model:**
        ```bash
        ollama pull phi3
        ```

3.  **Git**
    *   Usually pre-installed. If not, install via your package manager (e.g., `sudo apt install git`).

## Step 1: Get the Source Code

1.  **Fork the repository** on GitHub by clicking the "Fork" button at the top right of the [sam-ai repo page](https://github.com/your-username/sam-ai).
2.  **Clone your fork** to your local machine:
    ```bash
    git clone https://github.com/your-username/sam-ai.git
    cd sam-ai
    ```
3.  **(Optional) Add the upstream remote** to sync with the main project:
    ```bash
    git remote add upstream https://github.com/original-username/sam-ai.git
    ```

## Step 2: Create a Virtual Environment

It's best practice to isolate your project dependencies.

```bash
# Create the virtual environment in a folder named 'venv'
python3 -m venv venv

# Activate the environment
# On Linux/macOS:
source venv/bin/activate
# On Windows (Command Prompt):
.\venv\Scripts\activate.bat
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# Your terminal prompt should now show (venv)

## Step 3: Install Dependencies

Install the required Python packages from the 'requirements.txt' file.
bash
# Make sure your venv is active first!
pip install -r requirements.txt

# For development, also install packages for testing and formatting
pip install black isort pytest

## Step 4: Install in Development Mode
Install the sam_ai package itself in "editable" mode. This allows you to make changes to the code without having to reinstall it.

bash
pip install -e .
Step 5: Verify Your Setup
Test the Core: Run a simple Python check to see if you can import the main modules.

bash
python3 -c "from src.sam_ai.core.engine import Orchestrator; print('✓ Core import successful')"
python3 -c "from src.sam_ai.providers.ollama_provider import OllamaProvider; print('✓ Provider import successful')"
Test Ollama Connection: Run a quick test to see if Python can talk to Ollama.

bash
python3 -c "
from src.sam_ai.providers.ollama_provider import OllamaProvider
provider = OllamaProvider()
models = provider.list_models()
print(f'Models found: {models}')
"
You should see ['phi3'] or a similar list.

Run the Streamlit Prototype:

bash
streamlit run prototypes/streamlit_app.py
A browser window should open. Try sending a message!

(Optional) Step 6: Testing Cloud Providers
To test the OpenAI provider, you need an API key.

Get a key from platform.openai.com.

Do not hardcode it! Set it as an environment variable in your terminal session:

bash
export OPENAI_API_KEY='sk-your-key-here'  # Linux/macOS
# or
set OPENAI_API_KEY=sk-your-key-here       # Windows CMD
$env:OPENAI_API_KEY='sk-your-key-here'    # Windows PowerShell
The Streamlit app should now be able to use the OpenAI provider when selected.

Running Tests
To ensure your changes don't break existing functionality, run the test suite.

bash
# Navigate to the project root and run:
python -m pytest
Code Formatting
Please format your code before committing:

bash

black .   # Formats code
isort .   # Sorts imports

You're now ready to develop and contribute to Sam AI!

