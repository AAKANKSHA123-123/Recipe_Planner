"""Recipe generation logic with high-calorie rule."""
import json
import random
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
RECIPES_PATH = DATA_DIR / "recipes.json"

# Rule: If recipe has > 500 calories, mark as high-calorie
HIGH_CALORIE_THRESHOLD = 500


def _load_recipes() -> list[dict]:
    """Load recipes from JSON."""
    with open(RECIPES_PATH, encoding="utf-8") as f:
        return json.load(f)


def _apply_high_calorie_rule(recipe: dict) -> dict:
    """Apply rule: if calories > 500, mark as high-calorie."""
    calories = recipe.get("calories", 0)
    recipe["is_high_calorie"] = calories > HIGH_CALORIE_THRESHOLD
    return recipe


def suggest_recipes(available_ingredients: list[str]) -> list[dict]:
    """
    Suggest recipes based on available ingredients.
    Returns recipes that can be made with the given ingredients.
    Each recipe has is_high_calorie=True if calories > 500.
    """
    recipes = _load_recipes()
    ingredients_lower = [i.lower().strip() for i in available_ingredients]
    suggested = []
    for recipe in recipes:
        recipe_ingredients = [x.lower() for x in recipe.get("ingredients", [])]
        matches = sum(1 for ri in recipe_ingredients if ri in ingredients_lower)
        if matches > 0:
            recipe_copy = recipe.copy()
            recipe_copy["match_score"] = matches / len(recipe_ingredients) if recipe_ingredients else 0
            suggested.append(_apply_high_calorie_rule(recipe_copy))
    suggested.sort(key=lambda r: r["match_score"], reverse=True)
    return suggested


def generate_weekly_plan(available_ingredients: list[str], meals_per_day: int = 2) -> list[dict]:
    """
    Generate a 7-day meal plan using available ingredients.
    Returns list of {day, meal, recipe} entries.
    """
    recipes = _load_recipes()
    ingredients_lower = [i.lower().strip() for i in available_ingredients]
    eligible = [
        _apply_high_calorie_rule(r.copy())
        for r in recipes
        if any(ri.lower() in ingredients_lower for ri in r.get("ingredients", []))
    ]
    plan = []
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in days:
        for meal_num in range(meals_per_day):
            if eligible:
                recipe = random.choice(eligible)
                plan.append({"day": day, "meal": meal_num + 1, "recipe": recipe})
    return plan
