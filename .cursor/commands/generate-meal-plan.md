# Generate Weekly Meal Plan

**Slash:** `/meal-plan`  
**Natural language:** "Generate weekly meal plan"

## Purpose
Create a 7-day meal plan from available ingredients.

## Skill
Use the `generate-meal-plan` skill (`.cursor/skills/generate-meal-plan/`).

## Execute
Run: `python .cursor/skills/generate-meal-plan/scripts/generate_meal_plan_cli.py [ingredient1] [ingredient2] ...`

## Flow
1. Run the CLI script with ingredients (or use defaults: chicken, rice, broccoli)
2. Script calls `generate_weekly_plan()` from `src/recipes.py`
3. Display the printed meal plan
