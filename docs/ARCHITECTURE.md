# Sam AI Architecture Overview

This document provides a high-level overview of the Sam AI system architecture, its components, and how they interact.

## High-Level Architecture

Sam AI follows a modular, client-server design pattern, even when running on a single machine. The core principle is a clear separation of concerns between the user interface, the application logic, the AI providers, and the tools.

## Core Components

### 1. Client (Frontend)
The user-facing interface. Its sole responsibility is to:
*   Capture user input and render responses.
*   Provide controls for settings (model selection, mode, API keys).
*   Send user requests to the Core backend and display the results.

**Examples:** The Streamlit app, a future Flet desktop GUI, a mobile app.

### 2. Sam AI Core
The brain of the operation. It contains the main application logic and state.

*   **Orchestrator:** The central coordinator. It receives requests from the Client, manages the flow of data between other components, and returns the final response.
*   **Memory Manager:** Handles the persistent context for the user. This includes:
    *   **Conversation History:** The short-term message history for the current session.
    *   **Long-Term Memory:** A vector database (e.g., ChromaDB) for storing and retrieving relevant past interactions beyond the immediate context window.
*   **Configuration Manager:** Loads and manages application settings (e.g., selected provider, model names, API keys from the keyring).

### 3. Provider Abstraction Layer (PAL)
A critical abstraction that allows Sam AI to be agnostic of the specific AI model being used.

*   **Defines a `BaseProvider` interface** that all providers must implement (e.g., `.chat_completion()`, `.list_models()`).
*   **Concrete Implementations:**
    *   `OllamaProvider`: Communicates with the local Ollama server via its REST API.
    *   `OpenAIProvider`: Communicates with the OpenAI API using their official client library.
    *   (Future: `AnthropicProvider`, `GroqProvider`, etc.)
*   The Orchestrator uses the PAL, so its code never needs to change when a new provider is added.

### 4. Tool Registry & Executor
Manages the modular tools that extend Sam AI's capabilities in Agent mode.

*   **Tool Registry:** A catalog of available Python functions. Each tool is registered with a name, description, and the function itself.
*   **Executor:** Responsible for safely calling the Python function when requested by the AI model.
*   **Example Tools:** `read_file(filename)`, `web_search(query)`, `get_weather(location)`.

### 5. AI Providers
The external services that provide the LLM capabilities. The Core communicates with them via the PAL.

*   **Local (Ollama):** Runs on the user's machine. The default for privacy.
*   **Cloud (OpenAI, etc.):** Requires an internet connection and an API key. Used for maximum capability.

### 6. Data Flow: Handling a User Query

1.  **User Input:** A user sends a message and selects "Agent Mode".
2.  **Client -> Core:** The Client sends the message and mode to the Core's Orchestrator.
3.  **Context Enrichment:** The Orchestrator asks the Memory Manager for relevant conversation history and long-term context.
4.  **Prompt Construction:** The Orchestrator constructs a full prompt, including the context, the user's query, and instructions for tool usage.
5.  **LLM Request:** The Orchestrator uses the PAL to send the prompt to the user's configured AI Provider (e.g., ` OllamaProvider` for `llama3`).
6.  **Tool Use (Agent Mode):** The LLM returns a request to use a tool (e.g., `{"function": "read_file", "arguments": {"filename": "goals.txt"}}`).
7.  **Tool Execution:** The Orchestrator passes this request to the Tool Executor, which safely runs the `read_file` function and gets the result.
8.  **LLM Response:** The Orchestrator sends the tool's result back to the LLM via the PAL and asks for a final response.
9.  **Core -> Client:** The Orchestrator sends the LLM's final response back to the Client.
10. **Memory Update:** The Memory Manager saves the new interaction to the conversation history and potentially to long-term storage.
11. **Render:** The Client displays the response to the user.
