pip install plotly
import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(
    page_title="POMS Stress Index Calculator",
    page_icon="💭",
    layout="centered"
)

# Title and description
st.title("POMS Stress Index Calculator")
st.write("""
This calculator helps you assess your stress levels based on the Profile of Mood States (POMS) framework. 
Each factor has a score range from 0 (Not at all) to 4 (Extremely).
""")

# Dictionary of factors related to college students' mental health
factors = {
    "Tension/Anxiety": "Feeling stressed, nervous, or tense.",
    "Depression/Dejection": "Feeling sad, down, or hopeless.",
    "Anger/Hostility": "Feeling angry, irritated, or annoyed.",
    "Vigor/Activity": "Feeling energetic, lively, or active.",
    "Fatigue/Inertia": "Feeling tired, sluggish, or exhausted.",
    "Confusion/Bewilderment": "Feeling disoriented, uncertain, or distracted.",
    "Friendship/Social Support": "Feeling supported and connected to friends.",
    "Academic Pressure": "Feeling overwhelmed or pressured by academic responsibilities.",
    "Loneliness/Isolation": "Feeling isolated or disconnected from others.",
    "Self-Doubt": "Feeling unsure of your abilities or self-worth.",
    "Sleep Quality": "Feeling tired due to lack of restful sleep.",
    "Overall Happiness": "Feeling happy and satisfied with life."
}

# Function to collect scores
def collect_scores():
    scores = {}
    for factor, description in factors.items():
        scores[factor] = st.slider(f"{factor}: {description}", 0, 4, 2)
    return scores

# Function to calculate and interpret stress index
def calculate_stress_index(scores):
    total_score = sum(scores.values())
    max_score = len(factors) * 4
    st.write("## Results")
    st.write(f"**Total Stress Index**: {total_score} / {max_score}")
    
    # Add visual feedback
    st.progress(total_score / max_score)  # Progress bar

    # Interpretation of stress levels
    if total_score < len(factors) * 1:
        st.success("Your stress level appears to be low. Keep taking care of your well-being!")
    elif total_score < len(factors) * 2:
        st.warning("Your stress level is moderate. Consider using relaxation techniques or reaching out for support.")
    else:
        st.error("Your stress level is high. It's important to address these feelings. Consider speaking with a counselor or a mental health professional.")

    # Create a DataFrame and add a color column based on thresholds
    df = pd.DataFrame(list(scores.items()), columns=["Factor", "Score"])
    df["Color"] = df["Score"].apply(lambda x: "green" if x <= 1 else ("yellow" if x <= 2 else "red"))

    # Create a colored bar chart using Plotly
    fig = px.bar(
        df,
        x="Factor",
        y="Score",
        color="Color",
        color_discrete_map={"green": "green", "yellow": "yellow", "red": "red"},
        title="Stress Factor Scores",
        labels={"Score": "Score (0-4)", "Factor": "Stress Factors"},
    )
    st.plotly_chart(fig)

# Main logic
scores = collect_scores()
calculate_stress_index(scores)

# Reset button
if st.button("Reset Scores"):
    st.experimental_rerun()
