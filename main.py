import streamlit as st
import pandas as pd
import altair as alt

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

# Function to generate personalized reports with suggestions
def generate_personalized_reports(scores):
    reports = {}
    for factor, score in scores.items():
        if score <= 1:
            # Low score: Positive feedback and encouragement
            reports[factor] = {
                "feedback": f"Your {factor} score is low, indicating that you are handling this area well. Keep up the good work!",
                "short_term": "Continue practicing your healthy habits, such as regular exercise and mindful breathing, to maintain balance.",
                "long_term": "Consider developing a long-term plan, such as maintaining consistent self-care routines and staying socially connected."
            }
        elif score == 2:
            # Moderate score: Suggestions to monitor and maintain balance
            reports[factor] = {
                "feedback": f"Your {factor} score is moderate. You might want to monitor this area and use some strategies to maintain balance.",
                "short_term": "Try stress-relieving activities like a 10-minute walk, journaling, or a brief mindfulness session.",
                "long_term": "Consider setting long-term goals to reduce stress, such as scheduling regular relaxation breaks or developing better time management skills."
            }
        else:
            # High score: Recommendations for seeking support or making lifestyle changes
            reports[factor] = {
                "feedback": f"Your {factor} score is high, suggesting that this area is impacting your well-being. Consider seeking support or using techniques to manage this stressor.",
                "short_term": "Practice immediate stress relief methods like deep breathing, progressive muscle relaxation, or talking to a trusted friend.",
                "long_term": "Explore options for long-term support, such as therapy, joining a support group, or developing a structured self-care plan."
            }
    return reports

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

    # Use Altair for the bar chart
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("Factor", sort=None, title="Stress Factors"),
        y=alt.Y("Score", title="Score (0-4)"),
        color=alt.Color("Color", scale=None)  # Use the colors specified in the DataFrame
    ).properties(
        title="Stress Factor Scores",
        width=600,
        height=400
    )

    st.altair_chart(chart)

    # Generate and display personalized reports
    st.write("## Personalized Reports")
    reports = generate_personalized_reports(scores)
    for factor, report in reports.items():
        st.write(f"**{factor}**: {report['feedback']}")
        st.write(f"- **Short-term Suggestions**: {report['short_term']}")
        st.write(f"- **Long-term Suggestions**: {report['long_term']}")

# Main logic
scores = collect_scores()
calculate_stress_index(scores)

# Reset button
if st.button("Reset Scores"):
    st.experimental_rerun()
