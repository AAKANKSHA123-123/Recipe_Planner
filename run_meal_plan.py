"""Quick script to run generate_weekly_plan for /meal-plan command."""
from src.recipes import generate_weekly_plan

ingredients = ["chicken", "rice", "broccoli"]
plan = generate_weekly_plan(ingredients, meals_per_day=2)
for entry in plan:
    r = entry["recipe"]
    high = " (high-calorie)" if r.get("is_high_calorie") else ""
    print(f"{entry['day']} Meal {entry['meal']}: {r['name']} - {r.get('calories', 0)} cal{high}")
