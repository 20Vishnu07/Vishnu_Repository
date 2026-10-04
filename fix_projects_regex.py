import re

filepath = "src/components/Projects.jsx"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

pattern = re.compile(
    r'x:\s*\(\w+\)\s*=>\s*\{[^}]+\},\s*'
    r'y:\s*\(\w+\)\s*=>\s*\{[^}]+\},',
    re.MULTILINE
)

new_logic = """x: (i) => {
              const cardW = cardsRef.current[i]?.offsetWidth || 340;
              const gap = window.innerWidth * 0.02; // Dynamic 2vw gap to prevent overflow
              const { col } = getGridPos(i);
              return (col - 1) * (cardW + gap);
            },
            y: (i) => {
              const cardH = cardsRef.current[i]?.offsetHeight || 220;
              const gap = window.innerHeight * 0.03;
              const { row } = getGridPos(i);
              return (row - 1) * (cardH + gap);
            },"""

if pattern.search(content):
    content = pattern.sub(new_logic, content)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Replaced successfully using regex.")
else:
    print("Regex failed to match.")
