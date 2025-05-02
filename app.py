import streamlit as st

# Page config
st.set_page_config(page_title="Secret Soirée Bingo", layout="centered")

# Fonts and custom styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Abril+Fatface&family=Love+Lace&display=swap');

    h1 {
        font-family: 'Abril Fatface', cursive;
        text-align: center;
        font-size: 2.5em;
        margin-bottom: 1rem;
    }

    .bingo-btn {
        font-family: 'Love Lace', cursive;
        font-style: italic;
        font-size: 14px;
        height: 120px !important;
        width: 100% !important;
        white-space: normal !important;
        line-height: 1.2;
        border-radius: 10px;
        padding: 10px;
        border: 1px solid #ccc;
        text-align: center;
    }

    .marked {
        background-color: #8BC34A !important;
        color: black !important;
        font-weight: bold;
    }

    .unmarked {
        background-color: white !important;
        color: black !important;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("The Secret Soirée Bingo")
st.markdown("Tap each tile as you meet someone. Selections stay marked! 🎯")

# Bingo prompts
prompts = [
    "Building an intelligent AI marketing tool", "Loves Marathon", "Built and Sold a Start up", "Lose track of time while cooking",
    "Believes we will have a ChatGPT widget soon!", "Met a co-creator in a club or dinner", "Is into yoga and meditation", "With whom you would like to jam on an idea later",
    "Loves discussing e-tafdas", "Built a cloud cost optimization start up", "Is a DJ", "Has had wedding choreography gigs",
    "Have an interesting story about BANANA", "Started their career as a data scientist", "Conducts dance workshops", "Heard an insight that blew your mind"
]

# Initialize state for all tiles
for i in range(len(prompts)):
    if f"tile_selected_{i}" not in st.session_state:
        st.session_state[f"tile_selected_{i}"] = False

# Render 4x4 tile grid
for i in range(0, 16, 4):
    cols = st.columns(4)
    for j in range(4):
        idx = i + j
        state_key = f"tile_selected_{idx}"
        tile_text = prompts[idx]

        with cols[j]:
            # Button-like container with consistent height
            is_selected = st.session_state[state_key]
            css_class = "bingo-btn marked" if is_selected else "bingo-btn unmarked"

            if st.button(tile_text, key=f"tile_btn_{idx}", use_container_width=True):
                # Toggle only this tile’s selection
                st.session_state[state_key] = not is_selected

            # Post-render CSS injection
            st.markdown(f"""
                <style>
                button[data-testid="baseButton-tile_btn_{idx}"] {{
                    background-color: {'#8BC34A' if is_selected else 'white'} !important;
                    color: black;
                    font-weight: {'bold' if is_selected else 'normal'};
                    font-family: 'Love Lace', cursive;
                    font-style: italic;
                    font-size: 14px;
                    height: 120px;
                    border-radius: 10px;
                    padding: 10px;
                    border: 1px solid #ccc;
                    white-space: normal;
                    line-height: 1.2;
                }}
                </style>
            """, unsafe_allow_html=True)
