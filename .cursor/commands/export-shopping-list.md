# Export Shopping List

**Slash:** `/export-shopping-list`  
**Natural language:** "Export shopping list"

## Purpose
Export the meal plan ingredients as a CSV shopping list.

## Skill
Use the `export-shopping-list` skill (`.cursor/skills/export-shopping-list/`).

## Execute
Run: `python .cursor/skills/export-shopping-list/scripts/export_shopping_list_cli.py [ingredient1] [ingredient2] ...`

## Flow
1. Run the CLI script with ingredients (or use defaults: chicken, rice, broccoli)
2. Script generates meal plan, creates shopping list, writes `shopping_list.csv` to project root
