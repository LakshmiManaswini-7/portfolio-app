# app.py — Streamlit portfolio for Lakshmi Manaswini Pulicharla
# ----------------------------------------------------
# Run locally:  streamlit run app.py
# Requirements: streamlit, pillow

import streamlit as st
from PIL import Image
import base64

def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# -------------------------
# DATA from resume
# -------------------------
PROFILE = {
    "name": "Lakshmi Manaswini Pulicharla",
    "role": "AI & ML Engineer | Data Scientist",
    "email": "plakshmimanaswini@gmail.com",
    "phone": "+1 314-913-6194",
    "location": "Saint Louis, Missouri, USA",
    "about": (
        "Machine Learning Engineer with 1 year of experience in building real-time monitoring solutions, optimizing SQL pipelines, "
        "and applying machine learning for anomaly detection and predictive insights. Proficient in Python, SQL, and Scikit-learn, with a proven record of improving system. "
        "Skilled in data visualization, statistical modeling, and automation, eager to deliver scalable, data-driven solutions"
    ),
    "photo_path": "assets/profile.jpg",
    "github": "https://github.com/LakshmiManaswini-7",
    "linkedin": "https://www.linkedin.com/in/lakshmi-manaswini-pulicharla",
}

SKILLS = {
    "Programming": ["Python", "Java", "C++", "C"],
    "Libraries/Frameworks": ["NumPy", "Pandas", "Scikit-learn", "TensorFlow", "PyTorch", "Keras", "XGBoost"],
    "ML Techniques": ["Regression", "Decision Trees", "Random Forest", "Gradient Boosting", "SVMs", "Clustering", "PCA", "Time-Series Forecasting", "Anomaly Detection"],
    "Deep Learning": ["Neural Networks", "NLP", "Computer Vision,LLM"],
    "Math/Stats": ["Probability", "Statistics", "Linear Algebra"],
    "Visualization": ["Matplotlib", "Seaborn", "Power BI"],
    "Databases": ["MySQL", "SQL Server"],
    "Tools": ["Git", "Docker", "Flask", "Jupyter", "VS Code", "PyCharm"],
}

EXPERIENCE = [
    {
        "company": "Value Information Technology Solutions Pvt. Ltd.",
        "role": "Machine Learning & Analytics Intern",
        "period": "Jan 2023 – Dec 2023",
        "location": "India",
        "bullets": [
            "Designed and deployed real-time dashboards using Kibana, Logstash, and Elastic for anomaly detection.",
            "Performed time-series forecasting and regression modeling, improving system reliability by 15%.",
            "Optimized SQL pipelines in MySQL and SQL Server, reducing query time by 30%.",
            "Built automated analytics framework in Python + Playwright, cutting manual reporting by 50%.",
            "Applied ML models for predictive monitoring and anomaly detection of system health."
        ],
        "tech": ["Python", "SQL", "Kibana", "Elastic", "Playwright"],
    },
]

PROJECTS = [
    {
        "name": "AI-powered SQL Chatbot",
        "desc": "Streamlit + Mistral LLM (Ollama) chatbot to translate natural language queries into SQL for CSV datasets.",
        "tech": ["Python", "Streamlit", "Ollama", "Mistral LLM", "DuckDB", "SQL"],
        "link": "https://github.com/LakshmiManaswini-7/sql-chatbot-streamlit",
        "image": "sql_chatbot.png", 
        # "impact": "Enabled non-technical users to analyze CSV data securely without SQL knowledge.",
    },
]

EDUCATION = [
    {
        "school": "Southeast Missouri State University",
        "program": "M.S. in Computer and Information Sciences",
        "period": "Jan 2024 - Dec 2025",
        "details": "GPA 3.72/4.0 | Coursework: ML, AI, Data Structures, Networks, Software Engineering, Data Analysis",
    }
]

RESUME_PDF_PATH = "assets/LakshmiManaswini_Resume.pdf"

# -------------------------
# UI CONFIG
# -------------------------
st.set_page_config(page_title=f"{PROFILE['name']} — Portfolio", page_icon="👩‍💻", layout="wide")

st.markdown("""
<style>
/* Global typography (increase font size for all text except headings) */
html, body, [class*="css"]  {
  font-size: 18px !important;   /* increased */
  line-height: 1.7;
}

/* Hero heading */
h1.hero {
  font-size: 42px;                 
  font-weight: 800;
  letter-spacing: 0.3px;
  margin-top: 0.25rem;
  margin-bottom: 0.75rem;
}

/* Section subheaders */
h2, .stMarkdown h2 {
  font-size: 26px !important;
  font-weight: 700 !important;
}

/* Tabs look like chunky buttons */
.stTabs [data-baseweb="tab-list"] {
  gap: 12px;
  border-bottom: 2px solid #ddd;
  padding-bottom: 6px;
}
.stTabs [data-baseweb="tab"] {
  background: #f6f7f9;
  border: 1px solid #000;       /* black border */
  border-bottom: 3px solid #000;
  padding: 10px 16px;
  border-radius: 14px;
  color: #111827;
  font-weight: 600;
  box-shadow: 0 1px 0 rgba(0,0,0,0.03);
}
.stTabs [aria-selected="true"] {
  background: #000;             /* black bg for active tab */
  border-color: #000;
  color: #fff;                  /* white text */
  border-bottom-color: #000;
}

/* Sidebar name + role chip */
.sidebar-name { font-size: 26px; font-weight: 800; margin-bottom: 4px; }
.role-chip {
  display:inline-block; padding:6px 10px; border-radius:999px;
  background:#111827; color:#fff; font-size:14px; font-weight:600;
}

/* Contact labels spacing */
.sidebar-contact p { margin: 0.25rem 0 }

/* Manu intro message box */
.Manu-intro {
  background: #000;
  color: #fff;
  padding: 12px 16px;
  border-radius: 10px;
  font-size: 17px;
  font-weight: 500;
  margin-top: 10px;
}

/* Experience card hover styles */
.exp-card {
    display: block;
    width: 100%;
    border-radius: 14px;
    overflow: hidden;
    transition: transform 0.25s ease, box-shadow 0.25s ease;
    cursor: pointer;
    margin: 14px 0 22px 0;
    border: 2px solid #000000;
    box-shadow: 0 2px 6px rgba(0,0,0,0.06);
    background-color: #ffffff;
}

.exp-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 12px 24px rgba(0,0,0,0.18);
}

.exp-left {
    flex: 1;
    padding: 18px 14px;
    background-color: #fef3c7;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
}

.exp-right {
    flex: 2;
    padding: 18px;
    background-color: #ffffff;
}

/* Project card */
.project-card {
    display: flex;
    flex-direction: column;
    align-items: center;
    border-radius: 16px;
    overflow: hidden;
    padding: 14px;
    margin-bottom: 28px;
    background-color: #fff;
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}

# /* Project image with hover */
# .project-image {
#     width: 100%;
#     max-width: 360px;   /* smaller size */
#     border-radius: 12px;
#     transition: transform 0.25s ease, box-shadow 0.25s ease;
#     cursor: pointer;
#     margin-bottom: 12px;
#     display: block;
# }
.project-image {
    width: 500px;        /* 👈 smaller like profile photo */
    height: auto;
    border-radius: 12px;
    transition: transform 0.25s ease, box-shadow 0.25s ease;
    cursor: pointer;
    margin-bottom: 12px;
    display: block;
}

.project-image:hover {
    transform: translateY(-6px) scale(1.03);
    box-shadow: 0 10px 22px rgba(0,0,0,0.25);
}



</style>
""", unsafe_allow_html=True)


# Sidebar
# -------------------------
with st.sidebar:
    if PROFILE.get("photo_path"):
        try:
            st.image(Image.open(PROFILE["photo_path"]), width=180)
        except Exception:
            st.info("Add your photo at assets/profile.jpg")

    st.markdown(f"<div class='sidebar-name'>{PROFILE['name']}</div>", unsafe_allow_html=True)
    st.markdown(f"<span class='role-chip'>{PROFILE['role']}</span>", unsafe_allow_html=True)

    st.markdown("### Contact")
    st.write(f"**Email:** {PROFILE['email']}")
    st.write(f"**Phone:** {PROFILE['phone']}")
    st.write(f"**Location:** {PROFILE['location']}")

    links = []
    if PROFILE.get("github"): links.append(f"[GitHub]({PROFILE['github']})")
    if PROFILE.get("linkedin"): links.append(f"[LinkedIn]({PROFILE['linkedin']})")
    if links:
        st.markdown("---")
        st.markdown(" • ".join(links))

# -------------------------
# Main hero (card)
# -------------------------
st.markdown("<div class='main-content-card'>", unsafe_allow_html=True)
st.markdown(f"<h1 class='hero'>Hi, I am {PROFILE['name']}!</h1>", unsafe_allow_html=True)
st.write(PROFILE["about"])
st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# Tabs — each tab's content is inside a tab-panel card now
# -------------------------
about_tab, skills_tab, exp_tab, projects_tab, resume_tab = st.tabs(
    ["👤 About Me", "🛠️ Skills", "💼 Experience", "📁 Projects", "📄 Resume"]
)

with about_tab:
    # tab-panel has its own card via CSS .stTabs [data-baseweb="tab-panel"]
    st.subheader("Education")
    for edu in EDUCATION:
        st.write(f"**{edu['school']}** — {edu['program']} ({edu['period']})")
        if edu.get("details"): st.caption(edu["details"])

st.markdown("""
<style>
.skill-card {
    border-radius: 12px;
    padding: 16px 20px;
    margin-bottom: 14px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    cursor: pointer;
    display: inline-block;  /* important for hover in columns */
    width: 100%;            /* take full column width */
}
.skill-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 18px rgba(0,0,0,0.25);
}
</style>
""", unsafe_allow_html=True)
with skills_tab:
    st.subheader("Technical Skills")
    cols = st.columns(2)
    i = 0

    # pastel colors
    skill_colors = ["#fde2e2", "#e0f7fa", "#fff3e0", "#e8f5e9", "#f3e5f5", "#e1f5fe", "#fff9c4", "#ffe0b2"]

    for idx, (category, skills_list) in enumerate(SKILLS.items()):
        color = skill_colors[idx % len(skill_colors)]
        with cols[i % 2]:
            st.markdown(
                f"""
                <div class='skill-card' style='background-color:{color};'>
                    <strong>{category}:</strong> {', '.join(skills_list)}
                </div>
                """,
                unsafe_allow_html=True
            )
        i += 1



def experience_card(job, left_bg="#fef3c7"):
    st.markdown(
        f"""
        <div class="exp-card">
          <div style="display:flex; flex-direction:row; align-items:stretch;">
            <div class="exp-left" style="background-color:{left_bg};">
              <h4 style="margin:0; font-weight:700; color:#000000;">{job['company']}</h4>
              <p style="margin:6px 0 2px 0; font-weight:700; color:#000000;">{job['role']}</p>
              <p style="margin:0; font-size:13px; color:#111111;">{job['period']}</p>
            </div>
            <div class="exp-right">
              <ul style="margin:0; padding-left:20px;">
                {''.join([f"<li style='margin-bottom:8px; font-size:16px; color:#111111;'>{b}</li>" for b in job['bullets']])}
              </ul>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# inside your exp_tab
with exp_tab:
    st.subheader("Experience")
    for job in EXPERIENCE:
        experience_card(job)

# with projects_tab:
#     st.subheader("Featured Projects")
#     for p in PROJECTS:
#         title = f"**[{p['name']}]({p['link']})**" if p.get("link") else p['name']
#         st.markdown(f"{title} — {', '.join(p['tech'])}")
#         st.write(p['desc'])
#         if p.get("impact"): st.caption(p["impact"])
#         st.markdown("---")
with projects_tab:
    st.subheader("Featured Projects")

    for p in PROJECTS:
        img_b64 = img_to_base64(f"assets/{p['image']}")

        st.markdown(
            f"""
            <div class="project-card">
                <a href="{p['link']}" target="_blank">
                    <img src="data:image/png;base64,{img_b64}" class="project-image" alt="{p['name']}"/>
                </a>
                <h4 style="margin:6px 0; font-weight:700; color:#000000;">{p['name']}</h4>
                <p style="margin:6px 0; font-size:15px; color:#111111;">{p['desc']}</p>
                <p style="margin:0; font-size:13px; color:#555555;"><i>{", ".join(p['tech'])}</i></p>
            </div>
            """,
            unsafe_allow_html=True
        )



with resume_tab:
    st.subheader("Resume")
    try:
        st.download_button("⬇️ Download my resume", RESUME_PDF_PATH, file_name="LakshmiManaswini_Resume.pdf")
    except Exception:
        st.info("Place your PDF at assets/LakshmiManaswini_Resume.pdf")

# -------------------------
# Chatbot area — black intro card + chat bubbles
# -------------------------
st.markdown("<div class='chat-section'>", unsafe_allow_html=True)
st.subheader("Ask me anything about my profile 🚀")

# Black intro card under the bot
intro_html = """
<div class='bot-intro'>
Hi! I'm Manu, Lakshmi Manaswini's AI assistant. Ask me anything about her skills, experience, projects, qualifications or visa status! 🚀
</div>
# """
# st.markdown(intro_html, unsafe_allow_html=True)
st.markdown(
    "<div class='Manu-intro'>Hi! I'm Manu, Lakshmi Manaswini's AI assistant. "
    "Ask me anything about her skills, experience, projects, qualifications or visa status! 🚀</div>",
    unsafe_allow_html=True
)

# chat input
# question = st.chat_input("Type your question here…")
user_question = st.chat_input("Type your question here...")

# show conversational bubbles
if user_question:
    # show user bubble
    st.markdown(f"<div class='chat-user'>{user_question}</div>", unsafe_allow_html=True)

    # assistant reply logic (simple rule-based for demo)
    q = user_question.lower()
    if "skills" in q:
        answer = "Key skills: " + ", ".join(sum(SKILLS.values(), []))
    elif "experience" in q or "work" in q:
        answer = f"I have {len(EXPERIENCE)} professional role(s) listed, with impact in ML, SQL, and automation."
    elif "project" in q:
        answer = f"One highlight is my AI-powered SQL chatbot using Streamlit + Ollama Mistral."
    elif "visa" in q or "work authorization" in q or "sponsorship" in q:
        answer = "Currently on an F-1 visa, eligible to work on OPT, and seeking sponsorship after 3 years."
    else:
        answer = "Thanks for asking! I’d be happy to chat about my skills, projects, or goals."

    # show assistant bubble with black background + white text
    st.markdown(f"<div class='chat-assistant'>{answer}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)  # close chat-section
