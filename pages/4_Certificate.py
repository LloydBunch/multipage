import streamlit as st
from sidebar import inject_plexus_bg, get_base64_image

st.set_page_config(page_title="Certificates", layout="wide", initial_sidebar_state="collapsed")
inject_plexus_bg()

st.markdown("""
<style>
/* Show sidebar toggle button */
[data-testid="stSidebarCollapsedControl"] { visibility: visible !important; }
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
@import url('https://cdn.jsdelivr.net/npm/remixicon@4.1.0/fonts/remixicon.css');

* { box-sizing: border-box; margin: 0; padding: 0; }

/* ─── Hide Streamlit defaults ─── */
footer { visibility: hidden; }
.block-container { padding-top: 2rem; padding-bottom: 2rem; }

/* ─── Typing Effect ─── */
.typing-wrapper {
    text-align: center;
    margin-bottom: 50px;
    padding: 20px;
}
.section-title-container {
    display: inline-flex;
    align-items: center;
    gap: 14px;
    justify-content: center;
}
.section-icon {
    width: 48px;
    height: 48px;
    background: linear-gradient(135deg, #38bdf8, #6366f1);
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.4rem;
    color: white;
    box-shadow: 0 8px 25px rgba(56,189,248,0.3);
    flex-shrink: 0;
}
.section-title {
    display: inline-block;
    color: #f8fafc;
    font-size: clamp(1.8rem, 5vw, 2.8rem);
    font-family: 'Inter', sans-serif;
    font-weight: 800;
    overflow: hidden;
    white-space: nowrap;
    border-right: 3px solid #38bdf8;
    animation: typing 2.5s steps(20, end) forwards, blink 0.75s step-end infinite;
    width: 0;
    letter-spacing: -0.03em;
}
@keyframes typing {
    from { width: 0; }
    to { width: 100%; }
}
@keyframes blink {
    50% { border-color: transparent; }
}

.subtitle-text {
    color: #64748b;
    font-size: clamp(0.85rem, 2vw, 1.05rem);
    margin-top: 14px;
    opacity: 0;
    animation: fadeSlideUp 0.8s ease 2.5s forwards;
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
}
.subtitle-text i {
    color: #38bdf8;
    font-size: 1rem;
}
.subtitle-divider {
    width: 60px;
    height: 3px;
    background: linear-gradient(90deg, #38bdf8, #6366f1);
    border-radius: 3px;
    margin: 16px auto 0;
    opacity: 0;
    animation: fadeSlideUp 0.8s ease 2.7s forwards;
}

/* ─── Stats Bar ─── */
.stats-bar {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 0;
    margin-bottom: 40px;
    background: rgba(15, 23, 42, 0.6);
    border-radius: 20px;
    border: 1px solid rgba(56,189,248,0.08);
    max-width: 780px;
    margin-left: auto;
    margin-right: auto;
    opacity: 0;
    animation: fadeSlideUp 0.8s ease 3s forwards;
    overflow: hidden;
    backdrop-filter: blur(20px);
    box-shadow: 0 4px 30px rgba(0,0,0,0.2);
}
.stat-item {
    text-align: center;
    color: #f8fafc;
    padding: 24px 16px;
    position: relative;
    transition: all 0.3s ease;
}
.stat-item:not(:last-child)::after {
    content: '';
    position: absolute;
    right: 0;
    top: 20%;
    height: 60%;
    width: 1px;
    background: rgba(56,189,248,0.1);
}
.stat-item:hover {
    background: rgba(56,189,248,0.04);
}
.stat-icon-wrap {
    width: 40px;
    height: 40px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 10px;
    font-size: 1.1rem;
}
.stat-icon-wrap.blue { background: rgba(56,189,248,0.12); color: #38bdf8; }
.stat-icon-wrap.purple { background: rgba(99,102,241,0.12); color: #818cf8; }
.stat-icon-wrap.emerald { background: rgba(52,211,153,0.12); color: #34d399; }
.stat-icon-wrap.amber { background: rgba(251,191,36,0.12); color: #fbbf24; }
.stat-number {
    font-size: clamp(1.5rem, 4vw, 2rem);
    font-weight: 800;
    color: #f1f5f9;
    display: block;
    font-family: 'Inter', sans-serif;
    letter-spacing: -0.03em;
}
.stat-label {
    font-size: clamp(0.65rem, 1.5vw, 0.78rem);
    color: #64748b;
    font-family: 'Inter', sans-serif;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-top: 2px;
}

@media (max-width: 520px) {
    .stats-bar { grid-template-columns: repeat(2, 1fr); }
    .stat-item:nth-child(2)::after { display: none; }
    .stat-item:nth-child(1), .stat-item:nth-child(2) {
        border-bottom: 1px solid rgba(56,189,248,0.08);
    }
}

/* ─── Filter Buttons ─── */
.filter-section {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 40px;
    padding: 0 15px;
    opacity: 0;
    animation: fadeSlideUp 0.8s ease 3.2s forwards;
}
.filter-btn {
    padding: 10px 22px;
    border-radius: 12px;
    border: 1px solid rgba(56,189,248,0.12);
    background: rgba(15, 23, 42, 0.6);
    color: #94a3b8;
    cursor: pointer;
    font-size: clamp(0.78rem, 2vw, 0.88rem);
    font-family: 'Inter', sans-serif;
    font-weight: 500;
    transition: all 0.3s ease;
    white-space: nowrap;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    backdrop-filter: blur(10px);
}
.filter-btn i {
    font-size: 0.95rem;
    opacity: 0.7;
}
.filter-btn:hover {
    background: rgba(56,189,248,0.08);
    border-color: rgba(56,189,248,0.25);
    color: #cbd5e1;
    transform: translateY(-2px);
}
.filter-btn.active {
    background: linear-gradient(135deg, rgba(56,189,248,0.15), rgba(99,102,241,0.15));
    border-color: rgba(56,189,248,0.4);
    color: #38bdf8;
    box-shadow: 0 4px 20px rgba(56,189,248,0.15);
}
.filter-btn.active i {
    opacity: 1;
}

/* ─── Certificate Gallery ─── */
.cert-gallery {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: clamp(18px, 3vw, 28px);
    padding: 10px 15px 50px;
    max-width: 1200px;
    margin: 0 auto;
}

@media (max-width: 480px) {
    .cert-gallery {
        grid-template-columns: 1fr;
        gap: 16px;
        padding: 10px;
    }
}
@media (min-width: 481px) and (max-width: 768px) {
    .cert-gallery {
        grid-template-columns: repeat(2, 1fr);
    }
}

/* ─── Certificate Card ─── */
.cert-item {
    background: rgba(15, 23, 42, 0.7);
    border-radius: 20px;
    overflow: hidden;
    border: 1px solid rgba(56,189,248,0.08);
    transition: all 0.45s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    cursor: pointer;
    position: relative;
    opacity: 0;
    transform: translateY(40px);
    backdrop-filter: blur(20px);
}
.cert-item.visible {
    animation: cardAppear 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
}
.cert-item:nth-child(1) { animation-delay: 0.1s; }
.cert-item:nth-child(2) { animation-delay: 0.2s; }
.cert-item:nth-child(3) { animation-delay: 0.3s; }
.cert-item:nth-child(4) { animation-delay: 0.4s; }
.cert-item:nth-child(5) { animation-delay: 0.5s; }

@keyframes cardAppear {
    to { opacity: 1; transform: translateY(0); }
}

.cert-item:hover {
    transform: translateY(-8px);
    box-shadow:
        0 20px 50px rgba(0,0,0,0.3),
        0 0 0 1px rgba(56,189,248,0.2),
        0 0 60px rgba(56,189,248,0.08);
    border-color: rgba(56,189,248,0.2);
}

/* ─── Image Container ─── */
.cert-img-wrapper {
    position: relative;
    overflow: hidden;
    height: clamp(170px, 22vw, 210px);
}
.cert-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.6s ease, filter 0.4s ease;
}
.cert-item:hover .cert-img {
    transform: scale(1.06);
    filter: brightness(0.7);
}
.cert-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(
        135deg,
        rgba(56,189,248,0.8) 0%,
        rgba(99,102,241,0.8) 100%
    );
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    transition: opacity 0.4s ease;
    flex-direction: column;
    gap: 10px;
}
.cert-item:hover .cert-overlay {
    opacity: 1;
}
.overlay-icon-wrap {
    width: 56px;
    height: 56px;
    background: rgba(255,255,255,0.2);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.3);
    animation: pulseIcon 2s ease infinite;
}
.overlay-icon-wrap i {
    font-size: 1.4rem;
    color: white;
}
.overlay-text {
    color: white;
    font-size: clamp(0.7rem, 2vw, 0.82rem);
    font-weight: 600;
    font-family: 'Inter', sans-serif;
    letter-spacing: 2px;
    text-transform: uppercase;
}
@keyframes pulseIcon {
    0%, 100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255,255,255,0.3); }
    50% { transform: scale(1.08); box-shadow: 0 0 0 12px rgba(255,255,255,0); }
}

/* ─── Badge ─── */
.cert-badge {
    position: absolute;
    top: 14px;
    right: 14px;
    background: rgba(15, 23, 42, 0.8);
    backdrop-filter: blur(10px);
    color: #34d399;
    font-size: 0.68rem;
    font-weight: 700;
    padding: 5px 12px;
    border-radius: 8px;
    font-family: 'Inter', sans-serif;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    border: 1px solid rgba(52,211,153,0.2);
    z-index: 2;
    display: flex;
    align-items: center;
    gap: 4px;
}
.cert-badge i {
    font-size: 0.72rem;
}

/* ─── Card Info ─── */
.cert-info {
    padding: clamp(16px, 3vw, 22px);
    color: #f8fafc;
    font-family: 'Inter', sans-serif;
}
.cert-info h3 {
    margin: 0 0 10px;
    font-size: clamp(0.95rem, 2.5vw, 1.12rem);
    font-weight: 700;
    line-height: 1.35;
    letter-spacing: -0.02em;
    color: #f1f5f9;
}
.cert-meta {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 12px;
}
.cert-meta-left {
    display: flex;
    align-items: center;
    gap: 12px;
    color: #64748b;
    font-size: clamp(0.72rem, 1.8vw, 0.82rem);
    font-weight: 500;
}
.cert-meta-left span {
    display: inline-flex;
    align-items: center;
    gap: 5px;
}
.cert-meta-left i {
    font-size: 0.85rem;
    color: #475569;
}
.cert-category-tag {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    background: rgba(56,189,248,0.08);
    color: #38bdf8;
    border: 1px solid rgba(56,189,248,0.15);
    border-radius: 8px;
    padding: 3px 10px;
    font-size: 0.7rem;
    font-weight: 600;
    font-family: 'Inter', sans-serif;
    letter-spacing: 0.3px;
}

/* Skill chips */
.skill-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-bottom: 14px;
}
.skill-chip {
    background: rgba(99,102,241,0.08);
    color: #a5b4fc;
    border: 1px solid rgba(99,102,241,0.12);
    border-radius: 6px;
    padding: 3px 9px;
    font-size: 0.68rem;
    font-weight: 600;
    font-family: 'Inter', sans-serif;
}

/* ─── Progress Bar ─── */
.skill-progress {
    margin-top: 4px;
}
.progress-label {
    display: flex;
    justify-content: space-between;
    color: #64748b;
    font-size: 0.72rem;
    margin-bottom: 6px;
    font-weight: 500;
}
.progress-bar-bg {
    background: rgba(255,255,255,0.06);
    border-radius: 10px;
    height: 5px;
    overflow: hidden;
}
.progress-bar-fill {
    height: 100%;
    border-radius: 10px;
    background: linear-gradient(90deg, #38bdf8, #6366f1, #a78bfa);
    transition: width 1.5s cubic-bezier(0.4, 0, 0.2, 1);
    width: 0%;
    position: relative;
}
.progress-bar-fill::after {
    content: '';
    position: absolute;
    right: 0;
    top: 50%;
    transform: translateY(-50%);
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #a78bfa;
    box-shadow: 0 0 10px rgba(167,139,250,0.5);
    opacity: 0;
    transition: opacity 0.3s ease 1.2s;
}
.cert-item:hover .progress-bar-fill::after {
    opacity: 1;
}
.cert-item:hover .progress-bar-fill {
    width: var(--progress);
}

/* ─── Shine Effect ─── */
.cert-item::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -60%;
    width: 40%;
    height: 200%;
    background: linear-gradient(
        to right,
        rgba(255,255,255,0) 0%,
        rgba(255,255,255,0.04) 50%,
        rgba(255,255,255,0) 100%
    );
    transform: skewX(-20deg);
    transition: left 0.7s ease;
    z-index: 1;
    pointer-events: none;
}
.cert-item:hover::before {
    left: 120%;
}

/* ─── Ambient Glow Orbs ─── */
.ambient-glow {
    position: fixed;
    border-radius: 50%;
    pointer-events: none;
    filter: blur(80px);
    z-index: 0;
    opacity: 0.04;
}
.glow-1 {
    width: 400px;
    height: 400px;
    background: #38bdf8;
    top: 10%;
    left: -5%;
    animation: floatGlow 15s ease-in-out infinite;
}
.glow-2 {
    width: 350px;
    height: 350px;
    background: #6366f1;
    bottom: 10%;
    right: -5%;
    animation: floatGlow 18s ease-in-out infinite reverse;
}
@keyframes floatGlow {
    0%, 100% { transform: translate(0, 0); }
    33% { transform: translate(30px, -20px); }
    66% { transform: translate(-20px, 30px); }
}

/* ─── Modal ─── */
.modal-overlay {
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.8);
    z-index: 9999;
    justify-content: center;
    align-items: center;
    backdrop-filter: blur(12px);
    padding: 20px;
}
.modal-overlay.open {
    display: flex;
    animation: fadeIn 0.3s ease;
}
.modal-box {
    background: linear-gradient(160deg, rgba(15,23,42,0.98), rgba(30,41,59,0.95));
    border: 1px solid rgba(56,189,248,0.15);
    border-radius: 24px;
    padding: clamp(24px, 5vw, 36px);
    max-width: 520px;
    width: 100%;
    position: relative;
    animation: modalSlideIn 0.45s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    font-family: 'Inter', sans-serif;
    box-shadow:
        0 25px 60px rgba(0,0,0,0.5),
        0 0 80px rgba(56,189,248,0.08);
    max-height: 90vh;
    overflow-y: auto;
}
@keyframes modalSlideIn {
    from { transform: scale(0.85) translateY(30px); opacity: 0; }
    to { transform: scale(1) translateY(0); opacity: 1; }
}
.modal-close {
    position: absolute;
    top: 16px;
    right: 18px;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    color: #94a3b8;
    width: 36px;
    height: 36px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.3s ease;
    z-index: 1;
    font-size: 1.1rem;
}
.modal-close:hover {
    color: #f8fafc;
    background: rgba(239,68,68,0.15);
    border-color: rgba(239,68,68,0.3);
    transform: rotate(90deg);
}
.modal-cert-img {
    width: 100%;
    border-radius: 16px;
    margin-bottom: 22px;
    border: 1px solid rgba(56,189,248,0.1);
    box-shadow: 0 8px 30px rgba(0,0,0,0.3);
}
.modal-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 6px;
}
.modal-verified {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    color: #34d399;
    font-size: 0.72rem;
    font-weight: 600;
    background: rgba(52,211,153,0.1);
    padding: 3px 10px;
    border-radius: 6px;
    border: 1px solid rgba(52,211,153,0.15);
}
.modal-verified i { font-size: 0.78rem; }
.modal-title {
    color: #f1f5f9;
    font-size: clamp(1.15rem, 3vw, 1.45rem);
    font-weight: 800;
    margin-bottom: 10px;
    letter-spacing: -0.03em;
    line-height: 1.3;
}
.modal-desc {
    color: #94a3b8;
    font-size: clamp(0.82rem, 2vw, 0.92rem);
    line-height: 1.7;
    margin-bottom: 18px;
    font-weight: 400;
}
.modal-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 16px;
}
.modal-tag {
    background: rgba(56,189,248,0.08);
    color: #38bdf8;
    border: 1px solid rgba(56,189,248,0.15);
    border-radius: 8px;
    padding: 5px 14px;
    font-size: 0.78rem;
    font-weight: 600;
    display: inline-flex;
    align-items: center;
    gap: 5px;
}
.modal-tag i {
    font-size: 0.82rem;
    opacity: 0.8;
}
.modal-detail-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-bottom: 22px;
}
.modal-detail-item {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 12px;
    padding: 12px 14px;
    display: flex;
    align-items: center;
    gap: 10px;
}
.modal-detail-icon {
    width: 34px;
    height: 34px;
    border-radius: 9px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.9rem;
    flex-shrink: 0;
}
.modal-detail-icon.blue { background: rgba(56,189,248,0.12); color: #38bdf8; }
.modal-detail-icon.purple { background: rgba(99,102,241,0.12); color: #818cf8; }
.modal-detail-icon.emerald { background: rgba(52,211,153,0.12); color: #34d399; }
.modal-detail-icon.amber { background: rgba(251,191,36,0.12); color: #fbbf24; }
.modal-detail-text {
    font-size: 0.78rem;
    color: #64748b;
    font-weight: 500;
}
.modal-detail-value {
    color: #e2e8f0;
    font-weight: 600;
    font-size: 0.85rem;
    display: block;
}
.modal-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    background: linear-gradient(135deg, #38bdf8, #6366f1);
    color: white;
    padding: 14px 30px;
    border-radius: 14px;
    text-decoration: none;
    font-weight: 700;
    font-size: 0.92rem;
    border: none;
    cursor: pointer;
    transition: all 0.3s ease;
    width: 100%;
    text-align: center;
    font-family: 'Inter', sans-serif;
    letter-spacing: 0.3px;
    position: relative;
    overflow: hidden;
}
.modal-btn::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.15), transparent);
    transition: left 0.5s ease;
}
.modal-btn:hover::before {
    left: 100%;
}
.modal-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 30px rgba(56,189,248,0.35);
}
.modal-btn i { font-size: 1.1rem; }

/* ─── Scroll to top ─── */
.scroll-top {
    position: fixed;
    bottom: 30px;
    right: 30px;
    background: rgba(15, 23, 42, 0.8);
    backdrop-filter: blur(15px);
    color: #38bdf8;
    width: 48px;
    height: 48px;
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    font-size: 1.2rem;
    border: 1px solid rgba(56,189,248,0.2);
    opacity: 0;
    transition: all 0.3s ease;
    z-index: 1000;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}
.scroll-top.visible { opacity: 1; }
.scroll-top:hover {
    transform: translateY(-3px);
    border-color: #38bdf8;
    box-shadow: 0 8px 30px rgba(56,189,248,0.2);
    background: rgba(56,189,248,0.1);
}

@keyframes fadeSlideUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

/* ─── Scrollbar ─── */
.modal-box::-webkit-scrollbar { width: 5px; }
.modal-box::-webkit-scrollbar-track { background: transparent; }
.modal-box::-webkit-scrollbar-thumb {
    background: rgba(56,189,248,0.2);
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ── Data ──
certs = [f"Assets/Cert/Cert{i}.png" for i in range(1, 6)]
names = [
    "Introduction to Advanced Gen AI Tools",
    "Scikit-Learn for Beginners",
    "Basics of Web Scraping with Beautiful Soup for Beginners",
    "Data Structures & Algorithms in Python",
    "Python Django 101"
]
categories = ["Programming", "Web Dev", "Programming", "Cloud", "Design"]
cat_icons = {
    "Programming": "ri-code-s-slash-line",
    "Web Dev": "ri-global-line",
    "Cloud": "ri-cloud-line",
    "Design": "ri-palette-line"
}
dates = ["Jan 2024", "Mar 2024", "May 2024", "Jul 2024", "Sep 2024"]
issuers = ["Coursera", "Udemy", "freeCodeCamp", "AWS", "Google"]
skills = [
    ["Python", "OOP", "Data Types"],
    ["HTML", "CSS", "JavaScript"],
    ["Arrays", "Trees", "Graphs"],
    ["AWS", "Docker", "Kubernetes"],
    ["Figma", "Wireframing", "Prototyping"]
]
descriptions = [
    "Mastered Python from basics to advanced OOP concepts, file handling, and libraries.",
    "Built full-stack web apps using HTML, CSS, JavaScript, and modern frameworks.",
    "Solved complex problems using optimal data structures and algorithmic thinking.",
    "Learned cloud infrastructure, deployment pipelines, and scalable architecture.",
    "Designed user-centered interfaces with research-backed UX principles."
]
progress_vals = [92, 88, 85, 78, 82]

# ── Ambient Glow ──
st.markdown("""
<div class="ambient-glow glow-1"></div>
<div class="ambient-glow glow-2"></div>
""", unsafe_allow_html=True)

# ── Heading ──
st.markdown("""
<div class="typing-wrapper">
    <div class="section-title-container">
        <div class="section-icon"><i class="ri-award-line"></i></div>
        <div class="section-title">My Certifications</div>
    </div>
    <p class="subtitle-text">
        <i class="ri-verified-badge-line"></i>
        Verified achievements that reflect my learning journey
    </p>
    <div class="subtitle-divider"></div>
</div>
""", unsafe_allow_html=True)

# ── Stats ──
st.markdown("""
<div class="stats-bar">
    <div class="stat-item">
        <div class="stat-icon-wrap blue"><i class="ri-award-fill"></i></div>
        <span class="stat-number" id="cnt-certs">0</span>
        <span class="stat-label">Certificates</span>
    </div>
    <div class="stat-item">
        <div class="stat-icon-wrap purple"><i class="ri-building-2-line"></i></div>
        <span class="stat-number" id="cnt-platforms">0</span>
        <span class="stat-label">Platforms</span>
    </div>
    <div class="stat-item">
        <div class="stat-icon-wrap emerald"><i class="ri-lightbulb-flash-line"></i></div>
        <span class="stat-number" id="cnt-skills">0</span>
        <span class="stat-label">Skills Gained</span>
    </div>
    <div class="stat-item">
        <div class="stat-icon-wrap amber"><i class="ri-time-line"></i></div>
        <span class="stat-number" id="cnt-hours">0</span>
        <span class="stat-label">Hours Learned</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Filter Buttons ──
st.markdown("""
<div class="filter-section">
    <button class="filter-btn active" onclick="filterCerts('all', this)">
        <i class="ri-apps-line"></i> All
    </button>
    <button class="filter-btn" onclick="filterCerts('Programming', this)">
        <i class="ri-code-s-slash-line"></i> Programming
    </button>
    <button class="filter-btn" onclick="filterCerts('Web Dev', this)">
        <i class="ri-global-line"></i> Web Dev
    </button>
    <button class="filter-btn" onclick="filterCerts('Cloud', this)">
        <i class="ri-cloud-line"></i> Cloud
    </button>
    <button class="filter-btn" onclick="filterCerts('Design', this)">
        <i class="ri-palette-line"></i> Design
    </button>
</div>
""", unsafe_allow_html=True)

# ── Gallery ──
st.markdown('<div class="cert-gallery" id="certGallery">', unsafe_allow_html=True)

for i, (path, name, cat, date, issuer, skill_list, desc, prog) in enumerate(
    zip(certs, names, categories, dates, issuers, skills, descriptions, progress_vals)
):
    b64 = get_base64_image(path)
    if b64:
        tags_html = "".join(f'<span class="modal-tag">{s}</span>' for s in skill_list)
        skill_chips = "".join(f'<span class="skill-chip">{s}</span>' for s in skill_list[:3])
        cat_icon = cat_icons.get(cat, "ri-bookmark-line")

        st.markdown(f"""
        <div class="cert-item visible" data-category="{cat}"
             onclick="openModal({i})" style="--progress:{prog}%;">
            <span class="cert-badge"><i class="ri-shield-check-line"></i> Verified</span>
            <div class="cert-img-wrapper">
                <img src="{b64}" class="cert-img" alt="{name}" loading="lazy">
                <div class="cert-overlay">
                    <div class="overlay-icon-wrap">
                        <i class="ri-eye-line"></i>
                    </div>
                    <span class="overlay-text">View Details</span>
                </div>
            </div>
            <div class="cert-info">
                <h3>{name}</h3>
                <div class="cert-meta">
                    <div class="cert-meta-left">
                        <span><i class="ri-building-2-line"></i> {issuer}</span>
                        <span><i class="ri-calendar-line"></i> {date}</span>
                    </div>
                    <span class="cert-category-tag">
                        <i class="{cat_icon}"></i> {cat}
                    </span>
                </div>
                <div class="skill-chips">{skill_chips}</div>
                <div class="skill-progress">
                    <div class="progress-label">
                        <span>Proficiency</span>
                        <span>{prog}%</span>
                    </div>
                    <div class="progress-bar-bg">
                        <div class="progress-bar-fill" style="--progress:{prog}%;"></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Modal {i} -->
        <div class="modal-overlay" id="modal{i}" onclick="closeModalOutside(event, {i})">
            <div class="modal-box">
                <button class="modal-close" onclick="closeModal({i})">
                    <i class="ri-close-line"></i>
                </button>
                <img src="{b64}" class="modal-cert-img" alt="{name}">
                <div class="modal-header">
                    <span class="modal-verified">
                        <i class="ri-shield-check-fill"></i> Verified
                    </span>
                </div>
                <div class="modal-title">{name}</div>
                <p class="modal-desc">{desc}</p>
                <div class="modal-tags">{tags_html}</div>
                <div class="modal-detail-grid">
                    <div class="modal-detail-item">
                        <div class="modal-detail-icon blue">
                            <i class="ri-building-2-line"></i>
                        </div>
                        <div>
                            <span class="modal-detail-text">Issuer</span>
                            <span class="modal-detail-value">{issuer}</span>
                        </div>
                    </div>
                    <div class="modal-detail-item">
                        <div class="modal-detail-icon purple">
                            <i class="ri-calendar-event-line"></i>
                        </div>
                        <div>
                            <span class="modal-detail-text">Date</span>
                            <span class="modal-detail-value">{date}</span>
                        </div>
                    </div>
                    <div class="modal-detail-item">
                        <div class="modal-detail-icon emerald">
                            <i class="ri-price-tag-3-line"></i>
                        </div>
                        <div>
                            <span class="modal-detail-text">Category</span>
                            <span class="modal-detail-value">{cat}</span>
                        </div>
                    </div>
                    <div class="modal-detail-item">
                        <div class="modal-detail-icon amber">
                            <i class="ri-bar-chart-fill"></i>
                        </div>
                        <div>
                            <span class="modal-detail-text">Proficiency</span>
                            <span class="modal-detail-value">{prog}%</span>
                        </div>
                    </div>
                </div>
                <button class="modal-btn">
                    <i class="ri-download-2-line"></i>
                    Download Certificate
                </button>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ── Scroll to Top ──
st.markdown("""
<button class="scroll-top" id="scrollTopBtn"
    onclick="window.scrollTo({top:0,behavior:'smooth'})">
    <i class="ri-arrow-up-s-line"></i>
</button>
""", unsafe_allow_html=True)

# ── JavaScript ──
st.markdown("""
<script>
// ── Counter Animation ──
function animateCounter(id, target, suffix) {
    suffix = suffix || '';
    const el = document.getElementById(id);
    if (!el) return;
    let start = 0;
    const duration = 2000;
    const stepTime = 30;
    const steps = duration / stepTime;
    const increment = target / steps;
    const timer = setInterval(() => {
        start += increment;
        if (start >= target) {
            el.textContent = target + suffix;
            clearInterval(timer);
        } else {
            el.textContent = Math.floor(start) + suffix;
        }
    }, stepTime);
}
setTimeout(() => {
    animateCounter('cnt-certs', 5, '');
    animateCounter('cnt-platforms', 4, '');
    animateCounter('cnt-skills', 15, '+');
    animateCounter('cnt-hours', 120, 'h');
}, 3200);

// ── Filter ──
function filterCerts(cat, btn) {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    const cards = document.querySelectorAll('.cert-item');
    cards.forEach((card, idx) => {
        const match = cat === 'all' || card.dataset.category === cat;
        card.style.transition = 'all 0.45s cubic-bezier(0.4, 0, 0.2, 1)';
        if (match) {
            card.style.display = '';
            card.style.opacity = '0';
            card.style.transform = 'translateY(20px) scale(0.95)';
            setTimeout(() => {
                card.style.opacity = '1';
                card.style.transform = 'translateY(0) scale(1)';
            }, 50 + idx * 60);
        } else {
            card.style.opacity = '0';
            card.style.transform = 'scale(0.9)';
            setTimeout(() => { card.style.display = 'none'; }, 400);
        }
    });
}

// ── Modal ──
function openModal(i) {
    const modal = document.getElementById('modal' + i);
    if (modal) {
        modal.classList.add('open');
        document.body.style.overflow = 'hidden';
    }
}
function closeModal(i) {
    const modal = document.getElementById('modal' + i);
    if (modal) {
        modal.classList.remove('open');
        document.body.style.overflow = '';
    }
}
function closeModalOutside(e, i) {
    if (e.target === document.getElementById('modal' + i)) closeModal(i);
}
document.addEventListener('keydown', e => {
    if (e.key === 'Escape') {
        document.querySelectorAll('.modal-overlay.open').forEach(m => {
            m.classList.remove('open');
            document.body.style.overflow = '';
        });
    }
});

// ── Scroll to Top ──
window.addEventListener('scroll', () => {
    const btn = document.getElementById('scrollTopBtn');
    if (btn) btn.classList.toggle('visible', window.scrollY > 300);
});

// ── Progress bars on hover ──
document.querySelectorAll('.cert-item').forEach(card => {
    card.addEventListener('mouseenter', () => {
        card.querySelectorAll('.progress-bar-fill').forEach(bar => {
            const prog = bar.style.getPropertyValue('--progress') ||
                         getComputedStyle(bar).getPropertyValue('--progress');
            bar.style.width = prog;
        });
    });
    card.addEventListener('mouseleave', () => {
        card.querySelectorAll('.progress-bar-fill').forEach(bar => {
            bar.style.width = '0%';
        });
    });
});

// ── Intersection Observer ──
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, { threshold: 0.1 });
document.querySelectorAll('.cert-item').forEach(el => observer.observe(sel));
</script>
""", unsafe_allow_html=True)