---
name: generate-meal-plan
description: Generate weekly meal plan from ingredients. Use when the user says "Generate weekly meal plan" or asks to create a meal plan.
commands:
  - "Generate weekly meal plan"
  - "/meal-plan"
---

# Generate Weekly Meal Plan (Command)

## Purpose
Respond to the command "Generate weekly meal plan" by creating a 7-day plan from available ingredients.

## In-App Flow
1. User adds ingredients in the Streamlit UI.
2. User clicks "Generate weekly meal plan" button.
3. App calls `generate_weekly_plan(ingredients)` from `src/recipes.py`.
4. Plan is stored in `st.session_state.meal_plan` and displayed.

## Implementation Check

```python
from src.recipes import generate_weekly_plan

plan = generate_weekly_plan(available_ingredients, meals_per_day=2)
# Returns: [{"day": "Monday", "meal": 1, "recipe": {...}}, ...]
```

## Execute (CLI)

When user invokes `/meal-plan` or "Generate weekly meal plan", run:

```bash
python .cursor/skills/generate-meal-plan/scripts/generate_meal_plan_cli.py [ingredient1] [ingredient2] ...
```

Example: `python .cursor/skills/generate-meal-plan/scripts/generate_meal_plan_cli.py chicken rice broccoli`

If no ingredients are provided, uses defaults: chicken, rice, broccoli.

## When User Asks "Generate weekly meal plan"

1. Run the script above with their ingredients (or defaults).
2. Display the printed meal plan.
