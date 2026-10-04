import os

replacements = {
    "Hero.jsx": [
        ("SUSHMITA", "VISHNU D"),
        ("DEV.ENGINE", "DEV"),
        ("Software Engineer & Problem Solver", "AI & Full Stack Developer"),
        ("React â€¢ Node.js â€¢ PostgreSQL", "Node.js • React • Python"),
        ("React • Node.js • PostgreSQL", "Node.js • React • Python"),
        ("Docker & Cloud", "GenAI & RAG"),
        ("Architecting robust full-stack systems, building scalable multi-tenant SaaS platforms, and engineering cutting-edge AI integrations.", "Building AI-driven systems and end-to-end web applications with hands-on experience in Generative AI, React, Node.js, and Python."),
        ("Flipkart GRiD 7.0 Semi-Finalist, AlgoUniversity Tech Fellow, GitHub Foundations Certified.", "1st Prize - Internal Hackathon 2026, Backend Member at GDG, and AI Enthusiast."),
        ("SUSHMITA<span", "VISHNU<span"),
        ("picture.png", "vishnu_photo.jpg")
    ],
    "About.jsx": [
        ("Dasari Venkata Ratna Sri Sushmita", "Vishnu D"),
        ("a B.Tech student in Artificial Intelligence and Machine Learning at Aditya Engineering College", "a B.E. ECE student at R.M.K. Engineering College"),
        ("National Semi-Finalist in <strong className=\"text-white\">Flipkart GRiD 7.0</strong> competition.", "1st Prize in <strong className=\"text-white\">Internal Hackathon 2026 (RMKEC)</strong> & 3rd Prize in Paper Presentation."),
        ("Member of the elite <strong className=\"text-white\">AlgoUniversity Tech Fellowship</strong> for advanced data structures.", "Backend Development Member at <strong className=\"text-white\">Google Developer Group On-Campus - RMKEC</strong>."),
        ("Certified <strong className=\"text-white\">GitHub Foundations</strong> & <strong className=\"text-white\">AWS Certified AI Practitioner</strong>.", "Certified in <strong className=\"text-white\">Qualcomm AI Upskilling</strong> & <strong className=\"text-white\">IBM AI-Assisted Code</strong>."),
        ("'React', 'Node.js', 'Express', 'PostgreSQL', 'MongoDB', 'Docker', 'JavaScript'", "'React', 'Node.js', 'Python', 'FastAPI', 'PostgreSQL', 'GenAI', 'C++'"),
        ("ABOUT THE ENGINEER", "ABOUT THE DEVELOPER")
    ],
    "Expertise.jsx": [
        ("SUSHMITA", "VISHNU D")
    ],
    "Skills.jsx": [
        ("SUSHMITA", "VISHNU D")
    ],
    "Projects.jsx": [
        ("SUSHMITA", "VISHNU D")
    ],
    "Contact.jsx": [
        ("SUSHMITA", "VISHNU D"),
        ("dasarisushmita30@gmail.com", "240241.ea@rmkec.ac.in"),
        ("+91 1234567890", "+91 9342842677")
    ],
    "Footer.jsx": [
        ("SUSHMITA", "VISHNU D"),
        ("Dasari Venkata Ratna Sri Sushmita", "Vishnu D")
    ]
}

base_dir = "src/components"

for filename, rules in replacements.items():
    filepath = os.path.join(base_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        for old_text, new_text in rules:
            content = content.replace(old_text, new_text)
            
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {filename}")
