import re

filepath = "src/components/Skills.jsx"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the specific title
content = content.replace("title: 'Forward Deployed Eng',", "title: 'Forward Deployed Engineering',")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated Skills.jsx")
