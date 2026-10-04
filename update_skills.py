import re

new_skills_data = """const skillCategories = [
  { 
    title: 'Generative AI & LLMs', 
    desc: 'Building intelligent AI applications using state-of-the-art LLMs, RAG, and Context Engineering.', 
    tag: 'INTELLIGENCE',
    skills: ['OpenAI', 'Gemini & Claude', 'Ollama', 'RAG', 'Prompt Engineering'] 
  },
  { 
    title: 'Web Development', 
    desc: 'Developing scalable web architectures and user interfaces with modern web frameworks.', 
    tag: 'ARCHITECTURE',
    skills: ['React.js', 'Next.js', 'Node.js', 'FastAPI', 'MySQL'] 
  },
  { 
    title: 'Programming Languages', 
    desc: 'Core languages for backend logic, scripting, data analysis, and embedded system development.', 
    tag: 'CORE LOGIC',
    skills: ['C++', 'Python', 'Java', 'SQL', 'HTML/CSS'] 
  },
  { 
    title: 'Electronics & Hardware', 
    desc: 'Familiarity with foundational hardware, microcontrollers, and communication systems.', 
    tag: 'SYSTEMS',
    skills: ['Microcontrollers', 'Microprocessors', 'Communication Systems', 'Embedded C++', 'Sensors'] 
  },
  { 
    title: 'Tools & Cloud', 
    desc: 'Equipped with industry-grade instruments for version control, databases, and platform integration.', 
    tag: 'ECOSYSTEM',
    skills: ['Git & GitHub', 'PostgreSQL', 'Redis & Firebase', 'MATLAB', 'WebSockets'] 
  },
  { 
    title: 'Data & Machine Learning', 
    desc: 'Building predictive ML pipelines and data processing ecosystems for practical applications.', 
    tag: 'PREDICTIVE',
    skills: ['scikit-learn', 'Data Modeling', 'Data Visualization', 'Leaflet', 'Python Data Stack'] 
  },
];"""

filepath = "src/components/Skills.jsx"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

pattern = r'const skillCategories = \[\s*\{.*?\}\s*\];'
content = re.sub(pattern, new_skills_data, content, flags=re.DOTALL)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated Skills.jsx")
