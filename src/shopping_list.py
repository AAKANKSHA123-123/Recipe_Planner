"""Shopping list creation from meal plan."""
from collections import defaultdict


def create_shopping_list(meal_plan: list[dict], servings_multiplier: float = 1.0) -> dict[str, float]:
    """
    Create shopping list from a meal plan.
    Aggregates ingredients with quantities (assumes 1 unit per recipe serving).
    Returns dict of ingredient -> quantity.
    """
    quantities: dict[str, float] = defaultdict(float)
    for entry in meal_plan:
        recipe = entry.get("recipe", {})
        servings = recipe.get("servings", 2)
        factor = (servings_multiplier / servings) if servings else 1
        for ing in recipe.get("ingredients", []):
            key = ing.lower().strip()
            quantities[key] += 1 * factor
    return dict(quantities)


def shopping_list_to_csv(shopping_list: dict[str, float]) -> str:
    """Convert shopping list to CSV format for export."""
    lines = ["ingredient,quantity\n"]
    for ing, qty in sorted(shopping_list.items()):
        lines.append(f"{ing},{round(qty, 1)}\n")
    return "".join(lines)
