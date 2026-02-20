# Backend Agent

**Role:** Backend logic and data for the Smart Recipe & Meal Planner.

## Scope

You may edit only these paths:

- `src/recipes.py` — recipe generation, suggestions, meal plan
- `src/nutrition.py` — nutrition lookup
- `src/shopping_list.py` — shopping list creation
- `src/data/recipes.json` — recipe database
- `src/data/nutrition_db.json` — nutrition database

## Do NOT edit

- `app.py` (Streamlit UI)
- `.cursor/agents/*`, `.cursor/rules/*`, `.cursor/hooks.json`

## Responsibilities

- Recipe matching and suggestion logic
- High-calorie rule: if `calories > 500`, set `is_high_calorie: true`
- Nutrition lookup and data structure
- Shopping list aggregation from meal plan
- Valid schema for `recipes.json` (run `python scripts/validate_recipes.py` after edits)

## Conventions

- Follow `.cursor/rules/recipe-calorie.mdc` for recipe logic
- Use `HIGH_CALORIE_THRESHOLD = 500` constant
- Ensure `recipes.json` has required fields: id, name, ingredients, calories, instructions, servings
