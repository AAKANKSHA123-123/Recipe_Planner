---
name: recipe-generation
description: Add recipes, apply high-calorie rule, structure recipes.json. Use when adding or modifying recipes, building recipe logic, or when the user asks about recipe generation.
---

# Recipe Generation Skill

## Purpose
Add recipes and ensure they follow the calorie rule (mark high-calorie if > 500 cal).

## Data Location
- Database: `src/data/recipes.json`
- Module: `src/recipes.py`

## Recipe Schema

Each recipe in `recipes.json` must have:

```json
{
  "id": "unique_id",
  "name": "Recipe Name",
  "ingredients": ["ingredient1", "ingredient2"],
  "calories": 420,
  "instructions": "Step-by-step instructions.",
  "servings": 2
}
```

## Rule: High-Calorie
If `calories > 500`, the recipe is marked `is_high_calorie: true` (handled in `recipes.py`).

## Adding a New Recipe

1. Add to `src/data/recipes.json` in the array.
2. Ensure `calories` is a number and `ingredients` uses lowercase names matching `nutrition_db.json` where possible.
3. Run `python scripts/validate_recipes.py` to verify schema.

## Key Functions
- `suggest_recipes(ingredients)` — suggest recipes from available ingredients
- `generate_weekly_plan(ingredients)` — create 7-day meal plan
