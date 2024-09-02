import streamlit as st

# Configure the page
st.set_page_config(page_title="Namitha Muraleedharan - Portfolio", layout="wide", page_icon=":wave:")

# Custom CSS to mimic the look and feel
st.markdown("""
    <style>
    body {
        background-color: #000000;
        font-family: 'Arial', sans-serif;
        color: #ffffff;
    }
    .main {
        padding: 20px;
        background-color: #1c1c1c;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        margin-bottom: 20px;
        color: #ffffff;
    }
    .header {
        background-color: #000000;
        padding: 20px;
        text-align: center;
        color: #ffffff;
    }
    .header h1 {
        color: #ff0000;
    }
    .nav-links {
        margin-top: 10px;
    }
    .nav-links a {
        color: #ffffff;
        margin: 0 15px;
        text-decoration: none;
        font-weight: bold;
    }
    .nav-links a:hover {
        text-decoration: underline;
    }
    .section-title {
        font-size: 28px;
        margin: 20px 0;
        color: #ffffff;
        text-align: center;
    }
    .project {
        margin-bottom: 40px;
        color: #ffffff;
    }
    .footer {
        text-align: center;
        padding: 20px;
        background-color: #000000;
        color: #ffffff;
        margin-top: 20px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("""
    <div class="header">
        <h1>Namitha Muraleedharan</h1>
        <div class="nav-links">
            <a href="#about">About</a>
            <a href="#skills">Skills</a>
            <a href="#projects">Projects</a>
            <a href="#contact">Contact</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# About Section
st.markdown('<div class="main" id="about">', unsafe_allow_html=True)
st.markdown('<div class="section-title">About Me</div>', unsafe_allow_html=True)
st.write("""
Hi, I'm Namitha Muraleedharan, a Machine Learning Engineer with a passion for developing AI solutions. My expertise lies in Natural Language Processing, Computer Vision, and deploying machine learning models.
""")
st.markdown('</div>', unsafe_allow_html=True)

# Skills Section
st.markdown('<div class="main" id="skills">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Skills</div>', unsafe_allow_html=True)
st.write("""
- **Programming Languages**: Python, SQL, R, Java
- **Machine Learning/AI Frameworks**: TensorFlow, PyTorch, BERT, GPT-3.5, Langchain
- **Data Processing**: Pandas, NumPy, spaCy
- **Cloud Platforms**: AWS, Google Colab
- **Automation**: Docker, Airflow
- **Tools**: GIT, JIRA, Confluence
""")
st.markdown('</div>', unsafe_allow_html=True)

# Projects Section
st.markdown('<div class="main" id="projects">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Projects</div>', unsafe_allow_html=True)

# Project 1
st.markdown('<div class="project">', unsafe_allow_html=True)
st.image("https://play-lh.googleusercontent.com/U_rTBs4x6CTiaCb2IJjzAbExaWDjM3r6dRv2Yrx2yO-wCyeNBg4XrIjGUC8H0GwdiIrD", caption="AI-Powered Chatbot for FoodEasy", width=400)
st.write("""
Developed a chatbot using a custom LLM pipeline for personalized meal planning.
""")
st.markdown('</div>', unsafe_allow_html=True)

# Project 2
st.markdown('<div class="project">', unsafe_allow_html=True)
st.image("https://th.bing.com/th/id/R.6bc84f05421629a3613c76ac3ab640cc?rik=jbhcxoe%2fQi%2frag&pid=ImgRaw&r=0", caption="Waste Segregation System", width=400)
st.write("""
Built a waste segregation system using computer vision, deploying the model on AWS.
""")
st.markdown('</div>', unsafe_allow_html=True)

# Contact Section
st.markdown('<div class="main" id="contact">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Contact</div>', unsafe_allow_html=True)
st.write("Feel free to reach out through any of the following channels:")

st.write("📧 [Email](mailto:namithamurali01@gmail.com)")
st.write("🔗 [LinkedIn](https://www.linkedin.com/in/namitha-muraleedharan)")
st.write("📞 +1 (437)-566-3236")
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <p>© 2024 Namitha Muraleedharan</p>
    </div>
""", unsafe_allow_html=True)
