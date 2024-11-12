import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Function to provide personalized suggestions based on stress levels
def provide_suggestions():
    st.write("Here are some activities you can do to improve your mental health:")

    # Stress level-based activities for each factor
    st.write("### 1. Tension/Anxiety")
    st.write("- **Low Stress**: Try simple stretching exercises to alleviate minor muscle tension.")
    st.write("- **Mild Stress**: Practice deep breathing techniques, such as box breathing, to calm your body.")
    st.write("- **Moderate Stress**: Try mindfulness meditation for 10-15 minutes to relax your body and mind.")
    st.write("- **High Stress**: Engage in a full-body yoga session to release built-up tension and restore balance.")
    
    st.write("### 2. Depression")
    st.write("- **Low Stress**: Go for a walk outside in natural sunlight to boost your mood.")
    st.write("- **Mild Stress**: Write down 3 things you are grateful for to shift your mindset towards positivity.")
    st.write("- **Moderate Stress**: Practice journaling to explore and process your emotions.")
    st.write("- **High Stress**: Talk to a counselor or therapist for professional support or join a support group for emotional guidance.")
    
    st.write("### 3. Vigor (Energy)")
    st.write("- **Low Stress**: Take a quick 10-minute walk around campus to refresh your mind and body.")
    st.write("- **Mild Stress**: Engage in light physical activity, like stretching or yoga, to increase blood flow.")
    st.write("- **Moderate Stress**: Go for a brisk jog or cycle for 20-30 minutes to energize yourself.")
    st.write("- **High Stress**: Participate in an intense cardio workout or HIIT class to significantly boost your energy.")
    
    st.write("### 4. Fatigue")
    st.write("- **Low Stress**: Take a 15-minute power nap to recharge your energy levels.")
    st.write("- **Mild Stress**: Practice a short session of restorative yoga or stretching to help release tension.")
    st.write("- **Moderate Stress**: Establish a regular sleep schedule, ensuring 7-8 hours of sleep each night.")
    st.write("- **High Stress**: Prioritize sleep hygiene and take a longer break from screens before bedtime to improve sleep quality.")
    
    st.write("### 5. Anger")
    st.write("- **Low Stress**: Practice deep breathing exercises to calm your mind and body.")
    st.write("- **Mild Stress**: Write about what’s making you angry to release pent-up feelings.")
    st.write("- **Moderate Stress**: Engage in a physical outlet, such as a brisk walk or a workout, to release tension.")
    st.write("- **High Stress**: Seek anger management resources or consider professional counseling to manage and understand your anger.")
    
    st.write("### 6. Calmness")
    st.write("- **Low Stress**: Practice simple breathing techniques or take a 5-minute break to relax.")
    st.write("- **Mild Stress**: Listen to calming music or nature sounds to promote relaxation.")
    st.write("- **Moderate Stress**: Attend a guided meditation session to deepen your sense of calm and mindfulness.")
    st.write("- **High Stress**: Take part in a full mindfulness practice or yoga class to promote deep relaxation and calmness.")
    
    st.write("### 7. Overload")
    st.write("- **Low Stress**: Use a to-do list to organize tasks and reduce the sense of overwhelm.")
    st.write("- **Mild Stress**: Break large tasks into smaller, more manageable steps.")
    st.write("- **Moderate Stress**: Set specific time blocks for focused work and take regular breaks.")
    st.write("- **High Stress**: Seek help from a mentor or counselor to better manage time and workload.")
    
    st.write("### 8. Confidence/Optimism")
    st.write("- **Low Stress**: Write down your accomplishments and strengths to remind yourself of your capabilities.")
    st.write("- **Mild Stress**: Practice daily affirmations, such as “I am confident and capable,” to build self-belief.")
    st.write("- **Moderate Stress**: Take on a small challenge or goal and celebrate when you achieve it to build momentum.")
    st.write("- **High Stress**: Seek professional coaching or attend self-improvement workshops to develop long-term self-confidence.")
    
    st.write("### 9. Frustration")
    st.write("- **Low Stress**: Take a few minutes to practice deep breathing or go for a short walk.")
    st.write("- **Mild Stress**: Engage in a creative outlet, such as doodling or painting, to release frustration.")
    st.write("- **Moderate Stress**: Use physical activity, like jogging or dancing, to work out your frustration.")
    st.write("- **High Stress**: Explore therapeutic methods like CBT (Cognitive Behavioral Therapy) or talk to a counselor to address ongoing frustration.")
    
    st.write("### 10. Hopelessness")
    st.write("- **Low Stress**: Spend time with supportive friends or family to uplift your spirits.")
    st.write("- **Mild Stress**: Focus on a small, achievable goal to restore a sense of purpose.")
    st.write("- **Moderate Stress**: Participate in an activity that brings you joy, such as listening to your favorite music or watching an inspiring movie.")
    st.write("- **High Stress**: Seek professional help, such as therapy or counseling, to address deeper feelings of hopelessness.")
    
    st.write("### 11. Social Connection")
    st.write("- **Low Stress**: Call or message a close friend for a quick check-in.")
    st.write("- **Mild Stress**: Attend a social event or club meeting on campus to meet new people.")
    st.write("- **Moderate Stress**: Schedule a regular meet-up or study session with friends to deepen your connections.")
    st.write("- **High Stress**: Join a social support group or seek professional counseling to address isolation or social anxiety.")
    
    st.write("### 12. Mental Focus")
    st.write("- **Low Stress**: Take short, focused breaks using the Pomodoro technique to help improve concentration.")
    st.write("- **Mild Stress**: Eliminate distractions and create a study schedule to stay on track.")
    st.write("- **Moderate Stress**: Try brain exercises or apps that promote cognitive focus and improve attention span.")
    st.write("- **High Stress**: Engage in mindfulness or concentration training to sharpen mental clarity and focus.")

    # External mental health resources
    st.write("### External Mental Health Resources:")
    st.write("- [National Suicide Prevention Lifeline (USA)](https://988lifeline.org)")
    st.write("- [Crisis Text Line (Global)](https://www.crisistextline.org)")
    st.write("- [BetterHelp (Online Therapy)](https://www.betterhelp.com)")
    st.write("- [Talkspace (Online Therapy)](https://www.talkspace.com)")
    st.write("- [Mind (UK Mental Health Charity)](https://www.mind.org.uk)")
    st.write("- [The Trevor Project (LGBTQ+ Support)](https://www.thetrevorproject.org)")
    st.write("- [Mental Health America (USA)](https://www.mhanational.org)")
    st.write("- [7 Cups (Online Support Network)](https://www.7cups.com)")
    st.write("- [Headspace (Meditation & Mindfulness)](https://www.headspace.com)")
    st.write("- [Calm (Meditation & Relaxation)](https://www.calm.com)")
    st.write("- [ReachOut (Youth Mental Health Resources - Australia)](https://au.reachout.com)")
    st.write("- [Mindful Schools (Mindfulness Resources)](https://www.mindfulschools.org)")
    st.write("- [Samaritans (UK and Ireland)](https://www.samaritans.org)")
    st.write("- [National Alliance on Mental Illness (NAMI)](https://www.nami.org)")

# Main function to run the app
def main():
    st.title("POMS Stress Index Calculator")
    
    # Collecting answers from the user (example for one question)
    tension_level = st.slider("Tension/Anxiety", 1, 4, 2, step=1, format="Stress level: %d")
    depression_level = st.slider("Depression", 1, 4, 2, step=1, format="Stress level: %d")
    vigor_level = st.slider("Vigor (Energy)", 1, 4, 2, step=1, format="Stress level: %d")
    fatigue_level = st.slider("Fatigue", 1, 4, 2, step=1, format="Stress level: %d")
    anger_level = st.slider("Anger", 1, 4, 2, step=1, format="Stress level: %d")
    calmness_level = st.slider("Calmness", 1, 4, 2, step=1, format="Stress level: %d")
    overload_level = st.slider("Overload", 1, 4, 2, step=1, format="Stress level: %d")
    confidence_level = st.slider("Confidence/Optimism", 1, 4, 2, step=1, format="Stress level: %d")
    frustration_level = st.slider("Frustration", 1, 4, 2, step=1, format="Stress level: %d")
    hopelessness_level = st.slider("Hopelessness", 1, 4, 2, step=1, format="Stress level: %d")
    social_connection_level = st.slider("Social Connection", 1, 4, 2, step=1, format="Stress level: %d")
    mental_focus_level = st.slider("Mental Focus", 1, 4, 2, step=1, format="Stress level: %d")
    
    # Calculate the total score based on the user responses
    total_score = (tension_level + depression_level + vigor_level + fatigue_level + anger_level + 
                   calmness_level + overload_level + confidence_level + frustration_level + 
                   hopelessness_level + social_connection_level + mental_focus_level)
    
    # Suggest activities based on score
    if total_score <= 24:
        st.write("Your stress level is low. Keep up with your healthy habits!")
    elif total_score <= 48:
        st.write("Your stress level is moderate. Take some time to relax and practice stress-relief activities.")
    else:
        st.write("Your stress level is high. Consider seeking help and engaging in more intensive self-care practices.")

    # Provide suggestions based on the user's input
    provide_suggestions()

if __name__ == "__main__":
    main()
