import streamlit as st
import pandas as pd
import math

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Cricket Score Predictor", page_icon="??", layout="centered")

# ---------------- CUSTOM CRICKET STYLE ----------------
st.markdown("""
    <style>
    .main {
        background-color: #145214;
        padding: 20px;
        border-radius: 15px;
    }
    h1 {
        color: #FFD700;
        text-align: center;
    }
    .stRadio label {
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.title("?? Cricket Score Predictor")

# ---------------- MATCH FORMAT ----------------
format_type = st.radio("Choose Match Format:", ["T20", "ODI"])

if format_type == "T20":
    total_overs = 20
else:
    total_overs = 50

st.success(f"{format_type} Match - {total_overs} Overs")

# ---------------- INPUT SECTION ----------------
st.markdown("### Enter Current Match Situation")

col1, col2 = st.columns(2)

with col1:
    current_score = st.number_input("Current Score", min_value=0)

with col2:
    current_over = st.number_input("Overs Played", min_value=0.1, step=0.1)

# ---------------- CALCULATION ----------------
if current_over > 0 and current_score >= 0 and current_over <= total_overs:

    run_rate = current_score / current_over
    st.info(f"Current Run Rate: {run_rate:.2f}")

    # -------- FIND NEXT 5-OVER MILESTONE --------
    next_over = math.ceil(current_over / 5) * 5

    if next_over <= total_overs:
        overs_list = list(range(next_over, total_overs + 1, 5))

        predicted_scores = [int(run_rate * over) for over in overs_list]

        data = {
            "Overs": overs_list,
            "Predicted Score": predicted_scores
        }

        df = pd.DataFrame(data)

        st.markdown("### ?? Future Over Predictions")
        st.table(df)

    else:
        st.warning("Match is almost completed. No future 5-over milestones left.")

    # -------- FINAL PREDICTION --------
    final_prediction = int(run_rate * total_overs)
    st.markdown(f"## ?? Predicted Final Score: {final_prediction}")

else:
    st.warning("Please enter valid score and overs within match limit.")
