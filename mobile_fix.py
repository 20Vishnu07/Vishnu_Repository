import re

# 1. Fix Hero Photo Mobile Layout
with open("src/components/Hero.jsx", "r", encoding="utf-8") as f:
    hero = f.read()
hero = re.sub(
    r'className="w-full h-\[330px\] md:h-\[390px\] object-cover',
    r'className="w-full h-auto aspect-[4/5] md:aspect-auto md:h-[390px] object-cover',
    hero
)
# Turn down blur on mobile for Hero lag
hero = re.sub(
    r'blur-\[140px\]',
    r'blur-[60px] md:blur-[140px]',
    hero
)
with open("src/components/Hero.jsx", "w", encoding="utf-8") as f:
    f.write(hero)

# 2. Fix Skills gap on mobile
with open("src/components/Skills.jsx", "r", encoding="utf-8") as f:
    skills = f.read()
# Change snap gap
skills = re.sub(
    r'px-\[10vw\] md:px-0 gap-4 md:gap-0',
    r'px-[5vw] md:px-0 gap-6 md:gap-0',
    skills
)
with open("src/components/Skills.jsx", "w", encoding="utf-8") as f:
    f.write(skills)

# 3. Rewrite Projects.jsx to use native grid on mobile instead of buggy GSAP absolute positioning
with open("src/components/Projects.jsx", "r", encoding="utf-8") as f:
    projects = f.read()

# I will just write a clean Projects.jsx without the mobile GSAP logic, 
# replacing it with a simple tailwind responsive layout.
