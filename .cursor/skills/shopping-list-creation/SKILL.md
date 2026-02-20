---
name: shopping-list-creation
description: Create shopping list from meal plan and export to CSV. Use when implementing shopping list logic, export formats, or when the user asks to export a shopping list.
---

# Shopping List Creation Skill

## Purpose
Aggregate ingredients from a meal plan into a shopping list and export (CSV).

## Module Location
- `src/shopping_list.py`

## Functions

```python
from src.shopping_list import create_shopping_list, shopping_list_to_csv

# meal_plan: list of {day, meal, recipe}
shop_list = create_shopping_list(meal_plan, servings_multiplier=1.0)
# Returns: {"chicken": 2.5, "rice": 3, ...}

csv_content = shopping_list_to_csv(shop_list)
# Returns CSV string for download
```

## Export in Streamlit

```python
st.download_button(
    "Export shopping list (CSV)",
    data=shopping_list_to_csv(create_shopping_list(meal_plan)),
    file_name="shopping_list.csv",
    mime="text/csv",
)
```

## When to Use
- User asks to export shopping list
- Adding PDF export (future)
- Modifying aggregation logic
