import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="POMS Stress Index Calculator",
    page_icon="💭",
    layout="centered"
)

# Title of the App
st.title("POMS Stress Index Calculator")
st.write("""
This calculator helps you assess your stress levels based on the Profile of Mood States (POMS) framework. 
Each of the 12 factors has a score range from 0 (Not at all) to 4 (Extremely).
""")

# Create a dictionary of factors related to college students' mental health
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

# Initialize a dictionary to store user input scores
scores = {}

# Collect scores for each factor from the user
for factor, description in factors.items():
    scores[factor] = st.slider(f"{factor}: {description}", 0, 4, 2)

# Calculate the total stress index
total_stress_index = sum(scores.values())

# Display the result
st.write("## Results")
st.write(f"**Total Stress Index**: {total_stress_index} / {len(factors) * 4}")
st.write("### Interpretation:")
if total_stress_index < len(factors) * 1:
    st.success("Your stress level appears to be low. Keep taking care of your well-being!")
elif total_stress_index < len(factors) * 2:
    st.warning("Your stress level is moderate. Consider using relaxation techniques or reaching out for support.")
else:
    st.error("Your stress level is high. It's important to address these feelings. Consider speaking with a counselor or a mental health professional.")

# Provide a reset button
if st.button("Reset Scores"):
    st.experimental_rerun()
