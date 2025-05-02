import streamlit as st

# Set up the page
st.set_page_config(page_title="Secret Soirée Bingo", layout="centered")

# Inject custom styles and fonts
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Abril+Fatface&family=Love+Lace&display=swap');

    h1 {
        font-family: 'Abril Fatface', cursive;
        text-align: center;
        margin-bottom: 1rem;
    }

    .bingo-button {
        font-family: 'Love Lace', cursive;
        font-style: italic;
        font-size: 13px;
        height: 100px;
        padding: 10px;
        white-space: normal;
        border-radius: 10px;
        width: 100%;
        border: 1px solid #ccc;
        text-align: center;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .marked {
        background-color: #c5e1a5;
    }

    .unmarked {
        background-color: white;
    }

    .stForm {
        padding: 0;
    }

    button {
        margin-top: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

st.title("The Secret Soirée Bingo")
st.markdown("Tap a tile when you meet someone:")

# List of prompts for the bingo tiles
prompts = [
    "Building an intelligent AI marketing tool", "Loves Marathon", "Built and Sold a Start up", "Lose track of time while cooking",
    "Believes we will have a ChatGPT widget soon!", "Met a co-creator in a club or dinner", "Is into yoga and meditation", "With whom you would like to jam on an idea later",
    "Loves discussing e-tafdas", "Built a cloud cost optimization start up", "Is a DJ", "Has had wedding choreography gigs",
    "Have an interesting story about BANANA", "Started their career as a data scientist", "Conducts dance workshops", "Heard an insight that blew your mind"
]

# Initialize selection state
for i in range(len(prompts)):
    key = f"tile_{i}"
    if key not in st.session_state:
        st.session_state[key] = False

# Render the 4x4 grid
for i in range(0, 16, 4):
    cols = st.columns(4)
    for j in range(4):
        idx = i + j
        key = f"tile_{idx}"
        with cols[j]:
            with st.form(f"form_{idx}"):
                # Apply style based on selection
                style = "marked" if st.session_state[key] else "unmarked"
                tile_html = f'<div class="bingo-button {style}">{prompts[idx]}</div>'
                st.markdown(tile_html, unsafe_allow_html=True)
                clicked = st.form_submit_button("Tap", use_container_width=True)
                if clicked:
                    st.session_state[key] = not st.session_state[key]
                    st.experimental_rerun()
