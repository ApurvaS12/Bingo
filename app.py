import streamlit as st

# Page setup and font imports
st.set_page_config(page_title="The Secret Soirée Bingo", layout="centered")

# Add Google Fonts and button styles
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
        height: 100px;
        width: 100%;
        white-space: normal;
        padding: 10px;
        border-radius: 10px;
        border: none;
        text-align: center;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .bingo-marked {
        background-color: #c5e1a5;
        color: black;
    }

    .bingo-unmarked {
        background-color: #ffffff;
        color: #000;
        border: 1px solid #ccc;
    }

    button:focus { outline: none; }
    </style>
""", unsafe_allow_html=True)

# Page title
st.title("The Secret Soirée Bingo")
st.markdown("Tap on a tile when you meet someone that fits the description:")

# Bingo prompts (fixed 4x4 grid)
prompts = [
    "Building an intelligent AI marketing tool", "Loves Marathon", "Built and Sold a Start up", "Lose track of time while cooking",
    "Believes we will have a ChatGPT widget soon!", "Met a co-creator in a club or dinner", "Is into yoga and meditation", "With whom you would like to jam on an idea later",
    "Loves discussing e-tafdas", "Built a cloud cost optimization start up", "Is a DJ", "Has had wedding choreography gigs",
    "Have an interesting story about BANANA", "Started their career as a data scientist", "Conducts dance workshops", "Heard an insight that blew your mind"
]

# Render 4x4 grid of styled buttons
for i in range(0, 16, 4):
    cols = st.columns(4)
    for j in range(4):
        idx = i + j
        key = f"tile_{idx}"
        if key not in st.session_state:
            st.session_state[key] = False

        style = "bingo-marked" if st.session_state[key] else "bingo-unmarked"
        button_html = f"""
        <button class="bingo-tile {style}" onclick="fetch('/?{key}=toggle', {{method: 'GET'}})">
            {prompts[idx]}
        </button>
        """
        with cols[j]:
            if st.button(prompts[idx], key=f"btn_{idx}"):
                st.session_state[key] = not st.session_state[key]
            # Replace default button with styled visual
            st.markdown(
                f"<div class='bingo-tile {style}'>{prompts[idx]}</div>",
                unsafe_allow_html=True
            )
