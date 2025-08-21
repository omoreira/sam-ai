#!/usr/bin/env python3
"""
Helper script to install Ollama on different platforms.
"""

import os
import sys
import platform
import subprocess
import requests

def install_ollama_linux():
    """Install Ollama on Linux systems."""
    print("Installing Ollama on Linux...")
    
    try:
        # Use the official install script
        result = subprocess.run(
            "curl -fsSL https://ollama.com/install.sh | sh",
            shell=True,
            check=True,
            capture_output=True,
            text=True
        )
        print("Ollama installed successfully!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"Error installing Ollama: {e}")
        print(f"STDERR: {e.stderr}")
        return False

def install_ollama_macos():
    """Install Ollama on macOS."""
    print("Installing Ollama on macOS...")
    
    try:
        # Download and install
        subprocess.run(
            "curl -fsSL https://ollama.com/install.sh | sh",
            shell=True,
            check=True
        )
        print("Ollama installed successfully!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"Error installing Ollama: {e}")
        return False

def install_ollama_windows():
    """Install Ollama on Windows."""
    print("Installing Ollama on Windows...")
    
    try:
        # Download the installer
        url = "https://ollama.com/download/OllamaSetup.exe"
        installer_path = os.path.join(os.environ['TEMP'], "OllamaSetup.exe")
        
        print("Downloading Ollama installer...")
        response = requests.get(url, stream=True)
        with open(installer_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        # Run the installer
        print("Running installer...")
        subprocess.run([installer_path, "/S"], check=True)
        print("Ollama installed successfully!")
        return True
        
    except Exception as e:
        print(f"Error installing Ollama: {e}")
        return False

def main():
    """Main installation function."""
    system = platform.system().lower()
    
    print(f"Detected system: {system}")
    print("This script will attempt to install Ollama...")
    
    if system == "linux":
        success = install_ollama_linux()
    elif system == "darwin":  # macOS
        success = install_ollama_macos()
    elif system == "windows":
        success = install_ollama_windows()
    else:
        print(f"Unsupported system: {system}")
        success = False
    
    if success:
        print("\n🎉 Installation complete!")
        print("Please start Ollama by running: ollama serve")
        print("Then pull a model: ollama pull phi3")
    else:
        print("\n❌ Installation failed.")
        print("Please install Ollama manually from https://ollama.com")
        sys.exit(1)

if __name__ == "__main__":
    main()