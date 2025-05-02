import streamlit as st

# Page config
st.set_page_config(page_title="Secret Soirée Bingo", layout="centered")

# Load fonts and inject styles
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Abril+Fatface&family=Love+Lace&display=swap');

    h1 {
        font-family: 'Abril Fatface', cursive;
        text-align: center;
        margin-bottom: 1rem;
    }

    .bingo-tile {
        font-family: 'Love Lace', cursive;
        font-style: italic;
        font-size: 14px;
        width: 100%;
        height: 120px;
        white-space: normal;
        padding: 10px;
        border-radius: 10px;
        border: 1px solid #ccc;
        text-align: center;
        display: flex;
        justify-content: center;
        align-items: center;
        line-height: 1.2;
    }

    .bingo-tile.marked {
        background-color: #8BC34A; /* soft green */
        color: black;
        font-weight: bold;
    }

    .bingo-tile.unmarked {
        background-color: white;
    }

    button[title^="tile-btn"] {
        height: 120px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("The Secret Soirée Bingo")
st.markdown("Tap on a tile when you meet someone:")

# Prompts
prompts = [
    "Building an intelligent AI marketing tool", "Loves Marathon", "Built and Sold a Start up", "Lose track of time while cooking",
    "Believes we will have a ChatGPT widget soon!", "Met a co-creator in a club or dinner", "Is into yoga and meditation", "With whom you would like to jam on an idea later",
    "Loves discussing e-tafdas", "Built a cloud cost optimization start up", "Is a DJ", "Has had wedding choreography gigs",
    "Have an interesting story about BANANA", "Started their career as a data scientist", "Conducts dance workshops", "Heard an insight that blew your mind"
]

# Initialize session state
for i in range(len(prompts)):
    if f"tile_state_{i}" not in st.session_state:
        st.session_state[f"tile_state_{i}"] = False

# Render 4x4 grid
for i in range(0, 16, 4):
    cols = st.columns(4)
    for j in range(4):
        idx = i + j
        state_key = f"tile_state_{idx}"
        button_key = f"tile-btn-{idx}"

        with cols[j]:
            clicked = st.button(prompts[idx], key=button_key, use_container_width=True)
            if clicked:
                st.session_state[state_key] = not st.session_state[state_key]

            # Inject style based on selected state
            st.markdown(f"""
                <style>
                button[data-testid="baseButton-{button_key}"] {{
                    background-color: {"#8BC34A" if st.session_state[state_key] else "white"};
                    font-family: 'Love Lace', cursive;
                    font-style: italic;
                    font-size: 14px;
                    height: 120px;
                    border: 1px solid #ccc;
                    border-radius: 10px;
                    padding: 10px;
                    white-space: normal;
                    line-height: 1.2;
                }}
                </style>
            """, unsafe_allow_html=True)
