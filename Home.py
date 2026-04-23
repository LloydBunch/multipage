import streamlit as st
from sidebar import get_base64_image, inject_plexus_bg

st.set_page_config(page_title="Lloyd George Bibano", layout="wide", initial_sidebar_state="collapsed")
inject_plexus_bg()

st.markdown("""
<style>
/* Show sidebar toggle button */
button[kind="secondary"] { visibility: visible !important; }
/* ===== DESIGN TOKENS ===== */
:root {
  --primary: #38bdf8;
  --primary-dark: #0ea5e9;
  --primary-glow: rgba(56, 189, 248, 0.4);
  --text-main: #f8fafc;
  --text-sub: #cbd5e1;
  --text-muted: #94a3b8;
  --glass: rgba(15, 23, 42, 0.45);
  --glass-hover: rgba(15, 23, 42, 0.65);
  --border: rgba(56, 189, 248, 0.15);
  --border-hover: rgba(56, 189, 248, 0.45);
  --shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
  --shadow-glow: 0 8px 32px rgba(56, 189, 248, 0.2);
  --transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
  --transition-bounce: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
}

/* ===== RESET & BASE ===== */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow-x: hidden;
}

/* ===== KEYFRAME ANIMATIONS ===== */
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(32px); }
  to   { opacity: 1; transform: translateY(0); }
}
@keyframes fadeInLeft {
  from { opacity: 0; transform: translateX(-32px); }
  to   { opacity: 1; transform: translateX(0); }
}
@keyframes fadeInRight {
  from { opacity: 0; transform: translateX(32px); }
  to   { opacity: 1; transform: translateX(0); }
}
@keyframes fadeInScale {
  from { opacity: 0; transform: scale(0.88); }
  to   { opacity: 1; transform: scale(1); }
}
@keyframes shimmer {
  0%   { background-position: -200% center; }
  100% { background-position:  200% center; }
}
@keyframes pulseGlow {
  0%, 100% { box-shadow: 0 0 0 0 var(--primary-glow); }
  50%       { box-shadow: 0 0 0 12px transparent; }
}
@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50%       { transform: translateY(-8px); }
}
@keyframes rotateBorder {
  0%   { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
@keyframes blink {
  0%, 100% { border-color: var(--primary); }
  50%       { border-color: transparent; }
}
@keyframes countUp {
  from { opacity: 0; transform: translateY(16px) scale(0.8); }
  to   { opacity: 1; transform: translateY(0) scale(1); }
}
@keyframes slideInTag {
  from { opacity: 0; transform: translateX(-16px) scale(0.9); }
  to   { opacity: 1; transform: translateX(0) scale(1); }
}
@keyframes gradientShift {
  0%   { background-position: 0% 50%; }
  50%  { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
@keyframes underlineGrow {
  from { width: 0; }
  to   { width: 100%; }
}

/* ===== HERO WRAPPER ===== */
.hero-wrapper {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 60px;
  padding: 80px 0 40px;
  flex-wrap: wrap;
}

/* ===== HERO CONTENT ===== */
.hero-content {
  flex: 1;
  min-width: 280px;
  animation: fadeInLeft 0.8s cubic-bezier(0.4, 0, 0.2, 1) forwards;
}

.hero-content h1 {
  font-size: clamp(2rem, 5vw, 3.5rem);
  color: var(--text-main);
  margin: 0 0 10px;
  font-weight: 800;
  line-height: 1.1;
  letter-spacing: -0.02em;
}
.hero-content h1 .name-highlight {
  background: linear-gradient(135deg, var(--primary), #818cf8, var(--primary));
  background-size: 200% auto;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: gradientShift 4s ease infinite;
  display: inline-block;
}

.hero-content h2 {
  font-size: clamp(1.05rem, 2.5vw, 1.4rem);
  color: var(--text-sub);
  margin: 0 0 20px;
  font-weight: 500;
  position: relative;
  display: inline-block;
}
.hero-content h2::after {
  content: '';
  position: absolute;
  bottom: -4px; left: 0;
  height: 2px;
  background: linear-gradient(90deg, var(--primary), transparent);
  animation: underlineGrow 1.2s 0.8s cubic-bezier(0.4, 0, 0.2, 1) forwards;
  width: 0;
}

.hero-content p {
  font-size: clamp(0.95rem, 2vw, 1.08rem);
  color: var(--text-muted);
  line-height: 1.8;
  max-width: 600px;
  margin-bottom: 32px;
  animation: fadeInUp 0.8s 0.3s cubic-bezier(0.4, 0, 0.2, 1) both;
}

/* ===== TYPING CURSOR ===== */
.typing-container {
  display: inline;
}
.typing-text {
  display: inline;
  overflow: hidden;
  border-right: 3px solid var(--primary);
  white-space: nowrap;
  animation:
    typing-reveal 2.5s steps(5, end) 0.5s both,
    blink 0.8s step-end infinite;
  max-width: 0;
}
@keyframes typing-reveal {
  from { max-width: 0; }
  to   { max-width: 200px; }
}

/* ===== CTA BUTTONS ===== */
.cta-group {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
  margin-bottom: 36px;
  animation: fadeInUp 0.8s 0.5s cubic-bezier(0.4, 0, 0.2, 1) both;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  padding: 14px 30px;
  border-radius: 14px;
  font-weight: 700;
  font-size: 0.97rem;
  text-decoration: none;
  transition: var(--transition-bounce);
  cursor: pointer;
  border: none;
  min-height: 52px;
  position: relative;
  overflow: hidden;
  letter-spacing: 0.01em;
}

/* Ripple pseudo-element */
.btn::before {
  content: '';
  position: absolute;
  inset: 0;
  background: rgba(255,255,255,0.12);
  opacity: 0;
  border-radius: inherit;
  transition: opacity 0.3s;
}
.btn:hover::before { opacity: 1; }
.btn:active { transform: scale(0.97) !important; }

.btn-primary {
  background: linear-gradient(135deg, var(--primary-dark), var(--primary), #818cf8);
  background-size: 200% auto;
  color: white;
  box-shadow: 0 4px 18px rgba(56,189,248,0.35);
  animation: gradientShift 4s ease infinite;
}
.btn-primary:hover {
  transform: translateY(-3px) scale(1.03);
  box-shadow: 0 10px 30px rgba(56,189,248,0.5);
}

.btn-secondary {
  background: transparent;
  color: var(--text-sub);
  border: 1.5px solid var(--border);
  backdrop-filter: blur(8px);
}
.btn-secondary:hover {
  border-color: var(--primary);
  color: var(--primary);
  background: rgba(56,189,248,0.1);
  transform: translateY(-3px) scale(1.03);
  box-shadow: 0 6px 20px rgba(56,189,248,0.2);
}

/* ===== HERO IMAGE ===== */
.hero-image-wrapper {
  flex: 0 0 380px;
  position: relative;
  animation: fadeInRight 0.9s 0.2s cubic-bezier(0.4, 0, 0.2, 1) both;
}

/* Spinning border ring */
.hero-image-wrapper::before {
  content: '';
  position: absolute;
  inset: -6px;
  border-radius: 30px;
  background: conic-gradient(
    from 0deg,
    transparent 0deg,
    var(--primary) 60deg,
    transparent 120deg,
    #818cf8 180deg,
    transparent 240deg,
    var(--primary) 300deg,
    transparent 360deg
  );
  animation: rotateBorder 6s linear infinite;
  z-index: 0;
  opacity: 0.6;
}
.hero-image-wrapper::after {
  content: '';
  position: absolute;
  inset: -3px;
  border-radius: 27px;
  background: rgba(8, 14, 30, 1);
  z-index: 1;
}

.hero-img {
  width: 100%;
  border-radius: 24px;
  object-fit: cover;
  display: block;
  position: relative;
  z-index: 2;
  transition: var(--transition);
  animation: float 5s ease-in-out 1.5s infinite;
  box-shadow: 0 20px 60px rgba(0,0,0,0.5);
}
.hero-img:hover {
  animation-play-state: paused;
  transform: scale(1.04) rotate(1deg);
  box-shadow: 0 24px 70px rgba(56,189,248,0.3);
}

/* Fallback placeholder */
.hero-placeholder {
  width: 100%;
  height: 380px;
  background: var(--glass);
  border-radius: 24px;
  border: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-muted);
  font-size: 0.95rem;
  position: relative;
  z-index: 2;
}

/* ===== DIVIDER ===== */
.section-divider {
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--border), transparent);
  margin: 50px 0 32px;
  position: relative;
  overflow: visible;
}
.section-divider::after {
  content: '◆';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: var(--primary);
  font-size: 0.6rem;
  background: rgba(8,14,30,0.9);
  padding: 0 8px;
}

/* ===== SUBTITLE LABEL ===== */
.subtitle {
  font-size: 0.82rem;
  color: var(--primary);
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 2.5px;
  margin: 0 0 24px;
  display: inline-flex;
  align-items: center;
  gap: 10px;
}
.subtitle::before,
.subtitle::after {
  content: '';
  display: inline-block;
  width: 28px;
  height: 1.5px;
  background: var(--primary);
  opacity: 0.6;
}

/* ===== STAT CARDS ===== */
.stats-row {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
  margin: 8px 0 44px;
}

.stat-card {
  background: var(--glass);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 28px 20px 22px;
  text-align: center;
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  transition: var(--transition-bounce);
  cursor: default;
  position: relative;
  overflow: hidden;
  animation: fadeInUp 0.7s cubic-bezier(0.4, 0, 0.2, 1) both;
}

/* Shimmer sweep on hover */
.stat-card::before {
  content: '';
  position: absolute;
  top: 0; left: -100%;
  width: 60%;
  height: 100%;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(56,189,248,0.08),
    transparent
  );
  transition: left 0.6s ease;
}
.stat-card:hover::before { left: 150%; }

/* Top accent bar */
.stat-card::after {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--primary), #818cf8);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  border-radius: 20px 20px 0 0;
}
.stat-card:hover::after { transform: scaleX(1); }

.stat-card:hover {
  transform: translateY(-6px) scale(1.02);
  border-color: var(--border-hover);
  background: var(--glass-hover);
  box-shadow: var(--shadow-glow);
}

/* Stagger delays for stat cards */
.stat-card:nth-child(1) { animation-delay: 0.0s; }
.stat-card:nth-child(2) { animation-delay: 0.1s; }
.stat-card:nth-child(3) { animation-delay: 0.2s; }
.stat-card:nth-child(4) { animation-delay: 0.3s; }

.stat-icon-wrap {
  width: 48px;
  height: 48px;
  border-radius: 14px;
  background: rgba(56,189,248,0.12);
  border: 1px solid rgba(56,189,248,0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 14px;
  transition: var(--transition);
}
.stat-card:hover .stat-icon-wrap {
  background: rgba(56,189,248,0.22);
  transform: scale(1.1) rotate(-5deg);
  border-color: var(--primary);
}
.stat-icon {
  width: 22px;
  height: 22px;
  color: var(--primary);
}

.stat-number {
  font-size: clamp(1.6rem, 4vw, 2rem);
  font-weight: 800;
  color: var(--text-main);
  margin: 0 0 6px;
  line-height: 1;
  letter-spacing: -0.02em;
  animation: countUp 0.6s cubic-bezier(0.4, 0, 0.2, 1) both;
}
.stat-label {
  font-size: 0.82rem;
  color: var(--text-muted);
  font-weight: 500;
  letter-spacing: 0.02em;
}

/* ===== TECH TAGS ===== */
.tech-row {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 20px;
}

.tech-tag {
  display: inline-flex;
  align-items: center;
  gap: 9px;
  background: rgba(15, 23, 42, 0.55);
  border: 1px solid var(--border);
  padding: 10px 20px;
  border-radius: 50px;
  font-size: 0.9rem;
  color: var(--text-sub);
  transition: var(--transition-bounce);
  cursor: default;
  white-space: nowrap;
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  position: relative;
  overflow: hidden;
  animation: slideInTag 0.5s cubic-bezier(0.4, 0, 0.2, 1) both;
}

/* Stagger delays for tech tags */
.tech-tag:nth-child(1) { animation-delay: 0.0s; }
.tech-tag:nth-child(2) { animation-delay: 0.08s; }
.tech-tag:nth-child(3) { animation-delay: 0.16s; }
.tech-tag:nth-child(4) { animation-delay: 0.24s; }
.tech-tag:nth-child(5) { animation-delay: 0.32s; }
.tech-tag:nth-child(6) { animation-delay: 0.40s; }

.tech-tag::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, rgba(56,189,248,0.12), rgba(129,140,248,0.12));
  opacity: 0;
  transition: opacity 0.35s;
}
.tech-tag:hover::before { opacity: 1; }

.tech-tag:hover {
  border-color: var(--primary);
  color: var(--primary);
  transform: translateY(-4px) scale(1.06);
  box-shadow: 0 8px 24px rgba(56,189,248,0.2);
}
.tech-tag svg {
  width: 15px;
  height: 15px;
  flex-shrink: 0;
  transition: var(--transition);
}
.tech-tag:hover svg { transform: rotate(15deg) scale(1.2); }

/* Dot indicator */
.tech-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--primary);
  flex-shrink: 0;
  box-shadow: 0 0 6px var(--primary);
  animation: pulseGlow 2s ease infinite;
}

/* ===== STATUS BADGE ===== */
.status-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(34, 197, 94, 0.1);
  border: 1px solid rgba(34, 197, 94, 0.25);
  padding: 7px 16px;
  border-radius: 50px;
  font-size: 0.82rem;
  color: #86efac;
  font-weight: 600;
  margin-bottom: 18px;
  animation: fadeInUp 0.6s 0.1s both;
  width: fit-content;
}
.status-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #22c55e;
  animation: pulseGlow 2s ease infinite;
  box-shadow: 0 0 8px #22c55e;
}

/* ===== SCROLL INDICATOR ===== */
.scroll-hint {
  display: flex;
  align-items: center;
  gap: 8px;
  color: var(--text-muted);
  font-size: 0.8rem;
  margin-top: 8px;
  animation: fadeInUp 0.8s 1.2s both;
}
.scroll-arrow {
  width: 18px;
  height: 18px;
  animation: float 1.5s ease-in-out infinite;
}

/* ===== MOBILE RESPONSIVENESS ===== */
@media (max-width: 1024px) {
  .hero-image-wrapper { flex: 0 0 320px; }
  .stats-row { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 768px) {
  .hero-wrapper {
    flex-direction: column-reverse;
    text-align: center;
    gap: 36px;
    padding: 32px 0 16px;
  }
  .hero-content { min-width: unset; width: 100%; }
  .hero-content p { margin: 0 auto 28px; }
  .hero-content h2::after { left: 50%; transform: translateX(-50%); }
  .cta-group { justify-content: center; }
  .hero-image-wrapper {
    flex: 0 0 auto;
    width: min(280px, 80vw);
    margin: 0 auto;
  }
  .hero-image-wrapper::before { display: none; }
  .hero-image-wrapper::after  { display: none; }
  .hero-img {
    animation: float 5s ease-in-out 0.5s infinite;
    box-shadow: 0 0 0 3px var(--border), 0 12px 40px rgba(0,0,0,0.4);
  }
  .stats-row { grid-template-columns: repeat(2, 1fr); gap: 14px; }
  .status-badge { margin: 0 auto 18px; }
  .scroll-hint { justify-content: center; }
  .tech-row { justify-content: center; }
  .btn { min-width: 180px; }

  /* Disable typing animation on mobile for performance */
  .typing-text {
    animation: blink 0.8s step-end infinite;
    max-width: 200px !important;
    border-right: 3px solid var(--primary);
  }
}

@media (max-width: 520px) {
  .stats-row { grid-template-columns: repeat(2, 1fr); gap: 12px; }
  .stat-card { padding: 20px 14px 16px; }
  .stat-icon-wrap { width: 40px; height: 40px; }
  .stat-number { font-size: 1.5rem; }
  .tech-tag { padding: 9px 16px; font-size: 0.85rem; }
  .btn { width: 100%; max-width: 300px; }
  .cta-group { flex-direction: column; align-items: center; gap: 12px; }
  .hero-content h1 { font-size: 1.9rem; }
}

@media (max-width: 360px) {
  .stats-row { grid-template-columns: 1fr 1fr; }
  .hero-content h1 { font-size: 1.65rem; }
  .hero-content h2 { font-size: 1rem; }
  .tech-tag { font-size: 0.8rem; padding: 8px 13px; }
}

/* ===== ACCESSIBILITY ===== */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
  html { scroll-behavior: auto; }
  .typing-text { max-width: 200px !important; border-right: none !important; }
}

/* Large touch targets for coarse pointers */
@media (hover: none) and (pointer: coarse) {
  .btn         { min-height: 52px; }
  .tech-tag    { min-height: 46px; }
  .stat-card   { padding: 22px 16px 18px; }
}

/* ===== FOCUS STYLES (Keyboard navigation) ===== */
.btn:focus-visible,
.tech-tag:focus-visible {
  outline: 2px solid var(--primary);
  outline-offset: 3px;
}
</style>

<!-- Intersection Observer: triggers animations only when visible -->
<script>
(function() {
  const io = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.animationPlayState = 'running';
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08 });

  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll(
      '.stat-card, .tech-tag, .hero-content, .hero-image-wrapper'
    ).forEach(el => {
      el.style.animationPlayState = 'paused';
      io.observe(el);
    });
  });
})();
</script>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# HERO SECTION
# ─────────────────────────────────────────────────────────────
col1, col2 = st.columns([1.3, 1], gap="large")

with col1:
    st.markdown("""
    <div class="hero-content">
        <div class="status-badge">
            <span class="status-dot"></span>
            Open to Opportunities
        </div>
        <h1>Hello, I'm <span class="name-highlight"><span class="typing-text">Lloyd</span></span></h1>
        <h2>3rd Year Computer Science Student</h2>
        <p>
            Passionate about building innovative digital solutions, mastering 
            full-stack development, and turning complex problems into elegant, 
            user-friendly applications. Currently exploring AI, web technologies, 
            and software engineering best practices.
        </p>
        <div class="cta-group">
            <a href="/1_About" class="btn btn-primary" tabindex="0" style="color: white; display: inline-flex; align-items: center; gap: 8px;">
    <svg xmlns="http://www.w3.org/2000/svg" width="17" height="17" 
         viewBox="0 0 24 24" fill="none" stroke="currentColor" 
         stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
        <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
        <circle cx="12" cy="7" r="4"/>
    </svg>
    <span>View My Journey</span>
        </a>
            <a href="/3_Contact" class="btn btn-secondary" tabindex="0">
                <svg xmlns="http://www.w3.org/2000/svg" width="17" height="17"
                     viewBox="0 0 24 24" fill="none" stroke="currentColor"
                     stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                    <polyline points="22,6 12,13 2,6"/>
                </svg>
                Get In Touch
            </a>
        </div>
        <div class="scroll-hint">
            <svg class="scroll-arrow" xmlns="http://www.w3.org/2000/svg"
                 viewBox="0 0 24 24" fill="none" stroke="currentColor"
                 stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="6 9 12 15 18 9"/>
            </svg>
            Scroll to explore
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    img_b64 = get_base64_image("Assets/Profile/Profile1.png")
    if img_b64:
        img_html = f'<img src="{img_b64}" class="hero-img" alt="Lloyd George Bibano" loading="eager">'
    else:
        img_html = """
        <div class="hero-placeholder">
            <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48"
                 viewBox="0 0 24 24" fill="none" stroke="currentColor"
                 stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"
                 style="color:var(--text-muted);margin-bottom:10px;">
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
                <circle cx="12" cy="7" r="4"/>
            </svg>
        </div>"""
    st.markdown(f'<div class="hero-image-wrapper">{img_html}</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# QUICK STATS
# ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-divider"></div>
<h3 class="subtitle">Quick Snapshot</h3>
<div class="stats-row">

  <div class="stat-card">
    <div class="stat-icon-wrap">
      <svg class="stat-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
           fill="none" stroke="currentColor" stroke-width="2"
           stroke-linecap="round" stroke-linejoin="round">
        <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/>
      </svg>
    </div>
    <p class="stat-number">12+</p>
    <p class="stat-label">Projects Built</p>
  </div>

  <div class="stat-card">
    <div class="stat-icon-wrap">
      <svg class="stat-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
           fill="none" stroke="currentColor" stroke-width="2"
           stroke-linecap="round" stroke-linejoin="round">
        <polyline points="16 18 22 12 16 6"/>
        <polyline points="8 6 2 12 8 18"/>
      </svg>
    </div>
    <p class="stat-number">3</p>
    <p class="stat-label">Years Coding</p>
  </div>

  <div class="stat-card">
    <div class="stat-icon-wrap">
      <svg class="stat-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
           fill="none" stroke="currentColor" stroke-width="2"
           stroke-linecap="round" stroke-linejoin="round">
        <circle cx="12" cy="12" r="10"/>
        <polyline points="12 6 12 12 16 14"/>
      </svg>
    </div>
    <p class="stat-number">500+</p>
    <p class="stat-label">Hours Learning</p>
  </div>

  <div class="stat-card">
    <div class="stat-icon-wrap">
      <svg class="stat-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
           fill="none" stroke="currentColor" stroke-width="2"
           stroke-linecap="round" stroke-linejoin="round">
        <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
      </svg>
    </div>
    <p class="stat-number">Top 15%</p>
    <p class="stat-label">Course Rank</p>
  </div>

</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# TECH STACK
# ─────────────────────────────────────────────────────────────
st.markdown("""
<h3 class="subtitle">Core Technologies</h3>
<div class="tech-row">

  <div class="tech-tag">
    <span class="tech-dot"></span>
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
         stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>
    </svg>
    Python
  </div>

  <div class="tech-tag">
    <span class="tech-dot"></span>
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
         stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <rect x="2" y="3" width="20" height="14" rx="2" ry="2"/>
      <line x1="8" y1="21" x2="16" y2="21"/>
      <line x1="12" y1="17" x2="12" y2="21"/>
    </svg>
    JavaScript
  </div>

  <div class="tech-tag">
    <span class="tech-dot"></span>
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
         stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="12" cy="12" r="10"/>
      <line x1="2" y1="12" x2="22" y2="12"/>
      <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
    </svg>
    React
  </div>

  <div class="tech-tag">
    <span class="tech-dot"></span>
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
         stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <ellipse cx="12" cy="5" rx="9" ry="3"/>
      <path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/>
      <path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/>
    </svg>
    PostgreSQL
  </div>

  <div class="tech-tag">
    <span class="tech-dot"></span>
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
         stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2z"/>
      <path d="M12 8v4l3 3"/>
    </svg>
    Machine Learning
  </div>

  <div class="tech-tag">
    <span class="tech-dot"></span>
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
         stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="18" cy="18" r="3"/>
      <circle cx="6"  cy="6"  r="3"/>
      <path d="M13 6h3a2 2 0 0 1 2 2v7"/>
      <line x1="6" y1="9" x2="6" y2="21"/>
    </svg>
    Git & GitHub
  </div>

</div>
""", unsafe_allow_html=True)