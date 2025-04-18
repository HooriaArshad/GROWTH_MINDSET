import streamlit as st
import random
import datetime
import pandas as pd


quotes = [
    "Challenges are what make life interesting.",
    "Failure is simply the opportunity to begin again.",
    "Effort is the path to mastery.",
    "The mind is like a muscle – it grows stronger with use.",
    "Mistakes are proof that you are trying."
]

if 'reflections' not in st.session_state:
    st.session_state.reflections = []

st.title("🌱 Growth Mindset App")
st.subheader("Welcome! Embrace the journey of self-growth.")


st.markdown("### 💡 Daily Motivation")
st.info(random.choice(quotes))

st.markdown("### ✍️ Your Daily Reflection")
reflection = st.text_area("What did you learn or struggle with today?", "")
if st.button("Save Reflection"):
    st.session_state.reflections.append({
        "date": datetime.date.today(),
        "text": reflection
    })
    st.success("Reflection saved!")

st.markdown("### 📖 Your Growth Journal")
if st.session_state.reflections:
    df = pd.DataFrame(st.session_state.reflections)
    st.table(df)
else:
    st.info("No reflections yet. Start writing!")


st.markdown("### 🚀 Growth Mindset Tips")
st.markdown("""
- Embrace challenges.
- Learn from criticism.
- Celebrate small wins.
- Stay persistent.
- Keep learning every day.
""")