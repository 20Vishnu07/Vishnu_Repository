import re

new_projects_data = """const projectsData = [
  {
    title: "DEARES EV Estimator",
    category: "AI & Embedded Systems",
    description: "Energy-aware EV range and state-of-charge estimator using a Kalman filter and physics-based modelling. 1st Prize Hackathon.",
    tags: ["Python", "C++", "Kalman Filter"],
    match: "99%",
    episode: "S01 E01"
  },
  {
    title: "LangBridge",
    category: "Generative AI",
    description: "Multilingual speech and text translation pipeline (ASR, MT, TTS) for Indian regional languages built for Smart India Hackathon.",
    tags: ["Node.js", "React", "PostgreSQL", "Redis"],
    match: "98%",
    episode: "S01 E02"
  },
  {
    title: "NourishNet",
    category: "Full-Stack Web App",
    description: "Surplus food redistribution platform with map-based discovery, phone-OTP authentication, and ML surplus prediction.",
    tags: ["Next.js", "FastAPI", "MySQL", "Scikit-Learn"],
    match: "97%",
    episode: "S01 E03"
  },
  {
    title: "Bus Navigation Backend",
    category: "Backend Architecture",
    description: "Backend system for real-time bus navigation, developed as part of Google Developer Group On-Campus.",
    tags: ["Node.js", "FastAPI", "PostgreSQL"],
    match: "99%",
    episode: "S01 E04"
  },
  {
    title: "Workora Hospital DB",
    category: "Full-Stack Development",
    description: "User authentication system and hospital database maintenance website developed during internship.",
    tags: ["React", "SQL", "Auth"],
    match: "96%",
    episode: "S01 E05"
  },
  {
    title: "Thiranex E-Commerce",
    category: "Web Engineering",
    description: "E-commerce platform and task manager application built during full-stack internship.",
    tags: ["React", "JavaScript", "CSS"],
    match: "99%",
    episode: "S01 E06"
  },
  {
    title: "Portfolio Cinematics",
    category: "UI/UX & Animation",
    description: "Award-winning dark studio interactive portfolio featuring GSAP physics and responsive layouts.",
    tags: ["React", "GSAP", "Tailwind", "Vite"],
    match: "99%",
    episode: "S01 E07"
  }
];"""

filepath = "src/components/Projects.jsx"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the existing projectsData array
pattern = r'const projectsData = \[\s*\{.*?\}\s*\];'
content = re.sub(pattern, new_projects_data, content, flags=re.DOTALL)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated Projects.jsx")
