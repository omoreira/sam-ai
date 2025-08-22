#!/usr/bin/env python3
# run_sam.py - The reliable way to run Sam AI
import os
import sys
import subprocess

def main():
    """Run Sam AI with proper Python path configuration."""
    # Get the project root directory
    project_root = os.path.dirname(os.path.abspath(__file__))
    
    print(f"Project root: {project_root}")
    print("Starting Sam AI...")
    
    # Set the Python path
    env = os.environ.copy()
    if 'PYTHONPATH' in env:
        env['PYTHONPATH'] = project_root + os.pathsep + env['PYTHONPATH']
    else:
        env['PYTHONPATH'] = project_root
    
    # Run streamlit with the proper environment
    streamlit_cmd = [
        sys.executable, '-m', 'streamlit', 'run',
        'prototypes/streamlit_app.py',
        '--server.headless', 'false'
    ]
    
    print(f"Running command: {' '.join(streamlit_cmd)}")
    print(f"PYTHONPATH: {env['PYTHONPATH']}")
    
    try:
        subprocess.run(streamlit_cmd, env=env, check=True, cwd=project_root)
    except KeyboardInterrupt:
        print("\nSam AI stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"Error running Sam AI: {e}")
        print("Please make sure:")
        print("1. Ollama is installed and running (ollama serve)")
        print("2. You have pulled a model (ollama pull phi3)")
        print("3. All dependencies are installed (pip install -r requirements.txt)")

if __name__ == "__main__":
    main()