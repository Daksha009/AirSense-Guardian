"""
Test backend startup
"""
import sys
import os

print("Testing backend startup...")
print(f"Current directory: {os.getcwd()}")
print(f"Python path: {sys.path[:3]}")

try:
    print("\n1. Testing imports...")
    from models.predictor import AQIPredictor
    print("   [OK] Predictor imported")
    
    from models.source_attribution import SourceAttribution
    print("   [OK] SourceAttribution imported")
    
    from models.action_engine import ActionEngine
    print("   [OK] ActionEngine imported")
    
    print("\n2. Initializing models...")
    predictor = AQIPredictor()
    print("   [OK] Predictor initialized")
    
    source_attributor = SourceAttribution()
    print("   [OK] SourceAttributor initialized")
    
    action_engine = ActionEngine()
    print("   [OK] ActionEngine initialized")
    
    print("\n3. Testing FastAPI app...")
    from main import app
    print("   [OK] FastAPI app imported")
    
    print("\n[SUCCESS] All tests passed! Backend should start successfully.")
    print("\nTo start the server, run:")
    print("   python start_server.py")
    print("   or")
    print("   python main.py")
    
except Exception as e:
    print(f"\n[ERROR] {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

