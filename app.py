import streamlit as st

# Config
st.set_page_config(page_title="The Secret Soirée Bingo", layout="centered")

# Style and font setup
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Abril+Fatface&family=Love+Lace&display=swap');

    h1 {
        font-family: 'Abril Fatface', cursive;
        text-align: center;
        margin-bottom: 1rem;
    }

    .bingo-btn {
        font-family: 'Love Lace', cursive;
        font-style: italic;
        font-size: 13px;
        height: 100px;
        width: 100%;
        white-space: normal;
        padding: 10px;
        border-radius: 10px;
        border: 1px solid #ccc;
        text-align: center;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: white;
    }

    .bingo-btn.marked {
        background-color: #c5e1a5;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.title("The Secret Soirée Bingo")
st.markdown("Tap on a tile when you meet someone:")

# Static bingo tiles
prompts = [
    "Building an intelligent AI marketing tool", "Loves Marathon", "Built and Sold a Start up", "Lose track of time while cooking",
    "Believes we will have a ChatGPT widget soon!", "Met a co-creator in a club or dinner", "Is into yoga and meditation", "With whom you would like to jam on an idea later",
    "Loves discussing e-tafdas", "Built a cloud cost optimization start up", "Is a DJ", "Has had wedding choreography gigs",
    "Have an interesting story about BANANA", "Started their career as a data scientist", "Conducts dance workshops", "Heard an insight that blew your mind"
]

# Initialize state
for i in range(len(prompts)):
    if f"tile_{i}" not in st.session_state:
        st.session_state[f"tile_{i}"] = False

# Render 4x4 grid with styled Streamlit buttons
for i in range(0, 16, 4):
    cols = st.columns(4)
    for j in range(4):
        idx = i + j
        key = f"tile_{idx}"
        style_class = "bingo-btn marked" if st.session_state[key] else "bingo-btn"

        with cols[j]:
            if st.button(prompts[idx], key=key, use_container_width=True):
                st.session_state[key] = not st.session_state[key]

            # Inject custom style after the Streamlit button renders
            st.markdown(
                f"<style>button[data-testid='baseButton-{key}'] {{{'background-color:#c5e1a5;' if st.session_state[key] else ''}}}</style>",
                unsafe_allow_html=True
            )
