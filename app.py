import streamlit as st

# Config
st.set_page_config(page_title="Secret Soirée Bingo", layout="centered")

# Load Google Fonts and styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Abril+Fatface&family=Love+Lace&display=swap');

    h1 {
        font-family: 'Abril Fatface', cursive;
        text-align: center;
        margin-bottom: 1rem;
        font-size: 2.5em;
    }

    .stButton > button {
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
    }

    .green-btn {
        background-color: #8BC34A !important;
        color: black !important;
        font-weight: bold;
    }

    .white-btn {
        background-color: white !important;
        color: black !important;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("The Secret Soirée Bingo")
st.markdown("Tap a tile when you meet someone:")

# Static tile prompts
prompts = [
    "Building an intelligent AI marketing tool", "Loves Marathon", "Built and Sold a Start up", "Lose track of time while cooking",
    "Believes we will have a ChatGPT widget soon!", "Met a co-creator in a club or dinner", "Is into yoga and meditation", "With whom you would like to jam on an idea later",
    "Loves discussing e-tafdas", "Built a cloud cost optimization start up", "Is a DJ", "Has had wedding choreography gigs",
    "Have an interesting story about BANANA", "Started their career as a data scientist", "Conducts dance workshops", "Heard an insight that blew your mind"
]

# Initialize state
for i in range(len(prompts)):
    state_key = f"tile_{i}"
    if state_key not in st.session_state:
        st.session_state[state_key] = False

# Render 4x4 grid
for i in range(0, 16, 4):
    cols = st.columns(4)
    for j in range(4):
        idx = i + j
        btn_key = f"btn_{idx}"
        state_key = f"tile_{idx}"

        with cols[j]:
            clicked = st.button(prompts[idx], key=btn_key, use_container_width=True)
            if clicked:
                st.session_state[state_key] = not st.session_state[state_key]

            # Inject matching style post-render
            style = "green-btn" if st.session_state[state_key] else "white-btn"
            st.markdown(f"""
                <script>
                const btn = window.parent.document.querySelector('button[data-testid="baseButton-{btn_key}"]');
                if (btn) {{
                    btn.classList.remove('green-btn', 'white-btn');
                    btn.classList.add('{style}');
                }}
                </script>
            """, unsafe_allow_html=True)
