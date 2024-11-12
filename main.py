import streamlit as st

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
Each factor has a score range from 0 (Not at all) to 4 (Extremely lol).
""")

# Dictionary of factors related to college students' mental health
factors = {
    "Tension/Anxiety": "Feeling stressed, nervous, or tense.",
    "Depression/Dejection": "Feeling sad, down, or hopeless.",
    # Add the remaining factors...
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
    
    if total_score < len(factors) * 1:
        st.success("Your stress level appears to be low. Keep taking care of your well-being!")
    elif total_score < len(factors) * 2:
        st.warning("Your stress level is moderate. Consider using relaxation techniques or reaching out for support.")
    else:
        st.error("Your stress level is high. It's important to address these feelings. Consider speaking with a counselor or a mental health professional.")

# Main logic
scores = collect_scores()
calculate_stress_index(scores)

# Reset button
if st.button("Reset Scores"):
    st.experimental_rerun()
