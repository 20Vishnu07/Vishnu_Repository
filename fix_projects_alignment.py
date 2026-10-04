import re

filepath = "src/components/Projects.jsx"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the GSAP explosion coordinates to be fully responsive
old_block = """            // 3. Cards magically spread out into an ultra-clean blockbuster grid layout
            tl.to(cardsRef.current, {
              x: (i) => {
                const w = Math.max(...cardsRef.current.map(c => c?.offsetWidth || 0)) || 360;
                const gap = 40;
                const { col } = getGridPos(i);
                return (col - 1) * (w + gap);
              },
              y: (i) => {
                const h = Math.max(...cardsRef.current.map(c => c?.offsetHeight || 0)) || 240;
                const gap = 40;
                const { row } = getGridPos(i);
                return (row - 1) * (h + gap);
              },"""

new_block = """            // 3. Cards magically spread out into an ultra-clean blockbuster grid layout
            tl.to(cardsRef.current, {
              x: (i) => {
                // Responsively calculate width so it never overflows off the right side
                const cardW = cardsRef.current[i]?.offsetWidth || 340;
                const gap = Math.min(40, window.innerWidth * 0.02);
                const { col } = getGridPos(i);
                return (col - 1) * (cardW + gap);
              },
              y: (i) => {
                const cardH = cardsRef.current[i]?.offsetHeight || 220;
                const gap = Math.min(40, window.innerHeight * 0.03);
                const { row } = getGridPos(i);
                return (row - 1) * (cardH + gap);
              },"""

if old_block in content:
    content = content.replace(old_block, new_block)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Fixed GSAP X/Y calculations.")
else:
    print("Could not find the old block to replace.")
