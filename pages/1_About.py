import streamlit as st
from sidebar import inject_plexus_bg, get_base64_image
import html

st.set_page_config(page_title="About Me", layout="wide", initial_sidebar_state="collapsed")
inject_plexus_bg()

st.markdown("""
<style>
button[kind="secondary"] { visibility: visible !important; }
:root {
  --primary:      #38bdf8;
  --primary-dark: #0ea5e9;
  --primary-glow: rgba(56,189,248,0.35);
  --indigo:       #818cf8;
  --emerald:      #34d399;
  --rose:         #f472b6;
  --text-main:    #f8fafc;
  --text-sub:     #cbd5e1;
  --text-muted:   #94a3b8;
  --glass:        rgba(15,23,42,0.55);
  --glass-hover:  rgba(15,23,42,0.75);
  --border:       rgba(56,189,248,0.18);
  --border-hover: rgba(56,189,248,0.50);
  --transition:   all 0.38s cubic-bezier(0.4,0,0.2,1);
  --bounce:       all 0.45s cubic-bezier(0.34,1.56,0.64,1);
}
*,*::before,*::after{ box-sizing:border-box; margin:0; padding:0; }
html{ scroll-behavior:smooth; }
body{ -webkit-font-smoothing:antialiased; overflow-x:hidden; }

@keyframes fadeInUp {
  from{ opacity:0; transform:translateY(36px); }
  to  { opacity:1; transform:translateY(0);    }
}
@keyframes fadeInLeft {
  from{ opacity:0; transform:translateX(-40px); }
  to  { opacity:1; transform:translateX(0);     }
}
@keyframes fadeInRight {
  from{ opacity:0; transform:translateX(40px); }
  to  { opacity:1; transform:translateX(0);    }
}
@keyframes fadeInScale {
  from{ opacity:0; transform:scale(0.85); }
  to  { opacity:1; transform:scale(1);    }
}
@keyframes gradientShift {
  0%,100%{ background-position:0%   50%; }
  50%     { background-position:100% 50%; }
}
@keyframes pulseGlow {
  0%,100%{ box-shadow:0 0 0 0   var(--primary-glow); }
  50%     { box-shadow:0 0 0 10px transparent;        }
}
@keyframes blink {
  50%{ border-color:transparent; }
}
@keyframes typingReveal {
  from{ max-width:0;    }
  to  { max-width:620px;}
}
@keyframes float {
  0%,100%{ transform:translateY(0);    }
  50%     { transform:translateY(-8px); }
}
@keyframes rotateDash {
  to{ transform:rotate(360deg); }
}
@keyframes cardPop {
  from{ opacity:0; transform:translateY(28px) scale(0.94); }
  to  { opacity:1; transform:translateY(0)    scale(1);    }
}
@keyframes countUp {
  from{ opacity:0; transform:translateY(12px); }
  to  { opacity:1; transform:translateY(0);    }
}
@keyframes underlineGrow {
  from{ width:0;    }
  to  { width:100%; }
}
@keyframes slideInTag {
  from{ opacity:0; transform:translateX(-14px) scale(0.9); }
  to  { opacity:1; transform:translateX(0)     scale(1);   }
}
@keyframes shimmerSweep {
  from{ left:-100%; }
  to  { left: 150%; }
}
@keyframes profileReveal {
  from{ opacity:0; transform:scale(0.88) translateX(-24px); }
  to  { opacity:1; transform:scale(1)    translateX(0);     }
}
@keyframes timelineLineGrow {
  from{ height:0; }
  to  { height:100%; }
}
@keyframes tlCardLeft {
  from{ opacity:0; transform:translateX(-50px) scale(0.95); }
  to  { opacity:1; transform:translateX(0)     scale(1);    }
}
@keyframes tlCardRight {
  from{ opacity:0; transform:translateX(50px) scale(0.95); }
  to  { opacity:1; transform:translateX(0)    scale(1);    }
}
@keyframes dotPop {
  from{ transform:translateX(-50%) scale(0); }
  to  { transform:translateX(-50%) scale(1); }
}
@keyframes badgeDrop {
  from{ opacity:0; transform:translateX(-50%) translateY(-12px); }
  to  { opacity:1; transform:translateX(-50%) translateY(0);     }
}

/* ============================================================
   PAGE HEADER
   ============================================================ */
.page-header{
  text-align:center;
  padding:56px 0 32px;
  animation:fadeInUp 0.8s cubic-bezier(0.4,0,0.2,1) both;
}
.page-label{
  display:inline-flex; align-items:center; gap:8px;
  background:rgba(56,189,248,0.10);
  border:1px solid var(--border);
  padding:7px 18px; border-radius:50px;
  font-size:0.78rem; color:var(--primary);
  font-weight:700; letter-spacing:2.2px;
  text-transform:uppercase; margin-bottom:20px;
}
.page-label-dot{
  width:7px; height:7px; border-radius:50%;
  background:var(--primary);
  animation:pulseGlow 2s ease infinite;
  flex-shrink:0;
}
.page-title{
  font-size:clamp(2.1rem,5vw,3.8rem);
  font-weight:800; line-height:1.1;
  letter-spacing:-0.02em; color:var(--text-main);
  margin-bottom:16px;
}
.page-title .gradient-text{
  background:linear-gradient(135deg,var(--primary),var(--indigo),var(--primary));
  background-size:200% auto;
  -webkit-background-clip:text;
  -webkit-text-fill-color:transparent;
  background-clip:text;
  animation:gradientShift 4s ease infinite;
}
.typing-subtitle{
  display:inline-block; overflow:hidden;
  border-right:3px solid var(--primary);
  white-space:nowrap;
  font-size:clamp(0.95rem,2.2vw,1.15rem);
  color:var(--text-sub); font-weight:500;
  animation:
    typingReveal 2.8s steps(42,end) 0.8s both,
    blink 0.85s step-end infinite;
  max-width:0;
}

/* ============================================================
   PROFILE SECTION
   ============================================================ */
.profile-section{
  display:flex; gap:48px; align-items:center;
  margin:44px 0 16px;
  flex-wrap:wrap;
}
.profile-image-col{
  flex:0 0 auto;
  display:flex; align-items:center; justify-content:center;
  animation:profileReveal 0.9s 0.2s cubic-bezier(0.4,0,0.2,1) both;
}
.profile-img-wrapper{
  position:relative; width:260px; flex-shrink:0;
}
.profile-img-wrapper::before{
  content:'';
  position:absolute; inset:-7px;
  border-radius:26px;
  background:conic-gradient(
    from 0deg,
    transparent  0deg,
    var(--primary) 60deg,
    transparent  120deg,
    var(--indigo)  200deg,
    transparent  260deg,
    var(--primary) 320deg,
    transparent  360deg
  );
  animation:rotateDash 7s linear infinite;
  z-index:0; opacity:0.65;
}
.profile-img-wrapper::after{
  content:'';
  position:absolute; inset:-3px;
  border-radius:23px;
  background:rgba(8,14,30,1);
  z-index:1;
}
.profile-img{
  width:100%; border-radius:20px;
  display:block; position:relative; z-index:2;
  object-fit:cover;
  box-shadow:0 20px 60px rgba(0,0,0,0.5);
  animation:float 6s ease-in-out 1s infinite;
  transition:var(--transition);
}
.profile-img:hover{
  animation-play-state:paused;
  transform:scale(1.04) rotate(1deg);
  box-shadow:0 24px 70px rgba(56,189,248,0.3);
}
.profile-fallback{
  width:260px; height:290px;
  border-radius:20px;
  background:var(--glass);
  border:1px solid var(--border);
  display:flex; flex-direction:column;
  align-items:center; justify-content:center;
  gap:12px; color:var(--text-muted);
  font-size:0.88rem; position:relative; z-index:2;
}
.profile-status{
  position:absolute; bottom:-14px; left:50%;
  transform:translateX(-50%);
  display:inline-flex; align-items:center; gap:7px;
  background:rgba(8,14,30,0.95);
  border:1px solid rgba(34,197,94,0.35);
  padding:7px 16px; border-radius:50px;
  font-size:0.78rem; color:#86efac; font-weight:700;
  white-space:nowrap; z-index:3;
  box-shadow:0 4px 16px rgba(0,0,0,0.4);
}
.status-dot{
  width:7px; height:7px; border-radius:50%;
  background:#22c55e; box-shadow:0 0 8px #22c55e;
  animation:pulseGlow 2s ease infinite; flex-shrink:0;
}
.profile-bio-col{
  flex:1; min-width:260px;
  animation:fadeInRight 0.9s 0.3s cubic-bezier(0.4,0,0.2,1) both;
}
.bio-name{
  font-size:clamp(1.5rem,3.5vw,2.1rem);
  font-weight:800; color:var(--text-main);
  margin-bottom:6px; letter-spacing:-0.01em;
}
.bio-name span{
  background:linear-gradient(135deg,var(--primary),var(--indigo));
  background-size:200% auto;
  -webkit-background-clip:text;
  -webkit-text-fill-color:transparent;
  background-clip:text;
  animation:gradientShift 4s ease infinite;
}
.bio-role{
  font-size:1rem; color:var(--text-muted);
  font-weight:500; margin-bottom:22px;
  position:relative; display:inline-block;
}
.bio-role::after{
  content:'';
  position:absolute; bottom:-5px; left:0;
  height:2px; width:0;
  background:linear-gradient(90deg,var(--primary),transparent);
  animation:underlineGrow 1.2s 1s cubic-bezier(0.4,0,0.2,1) forwards;
}
.bio-description{
  font-size:0.97rem; color:var(--text-muted);
  line-height:1.85; margin-bottom:24px;
  max-width:560px;
}
.bio-chips{ display:flex; flex-wrap:wrap; gap:10px; margin-bottom:28px; }
.bio-chip{
  display:inline-flex; align-items:center; gap:8px;
  background:rgba(56,189,248,0.10);
  border:1px solid rgba(56,189,248,0.22);
  padding:8px 16px; border-radius:50px;
  font-size:0.81rem; color:var(--primary); font-weight:600;
  transition:var(--bounce);
}
.bio-chip:hover{
  background:rgba(56,189,248,0.22);
  transform:translateY(-2px) scale(1.06);
  box-shadow:0 4px 16px rgba(56,189,248,0.2);
}
.bio-chip svg{ width:13px; height:13px; flex-shrink:0; }
.bio-info-row{
  display:flex; flex-wrap:wrap; gap:20px;
}
.bio-info-item{
  display:flex; align-items:center; gap:9px;
  font-size:0.88rem; color:var(--text-muted);
}
.bio-info-item svg{ color:var(--primary); flex-shrink:0; }

/* ============================================================
   SECTION DIVIDER
   ============================================================ */
.section-divider{
  height:1px;
  background:linear-gradient(90deg,transparent,var(--border),transparent);
  margin:52px 0 32px; position:relative;
}
.section-divider::after{
  content:'';
  position:absolute; top:50%; left:50%;
  transform:translate(-50%,-50%);
  width:8px; height:8px; border-radius:50%;
  background:var(--primary);
  box-shadow:0 0 14px var(--primary-glow);
}
.section-label{
  font-size:0.79rem; font-weight:700;
  color:var(--primary); text-transform:uppercase;
  letter-spacing:2.5px; margin-bottom:28px;
  display:inline-flex; align-items:center; gap:10px;
}
.section-label::before,.section-label::after{
  content:''; display:inline-block;
  width:26px; height:1.5px;
  background:var(--primary); opacity:0.55;
}

/* ============================================================
   QUICK FACTS
   ============================================================ */
.facts-grid{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(165px,1fr));
  gap:18px; margin-top:8px;
}
.fact-card{
  background:var(--glass);
  border:1px solid var(--border);
  border-radius:20px; padding:26px 18px 22px;
  text-align:center; backdrop-filter:blur(14px);
  transition:var(--bounce); cursor:default;
  animation:cardPop 0.6s cubic-bezier(0.4,0,0.2,1) both;
  position:relative; overflow:hidden;
}
.fact-card::after{
  content:'';
  position:absolute; top:0; left:0; right:0; height:3px;
  background:linear-gradient(90deg,var(--primary),var(--indigo));
  transform:scaleX(0); transform-origin:left;
  transition:transform 0.4s cubic-bezier(0.4,0,0.2,1);
  border-radius:20px 20px 0 0;
}
.fact-card:hover::after{ transform:scaleX(1); }
.fact-card:hover{
  transform:translateY(-6px) scale(1.03);
  border-color:var(--border-hover);
  box-shadow:0 12px 34px rgba(56,189,248,0.15);
}
.fact-icon-wrap{
  width:46px; height:46px; border-radius:14px;
  background:rgba(56,189,248,0.10);
  border:1px solid rgba(56,189,248,0.20);
  display:flex; align-items:center; justify-content:center;
  margin:0 auto 14px; color:var(--primary);
  transition:var(--bounce);
}
.fact-card:hover .fact-icon-wrap{
  transform:rotate(-8deg) scale(1.14);
  background:rgba(56,189,248,0.22);
}
.fact-icon-wrap svg{ width:22px; height:22px; }
.fact-value{
  font-size:1.55rem; font-weight:800;
  background:linear-gradient(135deg,var(--primary),var(--indigo));
  -webkit-background-clip:text;
  -webkit-text-fill-color:transparent;
  background-clip:text;
  display:block; margin-bottom:6px;
  animation:countUp 0.6s cubic-bezier(0.4,0,0.2,1) both;
}
.fact-label{ font-size:0.80rem; color:var(--text-muted); font-weight:500; }

/* ============================================================
   TIMELINE — COMPLETELY REBUILT
   Always visible, no JS dependency, pure CSS animations
   ============================================================ */
.tl-wrapper{
  position:relative;
  max-width:1000px;
  margin:0 auto;
  padding:20px 0 40px;
}

/* vertical centre line */
.tl-wrapper::before{
  content:'';
  position:absolute;
  left:50%; top:0; bottom:0;
  width:3px;
  background:linear-gradient(
    to bottom,
    transparent 0%,
    var(--primary) 8%,
    var(--indigo) 50%,
    var(--primary) 92%,
    transparent 100%
  );
  transform:translateX(-50%);
  border-radius:3px;
  animation:timelineLineGrow 1.8s cubic-bezier(0.4,0,0.2,1) 0.3s both;
}

/* each row */
.tl-row{
  display:grid;
  grid-template-columns:1fr 80px 1fr;
  align-items:start;
  margin-bottom:60px;
  position:relative;
}
.tl-row:last-child{ margin-bottom:0; }

/* left cell */
.tl-left{
  padding-right:24px;
  display:flex;
  justify-content:flex-end;
}

/* right cell */
.tl-right{
  padding-left:24px;
  display:flex;
  justify-content:flex-start;
}

/* centre column: dot + badge */
.tl-centre{
  display:flex;
  flex-direction:column;
  align-items:center;
  gap:10px;
  padding-top:20px;
  position:relative;
  z-index:5;
}

/* glowing dot */
.tl-dot{
  width:20px; height:20px;
  border-radius:50%;
  background:var(--primary-dark);
  border:3px solid rgba(8,14,30,0.95);
  box-shadow:0 0 0 5px rgba(56,189,248,0.22),
             0 0 18px rgba(56,189,248,0.40);
  flex-shrink:0;
  transition:var(--bounce);
  animation:fadeInScale 0.5s cubic-bezier(0.4,0,0.2,1) both;
}
.tl-row:hover .tl-dot{
  background:#fff;
  box-shadow:0 0 0 8px rgba(56,189,248,0.20),
             0 0 28px rgba(56,189,248,0.65);
  transform:scale(1.25);
}

/* year badge */
.tl-badge{
  display:inline-flex;
  align-items:center;
  justify-content:center;
  background:linear-gradient(135deg,var(--primary-dark),var(--indigo));
  color:#fff;
  padding:6px 18px;
  border-radius:50px;
  font-weight:800;
  font-size:0.88rem;
  letter-spacing:0.06em;
  white-space:nowrap;
  box-shadow:0 0 22px rgba(56,189,248,0.40);
  transition:var(--bounce);
  animation:fadeInScale 0.5s 0.15s cubic-bezier(0.4,0,0.2,1) both;
}
.tl-row:hover .tl-badge{
  transform:scale(1.10);
  box-shadow:0 0 32px rgba(56,189,248,0.65);
}

/* the card */
.tl-card{
  background:var(--glass);
  border:1px solid var(--border);
  border-radius:20px;
  padding:26px 28px;
  backdrop-filter:blur(14px);
  -webkit-backdrop-filter:blur(14px);
  position:relative;
  overflow:hidden;
  transition:var(--bounce);
  width:100%;
  max-width:420px;
}

/* shimmer effect */
.tl-card::before{
  content:'';
  position:absolute; top:0; left:-100%;
  width:55%; height:100%;
  background:linear-gradient(90deg,
    transparent,rgba(56,189,248,0.07),transparent
  );
  pointer-events:none;
  transition:left 0.75s ease;
}
.tl-card:hover::before{ left:150%; }

/* top accent bar */
.tl-card::after{
  content:'';
  position:absolute; top:0; left:0; right:0; height:3px;
  background:linear-gradient(90deg,var(--primary),var(--indigo));
  transform:scaleX(0); transform-origin:left;
  transition:transform 0.42s cubic-bezier(0.4,0,0.2,1);
  border-radius:20px 20px 0 0;
}
.tl-card:hover::after{ transform:scaleX(1); }
.tl-card:hover{
  transform:translateY(-7px) scale(1.02);
  border-color:var(--border-hover);
  background:var(--glass-hover);
  box-shadow:0 16px 48px rgba(56,189,248,0.18);
}

/* left-side cards animate from left */
.tl-left .tl-card{
  animation:tlCardLeft 0.7s cubic-bezier(0.4,0,0.2,1) both;
}
.tl-row:nth-child(1) .tl-left .tl-card{ animation-delay:0.10s; }
.tl-row:nth-child(2) .tl-left .tl-card{ animation-delay:0.22s; }
.tl-row:nth-child(3) .tl-left .tl-card{ animation-delay:0.34s; }
.tl-row:nth-child(4) .tl-left .tl-card{ animation-delay:0.46s; }

/* right-side cards animate from right */
.tl-right .tl-card{
  animation:tlCardRight 0.7s cubic-bezier(0.4,0,0.2,1) both;
}
.tl-row:nth-child(1) .tl-right .tl-card{ animation-delay:0.10s; }
.tl-row:nth-child(2) .tl-right .tl-card{ animation-delay:0.22s; }
.tl-row:nth-child(3) .tl-right .tl-card{ animation-delay:0.34s; }
.tl-row:nth-child(4) .tl-right .tl-card{ animation-delay:0.46s; }

/* arrow connectors */
.tl-left .tl-card .tl-arrow{
  position:absolute; right:-11px; top:28px;
  border:10px solid transparent;
  border-left-color:var(--border);
}
.tl-right .tl-card .tl-arrow{
  position:absolute; left:-11px; top:28px;
  border:10px solid transparent;
  border-right-color:var(--border);
}

/* card internals */
.tl-icon-wrap{
  width:42px; height:42px; border-radius:13px;
  background:rgba(56,189,248,0.12);
  border:1px solid rgba(56,189,248,0.22);
  display:flex; align-items:center; justify-content:center;
  margin-bottom:14px; color:var(--primary);
  transition:var(--bounce); flex-shrink:0;
}
.tl-card:hover .tl-icon-wrap{
  transform:rotate(-8deg) scale(1.14);
  background:rgba(56,189,248,0.24);
}
.tl-icon-wrap svg{ width:20px; height:20px; }
.tl-title{
  color:var(--primary); font-weight:700;
  font-size:1.05rem; margin-bottom:10px;
}
.tl-desc{
  color:var(--text-muted); font-size:0.90rem;
  line-height:1.78; margin-bottom:14px;
}
.tl-tags{ display:flex; flex-wrap:wrap; gap:7px; }
.tl-tag{
  font-size:0.74rem; color:var(--text-sub);
  background:rgba(56,189,248,0.08);
  border:1px solid rgba(56,189,248,0.16);
  padding:4px 11px; border-radius:50px; font-weight:500;
}

/* empty placeholder so grid stays balanced */
.tl-empty{ width:100%; }

/* ============================================================
   SKILLS
   ============================================================ */
.skills-grid{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(278px,1fr));
  gap:20px; margin-top:8px;
}
.skill-category{
  background:var(--glass);
  border:1px solid var(--border);
  border-radius:22px; padding:26px 24px;
  backdrop-filter:blur(14px);
  transition:var(--bounce);
  animation:cardPop 0.6s cubic-bezier(0.4,0,0.2,1) both;
  position:relative; overflow:hidden;
}
.skill-category::before{
  content:'';
  position:absolute; top:0; left:0; right:0; height:3px;
  background:var(--cat-color,var(--primary));
  border-radius:22px 22px 0 0;
}
.skill-category:hover{
  transform:translateY(-5px);
  border-color:var(--border-hover);
  box-shadow:0 10px 36px rgba(56,189,248,0.13);
}
.skill-cat-header{
  display:flex; align-items:center; gap:13px; margin-bottom:22px;
}
.skill-cat-icon{
  width:46px; height:46px; border-radius:14px;
  background:rgba(56,189,248,0.10);
  border:1px solid rgba(56,189,248,0.20);
  display:flex; align-items:center; justify-content:center;
  color:var(--primary); transition:var(--bounce); flex-shrink:0;
}
.skill-category:hover .skill-cat-icon{
  transform:rotate(-8deg) scale(1.12);
  background:rgba(56,189,248,0.22);
}
.skill-cat-icon svg{ width:22px; height:22px; }
.skill-cat-title{ font-size:1rem; font-weight:700; color:var(--text-main); }
.skill-bar-wrap{ margin-bottom:15px; }
.skill-bar-label{
  display:flex; justify-content:space-between; margin-bottom:7px;
}
.skill-bar-name{ font-size:0.86rem; color:var(--text-sub); font-weight:500; }
.skill-bar-pct { font-size:0.81rem; color:var(--primary); font-weight:700; }
.skill-bar-track{
  height:7px; border-radius:50px;
  background:rgba(56,189,248,0.10); overflow:hidden;
}
.skill-bar-fill{
  height:100%; border-radius:50px;
  background:linear-gradient(90deg,var(--primary-dark),var(--primary));
  transition:width 1.5s cubic-bezier(0.4,0,0.2,1);
  box-shadow:0 0 10px rgba(56,189,248,0.40);
  animation:skillFill 1.5s cubic-bezier(0.4,0,0.2,1) 0.5s both;
}
@keyframes skillFill {
  from{ width:0 !important; }
}

/* ============================================================
   INTERESTS
   ============================================================ */
.interests-row{
  display:flex; flex-wrap:wrap; gap:13px; margin-top:8px;
}
.interest-chip{
  display:inline-flex; align-items:center; gap:9px;
  background:rgba(15,23,42,0.60);
  border:1px solid var(--border);
  padding:11px 20px; border-radius:50px;
  font-size:0.9rem; color:var(--text-sub);
  transition:var(--bounce); cursor:default;
  backdrop-filter:blur(8px);
  animation:slideInTag 0.5s cubic-bezier(0.4,0,0.2,1) both;
  position:relative; overflow:hidden;
}
@keyframes slideInTag {
  from{ opacity:0; transform:translateX(-14px) scale(0.9); }
  to  { opacity:1; transform:translateX(0)     scale(1);   }
}
.interest-chip::before{
  content:'';
  position:absolute; inset:0;
  background:linear-gradient(135deg,
    rgba(56,189,248,0.10),rgba(129,140,248,0.10)
  );
  opacity:0; transition:opacity 0.35s;
}
.interest-chip:hover::before{ opacity:1; }
.interest-chip:hover{
  border-color:var(--primary); color:var(--primary);
  transform:translateY(-4px) scale(1.06);
  box-shadow:0 8px 24px rgba(56,189,248,0.18);
}
.interest-chip svg{
  width:15px; height:15px; flex-shrink:0; color:var(--primary);
  transition:var(--transition);
}
.interest-chip:hover svg{ transform:rotate(15deg) scale(1.2); }
.interest-pulse{
  width:7px; height:7px; border-radius:50%;
  background:var(--primary);
  box-shadow:0 0 6px var(--primary);
  animation:pulseGlow 2s ease infinite; flex-shrink:0;
}

/* ============================================================
   MOBILE RESPONSIVE
   ============================================================ */
@media (max-width:900px){
  .tl-wrapper::before{
    left:24px;
  }
  .tl-row{
    grid-template-columns:0 48px 1fr;
    margin-bottom:40px;
  }
  .tl-left{ display:none; }
  .tl-right{
    padding-left:16px;
    justify-content:flex-start;
  }
  .tl-centre{
    padding-top:18px;
    align-items:center;
  }
  .tl-right .tl-card .tl-arrow{
    left:-11px; top:24px;
  }
  .tl-card{ max-width:100%; }
  .tl-badge{ font-size:0.78rem; padding:5px 13px; }
}

@media (max-width:768px){
  .profile-section{ flex-direction:column; align-items:center; text-align:center; }
  .profile-img-wrapper{ width:200px; }
  .profile-fallback{ width:200px; height:225px; }
  .profile-img-wrapper::before{ display:none; }
  .profile-img-wrapper::after { display:none; }
  .profile-img{
    box-shadow:0 0 0 3px var(--border), 0 12px 40px rgba(0,0,0,0.4);
    animation:float 6s ease-in-out 0.5s infinite;
  }
  .bio-role::after{ left:50%; transform:translateX(-50%); }
  .bio-chips{ justify-content:center; }
  .bio-info-row{ justify-content:center; }
  .facts-grid{ grid-template-columns:repeat(2,1fr); }
  .interests-row{ justify-content:center; }
  .skills-grid{ grid-template-columns:1fr; }
  .typing-subtitle{
    animation:blink 0.85s step-end infinite;
    max-width:480px !important;
    border-right:3px solid var(--primary);
  }
  .page-title{ font-size:2rem; }
  .bio-description{ margin:0 auto 24px; }
}

@media (max-width:480px){
  .facts-grid{ grid-template-columns:repeat(2,1fr); gap:13px; }
  .profile-section{ margin:28px 0 8px; gap:22px; }
  .profile-img-wrapper{ width:170px; }
  .profile-fallback{ width:170px; height:190px; }
  .interest-chip{ padding:9px 15px; font-size:0.83rem; }
  .tl-card{ padding:20px 18px; }
}

@media (prefers-reduced-motion:reduce){
  *,*::before,*::after{
    animation-duration:0.01ms !important;
    animation-iteration-count:1 !important;
    transition-duration:0.01ms !important;
  }
  .typing-subtitle{ max-width:620px !important; border-right:none !important; }
  .tl-wrapper::before{ animation:none; height:100%; }
  .skill-bar-fill{ animation:none !important; }
}
@media (hover:none) and (pointer:coarse){
  .interest-chip,.bio-chip{ min-height:46px; }
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────
# SVG ICON HELPER
# ─────────────────────────────────────────────────────────────────────
def svg(paths: str, size: int = 20) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" '
        f'viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
        f'{paths}</svg>'
    )

PATHS = {
    "user":        '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
    "map-pin":     '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
    "book-open":   '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>',
    "briefcase":   '<rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>',
    "code":        '<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>',
    "cpu":         '<rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><line x1="9" y1="1" x2="9" y2="4"/><line x1="15" y1="1" x2="15" y2="4"/><line x1="9" y1="20" x2="9" y2="23"/><line x1="15" y1="20" x2="15" y2="23"/><line x1="20" y1="9" x2="23" y2="9"/><line x1="20" y1="14" x2="23" y2="14"/><line x1="1" y1="9" x2="4" y2="9"/><line x1="1" y1="14" x2="4" y2="14"/>',
    "mail":        '<path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/>',
    "calendar":    '<rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/>',
    "layers":      '<polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/>',
    "folder":      '<path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/>',
    "clock":       '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
    "star":        '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>',
    "coffee":      '<path d="M18 8h1a4 4 0 0 1 0 8h-1"/><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/><line x1="6" y1="1" x2="6" y2="4"/><line x1="10" y1="1" x2="10" y2="4"/><line x1="14" y1="1" x2="14" y2="4"/>',
    "trending-up": '<polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/>',
    "seedling":    '<path d="M12 22V12"/><path d="M12 12C12 7 7 3 2 3c0 5 4 9 10 9z"/><path d="M12 12c0-5 5-9 10-9-1 5-5 9-10 9z"/>',
    "zap":         '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>',
    "target":      '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
    "rocket":      '<path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0"/><path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/>',
    "terminal":    '<polyline points="4 17 10 11 4 5"/><line x1="12" y1="19" x2="20" y2="19"/>',
    "layout":      '<rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/>',
    "tool":        '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
    "bar-chart":   '<line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/>',
    "brain":       '<path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96-.46 2.5 2.5 0 0 1-2.96-3.08 3 3 0 0 1-.34-5.58 2.5 2.5 0 0 1 1.32-4.24 2.5 2.5 0 0 1 1.98-3A2.5 2.5 0 0 1 9.5 2z"/><path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96-.46 2.5 2.5 0 0 0 2.96-3.08 3 3 0 0 0 .34-5.58 2.5 2.5 0 0 0-1.32-4.24 2.5 2.5 0 0 0-1.98-3A2.5 2.5 0 0 0 14.5 2z"/>',
    "globe":       '<circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
    "database":    '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/>',
    "gamepad":     '<line x1="6" y1="11" x2="10" y2="11"/><line x1="8" y1="9" x2="8" y2="13"/><line x1="15" y1="12" x2="15.01" y2="12"/><line x1="18" y1="10" x2="18.01" y2="10"/><path d="M17.32 5H6.68a4 4 0 0 0-3.978 3.59c-.006.052-.01.101-.017.152C2.604 9.416 2 14.456 2 16a3 3 0 0 0 3 3c1 0 1.5-.5 2-1l1.414-1.414A2 2 0 0 1 9.828 16h4.344a2 2 0 0 1 1.414.586L17 18c.5.5 1 1 2 1a3 3 0 0 0 3-3c0-1.545-.604-6.584-.685-7.258-.007-.05-.011-.1-.017-.151A4 4 0 0 0 17.32 5z"/>',
    "cloud":       '<path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"/>',
    "shield":      '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
    "smartphone":  '<rect x="5" y="2" width="14" height="20" rx="2" ry="2"/><line x1="12" y1="18" x2="12.01" y2="18"/>',
    "git-branch":  '<line x1="6" y1="3" x2="6" y2="15"/><circle cx="18" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M18 9a9 9 0 0 1-9 9"/>',
    "edit":        '<path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/>',
    "music":       '<path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/>',
    "award":       '<circle cx="12" cy="8" r="6"/><path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11"/>',
    "grid":        '<rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/>',
}


# ─────────────────────────────────────────────────────────────────────
# PAGE HEADER
# ─────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="page-header">
  <div class="page-label">
    <span class="page-label-dot"></span>
    About Me
  </div>
  <h1 class="page-title">
    Know <span class="gradient-text">Who I Am</span>
  </h1>
  <div class="typing-subtitle">
    Computer Science Student &nbsp;·&nbsp; Full-Stack Builder &nbsp;·&nbsp; Problem Solver
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────
# PROFILE SECTION
# ─────────────────────────────────────────────────────────────────────
b64 = get_base64_image("Assets/Profile/Profile1.png")

if b64:
    img_html = f'<img src="{b64}" class="profile-img" alt="Lloyd George Bibano" loading="eager">'
else:
    img_html = f"""
    <div class="profile-fallback">
      {svg(PATHS['user'], 52)}
      <span style="font-size:0.85rem;color:var(--text-muted)">Profile Image</span>
    </div>"""

bio_chips = [
    ("map-pin",   "Philippines"),
    ("book-open", "BS Computer Science"),
    ("briefcase", "Open to Internships"),
    ("code",      "Full-Stack Developer"),
    ("cpu",       "AI Enthusiast"),
]
chips_html = "".join(
    f'<span class="bio-chip">{svg(PATHS[k],13)}{label}</span>'
    for k, label in bio_chips
)

info_rows = [
    ("calendar", "Started CS · 2023"),
    ("award",    "Top 15% · Course Ranking"),
    ("mail",     "Open to collaborations"),
]
info_html = "".join(
    f'<div class="bio-info-item">{svg(PATHS[k],15)}<span>{label}</span></div>'
    for k, label in info_rows
)

st.markdown(f"""
<div class="profile-section">
  <div class="profile-image-col">
    <div class="profile-img-wrapper">
      {img_html}
      <div class="profile-status">
        <span class="status-dot"></span>
        Available for Opportunities
      </div>
    </div>
  </div>
  <div class="profile-bio-col">
    <h2 class="bio-name">Lloyd George <span>Bibano</span></h2>
    <div class="bio-role">3rd Year Computer Science Student</div>
    <p class="bio-description">
      Hello! I'm a passionate computer science student with a deep love for
      building things that matter. From crafting elegant front-end experiences
      to architecting robust back-end systems, I thrive at the intersection of
      creativity and logic. When I'm not coding, I'm learning something new —
      because in tech, curiosity is a superpower.
    </p>
    <div class="bio-chips">{chips_html}</div>
    <div class="bio-info-row">{info_html}</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────
# QUICK FACTS
# ─────────────────────────────────────────────────────────────────────
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-label">Quick Facts</div>', unsafe_allow_html=True)

facts = [
    ("layers",      "3rd Year",  "CS Student"),
    ("folder",      "12+",       "Projects Completed"),
    ("clock",       "500+",      "Hours of Learning"),
    ("star",        "Top 15%",   "Course Ranking"),
    ("coffee",      "999+",      "Cups of Coffee"),
    ("trending-up", "6+",        "Tech Stacks Learned"),
]

facts_html = "".join(f"""
<div class="fact-card">
  <div class="fact-icon-wrap">{svg(PATHS[ik], 22)}</div>
  <span class="fact-value">{val}</span>
  <span class="fact-label">{label}</span>
</div>
""" for ik, val, label in facts)

st.markdown(f'<div class="facts-grid">{facts_html}</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────
# TIMELINE — REBUILT WITH GRID LAYOUT (no JS dependency)
# Alternates: odd rows → card on LEFT, even rows → card on RIGHT
# ─────────────────────────────────────────────────────────────────────
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-label">My Journey</div>', unsafe_allow_html=True)

journey = [
    {
        "year": "2023", "icon": "seedling",
        "title": "The Beginning",
        "desc": "Started my Computer Science degree with zero prior experience. Built my first program in Python and immediately fell in love with the logical elegance of programming and problem-solving.",
        "tags": ["Python Basics", "CS Fundamentals", "Logic Building"],
        "side": "left"   # card appears on left
    },
    {
        "year": "2024", "icon": "zap",
        "title": "Exploration & Growth",
        "desc": "Dived deep into web development — mastered HTML, CSS, and JavaScript. Collaborated on academic group projects, learned version control with Git, and attended my first tech hackathon.",
        "tags": ["HTML/CSS/JS", "Git & GitHub", "Hackathon", "Teamwork"],
        "side": "right"  # card appears on right
    },
    {
        "year": "2025", "icon": "target",
        "title": "Specialization",
        "desc": "Focused on data structures, algorithms, and back-end architecture. Started contributing to open-source repositories and building portfolio-ready full-stack applications with React and FastAPI.",
        "tags": ["DSA", "Backend Dev", "React", "PostgreSQL", "Open Source"],
        "side": "left"
    },
    {
        "year": "2026", "icon": "rocket",
        "title": "Present Day",
        "desc": "3rd Year CS Student — developing advanced full-stack systems, exploring AI and machine learning, mastering cloud deployment, and preparing for industry-ready software engineering roles.",
        "tags": ["Full-Stack", "AI / ML", "Cloud", "Streamlit", "Career Prep"],
        "side": "right"
    },
]

def make_tl_card(item):
    tags_html = "".join(f'<span class="tl-tag">{html.escape(t)}</span>' for t in item["tags"])
    icon_html  = svg(PATHS[item["icon"]], 20)
    title_escaped = html.escape(item["title"])
    desc_escaped = html.escape(item["desc"])
    
    return f'<div class="tl-card"><div class="tl-arrow"></div><div class="tl-icon-wrap">{icon_html}</div><div class="tl-title">{title_escaped}</div><p class="tl-desc">{desc_escaped}</p><div class="tl-tags">{tags_html}</div></div>'

timeline_html = '<div class="tl-wrapper">'

for item in journey:
    card_html = make_tl_card(item)
    centre_html = f'<div class="tl-centre"><div class="tl-dot"></div><div class="tl-badge">{html.escape(item["year"])}</div></div>'

    if item["side"] == "left":
        left_cell  = f'<div class="tl-left">{card_html}</div>'
        right_cell = '<div class="tl-right"><div class="tl-empty"></div></div>'
    else:
        left_cell  = '<div class="tl-left"><div class="tl-empty"></div></div>'
        right_cell = f'<div class="tl-right">{card_html}</div>'

    timeline_html += f'<div class="tl-row">{left_cell}{centre_html}{right_cell}</div>'

timeline_html += '</div>'
st.markdown(timeline_html, unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────
# INTERESTS
# ─────────────────────────────────────────────────────────────────────
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-label">Interests &amp; Passions</div>', unsafe_allow_html=True)

interests = [
    ("brain",      "Artificial Intelligence"),
    ("globe",      "Web Development"),
    ("database",   "Data Science"),
    ("gamepad",    "Game Development"),
    ("cloud",      "Cloud Computing"),
    ("shield",     "Cybersecurity"),
    ("smartphone", "Mobile Apps"),
    ("git-branch", "Open Source"),
    ("edit",       "Tech Blogging"),
    ("music",      "Music & Coding"),
]

interest_chips_html = "".join(f"""
<div class="interest-chip" style="animation-delay:{i*0.07}s">
  <span class="interest-pulse"></span>
  {svg(PATHS[ik], 15)}
  {html.escape(label)}
</div>""" for i, (ik, label) in enumerate(interests))

st.markdown(f'<div class="interests-row">{interest_chips_html}</div>', unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)