import re

filepath = "src/components/Expertise.jsx"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

replacements = [
    (
        'title: "Full Stack Web Development"',
        'title: "Forward Deployed Engineering"'
    ),
    (
        'tag: "WEB ARCHITECTURE"',
        'tag: "ARCHITECTURE & INFRASTRUCTURE"'
    ),
    (
        'text: "Developing end-to-end web applications with React.js, Next.js, Node.js, and FastAPI. Architecting secure databases with PostgreSQL and MySQL."',
        'text: "Deploying and scaling complex web architectures using React, FastAPI, Node.js, and Docker. Ensuring seamless infrastructure with Kubernetes and automated CI/CD pipelines."'
    )
]

for old, new in replacements:
    content = content.replace(old, new)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated Expertise.jsx")
