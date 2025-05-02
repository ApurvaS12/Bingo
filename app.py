import streamlit as st
import random

st.set_page_config(page_title="The Secret Soirée Bingo", layout="centered")

st.title("🎉 The Secret Soirée Bingo")
st.markdown("Did you meet someone who...")

prompts = [
    "Building an intelligent AI marketing tool", "Loves Marathon", "Built and Sold a Start up",
    "Lose track of time while cooking", "Believes we will have a ChatGPT widget soon!",
    "Met a co-creator in a club or dinner", "Is into yoga and meditation",
    "With whom you would like to jam on an idea later", "Loves discussing e-tafdas",
    "Built a cloud cost optimization start up", "Is a DJ", "Has had wedding choreography gigs",
    "Have an interesting story about BANANA", "Started their career as a data scientist",
    "Conducts dance workshops", "Heard an insight that blew your mind"
]

# Fill up to 16 items
while len(prompts) < 16:
    prompts.append("✨ Free Spot – Just Vibe!")

random.shuffle(prompts)

marked = [False] * 16

# Create 4x4 grid
for i in range(0, 16, 4):
    cols = st.columns(4)
    for j in range(4):
        idx = i + j
        if st.session_state.get(f"tile_{idx}", False):
            button_style = "background-color:#c5e1a5;"
        else:
            button_style = ""
        if cols[j].button(prompts[idx], key=f"tile_{idx}", help="Click to mark/unmark"):
            st.session_state[f"tile_{idx}"] = not st.session_state.get(f"tile_{idx}", False)
