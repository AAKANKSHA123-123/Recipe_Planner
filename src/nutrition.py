"""Nutrition lookup functions for ingredients."""
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
NUTRITION_DB_PATH = DATA_DIR / "nutrition_db.json"


def _load_nutrition_db() -> dict:
    """Load nutrition database from JSON."""
    with open(NUTRITION_DB_PATH, encoding="utf-8") as f:
        return json.load(f)


def lookup_nutrition(ingredient: str, amount_g: float = 100) -> dict | None:
    """
    Look up nutrition info for an ingredient.
    Returns calories and protein for given amount, or None if not found.
    """
    db = _load_nutrition_db()
    key = ingredient.lower().strip()
    if key not in db:
        return None
    entry = db[key]
    factor = amount_g / 100
    return {
        "ingredient": key,
        "calories": round(entry["calories_per_100g"] * factor),
        "protein_g": round(entry["protein"] * factor, 1),
        "amount_g": amount_g,
    }


def get_all_ingredients() -> list[str]:
    """Return list of all ingredients in the nutrition database."""
    db = _load_nutrition_db()
    return list(db.keys())
