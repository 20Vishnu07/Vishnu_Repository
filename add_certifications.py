import os
import re

certifications_component = """import { useEffect, useRef } from 'react';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

const certData = [
  { issuer: "Microsoft", title: "Introduction to Generative AI Concepts", tag: "AI / GenAI", match: "99% Match" },
  { issuer: "Qualcomm", title: "AI Upskilling: Technical Foundation", tag: "Artificial Intelligence", match: "98% Match" },
  { issuer: "IBM / ProoV", title: "AI-Assisted Code Modernization", tag: "Code Modernization", match: "99% Match" },
  { issuer: "Scaler", title: "Docker & Kubernetes Masterclass", tag: "Cloud & DevOps", match: "97% Match" },
  { issuer: "Coursera", title: "Embedded Software Design Foundation", tag: "Hardware / C++", match: "98% Match" },
  { issuer: "Infosys", title: "TechA C++ Programming Advanced", tag: "Programming", match: "99% Match" },
  { issuer: "Infosys", title: "Internet of Things Foundation", tag: "IoT", match: "96% Match" },
  { issuer: "Infosys", title: "Software Engineering & Agile", tag: "Methodology", match: "97% Match" },
  { issuer: "Infosys", title: "Data Structures and Algorithms", tag: "Problem Solving", match: "99% Match" },
  { issuer: "MathWorks", title: "MATLAB Onramp", tag: "Data / Engineering", match: "95% Match" },
  { issuer: "Workora", title: "Full Stack Development Internship", tag: "Web Architecture", match: "100% Match" },
  { issuer: "Kodacy & SPACE", title: "AI & Machine Learning Internship", tag: "Machine Learning", match: "98% Match" },
  { issuer: "GDG RMKEC", title: "Backend Development Member", tag: "Community", match: "99% Match" },
  { issuer: "IEEE", title: "Communications Society Member", tag: "Professional", match: "95% Match" },
  { issuer: "NPTEL", title: "Soft Skill Development", tag: "Professional Skills", match: "94% Match" },
];

const Certifications = () => {
  const containerRef = useRef(null);
  const scrollRef = useRef(null);

  useEffect(() => {
    let ctx = gsap.context(() => {
      gsap.from(".cert-header", {
        y: 30,
        opacity: 0,
        duration: 0.8,
        ease: "power3.out",
        scrollTrigger: {
          trigger: containerRef.current,
          start: "top 80%",
        }
      });
      
      gsap.from(".cert-card", {
        x: 50,
        opacity: 0,
        duration: 0.6,
        stagger: 0.1,
        ease: "back.out(1.2)",
        scrollTrigger: {
          trigger: ".cert-card-container",
          start: "top 85%",
        }
      });
    }, containerRef);
    return () => ctx.revert();
  }, []);

  return (
    <section ref={containerRef} className="bg-[#050505] py-24 pl-6 md:pl-12 overflow-hidden select-none">
      <div className="cert-header mb-8 flex flex-col space-y-2">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded bg-red-600/10 border border-red-600/30 text-[10px] font-mono uppercase tracking-widest text-red-500 w-max">
          <span className="w-1.5 h-1.5 rounded-full bg-red-600 animate-pulse"></span>
          OFFICIAL CREDENTIALS
        </div>
        <h2 className="text-3xl md:text-4xl font-black text-white tracking-tight">
          Trending Certifications & Memberships
        </h2>
        <p className="text-white/60 text-sm font-light">
          A continuous commitment to mastering cutting-edge technology and engineering practices.
        </p>
      </div>

      {/* Horizontal Netflix-style scroll row */}
      <div 
        ref={scrollRef}
        className="cert-card-container flex gap-4 overflow-x-auto pb-8 pr-12 snap-x snap-mandatory scrollbar-hide"
        style={{ scrollbarWidth: 'none', msOverflowStyle: 'none' }}
      >
        <style>{`.scrollbar-hide::-webkit-scrollbar { display: none; }`}</style>
        
        {certData.map((cert, i) => (
          <div 
            key={i} 
            className="cert-card snap-start shrink-0 w-[260px] md:w-[320px] aspect-[16/9] bg-[#141414] border border-white/10 rounded-xl p-5 flex flex-col justify-between group hover:border-red-600/50 hover:bg-[#1a1a1a] hover:scale-105 transition-all duration-300 cursor-pointer shadow-xl relative overflow-hidden"
          >
            {/* Glossy overlay */}
            <div className="absolute inset-0 bg-gradient-to-tr from-red-600/0 via-white/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none" />
            
            <div className="flex justify-between items-start relative z-10">
              <span className="text-[10px] font-bold tracking-widest uppercase text-red-500 bg-red-600/10 px-2 py-0.5 rounded">
                {cert.issuer}
              </span>
              <span className="text-[10px] font-mono font-bold text-[#46d369]">
                {cert.match}
              </span>
            </div>
            
            <div className="space-y-1 relative z-10">
              <h3 className="text-lg font-bold text-white leading-tight group-hover:text-red-500 transition-colors">
                {cert.title}
              </h3>
            </div>
            
            <div className="flex items-center gap-2 pt-2 border-t border-white/10 relative z-10">
              <span className="text-[9px] font-mono uppercase tracking-widest text-white/50 border border-white/20 px-1.5 py-0.5 rounded">
                {cert.tag}
              </span>
              <span className="text-[9px] font-mono text-white/30 border border-white/10 px-1.5 py-0.5 rounded">
                VERIFIED
              </span>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
};

export default Certifications;
"""

with open("src/components/Certifications.jsx", "w", encoding="utf-8") as f:
    f.write(certifications_component)
print("Created Certifications.jsx")

# Now inject it into App.jsx
app_path = "src/App.jsx"
with open(app_path, "r", encoding="utf-8") as f:
    app_content = f.read()

if "import Certifications" not in app_content:
    # Insert import
    app_content = app_content.replace(
        "import Projects from './components/Projects';",
        "import Projects from './components/Projects';\nimport Certifications from './components/Certifications';"
    )
    # Insert component before Contact
    app_content = app_content.replace(
        "<Contact />",
        "<Certifications />\n      <Contact />"
    )
    with open(app_path, "w", encoding="utf-8") as f:
        f.write(app_content)
    print("Injected into App.jsx")

# Finally, update the milestones text in About.jsx
about_path = "src/components/About.jsx"
with open(about_path, "r", encoding="utf-8") as f:
    about_content = f.read()

old_ul = r'<ul className="space-y-3\.5 text-sm text-white/80 font-light">.*?</ul>'
new_ul = """<ul className="space-y-3.5 text-sm text-white/80 font-light">
                <li className="flex items-start gap-2.5">
                  <span className="text-red-500 font-bold">&#8250;</span>
                  <span>1st Prize in <strong className="text-white">Internal Hackathon 2026 (RMKEC)</strong> & 3rd Prize in Paper Presentation.</span>
                </li>
                <li className="flex items-start gap-2.5">
                  <span className="text-red-500 font-bold">&#8250;</span>
                  <span>Backend Member at <strong className="text-white">GDG On-Campus</strong> & active <strong className="text-white">IEEE ComSoc</strong> Student Member.</span>
                </li>
                <li className="flex items-start gap-2.5">
                  <span className="text-red-500 font-bold">&#8250;</span>
                  <span><strong>15+ Professional Certifications</strong> spanning AI (Microsoft, Qualcomm, IBM), Cloud & DevOps (Docker, Kubernetes), and Embedded Systems.</span>
                </li>
              </ul>"""

about_content = re.sub(old_ul, new_ul, about_content, flags=re.DOTALL)
with open(about_path, "w", encoding="utf-8") as f:
    f.write(about_content)
print("Updated About.jsx Milestones")
