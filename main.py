import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Define function to create the radar chart
def create_radar_chart(labels, values, thresholds):
    # Create radar chart
    fig = go.Figure()

    # Define colors for the zones (green = manageable, red = unmanageable)
    colors = ['green' if value <= threshold else 'red' for value, threshold in zip(values, thresholds)]

    # Text for hover info with threshold descriptions
    hover_text = [
        f'{label}<br>Score: {value}<br>Threshold: {threshold}<br>{get_threshold_info(value, threshold)}' 
        for label, value, threshold in zip(labels, values, thresholds)
    ]

    # Add the radar chart
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=labels,
        fill='toself',
        fillcolor='rgba(0,255,0,0.2)',  # Initial color (for manageable)
        line=dict(color='green', width=2),
        name='Stress Levels',
        hoverinfo='text',  # Enable hover text
        text=hover_text  # Attach custom hover text
    ))

    # Add threshold lines for each label (e.g., when values cross a certain threshold)
    for i in range(len(labels)):
        fig.add_trace(go.Scatterpolar(
            r=[thresholds[i]] * len(labels),
            theta=labels,
            mode='lines',
            line=dict(color='red', dash='dot'),
            showlegend=False
        ))

    # Update layout for readability
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 4],  # Modify based on the scale of your questions
                tickvals=[0, 1, 2, 3, 4],
                ticktext=['Not at all', 'A little', 'Moderately', 'Quite a bit', 'Extremely']
            ),
        ),
        showlegend=False,
        title="POMS Stress Index - Radar Chart"
    )

    return fig

# Function to provide an explanation about the thresholds
def get_threshold_info(value, threshold):
    if value <= threshold:
        return "Your score is within a healthy range. This indicates manageable stress levels and good mental health."
    else:
        return "Your score exceeds the recommended threshold, indicating higher levels of stress that may require attention or support."

# Function to generate personalized report
def generate_report(questions, responses, thresholds):
    report = []
    for i, (question, response, threshold) in enumerate(zip(questions, responses, thresholds)):
        if response > threshold:
            report.append(f"**{question}**: Your response of {response} is higher than the threshold. This suggests that you may be feeling more stressed than usual in this area. Consider exploring ways to reduce stress, such as relaxation techniques, physical activity, or reaching out for support.")
        elif response < threshold:
            report.append(f"**{question}**: Your response of {response} is lower than the threshold. This could indicate that you're managing this aspect of your mental health well. Keep up the good work and continue with the habits that support your wellbeing.")
    
    # If no significant points were found, return a default message
    if not report:
        report.append("Your responses indicate balanced stress levels across the board. Keep practicing healthy stress management techniques.")
    
    return report

# Streamlit App Interface
def main():
    st.title('POMS Stress Index Calculator')

    # Refined Questionnaire: Ask user to rate their emotional states on a scale from 0 to 4 (Not at all to Extremely)
    questions = [
        "How often have you felt tense or anxious recently?",
        "How often have you felt down or sad in the past week?",
        "How often have you felt energetic or excited recently?",
        "How often have you felt physically drained or tired?",
        "How often have you felt irritated or angry in the past week?",
        "How often have you felt calm and relaxed recently?",
        "How often have you felt overwhelmed by your responsibilities or tasks?",
        "How often have you felt confident or optimistic about the future?",
        "How often have you felt frustrated or upset in the past week?",
        "How often have you felt hopeless about your situation recently?",
        "How often have you felt connected with friends or family?",
        "How often have you felt mentally focused and sharp?"
    ]

    # Thresholds: These are example thresholds for each mood scale
    thresholds = [2, 2, 3, 2, 2, 3, 3, 3, 2, 2, 3, 3]  # Adjust based on the scale and research

    # Collect user responses via sliders (scale 0 to 4)
    responses = []
    for question in questions:
        response = st.slider(question, 0, 4, 2)
        responses.append(response)

    # Add a description for the user about the thresholds
    st.subheader("Understanding the Thresholds:")
    st.write("""
        The thresholds are based on psychological research about stress levels. Scores below the threshold are considered 
        within a healthy range, while scores above the threshold indicate that stress may be becoming unmanageable. 
        Regularly exceeding the threshold may be a sign of significant stress, and it might be helpful to seek additional 
        support or practice stress-relieving activities.
    """)

    # Calculate and visualize radar chart if data is collected
    if st.button('Generate Radar Chart'):
        # Create the radar chart
        fig = create_radar_chart(questions, responses, thresholds)

        # Display the radar chart in the app
        st.plotly_chart(fig)

        # Generate and display personalized report
        report = generate_report(questions, responses, thresholds)
        st.subheader("Personalized Stress Report:")
        for point in report:
            st.write(point)

if __name__ == '__main__':
    main()
