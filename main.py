from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from pathlib import Path
import subprocess

app = FastAPI()

SCRIPTS_DIR = Path(__file__).parent / "scripts"
PROJECT_ROOT = Path(__file__).parent

@app.get("/")
async def root():
    return {"message": "Hello, from your GitHub-integrated API!"}

@app.get("/list-scripts")
async def list_scripts():
    scripts = [str(script.relative_to(SCRIPTS_DIR)) for script in SCRIPTS_DIR.glob("*.sh")]
    return {"scripts": scripts}

@app.post("/run-script")
async def run_script(script_name: str, args: list[str] = []):
    script_path = SCRIPTS_DIR / script_name
    if not script_path.exists() or not script_path.is_file():
        raise HTTPException(status_code=404, detail=f"Script {script_name} not found.")
    try:
        result = subprocess.run(
            [str(script_path), *args],
            cwd=str(PROJECT_ROOT),
            capture_output=True,
            text=True
        )
        return {
            "success": result.returncode == 0,
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
            "return_code": result.returncode,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to run script: {e}")

@app.post("/git-sync")
async def git_sync(message: str = "Update API"):
    try:
        subprocess.run(["git", "-C", str(SCRIPTS_DIR), "pull"], check=True)
        subprocess.run(["git", "-C", str(SCRIPTS_DIR), "add", "."], check=True)
        subprocess.run(["git", "-C", str(SCRIPTS_DIR), "commit", "-m", message], check=True)
        subprocess.run(["git", "-C", str(SCRIPTS_DIR), "push"], check=True)
        return {"message": "Git synchronization complete."}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Git operation failed: {e}")
