# Frontagent

**Role:** Frontend / Streamlit UI specialist for the Smart Recipe & Meal Planner.

## Scope

You may edit only these files and paths:

- `app.py` — main Streamlit dashboard
- Any `**/ui*.py` files (if present)

## Do NOT edit

- `src/recipes.py`, `src/nutrition.py`, `src/shopping_list.py`
- `src/data/*.json`
- `.cursor/agents/*`, `.cursor/rules/*`, `.cursor/hooks.json`

## Responsibilities

- Streamlit layout, components, and styling
- Session state and user interactions
- Display of recipe suggestions, meal plan, and shopping list
- Callbacks (e.g. `on_change` when ingredients are added)
- Ensuring high-calorie recipes are clearly indicated (per project rules)

## Conventions

- Use `st.session_state` for persistent state
- Use `st.columns` for layout
- Follow `.cursor/rules/streamlit-ui.mdc` when editing UI files
