pip install plotly 
import streamlit as st
import plotly.graph_objects as go

# Customizing CSS for styling
st.markdown("""
    <style>
        .main-header {
            font-size: 36px;
            font-weight: bold;
            color: #1E3A8A;
            text-align: center;
            margin-bottom: 20px;
        }
        .sub-header {
            font-size: 24px;
            font-weight: bold;
            color: #1F2937;
        }
        .suggestions {
            margin-top: 20px;
            padding: 10px;
            border: 1px solid #D1D5DB;
            border-radius: 8px;
            background-color: #F9FAFB;
            max-height: 400px;
            overflow-y: scroll;
        }
        .slider-container {
            margin-top: 10px;
        }
        .section-title {
            font-size: 18px;
            font-weight: bold;
            color: #4B5563;
            margin-top: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# Function to provide personalized suggestions based on stress levels
def provide_suggestions(scores):
    # Factor names
    factors = [
        "Tension/Anxiety", "Depression", "Vigor (Energy)", "Fatigue", "Anger", 
        "Calmness", "Overload", "Confidence/Optimism", "Frustration", "Hopelessness", 
        "Social Connection", "Mental Focus"
    ]

    # Mapping for each factor to corresponding suggestions
    suggestions_map = {
        "Tension/Anxiety": [
            "Low Stress: Try simple stretching exercises to alleviate minor muscle tension.",
            "Mild Stress: Practice deep breathing techniques, such as box breathing, to calm your body.",
            "Moderate Stress: Try mindfulness meditation for 10-15 minutes to relax your body and mind.",
            "High Stress: Engage in a full-body yoga session to release built-up tension and restore balance."
        ],
        "Depression": [
            "Low Stress: Go for a walk outside in natural sunlight to boost your mood.",
            "Mild Stress: Write down 3 things you are grateful for to shift your mindset towards positivity.",
            "Moderate Stress: Practice journaling to explore and process your emotions.",
            "High Stress: Talk to a counselor or therapist for professional support or join a support group for emotional guidance."
        ],
        "Vigor (Energy)": [
            "Low Stress: Take a quick 10-minute walk around campus to refresh your mind and body.",
            "Mild Stress: Engage in light physical activity, like stretching or yoga, to increase blood flow.",
            "Moderate Stress: Go for a brisk jog or cycle for 20-30 minutes to energize yourself.",
            "High Stress: Participate in an intense cardio workout or HIIT class to significantly boost your energy."
        ],
        "Fatigue": [
            "Low Stress: Take a 15-minute power nap to recharge your energy levels.",
            "Mild Stress: Practice a short session of restorative yoga or stretching to help release tension.",
            "Moderate Stress: Establish a regular sleep schedule, ensuring 7-8 hours of sleep each night.",
            "High Stress: Prioritize sleep hygiene and take a longer break from screens before bedtime to improve sleep quality."
        ],
        "Anger": [
            "Low Stress: Practice deep breathing exercises to calm your mind and body.",
            "Mild Stress: Write about what’s making you angry to release pent-up feelings.",
            "Moderate Stress: Engage in a physical outlet, such as a brisk walk or a workout, to release tension.",
            "High Stress: Seek anger management resources or consider professional counseling to manage and understand your anger."
        ],
        "Calmness": [
            "Low Stress: Practice simple breathing techniques or take a 5-minute break to relax.",
            "Mild Stress: Listen to calming music or nature sounds to promote relaxation.",
            "Moderate Stress: Attend a guided meditation session to deepen your sense of calm and mindfulness.",
            "High Stress: Take part in a full mindfulness practice or yoga class to promote deep relaxation and calmness."
        ],
        "Overload": [
            "Low Stress: Use a to-do list to organize tasks and reduce the sense of overwhelm.",
            "Mild Stress: Break large tasks into smaller, more manageable steps.",
            "Moderate Stress: Set specific time blocks for focused work and take regular breaks.",
            "High Stress: Seek help from a mentor or counselor to better manage time and workload."
        ],
        "Confidence/Optimism": [
            "Low Stress: Write down your accomplishments and strengths to remind yourself of your capabilities.",
            "Mild Stress: Practice daily affirmations, such as 'I am confident and capable,' to build self-belief.",
            "Moderate Stress: Take on a small challenge or goal and celebrate when you achieve it to build momentum.",
            "High Stress: Seek professional coaching or attend self-improvement workshops to develop long-term self-confidence."
        ],
        "Frustration": [
            "Low Stress: Take a few minutes to practice deep breathing or go for a short walk.",
            "Mild Stress: Engage in a creative outlet, such as doodling or painting, to release frustration.",
            "Moderate Stress: Use physical activity, like jogging or dancing, to work out your frustration.",
            "High Stress: Explore therapeutic methods like CBT (Cognitive Behavioral Therapy) or talk to a counselor to address ongoing frustration."
        ],
        "Hopelessness": [
            "Low Stress: Spend time with supportive friends or family to uplift your spirits.",
            "Mild Stress: Focus on a small, achievable goal to restore a sense of purpose.",
            "Moderate Stress: Participate in an activity that brings you joy, such as listening to your favorite music or watching an inspiring movie.",
            "High Stress: Seek professional help, such as therapy or counseling, to address deeper feelings of hopelessness."
        ],
        "Social Connection": [
            "Low Stress: Call or message a close friend for a quick check-in.",
            "Mild Stress: Attend a social event or club meeting on campus to meet new people.",
            "Moderate Stress: Schedule a regular meet-up or study session with friends to deepen your connections.",
            "High Stress: Join a social support group or seek professional counseling to address isolation or social anxiety."
        ],
        "Mental Focus": [
            "Low Stress: Take short, focused breaks using the Pomodoro technique to help improve concentration.",
            "Mild Stress: Eliminate distractions and create a study schedule to stay on track.",
            "Moderate Stress: Try brain exercises or apps that promote cognitive focus and improve attention span.",
            "High Stress: Engage in mindfulness or concentration training to sharpen mental clarity and focus."
        ],
    }

    # Iterate through factors and display suggestions based on user score
    st.markdown('<div class="suggestions">', unsafe_allow_html=True)
    for idx, factor in enumerate(factors):
        score = scores[idx]
        st.write(f"### {factor}")
        
        # Show the suggestion based on the user's score
        st.write(suggestions_map[factor][score - 1])  # score-1 to get the correct index (1=Low, 4=High)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Modify plot_radar_chart function to include color styling based on score
def plot_radar_chart(scores):
    factors = [
        "Tension/Anxiety", "Depression", "Vigor (Energy)", "Fatigue", "Anger", 
        "Calmness", "Overload", "Confidence/Optimism", "Frustration", "Hopelessness", 
        "Social Connection", "Mental Focus"
    ]
    
    # Map colors to scores
    colors = ['green' if score <= 2 else 'yellow' if score == 3 else 'red' for score in scores]
    
    fig = go.Figure(data=[go.Scatterpolar(
        r=scores,
        theta=factors,
        fill='toself',
        name='User Stress Levels',
        line=dict(color='blue'),
        marker=dict(color=colors)  # Apply color based on stress level
    )])

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 4]
            )
        ),
        showlegend=False
    )
    
    return fig

# Main App
def main():
    st.title("Mental Health Stress Assessment Tool")
    st.markdown('<div class="main-header">Assess Your Stress</div>', unsafe_allow_html=True)
    
    # User Input Sliders
    st.markdown("<div class='section-title'>Please rate your current stress levels (1 = Low, 4 = High)</div>", unsafe_allow_html=True)
    
    scores = [
        st.slider("Tension/Anxiety", 1, 4, 2), 
        st.slider("Depression", 1, 4, 2), 
        st.slider("Vigor (Energy)", 1, 4, 2), 
        st.slider("Fatigue", 1, 4, 2), 
        st.slider("Anger", 1, 4, 2), 
        st.slider("Calmness", 1, 4, 2), 
        st.slider("Overload", 1, 4, 2), 
        st.slider("Confidence/Optimism", 1, 4, 2), 
        st.slider("Frustration", 1, 4, 2), 
        st.slider("Hopelessness", 1, 4, 2), 
        st.slider("Social Connection", 1, 4, 2), 
        st.slider("Mental Focus", 1, 4, 2)
    ]
    
    # Provide personalized suggestions based on user input
    provide_suggestions(scores)

    # Display radar chart
    fig = plot_radar_chart(scores)
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
