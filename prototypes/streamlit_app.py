"""
Streamlit prototype UI for Sam AI.
"""

import streamlit as st
import time
from src.sam_ai.core.engine import Orchestrator
from src.sam_ai.config import settings, load_config

# Page configuration
st.set_page_config(
    page_title="Sam AI - Prototype",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "orchestrator" not in st.session_state:
    st.session_state.orchestrator = Orchestrator()
if "current_mode" not in st.session_state:
    st.session_state.current_mode = "chat"

def initialize_app():
    """Initialize the application."""
    load_config()
    if "orchestrator" not in st.session_state:
        st.session_state.orchestrator = Orchestrator()

def clear_chat():
    """Clear the chat history."""
    st.session_state.messages = []
    st.session_state.orchestrator.clear_memory()
    st.rerun()

# App title and description
st.title("🤖 Sam AI - Prototype")
st.markdown("""
A modular, portable, and trauma-informed AI personal assistant.
*Currently in development - this is a prototype UI.*
""")

# Sidebar for configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Provider selection
    provider = st.selectbox(
        "AI Provider",
        ["ollama", "openai"],
        index=0,
        help="Choose which AI provider to use"
    )
    
    # Model selection
    if provider == "ollama":
        model = st.selectbox(
            "Model",
            ["phi3", "llama3:8b", "llama3:70b", "mistral", "mixtral"],
            index=0
        )
    else:
        model = st.selectbox(
            "Model",
            ["gpt-4o", "gpt-4-turbo", "gpt-3.5-turbo"],
            index=0
        )
    
    # Mode selection
    mode = st.radio(
        "Mode",
        ["chat", "agent"],
        index=0,
        horizontal=True,
        help="Chat mode for conversation, Agent mode for task execution"
    )
    
    # API key input for OpenAI
    if provider == "openai":
        api_key = st.text_input(
            "OpenAI API Key",
            type="password",
            help="Enter your OpenAI API key"
        )
        if api_key:
            try:
                st.session_state.orchestrator.provider.update_api_key(api_key)
                st.success("API key updated successfully")
            except Exception as e:
                st.error(f"Error updating API key: {e}")
    
    # Clear chat button
    if st.button("🗑️ Clear Chat", use_container_width=True):
        clear_chat()
    
    st.divider()
    st.markdown("**Debug Info**")
    st.text(f"Provider: {provider}")
    st.text(f"Model: {model}")
    st.text(f"Mode: {mode}")
    st.text(f"Messages: {len(st.session_state.messages)}")

# Main chat interface
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to talk about?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Display assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            # Get response from orchestrator
            response = st.session_state.orchestrator.process_message(prompt, mode)
            full_response = response
            
        except Exception as e:
            full_response = f"❌ Error: {str(e)}\n\nPlease check your configuration and ensure Ollama is running if using local models."
        
        # Display the response
        message_placeholder.markdown(full_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Initialize the app
initialize_app()