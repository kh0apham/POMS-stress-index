import streamlit as st
import plotly.graph_objects as go

# Function to create a radar chart
def create_radar_chart(scores):
    categories = [
        "Tension-Anxiety", "Depression-Dejection", "Anger-Hostility",
        "Vigor-Activity", "Fatigue-Inertia", "Confusion-Bewilderment",
        "Social Anxiety", "Loneliness", "Physical Wellness", "Burnout",
        "Frustration", "Overwhelmed"
    ]

    # Create a radar chart using Plotly
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=scores,
        theta=categories,
        fill='toself',
        name='POMS Score'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 4]  # Scale based on the rating from 0 to 4
            )
        ),
        showlegend=False
    )

    return fig

# Streamlit App
st.title("POMS Stress Index Calculator")
st.write("Please rate how often you have felt the following emotions in the past week:")

# Labels for each score on the scale
score_labels = {
    0: "Not at all",
    1: "A little",
    2: "Moderately",
    3: "Quite a bit",
    4: "Extremely"
}

# Questionnaire items
questions = [
    "I have felt nervous or anxious about upcoming assignments or exams.",
    "I have felt down or hopeless about my academic or social life.",
    "I have felt irritated or angry with myself or others due to school pressures.",
    "I have felt energetic and motivated to tackle my daily responsibilities.",
    "I have felt exhausted or worn out, even after getting a full night's sleep.",
    "I have felt mentally foggy or had difficulty concentrating during classes.",
    "I have felt tense or uneasy in social situations on campus, such as in study groups or social events.",
    "I have felt lonely or disconnected from friends and classmates.",
    "I have felt physically healthy and ready to take on physical activities or exercise.",
    "I have felt so tired that I struggle to stay focused or complete daily tasks.",
    "I have felt frustrated when things didn’t go as planned, such as when a project or study session went poorly.",
    "I have felt overwhelmed by the amount of work or responsibilities I have to manage."
]

# Collect user responses
scores = []
for question in questions:
    score = st.slider(
        question,
        min_value=0,
        max_value=4,
        value=0,  # Default value
        format="%d",
        help=f"0: {score_labels[0]}, 1: {score_labels[1]}, 2: {score_labels[2]}, 3: {score_labels[3]}, 4: {score_labels[4]}"
    )
    scores.append(score)

# Generate and display the radar chart
if st.button("Generate Radar Chart"):
    fig = create_radar_chart(scores)
    st.plotly_chart(fig)
