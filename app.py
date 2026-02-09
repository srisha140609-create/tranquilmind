import streamlit as st
from model import stress_score

st.title("TranquilMind – Stress Predictor")

sleep = st.slider("Sleep Hours", 0, 10, 6)
screen = st.slider("Screen Time (hours)", 0, 12, 5)
work = st.slider("Work Hours", 0, 12, 8)
activity = st.slider("Physical Activity (mins)", 0, 120, 30)

if st.button("Check Stress"):
    score = stress_score(sleep, screen, work, activity)

    st.subheader(f"Stress Score: {score}")

    if score < 30:
        st.success("Low Stress – Keep going 👍")
    elif score < 60:
        st.warning("Medium Stress – Take short breaks")
    else:
        st.error("High Stress – Rest & relax today")