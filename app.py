import streamlit as st

# Set page and initial style
st.set_page_config(page_title="The Secret Soirée Bingo", layout="centered")

# Load Google Fonts using custom HTML
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Abril+Fatface&family=Love+Lace&display=swap');

    h1 {
        font-family: 'Abril Fatface', cursive;
        text-align: center;
        margin-bottom: 0.5em;
    }

    .stButton>button {
        font-family: 'Love Lace', cursive;
        font-style: italic;
        font-size: 14px;
        height: 100px;
        white-space: normal;
        padding: 10px;
        border-radius: 10px;
    }

    .marked {
        background-color: #c5e1a5 !important;
        color: black !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("The Secret Soirée Bingo")
st.markdown("Did you meet someone who...")

# Static prompts (do not shuffle on rerun)
prompts = [
    "Building an intelligent AI marketing tool", "Loves Marathon", "Built and Sold a Start up", "Lose track of time while cooking",
    "Believes we will have a ChatGPT widget soon!", "Met a co-creator in a club or dinner", "Is into yoga and meditation", "With whom you would like to jam on an idea later",
    "Loves discussing e-tafdas", "Built a cloud cost optimization start up", "Is a DJ", "Has had wedding choreography gigs",
    "Have an interesting story about BANANA", "Started their career as a data scientist", "Conducts dance workshops", "Heard an insight that blew your mind"
]

# Display 4x4 grid
for i in range(0, 16, 4):
    cols = st.columns(4)
    for j in range(4):
        idx = i + j
        key = f"tile_{idx}"
        if key not in st.session_state:
            st.session_state[key] = False

        btn_class = "marked" if st.session_state[key] else ""
        with cols[j]:
            clicked = st.button(prompts[idx], key=key)
            if clicked:
                st.session_state[key] = not st.session_state[key]

# Inject JS to style selected buttons
st.markdown(f"""
    <script>
    const buttons = window.parent.document.querySelectorAll('button');
    const markedKeys = [{','.join([f'"tile_{i}"' for i in range(16) if st.session_state[f"tile_{i}"]])}];
    buttons.forEach(btn => {{
        const key = btn.getAttribute('data-streamlit-button-key');
        if (markedKeys.includes(key)) {{
            btn.classList.add('marked');
        }}
    }});
    </script>
""", unsafe_allow_html=True)

