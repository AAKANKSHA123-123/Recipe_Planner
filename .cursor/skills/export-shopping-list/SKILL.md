---
name: export-shopping-list
description: Export shopping list as CSV. Use when the user says "Export shopping list" or asks to download the shopping list.
commands:
  - "Export shopping list"
  - "/export-shopping-list"
---

# Export Shopping List (Command)

## Purpose
Respond to the command "Export shopping list" by creating and offering a CSV download.

## In-App Flow
1. User must have a meal plan generated first.
2. User clicks "Export shopping list (CSV)" button.
3. App creates list via `create_shopping_list(meal_plan)` and `shopping_list_to_csv()`.
4. Streamlit `st.download_button` provides the CSV file.

## Implementation Check

```python
from src.shopping_list import create_shopping_list, shopping_list_to_csv

shop_list = create_shopping_list(meal_plan)
csv = shopping_list_to_csv(shop_list)
# csv is ready for st.download_button(data=csv, file_name="shopping_list.csv", mime="text/csv")
```

## Execute (CLI)

When user invokes `/export-shopping-list` or "Export shopping list", run:

```bash
python .cursor/skills/export-shopping-list/scripts/export_shopping_list_cli.py [ingredient1] [ingredient2] ...
```

Example: `python .cursor/skills/export-shopping-list/scripts/export_shopping_list_cli.py chicken rice broccoli`

Generates a meal plan from ingredients, creates shopping list, and writes `shopping_list.csv` to project root. If no ingredients provided, uses defaults: chicken, rice, broccoli.

## When User Asks "Export shopping list"

1. Run the script above with their ingredients (or defaults).
2. Confirm the CSV was written to project root.
