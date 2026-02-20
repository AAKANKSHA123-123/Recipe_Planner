"""CLI for /export-shopping-list command. Generates meal plan and exports shopping list as CSV."""
import sys
from pathlib import Path

# Add project root to path (scripts/export-shopping-list/skills/.cursor/)
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent.parent))

from src.recipes import generate_weekly_plan
from src.shopping_list import create_shopping_list, shopping_list_to_csv

DEFAULT_INGREDIENTS = ["chicken", "rice", "broccoli"]
OUTPUT_FILE = "shopping_list.csv"


def main():
    if len(sys.argv) > 1:
        ingredients = [arg.strip().lower() for arg in sys.argv[1:] if arg.strip()]
    else:
        ingredients = DEFAULT_INGREDIENTS

    plan = generate_weekly_plan(ingredients, meals_per_day=2)
    shop_list = create_shopping_list(plan)
    csv = shopping_list_to_csv(shop_list)

    project_root = Path(__file__).parent.parent.parent.parent.parent
    output_path = project_root / OUTPUT_FILE
    output_path.write_text(csv, encoding="utf-8")
    print(f"Exported to {output_path}")


if __name__ == "__main__":
    main()
