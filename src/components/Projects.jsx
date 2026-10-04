import { useEffect, useRef } from 'react';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

const projectsData = [
  {
    title: "DEARES (Data Encoding & Retrieval System)",
    episode: "EPISODE 01",
    category: "RAG & LLM Engine",
    description: "Architected a decentralized query engine combining retrieval-augmented generation with high-availability datastores.",
    tags: ["LangChain", "VectorDB", "FastAPI"],
    match: "99%"
  },
  {
    title: "LangBridge Agentic Framework",
    episode: "EPISODE 02",
    category: "Autonomous Systems",
    description: "Built scalable multi-agent workflows capable of autonomous self-correction and complex reasoning pipelines.",
    tags: ["OpenAI", "React", "Python"],
    match: "98%"
  },
  {
    title: "NourishNet Optimization",
    episode: "EPISODE 03",
    category: "Cloud Infrastructure",
    description: "Deployed containerized predictive models reducing latency by 40% and orchestrating continuous delivery.",
    tags: ["Docker", "Kubernetes", "CI/CD"],
    match: "97%"
  },
  {
    title: "Portfolio Architecture",
    episode: "EPISODE 04",
    category: "Frontend Systems",
    description: "Engineered a high-performance web experience with fluid animations and responsive cinematic UI.",
    tags: ["React", "GSAP", "Tailwind"],
    match: "96%"
  },
  {
    title: "IoT Fleet Manager",
    episode: "EPISODE 05",
    category: "Edge Computing",
    description: "Designed robust firmware integrations communicating securely with cloud dashboards for real-time tracking.",
    tags: ["C++", "IoT", "AWS"],
    match: "95%"
  }
];

const Projects = () => {
  const containerRef = useRef(null);
  const folderBackRef = useRef(null);
  const folderFrontRef = useRef(null);
  const cardsRef = useRef([]);

  useEffect(() => {
    let ctx = gsap.context(() => {
      // ONLY apply GSAP to Desktop (>768px)
      ScrollTrigger.matchMedia({
        "(min-width: 768px)": function() {
          const tl = gsap.timeline({
            scrollTrigger: {
              trigger: containerRef.current,
              start: "top top",
              end: "+=2000",
              scrub: 1,
              pin: true,
              anticipatePin: 1
            }
          });

          // Reset everything for desktop
          gsap.set(cardsRef.current, { clearProps: "all" });
          gsap.set(cardsRef.current, { 
            y: 0, 
            scale: 0.8, 
            opacity: 0,
            rotation: 0
          });
          gsap.set(folderFrontRef.current, { transformOrigin: "bottom center" });
          
          const getGridPos = (index) => {
            let row, col;
            if (index < 3) { row = 0; col = index; }
            else if (index === 3) { row = 1; col = 0; }
            else if (index === 4) { row = 1; col = 2; }
            else { row = 2; col = index - 5; }
            return { row, col };
          };

          tl.to(folderFrontRef.current, {
            rotationX: -85,
            duration: 0.5,
            ease: "power2.inOut"
          });

          tl.to(cardsRef.current, {
            y: -300,
            opacity: 1,
            scale: 0.9,
            duration: 0.8,
            stagger: 0.1,
            ease: "back.out(1.2)"
          }, "-=0.6");

          tl.to(cardsRef.current, {
            x: (i) => {
              const w = 380;
              const gap = 40;
              const { col } = getGridPos(i);
              return (col - 1) * (w + gap);
            },
            y: (i) => {
              const h = 240;
              const gap = 40;
              const { row } = getGridPos(i);
              return (row - 1) * (h + gap);
            },
            rotation: () => gsap.utils.random(-3, 3),
            scale: 1,
            duration: 1.4,
            stagger: 0.05,
            ease: "power3.inOut"
          }, "-=0.2");
        },
        
        // Mobile cleanup
        "(max-width: 767px)": function() {
          // Clear GSAP properties on mobile so Tailwind takes over
          gsap.set(cardsRef.current, { clearProps: "all" });
        }
      });
    }, containerRef);

    return () => ctx.revert();
  }, []);

  return (
    <section id="projects" ref={containerRef} className="bg-[#0b0b0b] min-h-[100svh] md:min-h-[170vh] relative font-sans overflow-x-clip text-white w-full flex flex-col md:items-center md:justify-center py-24 md:py-40 select-none">
      
      {/* Background Netflix Cinematic Title Watermark */}
      <div className="absolute top-10 left-0 w-full flex items-start justify-center pointer-events-none z-0">
        <h1 className="text-[14vw] sm:text-[17vw] md:text-[20vw] font-black text-white/[0.03] tracking-tighter leading-none whitespace-nowrap uppercase">
          ORIGINALS
        </h1>
      </div>

      {/* Ambient Crimson Glow behind folder */}
      <div className="hidden md:block absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[55vw] h-[55vw] bg-red-600/15 rounded-full blur-[100px] pointer-events-none z-0" />

      {/* Desktop Perspective Container (Hidden on Mobile) */}
      <div className="hidden md:flex mt-12 relative w-full max-w-7xl h-full items-center justify-center perspective-[2000px] z-10">
        
        {/* Origin Container */}
        <div className="relative w-0 h-0 transform-style-3d">
          
          {/* Folder Back */}
          <div 
            ref={folderBackRef}
            className="absolute w-[32vw] max-w-[380px] aspect-video bg-[#141414] rounded-[24px] border border-red-600/40 shadow-[0_20px_50px_rgba(229,9,20,0.25)] flex items-center justify-center"
            style={{ zIndex: 5 }}
          >
            <div className="absolute -top-6 left-6 w-32 h-8 bg-[#1f1f1f] rounded-t-xl border-t border-red-600/30" />
            <div className="relative z-10 text-red-600 font-mono font-black text-2xl tracking-widest uppercase opacity-60">
              ARCHIVE_SLOTS
            </div>
          </div>

          {/* Desktop Project Cards */}
          {projectsData.map((project, i) => (
            <div 
              key={i}
              ref={el => cardsRef.current[i] = el}
              className="absolute w-[33vw] max-w-[380px] aspect-[16/10] will-change-transform"
              style={{ zIndex: 10 + i }}
            >
              <div className="w-full h-full rounded-[24px] overflow-hidden border border-white/15 bg-[#141414]/95 backdrop-blur-2xl shadow-[0_25px_50px_rgba(0,0,0,0.9)] transition-all duration-500 group hover:scale-[1.04] hover:border-red-600 hover:shadow-[0_35px_80px_rgba(229,9,20,0.35)] hover:-translate-y-2 cursor-pointer relative z-10 p-7 flex flex-col justify-between">
                
                {/* Top Card Header */}
                <div className="flex items-center justify-between">
                  <span className="text-[10px] font-mono font-bold tracking-widest uppercase text-red-500 bg-red-600/10 px-2.5 py-1 rounded border border-red-600/20">
                    {project.episode}
                  </span>
                  <div className="flex items-center gap-2">
                    <span className="text-xs font-mono text-red-400 font-bold">{project.match} Match</span>
                    <span className="text-[10px] font-mono border border-white/30 px-1 text-white/70">HD</span>
                  </div>
                </div>

                {/* Middle Title & Description */}
                <div className="space-y-2 my-auto">
                  <div className="text-[11px] font-mono uppercase tracking-widest text-white/40">
                    {project.category}
                  </div>
                  <h3 className="text-2xl font-black text-white tracking-tight group-hover:text-red-500 transition-colors duration-300">
                    {project.title}
                  </h3>
                  <p className="text-xs text-white/70 font-light leading-relaxed line-clamp-2">
                    {project.description}
                  </p>
                </div>

                {/* Bottom Tech Tags */}
                <div className="flex flex-wrap gap-1.5 pt-3 border-t border-white/10">
                  {project.tags.map((tag, tIdx) => (
                    <span key={tIdx} className="text-[10px] font-mono text-white/70 bg-white/5 px-2 py-0.5 rounded group-hover:border-red-600/30 transition-colors">
                      {tag}
                    </span>
                  ))}
                </div>

                {/* Red Glowing Corner Accent */}
                <div className="absolute bottom-4 right-4 w-2 h-2 rounded-full bg-red-600 group-hover:shadow-[0_0_15px_#E50914] transition-all" />
              </div>
            </div>
          ))}

          {/* Folder Front Flap */}
          <div 
            ref={folderFrontRef}
            className="absolute w-[32vw] max-w-[380px] aspect-video pointer-events-none will-change-transform"
            style={{ zIndex: 60 }}
          >
            <div className="absolute bottom-0 w-full h-[85%] bg-[#1c1c1c] rounded-b-[24px] rounded-t-md shadow-[0_-5px_20px_rgba(0,0,0,0.8)] flex flex-col justify-end p-6 border-t border-red-600/40">
              <div className="w-20 h-1.5 bg-white/20 rounded-full mx-auto mb-2" />
            </div>
          </div>

        </div>
      </div>

      {/* MOBILE ONLY Layout: Standard Grid instead of GSAP animations for performance & stability */}
      <div className="md:hidden mt-20 relative w-full z-10 px-6 flex flex-col gap-6">
        <h2 className="text-3xl font-black mb-4">Original Series</h2>
        {projectsData.map((project, i) => (
          <div key={`mob-${i}`} className="w-full bg-[#141414] rounded-2xl border border-white/10 p-6 shadow-xl relative overflow-hidden">
             {/* Red Glowing Corner Accent */}
             <div className="absolute top-0 right-0 w-16 h-16 bg-red-600/20 rounded-bl-full blur-[20px]" />
             
             <div className="flex items-center justify-between mb-4 relative z-10">
                <span className="text-[10px] font-mono font-bold tracking-widest text-red-500 bg-red-600/10 px-2.5 py-1 rounded border border-red-600/20">
                  {project.episode}
                </span>
                <span className="text-[11px] font-mono text-[#46d369] font-bold">{project.match} Match</span>
             </div>
             
             <div className="space-y-1 relative z-10">
                <div className="text-[10px] font-mono uppercase tracking-widest text-white/50">{project.category}</div>
                <h3 className="text-xl font-black text-white">{project.title}</h3>
                <p className="text-sm text-white/70 font-light leading-relaxed mt-2">{project.description}</p>
             </div>
             
             <div className="flex flex-wrap gap-2 pt-4 mt-4 border-t border-white/10 relative z-10">
                {project.tags.map((tag, tIdx) => (
                  <span key={tIdx} className="text-[10px] font-mono text-white/60 bg-white/5 px-2 py-0.5 rounded border border-white/10">
                    {tag}
                  </span>
                ))}
             </div>
          </div>
        ))}
      </div>

    </section>
  );
};

export default Projects;