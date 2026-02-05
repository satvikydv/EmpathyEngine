import uvicorn
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

if "PYTHONPATH" in os.environ:
    os.environ["PYTHONPATH"] = parent_dir + os.pathsep + os.environ["PYTHONPATH"]
else:
    os.environ["PYTHONPATH"] = parent_dir

if __name__ == "__main__":
    print(f"Starting The Empathy Engine Web Server...")
    print(f"Project Root (added to PYTHONPATH): {parent_dir}")
    print("Open http://localhost:8000 in your browser.")
    
    uvicorn.run("empathy_engine.api.app:app", host="127.0.0.1", port=8000, reload=True)
