import streamlit as st
from sidebar import inject_plexus_bg

st.set_page_config(page_title="Skills", layout="wide", initial_sidebar_state="collapsed")
inject_plexus_bg()

st.markdown("""
<style>
/* Show sidebar toggle button */
button[kind="secondary"] { visibility: visible !important; }
:root {
  --primary: #38bdf8;
  --primary-dark: #0ea5e9;
  --primary-glow: rgba(56,189,248,0.35);
  --text-main: #f8fafc;
  --text-sub: #cbd5e1;
  --text-muted: #94a3b8;
  --glass: rgba(30, 41, 59, 0.6);
  --glass-hover: rgba(30, 41, 59, 0.85);
  --border: rgba(56,189,248,0.18);
  --border-hover: rgba(56,189,248,0.55);
  --shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
  --shadow-glow: 0 8px 32px rgba(56, 189, 248, 0.2);
  --transition: all 0.4s cubic-bezier(0.4,0,0.2,1);
  --transition-bounce: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
}

/* ===== Animations ===== */
@keyframes fadeUp {
  from {opacity:0; transform:translateY(40px);}
  to   {opacity:1; transform:translateY(0);}
}
@keyframes gradientShift {
  0%,100% {background-position:0% 50%;}
  50% {background-position:100% 50%;}
}
@keyframes shimmer {
  from {left:-100%;}
  to {left:150%;}
}
@keyframes pulseGlow {
  0%, 100% { box-shadow: 0 0 0 0 var(--primary-glow); }
  50%       { box-shadow: 0 0 0 12px transparent; }
}

/* ===== Title ===== */
.section-title {
  text-align: center;
  font-size: clamp(2rem,5vw,3rem);
  font-weight: 800;
  margin: 50px 0 40px;
  background: linear-gradient(135deg,#38bdf8,#818cf8,#38bdf8);
  background-size: 200% auto;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gradientShift 4s ease infinite;
  position: relative;
  display: inline-block;
  left: 50%;
  transform: translateX(-50%);
}
.section-title::after {
  content: '';
  position: absolute;
  bottom: -8px;
  left: 50%;
  transform: translateX(-50%);
  width: 60px;
  height: 3px;
  background: linear-gradient(90deg, var(--primary), transparent);
  border-radius: 2px;
}

/* ===== Grid ===== */
.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 25px;
  max-width: 1100px;
  margin: 0 auto 80px;
  padding: 0 10px;
}

/* ===== Card ===== */
.skill-card {
  background: var(--glass);
  padding: 28px 24px;
  border-radius: 20px;
  border: 1px solid var(--border);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  transition: var(--transition-bounce);
  position: relative;
  overflow: hidden;
  animation: fadeUp 0.7s cubic-bezier(0.4, 0, 0.2, 1) both;
  cursor: default;
}

/* Stagger delays - matches homepage pattern */
.skill-card:nth-child(1) { animation-delay: 0.0s; }
.skill-card:nth-child(2) { animation-delay: 0.1s; }
.skill-card:nth-child(3) { animation-delay: 0.2s; }
.skill-card:nth-child(4) { animation-delay: 0.3s; }
.skill-card:nth-child(5) { animation-delay: 0.4s; }
.skill-card:nth-child(6) { animation-delay: 0.5s; }

/* Top accent bar */
.skill-card::after {
  content:'';
  position:absolute;
  top:0; left:0; right:0;
  height:3px;
  background:linear-gradient(90deg,var(--primary),#818cf8);
  transform:scaleX(0);
  transform-origin:left;
  transition:transform .4s cubic-bezier(0.4, 0, 0.2, 1);
  border-radius: 20px 20px 0 0;
}
.skill-card:hover::after { transform:scaleX(1); }

/* Shimmer sweep */
.skill-card::before {
  content:'';
  position:absolute;
  top:0; left:-100%;
  width:60%;
  height:100%;
  background:linear-gradient(90deg,transparent,rgba(56,189,248,0.08),transparent);
  transition:left .7s ease;
  pointer-events: none;
}
.skill-card:hover::before { left:150%; }

.skill-card:hover {
  transform: translateY(-8px) scale(1.02);
  border-color: var(--border-hover);
  background: var(--glass-hover);
  box-shadow: var(--shadow-glow);
}

/* ===== Skill Name ===== */
.skill-name {
  color: var(--text-main);
  font-size: clamp(0.95rem, 2vw, 1.05rem);
  font-weight: 600;
  margin-bottom: 18px;
  display: flex;
  align-items: center;
  gap: 10px;
  letter-spacing: 0.01em;
}
.skill-name svg {
  width: 20px;
  height: 20px;
  color: var(--primary);
  flex-shrink: 0;
  transition: var(--transition);
}
.skill-card:hover .skill-name svg {
  transform: rotate(-10deg) scale(1.2);
}

/* ===== Progress Bar ===== */
.skill-bar-bg {
  background: rgba(30, 41, 59, 0.8);
  height: 10px;
  border-radius: 50px;
  overflow: hidden;
  border: 1px solid var(--border);
  position: relative;
}
.skill-bar {
  height: 100%;
  width: 0%;
  border-radius: 50px;
  background: linear-gradient(90deg,var(--primary-dark),var(--primary));
  transition: width 1.5s cubic-bezier(0.4,0,0.2,1);
  box-shadow: 0 0 10px var(--primary-glow);
  position: relative;
}
/* Subtle inner glow on progress */
.skill-bar::after {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
  opacity: 0.3;
}

/* ===== Percentage Label ===== */
.skill-percent {
  text-align: right;
  font-size: 0.8rem;
  color: var(--text-muted);
  margin-top: 8px;
  font-weight: 600;
  letter-spacing: 0.02em;
}

/* ===== Focus States (Keyboard Nav) ===== */
.skill-card:focus-visible {
  outline: 2px solid var(--primary);
  outline-offset: 3px;
}

/* ===== Responsive ===== */
@media (max-width: 768px) {
  .skills-grid { gap: 20px; padding: 0 16px; }
  .skill-card { padding: 22px 18px; }
  .section-title { font-size: 2.2rem; }
}

@media (max-width: 520px) {
  .skills-grid { grid-template-columns: 1fr; }
  .skill-card { padding: 20px 16px; }
  .skill-name { font-size: 1rem; gap: 8px; }
  .skill-bar-bg { height: 8px; }
  .skill-percent { font-size: 0.75rem; }
  .section-title { font-size: 1.8rem; margin: 30px 0 25px; }
}

/* Touch targets for coarse pointers */
@media (hover: none) and (pointer: coarse) {
  .skill-card { min-height: 120px; padding: 24px 20px; }
}

/* ===== Accessibility: Reduced Motion ===== */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
  .skill-bar { transition: none !important; }
}
</style>

<script>
document.addEventListener("DOMContentLoaded", function(){
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if(entry.isIntersecting){
        const bars = entry.target.querySelectorAll(".skill-bar");
        bars.forEach(bar => {
          if (prefersReduced) {
            // Instant set for accessibility
            bar.style.width = bar.dataset.width;
            bar.style.transition = 'none';
          } else {
            // Normal animated transition
            bar.style.width = bar.dataset.width;
          }
        });
        observer.unobserve(entry.target);
      }
    });
  }, {threshold: 0.25});

  document.querySelectorAll(".skill-card").forEach(card => {
    // Start with animation paused for scroll-trigger
    card.style.animationPlayState = 'paused';
    observer.observe(card);
  });

  // Resume animations when visible (matches homepage pattern)
  const io = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.animationPlayState = 'running';
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08 });
  
  document.querySelectorAll(".skill-card").forEach(el => io.observe(el));
});
</script>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# SECTION TITLE
# ─────────────────────────────────────────────────────────────
st.markdown('<h1 class="section-title">Technical Skills</h1>', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# SKILLS DATA
# ─────────────────────────────────────────────────────────────
skills = [
    {"name": "Python & Data Structures", "level": "90%", "aria": 90},
    {"name": "Web Development (HTML/CSS/JS)", "level": "85%", "aria": 85},
    {"name": "Streamlit & Flask Frameworks", "level": "80%", "aria": 80},
    {"name": "Database & SQL Management", "level": "75%", "aria": 75},
    {"name": "Git & Version Control", "level": "85%", "aria": 85},
    {"name": "UI/UX Design Principles", "level": "70%", "aria": 70}
]

# ─────────────────────────────────────────────────────────────
# SKILLS GRID
# ─────────────────────────────────────────────────────────────
st.markdown('<div class="skills-grid">', unsafe_allow_html=True)

for i, skill in enumerate(skills):
    st.markdown(f"""
    <div class="skill-card" tabindex="0">
        <div class="skill-name">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
                 stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                 aria-hidden="true">
                <polyline points="16 18 22 12 16 6"/>
                <polyline points="8 6 2 12 8 18"/>
            </svg>
            <span>{skill['name']}</span>
        </div>
        <div class="skill-bar-bg" 
             role="progressbar" 
             aria-valuenow="{skill['aria']}" 
             aria-valuemin="0" 
             aria-valuemax="100"
             aria-label="{skill['name']} proficiency: {skill['level']}">
            <div class="skill-bar" data-width="{skill['level']}"></div>
        </div>
        <div class="skill-percent">{skill['level']}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)