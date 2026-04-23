import streamlit as st
from sidebar import inject_plexus_bg

st.set_page_config(page_title="Skills", layout="wide", initial_sidebar_state="collapsed")
inject_plexus_bg()

st.markdown("""
<style>
/* ===== Base Variables ===== */
:root {
  --primary: #38bdf8;
  --primary-dark: #0ea5e9;
  --primary-glow: rgba(56,189,248,0.35);
  --indigo: #818cf8;
  --emerald: #34d399;
  --rose: #f472b6;
  --amber: #fbbf24;
  --text-main: #f8fafc;
  --text-sub: #cbd5e1;
  --text-muted: #94a3b8;
  --glass: rgba(30, 41, 59, 0.55);
  --glass-hover: rgba(30, 41, 59, 0.85);
  --border: rgba(56,189,248,0.18);
  --border-hover: rgba(56,189,248,0.55);
  --shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
  --shadow-glow: 0 8px 32px rgba(56, 189, 248, 0.18);
  --transition: all 0.3s cubic-bezier(0.4,0,0.2,1);
  --bounce: all 0.35s cubic-bezier(0.34, 1.56, 0.64, 1);
}

/* ===== Reset & Base ===== */
*,*::before,*::after{ box-sizing:border-box; margin:0; padding:0; }
html{ scroll-behavior:smooth; }
body{ -webkit-font-smoothing:antialiased; overflow-x:hidden; }

/* ===== Animations ===== */
@keyframes fadeUp { from{opacity:0; transform:translateY(24px);} to{opacity:1; transform:translateY(0);} }
@keyframes gradientShift { 0%,100%{background-position:0% 50%;} 50%{background-position:100% 50%;} }
@keyframes shimmer { from{left:-100%;} to{left:150%;} }
@keyframes pulseGlow { 0%,100%{box-shadow:0 0 0 0 var(--primary-glow);} 50%{box-shadow:0 0 0 10px transparent;} }
@keyframes float { 0%,100%{transform:translateY(0);} 50%{transform:translateY(-4px);} }
@keyframes countPop { 0%{transform:scale(0.8); opacity:0;} 60%{transform:scale(1.1);} 100%{transform:scale(1); opacity:1;} }
@keyframes iconSpin { to{transform:rotate(360deg);} }
@keyframes ripple { to{transform:scale(4); opacity:0;} }

/* ===== Compact Title ===== */
.section-title{
  text-align:center;
  font-size:clamp(1.4rem,4vw,2rem);
  font-weight:800;
  margin:28px 0 20px;
  background:linear-gradient(135deg,var(--primary),var(--indigo),var(--primary));
  background-size:200% auto;
  -webkit-background-clip:text;
  -webkit-text-fill-color:transparent;
  animation:gradientShift 4s ease infinite;
  position:relative;
  display:inline-block;
  left:50%;
  transform:translateX(-50%);
}
.section-title::after{
  content:'';
  position:absolute;
  bottom:-6px; left:50%;
  transform:translateX(-50%);
  width:48px; height:2px;
  background:linear-gradient(90deg,var(--primary),transparent);
  border-radius:2px;
}

/* ===== Compact Grid ===== */
.skills-grid{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
  gap:14px;
  max-width:1000px;
  margin:0 auto 40px;
  padding:0 12px;
}

/* ===== Compact Card ===== */
.skill-card{
  background:var(--glass);
  padding:16px 14px;
  border-radius:14px;
  border:1px solid var(--border);
  backdrop-filter:blur(12px);
  -webkit-backdrop-filter:blur(12px);
  transition:var(--bounce);
  position:relative;
  overflow:hidden;
  animation:fadeUp 0.5s cubic-bezier(0.4,0,0.2,1) both;
  cursor:pointer;
  user-select:none;
}
.skill-card:nth-child(1){animation-delay:0s} .skill-card:nth-child(2){animation-delay:0.06s}
.skill-card:nth-child(3){animation-delay:0.12s} .skill-card:nth-child(4){animation-delay:0.18s}
.skill-card:nth-child(5){animation-delay:0.24s} .skill-card:nth-child(6){animation-delay:0.3s}

/* Category color accents */
.skill-card[data-cat="code"]::after{background:linear-gradient(90deg,var(--primary),var(--indigo))}
.skill-card[data-cat="database"]::after{background:linear-gradient(90deg,var(--emerald),#10b981)}
.skill-card[data-cat="design"]::after{background:linear-gradient(90deg,var(--rose),#ec4899)}
.skill-card[data-cat="tools"]::after{background:linear-gradient(90deg,var(--amber),#f59e0b)}

.skill-card::after{
  content:''; position:absolute; top:0; left:0; right:0; height:2px;
  transform:scaleX(0); transform-origin:left;
  transition:transform 0.3s ease; border-radius:14px 14px 0 0;
}
.skill-card:hover::after{transform:scaleX(1)}

/* Shimmer */
.skill-card::before{
  content:''; position:absolute; top:0; left:-100%;
  width:50%; height:100%;
  background:linear-gradient(90deg,transparent,rgba(56,189,248,0.06),transparent);
  transition:left 0.6s ease; pointer-events:none;
}
.skill-card:hover::before{left:150%}

.skill-card:hover{
  transform:translateY(-4px) scale(1.015);
  border-color:var(--border-hover);
  background:var(--glass-hover);
  box-shadow:var(--shadow-glow);
  z-index:2;
}
.skill-card:active{transform:translateY(-1px) scale(1.005)}

/* ===== Skill Header ===== */
.skill-header{
  display:flex; align-items:center; gap:9px;
  margin-bottom:10px; padding-bottom:8px;
  border-bottom:1px dashed rgba(56,189,248,0.12);
}
.skill-icon{
  width:26px; height:26px; border-radius:8px;
  background:rgba(56,189,248,0.12);
  border:1px solid rgba(56,189,248,0.22);
  display:flex; align-items:center; justify-content:center;
  color:var(--primary); flex-shrink:0;
  transition:var(--bounce);
}
.skill-card:hover .skill-icon{
  transform:rotate(-8deg) scale(1.15);
  background:rgba(56,189,248,0.22);
}
.skill-icon svg{width:14px; height:14px}

.skill-name{
  color:var(--text-main);
  font-size:0.82rem;
  font-weight:600;
  line-height:1.3;
  letter-spacing:0.01em;
}

/* ===== Progress Section ===== */
.skill-progress{
  display:flex; align-items:center; gap:8px;
  margin-bottom:6px;
}
.skill-bar-bg{
  flex:1; height:6px; border-radius:50px;
  background:rgba(30,41,59,0.75);
  border:1px solid var(--border);
  overflow:hidden; position:relative;
}
.skill-bar{
  height:100%; width:0%;
  border-radius:50px;
  background:linear-gradient(90deg,var(--primary-dark),var(--primary));
  transition:width 1.2s cubic-bezier(0.4,0,0.2,1);
  position:relative;
}
.skill-bar::after{
  content:''; position:absolute; top:0; left:0; right:0; bottom:0;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,0.25),transparent);
  opacity:0.4;
}

/* ===== Percentage Badge ===== */
.skill-badge{
  min-width:38px; height:20px;
  display:flex; align-items:center; justify-content:center;
  background:rgba(56,189,248,0.15);
  border:1px solid rgba(56,189,248,0.3);
  border-radius:6px;
  font-size:0.7rem; font-weight:700;
  color:var(--primary);
  transition:var(--bounce);
}
.skill-card:hover .skill-badge{
  transform:scale(1.08);
  background:rgba(56,189,248,0.25);
  box-shadow:0 0 12px rgba(56,189,248,0.25);
}

/* ===== Level Label ===== */
.skill-level{
  font-size:0.68rem; color:var(--text-muted);
  text-align:right; font-weight:500;
  opacity:0.9;
}

/* ===== Interactive Tooltip ===== */
.skill-card::after, .skill-tooltip{
  pointer-events:none;
}
.skill-tooltip{
  position:absolute; top:-8px; right:-8px;
  width:22px; height:22px;
  border-radius:50%;
  background:rgba(56,189,248,0.2);
  border:1px solid var(--border);
  display:flex; align-items:center; justify-content:center;
  color:var(--primary); font-size:0.7rem; font-weight:700;
  opacity:0; transform:scale(0.8);
  transition:var(--transition);
  z-index:3;
}
.skill-card:hover .skill-tooltip{
  opacity:1; transform:scale(1);
  animation:pulseGlow 2s ease infinite;
}

/* ===== Ripple Effect ===== */
.ripple{
  position:absolute; border-radius:50%;
  background:rgba(56,189,248,0.3);
  transform:scale(0); animation:ripple 0.5s ease-out;
  pointer-events:none;
}

/* ===== Category Tags ===== */
.skill-cat{
  display:inline-flex; align-items:center; gap:4px;
  padding:3px 8px; border-radius:4px;
  font-size:0.65rem; font-weight:600;
  background:rgba(56,189,248,0.08);
  color:var(--primary); margin-top:6px;
}
.skill-cat svg{width:10px; height:10px}

/* ===== Focus States ===== */
.skill-card:focus-visible{
  outline:2px solid var(--primary);
  outline-offset:2px;
}

/* ===== Responsive ===== */
@media (max-width:768px){
  .skills-grid{grid-template-columns:repeat(2,1fr); gap:12px; padding:0 8px}
  .skill-card{padding:14px 12px}
  .skill-name{font-size:0.78rem}
  .section-title{font-size:1.5rem; margin:22px 0 16px}
}

@media (max-width:520px){
  .skills-grid{grid-template-columns:1fr; gap:10px}
  .skill-card{padding:12px 10px}
  .skill-header{gap:7px; padding-bottom:6px}
  .skill-icon{width:24px; height:24px}
  .skill-icon svg{width:12px; height:12px}
  .skill-name{font-size:0.76rem}
  .skill-bar-bg{height:5px}
  .skill-badge{min-width:34px; height:18px; font-size:0.68rem}
  .skill-level{font-size:0.65rem}
  .skill-cat{font-size:0.62rem; padding:2px 6px}
  .section-title{font-size:1.3rem}
}

/* ===== Touch Optimization ===== */
@media (hover:none) and (pointer:coarse){
  .skill-card{min-height:90px; padding:14px 12px}
  .skill-card:hover{transform:none}
  .skill-tooltip{display:none}
}

/* ===== Reduced Motion ===== */
@media (prefers-reduced-motion:reduce){
  *,*::before,*::after{
    animation-duration:0.01ms !important;
    animation-iteration-count:1 !important;
    transition-duration:0.01ms !important;
  }
  .skill-bar{transition:none !important}
  .skill-card:hover{transform:none !important}
}
</style>

<script>
document.addEventListener("DOMContentLoaded", function(){
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  
  // Intersection Observer for scroll-triggered animations
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if(entry.isIntersecting){
        const bar = entry.target.querySelector(".skill-bar");
        const badge = entry.target.querySelector(".skill-badge");
        const width = bar.dataset.width;
        
        if(prefersReduced){
          bar.style.width = width;
          badge.textContent = width;
        } else {
          // Animate counter
          const target = parseInt(width);
          let current = 0;
          const duration = 1200;
          const step = Math.ceil(target / (duration/16));
          
          const counter = setInterval(() => {
            current += step;
            if(current >= target){
              current = target;
              clearInterval(counter);
            }
            bar.style.width = current + "%";
            badge.textContent = current + "%";
          }, 16);
        }
        observer.unobserve(entry.target);
      }
    });
  }, {threshold: 0.3});

  // Ripple effect on click/tap
  document.querySelectorAll(".skill-card").forEach(card => {
    observer.observe(card);
    
    card.addEventListener("click", function(e){
      if(prefersReduced) return;
      
      const rect = card.getBoundingClientRect();
      const ripple = document.createElement("span");
      ripple.className = "ripple";
      
      const size = Math.max(rect.width, rect.height);
      const x = e.clientX - rect.left - size/2;
      const y = e.clientY - rect.top - size/2;
      
      ripple.style.width = ripple.style.height = size + "px";
      ripple.style.left = x + "px";
      ripple.style.top = y + "px";
      
      card.appendChild(ripple);
      setTimeout(() => ripple.remove(), 500);
      
      // Subtle haptic feedback simulation (visual)
      card.style.transform = "translateY(-1px) scale(1.005)";
      setTimeout(() => {
        card.style.transform = "";
      }, 100);
    });
  });

  // Resume entrance animations on scroll
  const io = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if(entry.isIntersecting){
        entry.target.style.animationPlayState = "running";
        io.unobserve(entry.target);
      }
    });
  }, {threshold: 0.1});
  
  document.querySelectorAll(".skill-card").forEach(el => {
    el.style.animationPlayState = "paused";
    io.observe(el);
  });
});
</script>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# SECTION TITLE
# ─────────────────────────────────────────────────────────────
st.markdown('<h1 class="section-title">Technical Skills</h1>', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# SVG ICON HELPER
# ─────────────────────────────────────────────────────────────
def svg_icon(name: str, size: int = 14) -> str:
    icons = {
        "code": '<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>',
        "database": '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/>',
        "layout": '<rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/>',
        "git": '<circle cx="18" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M18 9a9 9 0 0 1-9 9"/><line x1="6" y1="3" x2="6" y2="15"/>',
        "palette": '<circle cx="13.5" cy="6.5" r="2.5"/><circle cx="17.5" cy="10.5" r="2.5"/><circle cx="8.5" cy="7.5" r="2.5"/><circle cx="6.5" cy="12.5" r="2.5"/><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10c.926 0 1.648-.746 1.648-1.688 0-.437-.18-.835-.437-1.125-.29-.289-.438-.652-.438-1.125a1.64 1.64 0 0 1 1.668-1.668h1.996c3.051 0 5.555-2.503 5.555-5.555C21.965 6.012 17.461 2 12 2z"/>',
        "zap": '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>',
        "terminal": '<polyline points="4 17 10 11 4 5"/><line x1="12" y1="19" x2="20" y2="19"/>',
        "cloud": '<path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"/>',
        "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
        "cpu": '<rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><line x1="9" y1="1" x2="9" y2="4"/><line x1="15" y1="1" x2="15" y2="4"/><line x1="9" y1="20" x2="9" y2="23"/><line x1="15" y1="20" x2="15" y2="23"/><line x1="20" y1="9" x2="23" y2="9"/><line x1="20" y1="14" x2="23" y2="14"/><line x1="1" y1="9" x2="4" y2="9"/><line x1="1" y1="14" x2="4" y2="14"/>',
    }
    path = icons.get(name, icons["code"])
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{path}</svg>'

# ─────────────────────────────────────────────────────────────
# SKILLS DATA (Compact & Categorized)
# ─────────────────────────────────────────────────────────────
skills = [
    {"name": "Python & Algorithms", "level": 90, "cat": "code", "icon": "code", "label": "Advanced"},
    {"name": "HTML/CSS/JavaScript", "level": 85, "cat": "code", "icon": "layout", "label": "Proficient"},
    {"name": "Streamlit & Flask", "level": 80, "cat": "code", "icon": "terminal", "label": "Proficient"},
    {"name": "SQL & PostgreSQL", "level": 75, "cat": "database", "icon": "database", "label": "Intermediate"},
    {"name": "Git & GitHub", "level": 85, "cat": "tools", "icon": "git", "label": "Proficient"},
    {"name": "UI/UX Principles", "level": 70, "cat": "design", "icon": "palette", "label": "Growing"},
]

# ─────────────────────────────────────────────────────────────
# SKILLS GRID (Compact Cards)
# ─────────────────────────────────────────────────────────────
st.markdown('<div class="skills-grid">', unsafe_allow_html=True)

for skill in skills:
    st.markdown(f"""
    <div class="skill-card" tabindex="0" data-cat="{skill['cat']}">
        <div class="skill-tooltip">★</div>
        <div class="skill-header">
            <div class="skill-icon">{svg_icon(skill['icon'], 14)}</div>
            <span class="skill-name">{skill['name']}</span>
        </div>
        <div class="skill-progress">
            <div class="skill-bar-bg" role="progressbar" 
                 aria-valuenow="{skill['level']}" aria-valuemin="0" aria-valuemax="100">
                <div class="skill-bar" data-width="{skill['level']}%"></div>
            </div>
            <div class="skill-badge">{skill['level']}%</div>
        </div>
        <div class="skill-level">{skill['label']}</div>
        <div class="skill-cat">{svg_icon(skill['icon'], 10)} {skill['cat'].title()}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# LEGEND / FOOTER
# ─────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; padding:12px 0 24px; color:var(--text-muted); font-size:0.72rem;">
  <span style="display:inline-flex; align-items:center; gap:6px; margin:0 8px;">
    <span style="width:8px; height:8px; border-radius:50%; background:var(--primary); box-shadow:0 0 6px var(--primary-glow)"></span>
    Proficient (75%+)
  </span>
  <span style="display:inline-flex; align-items:center; gap:6px; margin:0 8px;">
    <span style="width:8px; height:8px; border-radius:50%; background:var(--emerald); opacity:0.8"></span>
    Growing (60-74%)
  </span>
  <span style="display:inline-flex; align-items:center; gap:6px; margin:0 8px;">
    <span style="width:8px; height:8px; border-radius:50%; background:var(--amber); opacity:0.8"></span>
    Learning (&lt;60%)
  </span>
</div>
""", unsafe_allow_html=True)