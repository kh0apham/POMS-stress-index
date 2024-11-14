import streamlit as st
import pandas as pd
import altair as alt

# Set page configuration
st.set_page_config(
    page_title="College Student Stress Survey",
    page_icon="💭", 
    layout="centered"
)

# Title and description with a more visually appealing layout
st.title("College Student Stress Survey")
st.markdown("""
Please rate how much each factor affects your stress levels on a scale from 1 to 10.
""")

# Add a divider for visual separation
st.markdown("---")

# Questions based on college student stress
questions = {
    "Classes and Assignments": "How stressed do you feel about keeping up with your classes and assignments?",
    "Financial Worries": "How often do financial worries, like paying for tuition or daily expenses, stress you out?",
    "Time Management": "How difficult is it for you to manage your time between school, work, and personal life?",
    "Career Uncertainty": "How uncertain or anxious are you about your future career plans and job opportunities?",
    "Social Life": "How often do challenges in your social life, like making friends or feeling homesick, cause you stress?",
    "Health Concerns": "How much do physical or mental health concerns, like sleep issues or anxiety, impact your stress levels?"
}

# Suggestions for additional stressors
additional_stressor_suggestions = {
    "Workload": {
        "short_term": "Try breaking your tasks into smaller, manageable pieces and focus on one at a time.",
        "long_term": "Consider adjusting your schedule and setting realistic goals to prevent overwork."
    },
    "Family Issues": {
        "short_term": "Reach out to a supportive family member or friend to share your feelings.",
        "long_term": "Work on establishing boundaries and communication to reduce stress in the long run."
    },
    "Financial Stress": {
        "short_term": "Create a budget or seek financial advice to manage immediate concerns.",
        "long_term": "Look into scholarships, part-time jobs, or financial planning for long-term stability."
    },
    "Health Issues": {
        "short_term": "Consult with a healthcare professional for immediate support and relief.",
        "long_term": "Focus on building a healthy routine, including regular exercise and a balanced diet."
    },
    "Relationship Problems": {
        "short_term": "Consider having an open and honest conversation with the person involved to clear up misunderstandings.",
        "long_term": "Work on building strong communication skills and mutual respect in relationships."
    },
    "Other": {
        "short_term": "Identify the specific issue and talk to someone you trust to gain perspective.",
        "long_term": "Develop strategies to manage the situation, whether through counseling, time management, or other means."
    }
}

# Function to collect scores
def collect_scores():
    scores = {}
    for question, description in questions.items():
        scores[question] = st.slider(f"{question}: {description}", 1, 10, 5, step=1)
    return scores

# Function to generate personalized reports with checkboxes for goals
def generate_personalized_reports(scores):
    reports = {}
    selected_goals = []  # List to store selected goals
    for question, score in scores.items():
        if score >= 7:  # Only show report for high scores (7 or above)
            reports[question] = {
                "feedback": f"Your stress level regarding {question} is high. Consider implementing some strategies to manage this stressor.",
                "short_term": additional_stressor_suggestions.get(question, {}).get("short_term", "No suggestion available."),
                "long_term": additional_stressor_suggestions.get(question, {}).get("long_term", "No suggestion available.")
            }

            # Display feedback and short-term/long-term suggestions with checkboxes
            st.markdown(f"### {question}")
            st.write(f"**Feedback**: {reports[question]['feedback']}")

            # Short-term goal checkbox
            if f"short_term_{question}" not in st.session_state:
                st.session_state[f"short_term_{question}"] = False
            short_term_goal = st.checkbox(f"Select Short-term Goal for {question}: {reports[question]['short_term']}", 
                                         key=f"short_term_{question}")
            if short_term_goal:
                selected_goals.append(f"Short-term Goal for {question}: {reports[question]['short_term']}")

            # Long-term goal checkbox
            if f"long_term_{question}" not in st.session_state:
                st.session_state[f"long_term_{question}"] = False
            long_term_goal = st.checkbox(f"Select Long-term Goal for {question}: {reports[question]['long_term']}", 
                                        key=f"long_term_{question}")
            if long_term_goal:
                selected_goals.append(f"Long-term Goal for {question}: {reports[question]['long_term']}")

    return selected_goals

# Function to display the list of selected goals in a nicely styled box
def display_selected_goals(selected_goals):
    if selected_goals:
        st.markdown("""
        <div style="background-color: #f9f9f9; padding: 20px; border-radius: 10px; border: 1px solid #ddd; box-shadow: 2px 2px 12px rgba(0,0,0,0.1);">
            <h3 style="color: #2c3e50;">Your Selected Goals</h3>
            <ul style="list-style-type: none; padding-left: 0;">
                """ + ''.join([f"<li style='margin: 5px 0; color: #2c3e50;'>{goal}</li>" for goal in selected_goals]) + """
            </ul>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.write("No goals selected yet. Check the boxes to add goals.")

# Function to calculate and interpret stress index
def calculate_stress_index(scores):
    total_score = sum(scores.values())
    max_score = len(questions) * 10
    st.write("## Results")
    st.write(f"**Total Stress Index**: {total_score} / {max_score}")
    
    # Add visual feedback
    st.progress(total_score / max_score)  # Progress bar

    # Interpretation of stress levels with styled messages
    if total_score < len(questions) * 4:
        st.success("Your stress level appears to be low. Keep taking care of your well-being!")
    elif total_score < len(questions) * 6:
        st.warning("Your stress level is moderate. Consider using relaxation techniques or reaching out for support.")
    else:
        st.error("Your stress level is high. It's important to address these feelings. Consider speaking with a counselor or a mental health professional.")

    # Create a DataFrame and add a color column based on thresholds
    df = pd.DataFrame(list(scores.items()), columns=["Factor", "Score"])

    # Set color based on score thresholds
    df["Color"] = df["Score"].apply(lambda x: "green" if x <= 4 else ("yellow" if x <= 7 else "red"))

    # Define tooltip content based on color
    df["Tooltip"] = df["Color"].apply(lambda x: (
        "Low stress: You're managing well in this area." if x == "green" 
        else "Moderate stress: This area might be affecting you. Consider stress management techniques."
        if x == "yellow" 
        else "High stress: This area is significantly impacting your well-being. Consider seeking professional support."
    ))

    # Create the chart with color and tooltips
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("Factor", sort=None, title="Stress Factors"),
        y=alt.Y("Score", title="Score (1-10)"),
        color=alt.Color("Color", scale=None),  # Dynamically color the bars based on score
        tooltip=["Factor", "Score", "Tooltip"]  # Tooltip with Factor name, Score, and Stress level explanation
    ).properties(
        title="Stress Factor Scores",
        width=600,
        height=400
    )

    st.altair_chart(chart)

    # Generate personalized reports and get selected goals
    selected_goals = generate_personalized_reports(scores)

    # Display the selected goals
    display_selected_goals(selected_goals)

# Function to add stressor factors with suggestions
def ask_about_stressors():
    st.subheader("Additional Stressor Factors")
    stressors = st.multiselect(
        "Please select any additional stressor factors you are currently facing:",
        ["Workload", "Family Issues", "Financial Stress", "Health Issues", "Relationship Problems", "Other"]
    )
    if stressors:
        st.write("You have selected the following stressors: ", ", ".join(stressors))
        for stressor in stressors:
            # Display short-term and long-term suggestions for each selected stressor
            st.markdown(f"### {stressor} Suggestions")
            st.write(f"**Short-term Tip**: {additional_stressor_suggestions[stressor]['short_term']}")
            st.write(f"**Long-term Tip**: {additional_stressor_suggestions[stressor]['long_term']}")

# Collecting stress level responses
scores = collect_scores()

# Calculate and display the stress index
calculate_stress_index(scores)

# Additional stressor inquiry
ask_about_stressors()
