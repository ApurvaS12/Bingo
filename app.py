import streamlit as st

# Set up page and fonts
st.set_page_config(page_title="The Secret Soirée Bingo", layout="centered")

# Inject custom fonts and styles
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Abril+Fatface&family=Love+Lace&display=swap');

    h1 {
        font-family: 'Abril Fatface', cursive;
        text-align: center;
    }

    .bingo-button {
        font-family: 'Love Lace', cursive;
        font-style: italic;
        font-size: 14px;
        height: 100px;
        white-space: normal;
        padding: 10px;
        border-radius: 10px;
        border: 1px solid #ddd;
    }

    .bingo-marked {
        background-color: #c5e1a5;
        color: black;
    }
    </style>
""", unsafe_allow_html=True)

st.title("The Secret Soirée Bingo")
st.markdown("Did you meet someone who...")

# Static prompt list
prompts = [
    "Building an intelligent AI marketing tool", "Loves Marathon", "Built and Sold a Start up", "Lose track of time while cooking",
    "Believes we will have a ChatGPT widget soon!", "Met a co-creator in a club or dinner", "Is into yoga and meditation", "With whom you would like to jam on an idea later",
    "Loves discussing e-tafdas", "Built a cloud cost optimization start up", "Is a DJ", "Has had wedding choreography gigs",
    "Have an interesting story about BANANA", "Started their career as a data scientist", "Conducts dance workshops", "Heard an insight that blew your mind"
]

# Display in 4x4 grid
for i in range(0, 16, 4):
    cols = st.columns(4)
    for j in range(4):
        idx = i + j
        state_key = f"selected_{idx}"
        if state_key not in st.session_state:
            st.session_state[state_key] = False

        # Custom style via
