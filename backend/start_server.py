# Author: Daksha009
# Repo: https://github.com/Daksha009/AirSense-Guardian.git

"""
Start FastAPI server with proper error handling
"""
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    import uvicorn
    from main import app
    
    print("="*60)
    print("Starting AirSense Guardian Backend Server")
    print("="*60)
    print("Server will be available at: http://localhost:5000")
    print("API Documentation: http://localhost:5000/docs")
    print("="*60)
    print()
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=5000,
        reload=False,  # Disable reload for stability
        log_level="info"
    )
except Exception as e:
    print(f"ERROR: Failed to start server: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

