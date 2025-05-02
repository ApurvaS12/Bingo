import streamlit as st

# Page setup
st.set_page_config(page_title="Secret Soirée Bingo", layout="centered")

# Custom styling and fonts
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
        font-weight: bold;
    }

    .unmarked {
        background-color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("The Secret Soirée Bingo")
st.markdown("Tap a tile when you meet someone:")

# Bingo prompts
prompts = [
    "Building an intelligent AI marketing tool", "Loves Marathon", "Built and Sold a Start up", "Lose track of time while cooking",
    "Believes we will have a ChatGPT widget soon!", "Met a co-creator in a club or dinner", "Is into yoga and meditation", "With whom you would like to jam on an idea later",
    "Loves discussing e-tafdas", "Built a cloud cost optimization start up", "Is a DJ", "Has had wedding choreography gigs",
    "Have an interesting story about BANANA", "Started their career as a data scientist", "Conducts dance workshops", "Heard an insight that blew your mind"
]

# Initialize session state
for i in range(len(prompts)):
    state_key = f"tile_state_{i}"
    if state_key not in st.session_state:
        st.session_state[state_key] = False

# Render 4x4 grid of tappable tiles
for i in range(0, 16, 4):
    cols = st.columns(4)
    for j in range(4):
        idx = i + j
        state_key = f"tile_state_{idx}"   # for session state
        button_key = f"btn_{idx}"         # for Streamlit widget key
        style_class = "marked" if st.session_state[state_key] else "unmarked"
        label = prompts[idx]

        with cols[j]:
            clicked = st.button(label, key=button_key, use_container_width=True)
            if clicked:
                st.session_state[state_key] = not st.session_state[state_key]

            # Re-render button style
            st.markdown(
                f"<style>button[data-testid='baseButton-{button_key}'] {{ background-color: {'#c5e1a5' if st.session_state[state_key] else 'white'}; }}</style>",
                unsafe_allow_html=True
            )
