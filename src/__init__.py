"""Smart Recipe & Meal Planner - Core modules."""
from src.nutrition import lookup_nutrition
from src.recipes import suggest_recipes, generate_weekly_plan
from src.shopping_list import create_shopping_list

__all__ = ["lookup_nutrition", "suggest_recipes", "generate_weekly_plan", "create_shopping_list"]
