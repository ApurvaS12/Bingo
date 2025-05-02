import streamlit as st

# Page setup
st.set_page_config(page_title="The Secret Soirée Bingo", layout="centered")

# Load fonts and custom styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Abril+Fatface&family=Love+Lace&display=swap');

    h1 {
        font-family: 'Abril Fatface', cursive;
        text-align: center;
        margin-bottom: 0.5em;
    }

    .bingo-tile {
        font-family: 'Love Lace', cursive;
        font-style: italic;
        font-size: 14px;
        height: 100px;
        white-space: normal;
        padding: 10px;
        border-radius: 10px;
        border: 1px solid #ccc;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
    }

    .marked {
        background-color: #c5e1a5;
        font-weight: bold;
    }

    .unmarked {
        background-color: #fff;
    }

    button[title="tile-btn"] {
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("The Secret Soirée Bingo")
st.markdown("Tap a tile when you meet someone that fits the description:")

# Prompts (fixed)
prompts = [
    "Building an intelligent AI marketing tool", "Loves Marathon", "Built and Sold a Start up", "Lose track of time while cooking",
    "Believes we will have a ChatGPT widget soon!", "Met a co-creator in a club or dinner", "Is into yoga and meditation", "With whom you would like to jam on an idea later",
    "Loves discussing e-tafdas", "Built a cloud cost optimization start up", "Is a DJ", "Has had wedding choreography gigs",
    "Have an interesting story about BANANA", "Started their career as a data scientist", "Conducts dance workshops", "Heard an insight that blew your mind"
]

# Initialize session state
for idx in range(len(prompts)):
    key = f"tile_{idx}"
    if key not in st.session_state:
        st.session_state[key] = False

# Display grid
for i in range(0, 16, 4):
    cols = st.columns(4)
    for j in range(4):
        idx = i + j
        key = f"tile_{idx}"
        label = prompts[idx]
        style = "marked" if st.session_state[key] else "unmarked"
        button_label = f'<div class="bingo-tile {style}">{label}</div>'

        with cols[j]:
            if st.button(button_label, key=f"btn_{idx}", help="Tap to mark/unmark", use_container_width=True):
                st.session_state[key] = not st.session_state[key]
