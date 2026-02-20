"""CLI for /generate-meal-plan command. Generates weekly meal plan from ingredients."""
import sys
from pathlib import Path

# Add project root to path (scripts/generate-meal-plan/skills/.cursor/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent.parent))

from src.recipes import generate_weekly_plan

DEFAULT_INGREDIENTS = ["chicken", "rice", "broccoli"]


def main():
    if len(sys.argv) > 1:
        ingredients = [arg.strip().lower() for arg in sys.argv[1:] if arg.strip()]
    else:
        ingredients = DEFAULT_INGREDIENTS

    plan = generate_weekly_plan(ingredients, meals_per_day=2)
    for entry in plan:
        r = entry["recipe"]
        high = " (high-calorie)" if r.get("is_high_calorie") else ""
        cal = r.get("calories", 0)
        print(f"{entry['day']} Meal {entry['meal']}: {r['name']} - {cal} cal{high}")


if __name__ == "__main__":
    main()
