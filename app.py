"""Smart Recipe & Meal Planner - Streamlit Dashboard."""
import streamlit as st
from src.recipes import suggest_recipes, generate_weekly_plan
from src.shopping_list import create_shopping_list, shopping_list_to_csv


def init_session_state():
    """Initialize session state for ingredients and meal plan."""
    if "ingredients" not in st.session_state:
        st.session_state.ingredients = []
    if "meal_plan" not in st.session_state:
        st.session_state.meal_plan = []
    if "suggestions" not in st.session_state:
        st.session_state.suggestions = []
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False


def inject_dark_mode_css():
    """Inject dark mode CSS when toggle is on."""
    if st.session_state.get("dark_mode"):
        st.markdown("""
            <style>
                .stApp { background-color: #1e1e1e; }
                [data-testid="stAppViewContainer"] { background-color: #1e1e1e; }
                [data-testid="stHeader"] { background-color: #2d2d2d; }
                .block-container { background-color: #1e1e1e; color: #e0e0e0; }
                p, span, div { color: #e0e0e0 !important; }
                h1, h2, h3 { color: #ffffff !important; }
                label { color: #e0e0e0 !important; }
            </style>
        """, unsafe_allow_html=True)


def on_ingredient_added():
    """Hook: when new ingredient is added, suggest recipes."""
    ingredients = st.session_state.get("ingredients", [])
    st.session_state.suggestions = suggest_recipes(ingredients)


def main():
    st.set_page_config(page_title="Smart Recipe & Meal Planner", page_icon="🍳", layout="wide")
    init_session_state()

    with st.sidebar:
        st.toggle("Dark mode", value=st.session_state.get("dark_mode", False), key="dark_mode")
    inject_dark_mode_css()

    st.title("🍳 Smart Recipe & Meal Planner")
    st.markdown("Enter ingredients you have — we suggest recipes and help you plan meals.")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("My Ingredients")
        new_ing = st.text_input(
            "Add ingredient",
            placeholder="e.g. chicken, rice, broccoli",
            key="new_ingredient_input",
        )
        if st.button("Add", key="add_btn"):
            if new_ing and new_ing.strip():
                ing = new_ing.strip().lower()
                if ing not in [x.lower() for x in st.session_state.ingredients]:
                    st.session_state.ingredients.append(ing)
                    on_ingredient_added()
                st.rerun()

        if st.session_state.ingredients:
            for i, ing in enumerate(st.session_state.ingredients):
                ic, dc = st.columns([3, 1])
                with ic:
                    st.text(ing.title())
                with dc:
                    if st.button("✕", key=f"del_{i}"):
                        st.session_state.ingredients.pop(i)
                        on_ingredient_added()
                        st.rerun()

    with col2:
        st.subheader("Recipe Suggestions")
        if st.session_state.ingredients:
            if not st.session_state.suggestions:
                on_ingredient_added()
            for r in st.session_state.suggestions[:8]:
                high = " 🔴 High-calorie" if r.get("is_high_calorie") else ""
                st.markdown(f"**{r['name']}** ({r['calories']} cal{high})")
                st.caption(", ".join(r["ingredients"]))
        else:
            st.info("Add ingredients above to see recipe suggestions.")

    st.divider()
    st.subheader("Commands")

    cmd_col1, cmd_col2 = st.columns(2)

    with cmd_col1:
        if st.button("📅 Generate weekly meal plan", type="primary"):
            if st.session_state.ingredients:
                st.session_state.meal_plan = generate_weekly_plan(st.session_state.ingredients, meals_per_day=2)
                st.success("Meal plan generated!")
                st.rerun()
            else:
                st.warning("Add ingredients first.")

    with cmd_col2:
        if st.session_state.meal_plan:
            shop_list = create_shopping_list(st.session_state.meal_plan)
            csv = shopping_list_to_csv(shop_list)
            st.download_button(
                "📋 Export shopping list (CSV)",
                data=csv,
                file_name="shopping_list.csv",
                mime="text/csv",
            )
        else:
            st.button("📋 Export shopping list (CSV)", disabled=True)

    if st.session_state.meal_plan:
        st.subheader("Weekly Meal Plan")
        for entry in st.session_state.meal_plan:
            day, meal, recipe = entry["day"], entry["meal"], entry["recipe"]
            high = " 🔴 High-calorie" if recipe.get("is_high_calorie") else ""
            st.markdown(f"**{day}** Meal {meal}: {recipe['name']} ({recipe['calories']} cal{high})")


if __name__ == "__main__":
    main()
