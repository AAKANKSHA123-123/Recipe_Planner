# Smart Recipe & Meal Planner

A Streamlit dashboard for planning meals from ingredients you have. Demonstrates Cursor features: Rules, Hooks, Skills, Commands, and Agents.

## Run the App

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Features

- **Ingredient entry** — Add ingredients; recipe suggestions appear automatically
- **Recipe rule** — Recipes over 500 cal are marked as high-calorie
- **Commands** — "Generate weekly meal plan" and "Export shopping list"

## Cursor Features (Demo)

| Feature | Location |
|---------|----------|
| **Rules** | `.cursor/rules/` — recipe-calorie, streamlit-ui |
| **Hooks** | `.cursor/hooks/` — after-file-edit.py validates recipes.json after edit |
| **Skills** | `.cursor/skills/` — nutrition, recipe, shopping, meal-plan, export |
| **Commands** | `.cursor/commands/` — generate-meal-plan, export-shopping-list |
| **Agents** | `.cursor/agents/` — frontagent, backend-agent, deploy-agent, plan-agent |
| **AGENTS.md** | Root coordination for all agents |

See [AGENTS.md](AGENTS.md) for agent and command usage.
