#!/usr/bin/env python3
# test_sam.py - Basic functionality test
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_basic_functionality():
    """Test basic Sam AI functionality."""
    try:
        from src.sam_ai.core.engine import Orchestrator
        from src.sam_ai.config import settings
        
        print("✓ Basic imports successful")
        print(f"Default model: {settings.default_model}")
        print(f"Default provider: {settings.default_provider}")
        
        # Test creating orchestrator
        orchestrator = Orchestrator()
        print("✓ Orchestrator created successfully")
        
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Testing Sam AI basic functionality...")
    if test_basic_functionality():
        print("🎉 All basic tests passed!")
    else:
        print("💥 Some tests failed")
        sys.exit(1)