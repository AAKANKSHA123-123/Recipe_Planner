---
name: nutrition-lookup
description: Add or use nutrition lookup for ingredients. Use when working with ingredient nutrition, calories, extending the nutrition database, or when the user asks about nutrition lookup.
---

# Nutrition Lookup Skill

## Purpose
Look up nutrition information (calories, protein) for ingredients in the Recipe Planner.

## Data Location
- Database: `src/data/nutrition_db.json`
- Module: `src/nutrition.py`

## Adding a New Ingredient to the Database

Edit `src/data/nutrition_db.json` and add an entry:

```json
"ingredient_name": {
  "calories_per_100g": 100,
  "protein": 10,
  "unit": "g"
}
```

## Using the Lookup in Code

```python
from src.nutrition import lookup_nutrition, get_all_ingredients

# Look up nutrition for 150g of chicken
result = lookup_nutrition("chicken", 150)
# Returns: {"ingredient": "chicken", "calories": 248, "protein_g": 46.5, "amount_g": 150}

# Get all known ingredients
ingredients = get_all_ingredients()
```

## When to Use
- User asks to add nutrition for a new ingredient
- User wants to extend the nutrition database
- Implementing calorie calculations for recipes
