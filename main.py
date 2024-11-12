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

# Specific suggestions by factor
suggestions = {
    "Tension/Anxiety": {
        "short_term": "Try deep breathing exercises or a quick mindfulness meditation.",
        "long_term": "Consider incorporating regular relaxation practices like yoga or mindful breathing into your routine."
    },
    "Depression/Dejection": {
        "short_term": "Engage in an activity you usually enjoy, like listening to uplifting music or going for a walk.",
        "long_term": "It may help to talk to a counselor, and gradually build a routine around activities that bring joy."
    },
    "Anger/Hostility": {
        "short_term": "Take a few moments to step away and cool down with deep breaths or a quick walk.",
        "long_term": "Consider anger management techniques, like journaling your feelings or practicing assertive communication."
    },
    "Vigor/Activity": {
        "short_term": "Boost energy by moving around, stretching, or drinking water if feeling low.",
        "long_term": "Incorporate regular exercise, balanced diet, and adequate rest to maintain vigor over time."
    },
    "Fatigue/Inertia": {
        "short_term": "Take a short, refreshing break – consider a power nap or stretching.",
        "long_term": "Focus on a consistent sleep schedule, balanced diet, and exercise to improve energy levels sustainably."
    },
    "Confusion/Bewilderment": {
        "short_term": "Organize tasks or take a quick break to clear your mind.",
        "long_term": "Consider using productivity tools, like planners, to help structure your tasks and minimize confusion."
    },
    "Friendship/Social Support": {
        "short_term": "Reach out to a friend or family member for a quick chat.",
        "long_term": "Consider nurturing friendships by scheduling regular catch-ups or joining groups with shared interests."
    },
    "Academic Pressure": {
        "short_term": "Break tasks down and start with one small part, or take a quick break if overwhelmed.",
        "long_term": "Work on time management skills, and consider seeking support from advisors or tutors."
    },
    "Loneliness/Isolation": {
        "short_term": "Reach out to someone you trust for a short chat or consider joining an online interest group.",
        "long_term": "Consider engaging in social activities or volunteering to connect with others and reduce feelings of isolation."
    },
    "Self-Doubt": {
        "short_term": "Write down recent achievements, however small, to boost self-confidence.",
        "long_term": "Engage in personal development activities like skill-building and seek supportive mentors or coaches."
    },
    "Sleep Quality": {
        "short_term": "Avoid screens before bed and create a calm bedtime environment.",
        "long_term": "Develop a consistent sleep routine, possibly with relaxing activities before bed like reading or meditation."
    },
    "Overall Happiness": {
        "short_term": "Engage in a feel-good activity, like listening to favorite music or spending time in nature.",
        "long_term": "Focus on setting personal goals that align with your values and find ways to incorporate joy regularly into your life."
    }
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
                "short_term": suggestions[factor]["short_term"],
                "long_term": suggestions[factor]["long_term"]
            }
        elif score == 2:
            # Moderate score: Suggestions to monitor and maintain balance
            reports[factor] = {
                "feedback": f"Your {factor} score is moderate. You might want to monitor this area and use some strategies to maintain balance.",
                "short_term": suggestions[factor]["short_term"],
                "long_term": suggestions[factor]["long_term"]
            }
        else:
            # High score: Recommendations for seeking support or making lifestyle changes
            reports[factor] = {
                "feedback": f"Your {factor} score is high, suggesting that this area is impacting your well-being. Consider seeking support or using techniques to manage this stressor.",
                "short_term": suggestions[factor]["short_term"],
                "long_term": suggestions[factor]["long_term"]
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
