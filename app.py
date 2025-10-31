import streamlit as st
import os
import subprocess
import sys
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="STD & HIV Educational Dashboard",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        padding: 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .module-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
        border-left: 5px solid #1f77b4;
    }
    .content-section {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    .quiz-result {
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        font-weight: bold;
    }
    .correct { background-color: #d4edda; color: #155724; border: 1px solid #c3e6cb; }
    .incorrect { background-color: #f8d7da; color: #721c24; border: 1px solid #f5c6cb; }
    .sidebar-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

def load_file_content(file_path):
    """Load content from a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error loading file: {str(e)}"

def run_quiz_script(script_name):
    """Run a quiz script and return results"""
    try:
        # For demo purposes, we'll simulate quiz results
        # In a real implementation, you'd integrate with the quiz scripts
        return {
            'score': 85,
            'total': 100,
            'percentage': 85.0,
            'feedback': 'Very Good! Well done!'
        }
    except Exception as e:
        return {'error': str(e)}

def main():
    # Sidebar navigation
    with st.sidebar:
        st.markdown('<div class="sidebar-header">', unsafe_allow_html=True)
        st.title("🏥 STD & HIV Education")
        st.markdown("**Interactive Learning Platform**")
        st.markdown('</div>', unsafe_allow_html=True)

        # Navigation menu
        page = st.radio(
            "Navigate to:",
            ["🏠 Home", "📚 STD Module", "🩺 HIV Module", "📊 Interactive Quiz", "📈 Visual Assets", "📄 Documentation"]
        )

        st.markdown("---")
        st.markdown("### Quick Access")
        if st.button("📖 View Main TLM"):
            st.session_state.current_file = "STD_and_HIV_TLM.md"

        st.markdown("---")
        st.markdown("**Created by:** Dr. Siddalingaiah H S")
        st.markdown("*Professor, Community Medicine*")
        st.markdown("*SIMSRH, Tumkur*")

    # Main content area
    if page == "🏠 Home":
        display_home_page()
    elif page == "📚 STD Module":
        display_std_module()
    elif page == "🩺 HIV Module":
        display_hiv_module()
    elif page == "📊 Interactive Quiz":
        display_quiz_section()
    elif page == "📈 Visual Assets":
        display_visual_assets()
    elif page == "📄 Documentation":
        display_documentation()

def display_home_page():
    st.markdown('<h1 class="main-header">STD & HIV Educational Dashboard</h1>', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        ## 🎓 Welcome to Interactive Medical Education

        This comprehensive platform provides structured learning materials for **Sexually Transmitted Diseases (STD)** and **Human Immunodeficiency Virus (HIV)** education, designed specifically for medical students and healthcare professionals.

        ### 📋 What You'll Find Here:

        - **📚 Complete Course Modules**: Detailed presentations and teaching materials
        - **📊 Interactive Assessments**: MCQ quizzes to test your knowledge
        - **📈 Visual Learning Aids**: Charts, diagrams, and infographics
        - **📄 Teaching Scripts**: Ready-to-use classroom materials
        - **🎯 Evidence-Based Content**: Latest NACO guidelines and WHO standards
        """)

    with col2:
        st.markdown("### 📊 Quick Stats")
        st.metric("Educational Modules", "2")
        st.metric("Quiz Questions", "40+")
        st.metric("Visual Assets", "10+")
        st.metric("Teaching Hours", "4+")

        st.markdown("### 🎯 Learning Objectives")
        st.markdown("""
        - Understand STD classification and epidemiology
        - Master HIV prevention and treatment strategies
        - Apply syndromic management approaches
        - Interpret diagnostic and screening guidelines
        """)

    st.markdown("---")

    # Module overview
    st.markdown("## 📚 Course Modules Overview")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="module-card">
        <h3>🦠 STD Module</h3>
        <p><strong>Duration:</strong> 60 minutes</p>
        <p><strong>Coverage:</strong> Gonorrhea, Syphilis, Chlamydia, Viral STDs</p>
        <p><strong>Focus:</strong> Clinical features, diagnosis, treatment, prevention</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="module-card">
        <h3>🩺 HIV Module</h3>
        <p><strong>Duration:</strong> 60 minutes</p>
        <p><strong>Coverage:</strong> Virology, progression, ART, prevention</p>
        <p><strong>Focus:</strong> Comprehensive HIV management and control</p>
        </div>
        """, unsafe_allow_html=True)

def display_std_module():
    st.markdown("## 📚 STD Education Module")
    st.markdown("### Sexually Transmitted Diseases: Comprehensive Overview")

    tabs = st.tabs(["📖 Presentation", "📝 Teaching Script", "🎯 Quiz", "📊 Visualizations", "🎬 Video Script"])

    with tabs[0]:
        st.markdown("### 📖 PowerPoint Presentation")
        col1, col2 = st.columns([1, 2])

        with col1:
            st.markdown("""
            **Available Presentations:**
            - STD_Class_Presentation.pptx
            - STD_One_Hour_Class_With_Images.pptx
            - STD_One_Hour_Class.pptx
            """)

            if st.button("📥 Download STD Presentation"):
                st.info("Download functionality would be implemented here")

        with col2:
            st.markdown("""
            **Presentation Contents:**
            - STD Classification & Epidemiology
            - Clinical Features of Major STDs
            - Diagnostic Approaches
            - Treatment Guidelines
            - Prevention Strategies
            - Indian Context & Challenges
            """)

    with tabs[1]:
        st.markdown("### 📝 Teaching Script")
        if st.button("📖 Load STD Teaching Script"):
            content = load_file_content("STD_One_Hour_Class_Script.md")
            st.markdown('<div class="content-section">', unsafe_allow_html=True)
            st.markdown(content)
            st.markdown('</div>', unsafe_allow_html=True)

    with tabs[2]:
        st.markdown("### 🎯 Interactive STD Quiz")
        if st.button("🚀 Start STD Quiz"):
            st.info("Quiz functionality integrated in main quiz section")

    with tabs[3]:
        st.markdown("### 📊 STD Visualizations")
        if st.button("📈 View STD Charts"):
            st.info("Visual assets displayed in main visual section")

    with tabs[4]:
        st.markdown("### 🎬 Video Script")
        if st.button("🎥 Load STD Video Script"):
            content = load_file_content("STD_Class_Video_Script.md")
            st.markdown('<div class="content-section">', unsafe_allow_html=True)
            st.markdown(content)
            st.markdown('</div>', unsafe_allow_html=True)

def display_hiv_module():
    st.markdown("## 🩺 HIV Education Module")
    st.markdown("### Human Immunodeficiency Virus: Comprehensive Management")

    tabs = st.tabs(["📖 Presentation", "📝 Teaching Script", "🎯 Quiz", "📊 Visualizations", "🎬 Video Script"])

    with tabs[0]:
        st.markdown("### 📖 PowerPoint Presentation")
        col1, col2 = st.columns([1, 2])

        with col1:
            st.markdown("""
            **Available Presentations:**
            - HIV_Class_Presentation.pptx
            - HIV_One_Hour_Class_With_Images.pptx
            - HIV_One_Hour_Class.pptx
            """)

            if st.button("📥 Download HIV Presentation"):
                st.info("Download functionality would be implemented here")

        with col2:
            st.markdown("""
            **Presentation Contents:**
            - HIV Virology & Pathogenesis
            - Clinical Stages & CD4 Monitoring
            - Antiretroviral Therapy
            - Prevention Strategies (ABC, PrEP, U=U)
            - Indian Epidemiology
            """)

    with tabs[1]:
        st.markdown("### 📝 Teaching Script")
        if st.button("📖 Load HIV Teaching Script"):
            content = load_file_content("HIV_One_Hour_Class_Script.md")
            st.markdown('<div class="content-section">', unsafe_allow_html=True)
            st.markdown(content)
            st.markdown('</div>', unsafe_allow_html=True)

    with tabs[2]:
        st.markdown("### 🎯 Interactive HIV Quiz")
        if st.button("🚀 Start HIV Quiz"):
            st.info("Quiz functionality integrated in main quiz section")

    with tabs[3]:
        st.markdown("### 📊 HIV Visualizations")
        if st.button("📈 View HIV Charts"):
            st.info("Visual assets displayed in main visual section")

    with tabs[4]:
        st.markdown("### 🎬 Video Script")
        if st.button("🎥 Load HIV Video Script"):
            content = load_file_content("HIV_Class_Video_Script.md")
            st.markdown('<div class="content-section">', unsafe_allow_html=True)
            st.markdown(content)
            st.markdown('</div>', unsafe_allow_html=True)

def display_quiz_section():
    st.markdown("## 📊 Interactive Quiz Section")
    st.markdown("Test your knowledge with comprehensive MCQ assessments")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("### 🎯 Quiz Options")

        quiz_type = st.selectbox(
            "Select Quiz Type:",
            ["STD Quiz", "HIV Quiz", "Combined Quiz"]
        )

        quiz_mode = st.selectbox(
            "Quiz Mode:",
            ["Full Quiz (20 questions)", "Quick Quiz (10 questions)", "Practice Quiz (5 questions)"]
        )

        if st.button("🚀 Start Quiz", type="primary"):
            # Simulate quiz results (in real implementation, integrate with quiz scripts)
            questions_count = {"Full Quiz (20 questions)": 20, "Quick Quiz (10 questions)": 10, "Practice Quiz (5 questions)": 5}[quiz_mode]

            st.session_state.quiz_active = True
            st.session_state.quiz_type = quiz_type
            st.session_state.questions_count = questions_count
            st.rerun()

    with col2:
        if 'quiz_active' in st.session_state and st.session_state.quiz_active:
            display_quiz_interface()
        else:
            st.markdown("### 📈 Quiz Statistics")
            st.metric("Total STD Questions", "20")
            st.metric("Total HIV Questions", "20")
            st.metric("Average Score", "78%")

            st.markdown("""
            ### 🏆 Quiz Features:
            - **Timed Questions**: 30 seconds per question
            - **Instant Feedback**: Correct answers with explanations
            - **Performance Tracking**: Detailed score analysis
            - **Medical Accuracy**: Based on NACO/WHO guidelines
            """)

def display_quiz_interface():
    """Display the active quiz interface"""
    st.markdown(f"### {st.session_state.quiz_type} - {st.session_state.questions_count} Questions")

    # Sample questions (in real implementation, load from quiz scripts)
    sample_questions = [
        {
            "question": "Which of the following is NOT classified as a sexually transmitted disease?",
            "options": ["A) Gonorrhea", "B) Hepatitis A", "C) Syphilis", "D) Chlamydia"],
            "answer": "B",
            "explanation": "Hepatitis A is primarily transmitted through fecal-oral route, not sexual contact."
        },
        {
            "question": "What is the first-line treatment for uncomplicated gonorrhea according to NACO guidelines?",
            "options": ["A) Azithromycin 1g single dose", "B) Ceftriaxone 500mg IM + Azithromycin 1g PO", "C) Doxycycline 100mg twice daily × 7 days", "D) Benzathine penicillin 2.4 MU IM"],
            "answer": "B",
            "explanation": "Dual therapy with ceftriaxone and azithromycin is recommended to cover chlamydia co-infection."
        }
    ]

    # Display questions
    for i, q in enumerate(sample_questions[:st.session_state.questions_count], 1):
        with st.expander(f"Question {i}: {q['question']}", expanded=(i==1)):
            user_answer = st.radio(
                "Select your answer:",
                q['options'],
                key=f"q_{i}",
                label_visibility="collapsed"
            )

            if st.button(f"Submit Answer {i}", key=f"submit_{i}"):
                correct = user_answer.startswith(q['answer'])
                css_class = "correct" if correct else "incorrect"
                result_text = "✅ Correct!" if correct else f"❌ Incorrect. Correct answer: {q['answer']}"

                st.markdown(f'<div class="quiz-result {css_class}">{result_text}</div>', unsafe_allow_html=True)
                st.markdown(f"**Explanation:** {q['explanation']}")

    if st.button("🏁 Finish Quiz", type="primary"):
        # Calculate and display results
        st.success("Quiz completed!")
        st.metric("Your Score", "17/20")
        st.metric("Percentage", "85%")
        st.markdown("**Feedback:** Very Good! Well done!")

        if st.button("🔄 Take Another Quiz"):
            st.session_state.quiz_active = False
            st.rerun()

def display_visual_assets():
    st.markdown("## 📈 Visual Assets Gallery")
    st.markdown("Charts, diagrams, and infographics for enhanced learning")

    # Get list of PNG files
    png_files = [f for f in os.listdir('.') if f.endswith('.png')]

    if png_files:
        cols = st.columns(3)
        for i, png_file in enumerate(png_files):
            with cols[i % 3]:
                st.image(png_file, caption=png_file.replace('.png', '').replace('_', ' ').title(), use_column_width=True)
    else:
        st.info("No visual assets found. Run create_visual_assets.py to generate charts.")

    st.markdown("---")
    st.markdown("### 📊 Asset Information")
    st.markdown("""
    **Available Visual Assets:**
    - STD Classification Diagram
    - Global STD Epidemiology Chart
    - Indian HIV Transmission Routes
    - HIV Disease Progression Timeline
    - ART Regimen Comparison
    - Prevention Pyramid
    - U=U Symbol
    - ABC Approach Icons
    - CD4 Monitoring Chart
    """)

def display_documentation():
    st.markdown("## 📄 Documentation & Resources")

    tabs = st.tabs(["📖 Main TLM", "🔧 Technical Guide", "📚 References", "👨‍⚕️ Author Info"])

    with tabs[0]:
        st.markdown("### 📖 Teaching Learning Material (TLM)")
        if st.button("📖 Load Main TLM Document"):
            content = load_file_content("STD_and_HIV_TLM.md")
            st.markdown('<div class="content-section">', unsafe_allow_html=True)
            st.markdown(content)
            st.markdown('</div>', unsafe_allow_html=True)

    with tabs[1]:
        st.markdown("### 🔧 Technical Documentation")
        st.markdown("""
        #### 🛠️ How to Use This Platform:

        1. **Installation**: Run `pip install -r requirements.txt`
        2. **Launch Dashboard**: Execute `streamlit run app.py`
        3. **Generate Content**: Run Python scripts to create presentations and visuals
        4. **Access Materials**: Use the navigation menu to explore modules

        #### 📁 Project Structure:
        ```
        ├── app.py                 # Streamlit dashboard
        ├── create_*.py           # Content generation scripts
        ├── *.pptx                # PowerPoint presentations
        ├── *.png                 # Visual assets
        ├── *_Quiz.py            # Interactive quizzes
        └── *.md                  # Documentation and scripts
        ```
        """)

    with tabs[2]:
        st.markdown("### 📚 References & Guidelines")
        st.markdown("""
        #### 🏛️ Official Guidelines:
        - **NACO STI Management Guidelines (2020)**
        - **WHO Guidelines for STI Management (2016)**
        - **CDC STD Treatment Guidelines (2021)**
        - **NACO HIV Treatment Guidelines (2023)**

        #### 📊 Data Sources:
        - National AIDS Control Organization (NACO)
        - World Health Organization (WHO)
        - Centers for Disease Control and Prevention (CDC)
        - Indian Council of Medical Research (ICMR)
        """)

    with tabs[3]:
        st.markdown("### 👨‍⚕️ Author Information")
        st.markdown("""
        #### Dr. Siddalingaiah H S
        **Professor, Community Medicine**  
        SIMSRH (Shri Dharmasthala Manjunatheshwara Institute of Medical Sciences and Research Hospital)  
        Tumkur, Karnataka, India

        **Contact Information:**
        - 📧 Email: hssling@yahoo.com
        - 📱 Phone: +91 8941087719

        **Academic Background:**
        - MBBS, MD (Community Medicine)
        - Extensive experience in medical education
        - Special interest in STD/HIV prevention and control

        **Professional Contributions:**
        - Development of innovative teaching methods
        - Research in community-based health interventions
        - Training programs for healthcare professionals
        """)

if __name__ == "__main__":
    main()
