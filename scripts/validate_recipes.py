"""Validate recipes.json schema and calorie field. Run by Cursor hook after file edit."""
import json
import sys
from pathlib import Path

RECIPES_PATH = Path(__file__).parent.parent / "src" / "data" / "recipes.json"
REQUIRED_FIELDS = {"id", "name", "ingredients", "calories", "instructions", "servings"}


def validate():
    try:
        with open(RECIPES_PATH, encoding="utf-8") as f:
            recipes = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Validation failed: {e}", file=sys.stderr)
        sys.exit(1)

    errors = []
    for i, r in enumerate(recipes):
        if not isinstance(r, dict):
            errors.append(f"Recipe {i}: must be object")
            continue
        missing = REQUIRED_FIELDS - set(r.keys())
        if missing:
            errors.append(f"Recipe {i} ({r.get('name', '?')}): missing {missing}")
        if "calories" in r and not isinstance(r["calories"], (int, float)):
            errors.append(f"Recipe {i} ({r.get('name', '?')}): calories must be number")
        if "ingredients" in r and not isinstance(r["ingredients"], list):
            errors.append(f"Recipe {i} ({r.get('name', '?')}): ingredients must be list")

    if errors:
        for e in errors:
            print(e, file=sys.stderr)
        sys.exit(1)
    print("Recipes valid.")


if __name__ == "__main__":
    validate()
