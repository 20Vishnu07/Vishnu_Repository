import re

filepath = "src/components/Skills.jsx"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Extract from "const skillCategories =" to "];"
pattern = r'const skillCategories = \[.*?\];'

new_skills_data = """const skillCategories = [
  { 
    title: 'Generative AI & LLMs', 
    desc: 'Building intelligent AI applications using state-of-the-art LLMs, LangChain, RAG, and Context Engineering.', 
    tag: 'INTELLIGENCE',
    skills: ['OpenAI', 'Gemini & Claude', 'LangChain', 'RAG', 'Prompt Engineering'] 
  },
  { 
    title: 'Forward Deployed Eng', 
    desc: 'Bridging technical gaps by developing scalable architectures and driving customer-facing integrations.', 
    tag: 'ARCHITECTURE',
    skills: ['React.js', 'Next.js', 'Node.js', 'FastAPI', 'Microservices'] 
  },
  { 
    title: 'Programming Languages', 
    desc: 'Core languages for backend logic, scripting, data analysis, and embedded system development.', 
    tag: 'CORE LOGIC',
    skills: ['C++', 'Python', 'Java', 'SQL', 'HTML/CSS'] 
  },
  { 
    title: 'Cloud & Kubernetes', 
    desc: 'Deploying scalable production architectures using Kubernetes, Docker, and highly automated CI/CD.', 
    tag: 'INFRASTRUCTURE',
    skills: ['Kubernetes', 'Docker', 'CI/CD Pipelines', 'AWS', 'GCP'] 
  },
  { 
    title: 'Tools & Ecosystem', 
    desc: 'Equipped with industry-grade instruments for version control, databases, and platform integration.', 
    tag: 'ECOSYSTEM',
    skills: ['Git & GitHub', 'PostgreSQL', 'Redis', 'MATLAB', 'WebSockets'] 
  },
  { 
    title: 'Data & Machine Learning', 
    desc: 'Building predictive ML pipelines and data processing ecosystems for practical applications.', 
    tag: 'PREDICTIVE',
    skills: ['scikit-learn', 'Data Modeling', 'Data Visualization', 'Leaflet', 'Python Data Stack'] 
  },
];"""

content = re.sub(pattern, new_skills_data, content, flags=re.DOTALL)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated Skills.jsx")
