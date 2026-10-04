import { useEffect, useRef } from 'react';
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

  useEffect(() => {
    let ctx = gsap.context(() => {
      // Header Entrance Animation
      gsap.from(".cert-header", {
        y: 40,
        opacity: 0,
        duration: 1,
        ease: "power3.out",
        scrollTrigger: {
          trigger: containerRef.current,
          start: "top 80%",
        }
      });
      
      // BURST EFFECT for the certificates
      gsap.fromTo(".burst-container", 
        { 
          scale: 0.2, 
          opacity: 0, 
          rotationZ: 4,
          filter: "blur(10px)"
        },
        {
          scale: 1,
          opacity: 1,
          rotationZ: 0,
          filter: "blur(0px)",
          duration: 1.5,
          ease: "elastic.out(1, 0.6)",
          scrollTrigger: {
            trigger: ".burst-container",
            start: "top 85%",
          }
        }
      );
    }, containerRef);
    
    return () => ctx.revert();
  }, []);

  // Duplicate the array to create a seamless infinite loop
  const duplicatedData = [...certData, ...certData];

  return (
    <section ref={containerRef} className="bg-[#050505] py-24 overflow-hidden select-none relative">
      
      <div className="cert-header mb-14 flex flex-col space-y-3 px-6 md:px-12 items-center text-center md:items-start md:text-left">
        <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded bg-red-600/10 border border-red-600/30 text-[10px] font-mono uppercase tracking-widest text-red-500 w-max shadow-[0_0_15px_rgba(229,9,20,0.15)]">
          <span className="w-1.5 h-1.5 rounded-full bg-red-600 animate-pulse"></span>
          OFFICIAL CREDENTIALS
        </div>
        <h2 className="text-4xl md:text-5xl font-black text-white tracking-tight">
          Acclaimed Certifications
        </h2>
        <p className="text-white/60 text-sm md:text-base font-light max-w-lg">
          A continuous commitment to mastering cutting-edge technology, cloud infrastructure, and AI engineering practices.
        </p>
      </div>

      {/* Marquee Wrapper with Burst Animation target */}
      <div className="burst-container w-full relative pt-4 pb-12">
        
        {/* CSS Animation for Infinite Marquee Scroll */}
        <style>{`
          @keyframes marquee {
            0% { transform: translateX(0%); }
            100% { transform: translateX(-50%); }
          }
          .animate-marquee {
            display: flex;
            width: max-content;
            animation: marquee 45s linear infinite;
          }
          .animate-marquee:hover {
            animation-play-state: paused;
          }
        `}</style>
        
        {/* Cinematic Ambient Glow behind the track */}
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-3/4 h-[250px] bg-red-600/10 blur-[100px] pointer-events-none rounded-full" />

        {/* The Auto-Scrolling Track */}
        <div className="animate-marquee gap-6 px-3">
          {duplicatedData.map((cert, i) => (
            <div 
              key={i} 
              className="shrink-0 w-[280px] md:w-[350px] h-[180px] md:h-[200px] bg-[#101010] border border-white/10 rounded-2xl p-6 flex flex-col justify-between group hover:border-red-600/60 hover:bg-[#151515] hover:-translate-y-2 hover:shadow-[0_15px_40px_rgba(229,9,20,0.2)] transition-all duration-300 cursor-pointer relative overflow-hidden"
            >
              {/* Internal Glossy Gradient */}
              <div className="absolute inset-0 bg-gradient-to-br from-red-600/0 via-transparent to-red-600/10 opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none" />
              
              <div className="flex justify-between items-start relative z-10">
                <span className="text-[10px] font-bold tracking-widest uppercase text-red-500 bg-red-600/10 px-2.5 py-1 rounded">
                  {cert.issuer}
                </span>
                <span className="text-[11px] font-mono font-bold text-[#46d369]">
                  {cert.match}
                </span>
              </div>
              
              <div className="space-y-1 relative z-10 my-auto pt-4 pb-2">
                <h3 className="text-lg md:text-xl font-black text-white leading-snug group-hover:text-red-500 transition-colors">
                  {cert.title}
                </h3>
              </div>
              
              <div className="flex flex-wrap items-center gap-2 pt-3 border-t border-white/10 relative z-10">
                <span className="text-[10px] font-mono uppercase tracking-widest text-white/70 bg-white/5 border border-white/10 px-2.5 py-1 rounded">
                  {cert.tag}
                </span>
                <span className="text-[10px] font-mono text-white/40 border border-white/5 px-2.5 py-1 rounded">
                  VERIFIED
                </span>
              </div>
            </div>
          ))}
        </div>
        
        {/* Edge Fade Overlays to make it look cinematic */}
        <div className="absolute top-0 left-0 w-16 md:w-32 h-full bg-gradient-to-r from-[#050505] to-transparent pointer-events-none z-20" />
        <div className="absolute top-0 right-0 w-16 md:w-32 h-full bg-gradient-to-l from-[#050505] to-transparent pointer-events-none z-20" />
      </div>
      
    </section>
  );
};

export default Certifications;
