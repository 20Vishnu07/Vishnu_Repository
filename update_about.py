import re

filepath = "src/components/About.jsx"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

replacements = [
    (
        "My technical narrative bridges rigorous algorithmic problem-solving with full-stack software architecture, translating complex backend logic into seamless, high-performance interfaces.",
        "My technical narrative bridges rigorous algorithmic problem-solving with scalable forward-deployed engineering. I specialize in translating complex GenAI models and backend logic into resilient, production-ready infrastructure using modern CI/CD, Docker, and Kubernetes."
    ),
    (
        ">Full-Stack Development<",
        ">Forward Deployed Engineering<"
    )
]

for old, new in replacements:
    content = content.replace(old, new)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated About.jsx")
