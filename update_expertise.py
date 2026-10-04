import re

new_expertise_data = """const expertiseData = [
  {
    number: "01",
    title: "Generative AI & LLMs",
    text: "Building AI-driven systems utilizing OpenAI, Gemini, Claude models, and local LLMs. Experienced in RAG and Prompt Engineering.",
    tag: "AI & INTELLIGENCE",
    gradient: "from-[#1f0a0c] via-[#121212] to-[#0a0a0a]"
  },
  {
    number: "02",
    title: "Full Stack Web Development",
    text: "Developing end-to-end web applications with React.js, Next.js, Node.js, and FastAPI. Architecting secure databases with PostgreSQL and MySQL.",
    tag: "WEB ARCHITECTURE",
    gradient: "from-[#1a0809] via-[#111111] to-[#090909]"
  },
  {
    number: "03",
    title: "Electronics & Embedded",
    text: "Developing embedded C++ firmware, communication systems, and microcontrollers. Prototyped EV range estimators with Kalman filters.",
    tag: "HARDWARE & SYSTEMS",
    gradient: "from-[#220a0d] via-[#131313] to-[#0a0a0a]"
  },
  {
    number: "04",
    title: "Machine Learning & Predictive",
    text: "Implementing predictive models using scikit-learn and Python. Applied ML for surplus food prediction and EV state-of-charge tracking.",
    tag: "PREDICTIVE MODELING",
    gradient: "from-[#1d090b] via-[#101010] to-[#080808]"
  }
];"""

filepath = "src/components/Expertise.jsx"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

pattern = r'const expertiseData = \[\s*\{.*?\}\s*\];'
content = re.sub(pattern, new_expertise_data, content, flags=re.DOTALL)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated Expertise.jsx")
