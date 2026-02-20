"""Cursor hook: runs validation when recipes.json is edited."""
import json
import subprocess
import sys
from pathlib import Path

# Read Cursor's payload from stdin
try:
    payload = json.load(sys.stdin)
except json.JSONDecodeError:
    sys.exit(0)

file_path = payload.get("file_path", "")
if "recipes.json" in file_path.replace("\\", "/"):
    project_root = Path(__file__).parent.parent.parent
    validate_script = project_root / "scripts" / "validate_recipes.py"
    result = subprocess.run([sys.executable, str(validate_script)], capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stderr, file=sys.stderr)
        sys.exit(result.returncode)
