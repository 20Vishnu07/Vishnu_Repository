import re

filepath = "src/components/Hero.jsx"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Replacements for Hero.jsx
replacements = [
    (
        "AI & Full Stack Developer",
        "Forward Deployed Engineer"
    ),
    (
        "Node.js • React • Python",
        "GenAI • RAG • Kubernetes"
    ),
    (
        "GenAI & RAG",
        "Docker & CI/CD"
    ),
    (
        "Building AI-driven systems and end-to-end web applications with hands-on experience in Generative AI, React, Node.js, and Python.",
        "Architecting production-ready GenAI applications using LangChain and RAG pipelines. Bridging cutting-edge AI models with scalable infrastructure via Docker, Kubernetes, and highly automated CI/CD workflows."
    ),
    (
        "'FEATURE FILM // FULL-STACK ARCHITECT',\\s*'ORIGINAL SERIES // AI & ML SPECIALIST',\\s*'BLOCKBUSTER // DISTRIBUTED SYSTEMS',\\s*'ACCLAIMED // ALGORITHMIC PROBLEM SOLVER'",
        "'FEATURE FILM // FORWARD DEPLOYED ENGINEER',\n    'ORIGINAL SERIES // GEN-AI & RAG SPECIALIST',\n    'BLOCKBUSTER // KUBERNETES & CLOUD',\n    'ACCLAIMED // LANGCHAIN & LLM ARCHITECT'"
    )
]

for old, new in replacements:
    if isinstance(old, str) and '\\s*' in old:
        content = re.sub(old, new, content)
    else:
        content = content.replace(old, new)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated Hero.jsx")
