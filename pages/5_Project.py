import streamlit as st
from sidebar import inject_plexus_bg, get_base64_image

st.set_page_config(page_title="Projects", layout="wide", initial_sidebar_state="collapsed")
inject_plexus_bg()

# ─────────────────────────────────────────────────────────────
# SVG ICON HELPER - All icons inline, no CDN dependency
# ─────────────────────────────────────────────────────────────
def svg_icon(name: str, size: int = 20) -> str:
    icons = {
        "code-box": '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M8 12l4-4 4 4"/><path d="M12 8v8"/>',
        "rocket": '<path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0"/><path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/>',
        "folder-open": '<path d="M6 14l1-4h10l1 4"/><path d="M20 12H8l-2-6h14a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4"/>',
        "stack": '<path d="m12 2-8.5 5v10L12 22l8.5-5V7z"/><path d="M12 22V12"/><path d="m20.5 7-8.5 5-8.5-5"/><path d="m20.5 12-8.5 5-8.5-5"/>',
        "git-branch": '<line x1="6" y1="3" x2="6" y2="15"/><circle cx="18" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M18 9a9 9 0 0 1-9 9"/>',
        "star": '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>',
        "apps": '<rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/>',
        "robot": '<rect x="3" y="11" width="18" height="10" rx="2"/><circle cx="12" cy="5" r="2"/><path d="M12 7v4"/><line x1="8" y1="16" x2="8" y2="16"/><line x1="16" y1="16" x2="16" y2="16"/>',
        "globe": '<circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
        "pie-chart": '<path d="M21.21 15.89A10 10 0 1 1 8 2.83"/><path d="M22 12A10 10 0 0 0 12 2v10z"/>',
        "book-open": '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>',
        "check": '<polyline points="20 6 9 17 4 12"/>',
        "time": '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
        "git-commit": '<circle cx="12" cy="12" r="4"/><line x1="1.05" y1="12" x2="7" y2="12"/><line x1="17.01" y1="12" x2="22.96" y2="12"/>',
        "eye": '<path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/>',
        "close": '<line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>',
        "tag": '<path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/>',
        "bar-chart": '<line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/>',
        "calendar": '<rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/>',
        "arrow-up": '<line x1="12" y1="19" x2="12" y2="5"/><polyline points="5 12 12 5 19 12"/>',
        "github": '<path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/>',
        "check-double": '<polyline points="18 6 9 17 4 12"/><polyline points="22 6 13 17"/>',
    }
    path = icons.get(name, icons["code-box"])
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{path}</svg>'

st.markdown("""
<style>
/* Show sidebar toggle button */
[data-testid="stSidebarCollapsedControl"] { visibility: visible !important; }
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

* { box-sizing: border-box; margin: 0; padding: 0; }

footer { visibility: hidden; }
.block-container { padding-top: 2rem; padding-bottom: 2rem; }

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
    color: white;
    box-shadow: 0 8px 25px rgba(56,189,248,0.3);
    flex-shrink: 0;
}
.section-icon svg { width: 24px; height: 24px; }
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
@keyframes typing { from { width: 0; } to { width: 100%; } }
@keyframes blink { 50% { border-color: transparent; } }

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
.subtitle-text svg { width: 18px; height: 18px; color: #38bdf8; }
.subtitle-divider {
    width: 60px; height: 3px;
    background: linear-gradient(90deg, #38bdf8, #6366f1);
    border-radius: 3px; margin: 16px auto 0;
    opacity: 0; animation: fadeSlideUp 0.8s ease 2.7s forwards;
}

.stats-bar {
    display: grid; grid-template-columns: repeat(4, 1fr); gap: 0;
    margin-bottom: 40px;
    background: rgba(15, 23, 42, 0.6);
    border-radius: 20px;
    border: 1px solid rgba(56,189,248,0.08);
    max-width: 780px; margin: 0 auto 40px;
    opacity: 0; animation: fadeSlideUp 0.8s ease 3s forwards;
    overflow: hidden; backdrop-filter: blur(20px);
    box-shadow: 0 4px 30px rgba(0,0,0,0.2);
}
.stat-item {
    text-align: center; color: #f8fafc; padding: 24px 16px; position: relative; transition: all 0.3s ease;
}
.stat-item:not(:last-child)::after {
    content: ''; position: absolute; right: 0; top: 20%; height: 60%; width: 1px;
    background: rgba(56,189,248,0.1);
}
.stat-item:hover { background: rgba(56,189,248,0.04); }
.stat-icon-wrap {
    width: 40px; height: 40px; border-radius: 12px;
    display: flex; align-items: center; justify-content: center;
    margin: 0 auto 10px;
}
.stat-icon-wrap svg { width: 20px; height: 20px; }
.stat-icon-wrap.blue { background: rgba(56,189,248,0.12); color: #38bdf8; }
.stat-icon-wrap.purple { background: rgba(99,102,241,0.12); color: #818cf8; }
.stat-icon-wrap.emerald { background: rgba(52,211,153,0.12); color: #34d399; }
.stat-icon-wrap.amber { background: rgba(251,191,36,0.12); color: #fbbf24; }
.stat-number {
    font-size: clamp(1.5rem, 4vw, 2rem); font-weight: 800; color: #f1f5f9;
    display: block; font-family: 'Inter', sans-serif; letter-spacing: -0.03em;
}
.stat-label {
    font-size: clamp(0.65rem, 1.5vw, 0.78rem); color: #64748b;
    font-family: 'Inter', sans-serif; font-weight: 500;
    text-transform: uppercase; letter-spacing: 0.5px; margin-top: 2px;
}

.filter-section {
    display: flex; justify-content: center; flex-wrap: wrap; gap: 8px;
    margin-bottom: 40px; padding: 0 15px;
    opacity: 0; animation: fadeSlideUp 0.8s ease 3.2s forwards;
}
.filter-btn {
    padding: 10px 22px; border-radius: 12px;
    border: 1px solid rgba(56,189,248,0.12);
    background: rgba(15, 23, 42, 0.6);
    color: #94a3b8; cursor: pointer;
    font-size: clamp(0.78rem, 2vw, 0.88rem);
    font-family: 'Inter', sans-serif; font-weight: 500;
    transition: all 0.3s ease; white-space: nowrap;
    display: inline-flex; align-items: center; gap: 6px;
    backdrop-filter: blur(10px);
}
.filter-btn svg { width: 16px; height: 16px; opacity: 0.7; }
.filter-btn:hover {
    background: rgba(56,189,248,0.08); border-color: rgba(56,189,248,0.25);
    color: #cbd5e1; transform: translateY(-2px);
}
.filter-btn.active {
    background: linear-gradient(135deg, rgba(56,189,248,0.15), rgba(99,102,241,0.15));
    border-color: rgba(56,189,248,0.4); color: #38bdf8;
    box-shadow: 0 4px 20px rgba(56,189,248,0.15);
}
.filter-btn.active svg { opacity: 1; }

.project-gallery {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: clamp(18px, 3vw, 28px); padding: 10px 15px 50px;
    max-width: 1200px; margin: 0 auto;
}

.project-item {
    background: rgba(15, 23, 42, 0.7); border-radius: 20px; overflow: hidden;
    border: 1px solid rgba(56,189,248,0.08);
    transition: all 0.45s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    cursor: pointer; position: relative;
    backdrop-filter: blur(20px);
    animation: cardAppear 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
}
.project-item:nth-child(1) { animation-delay: 0.1s; opacity: 0; }
.project-item:nth-child(2) { animation-delay: 0.2s; opacity: 0; }
.project-item:nth-child(3) { animation-delay: 0.3s; opacity: 0; }
.project-item:nth-child(4) { animation-delay: 0.4s; opacity: 0; }
.project-item:nth-child(5) { animation-delay: 0.5s; opacity: 0; }

@keyframes cardAppear { 
    from { opacity: 0; transform: translateY(40px); }
    to { opacity: 1; transform: translateY(0); } 
}

.project-item:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 50px rgba(0,0,0,0.3), 0 0 0 1px rgba(56,189,248,0.2), 0 0 60px rgba(56,189,248,0.08);
    border-color: rgba(56,189,248,0.2);
}

.project-img-wrapper { position: relative; overflow: hidden; height: clamp(170px, 22vw, 210px); }
.project-img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.6s ease, filter 0.4s ease; }
.project-item:hover .project-img { transform: scale(1.06); filter: brightness(0.7); }

.project-overlay {
    position: absolute; inset: 0;
    background: linear-gradient(135deg, rgba(56,189,248,0.8) 0%, rgba(99,102,241,0.8) 100%);
    display: flex; align-items: center; justify-content: center;
    opacity: 0; transition: opacity 0.4s ease; flex-direction: column; gap: 10px;
}
.project-item:hover .project-overlay { opacity: 1; }
.overlay-icon-wrap {
    width: 56px; height: 56px; background: rgba(255,255,255,0.2); border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.3);
}
.overlay-icon-wrap svg { width: 24px; height: 24px; color: white; }
.overlay-text {
    color: white; font-size: clamp(0.7rem, 2vw, 0.82rem); font-weight: 600;
    font-family: 'Inter', sans-serif; letter-spacing: 2px; text-transform: uppercase;
}

.project-badge {
    position: absolute; top: 14px; right: 14px;
    background: rgba(15, 23, 42, 0.8); backdrop-filter: blur(10px);
    color: #34d399; font-size: 0.68rem; font-weight: 700;
    padding: 5px 12px; border-radius: 8px;
    font-family: 'Inter', sans-serif; letter-spacing: 0.5px;
    text-transform: uppercase; border: 1px solid rgba(52,211,153,0.2);
    z-index: 2; display: flex; align-items: center; gap: 4px;
}
.project-badge svg { width: 14px; height: 14px; }

.project-info { padding: clamp(16px, 3vw, 22px); color: #f8fafc; font-family: 'Inter', sans-serif; }
.project-info h3 {
    margin: 0 0 10px; font-size: clamp(0.95rem, 2.5vw, 1.12rem);
    font-weight: 700; line-height: 1.35; letter-spacing: -0.02em; color: #f1f5f9;
}
.project-meta {
    display: flex; justify-content: space-between; align-items: center;
    flex-wrap: wrap; gap: 8px; margin-bottom: 12px;
}
.project-meta-left {
    display: flex; align-items: center; gap: 12px;
    color: #64748b; font-size: clamp(0.72rem, 1.8vw, 0.82rem); font-weight: 500;
}
.project-meta-left span { display: inline-flex; align-items: center; gap: 5px; }
.project-meta-left svg { width: 14px; height: 14px; color: #475569; }

.project-category-tag {
    display: inline-flex; align-items: center; gap: 4px;
    background: rgba(56,189,248,0.08); color: #38bdf8;
    border: 1px solid rgba(56,189,248,0.15); border-radius: 8px;
    padding: 3px 10px; font-size: 0.7rem; font-weight: 600;
    font-family: 'Inter', sans-serif; letter-spacing: 0.3px;
}
.project-category-tag svg { width: 12px; height: 12px; }

.skill-chips { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 14px; }
.skill-chip {
    background: rgba(99,102,241,0.08); color: #a5b4fc;
    border: 1px solid rgba(99,102,241,0.12); border-radius: 6px;
    padding: 3px 9px; font-size: 0.68rem; font-weight: 600;
    font-family: 'Inter', sans-serif;
}

.skill-progress { margin-top: 4px; }
.progress-label {
    display: flex; justify-content: space-between; color: #64748b;
    font-size: 0.72rem; margin-bottom: 6px; font-weight: 500;
}
.progress-bar-bg {
    background: rgba(255,255,255,0.06); border-radius: 10px; height: 5px; overflow: hidden;
}
.progress-bar-fill {
    height: 100%; border-radius: 10px;
    background: linear-gradient(90deg, #38bdf8, #6366f1, #a78bfa);
    width: 0%;
    transition: width 1.2s cubic-bezier(0.4, 0, 0.2, 1);
}

/* ─── MODAL - Fixed for Streamlit ─── */
.modal-overlay {
    display: none;
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    width: 100vw; height: 100vh;
    background: rgba(0, 0, 0, 0.88);
    z-index: 999999;
    justify-content: center;
    align-items: center;
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    padding: 20px;
}
.modal-overlay.open {
    display: flex !important;
    animation: fadeIn 0.3s ease;
}

.modal-box {
    background: linear-gradient(160deg, rgba(15,23,42,0.99), rgba(30,41,59,0.97));
    border: 1px solid rgba(56,189,248,0.2);
    border-radius: 24px;
    padding: clamp(20px, 4vw, 32px);
    max-width: 680px; width: 100%;
    position: relative;
    animation: modalSlideIn 0.45s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    font-family: 'Inter', sans-serif;
    box-shadow: 0 30px 80px rgba(0,0,0,0.7), 0 0 100px rgba(56,189,248,0.1);
    max-height: 90vh;
    overflow-y: auto;
    z-index: 1000000;
}

@keyframes modalSlideIn {
    from { transform: scale(0.85) translateY(40px); opacity: 0; }
    to { transform: scale(1) translateY(0); opacity: 1; }
}

.modal-close {
    position: absolute;
    top: 16px;
    right: 18px;
    background: rgba(239,68,68,0.12);
    border: 1px solid rgba(239,68,68,0.2);
    color: #f87171;
    width: 38px; height: 38px;
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    cursor: pointer;
    transition: all 0.3s ease;
    z-index: 10;
    flex-shrink: 0;
}
.modal-close svg { width: 18px; height: 18px; }
.modal-close:hover {
    background: rgba(239,68,68,0.25);
    border-color: rgba(239,68,68,0.5);
    color: white;
    transform: rotate(90deg) scale(1.1);
}

.modal-img-container {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 22px;
    background: rgba(0,0,0,0.25);
    border-radius: 16px;
    padding: 14px;
    border: 1px solid rgba(56,189,248,0.12);
    overflow: hidden;
}
.modal-project-img {
    max-width: 100%;
    max-height: 38vh;
    width: auto;
    height: auto;
    object-fit: contain;
    border-radius: 10px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.4);
    display: block;
}

.modal-header { display: flex; align-items: center; gap: 10px; margin-bottom: 10px; }
.modal-verified {
    display: inline-flex; align-items: center; gap: 5px; color: #34d399;
    font-size: 0.72rem; font-weight: 700;
    background: rgba(52,211,153,0.1);
    padding: 4px 12px; border-radius: 8px;
    border: 1px solid rgba(52,211,153,0.2);
}
.modal-verified svg { width: 14px; height: 14px; }

.modal-title {
    color: #f1f5f9;
    font-size: clamp(1.25rem, 3vw, 1.6rem);
    font-weight: 800;
    margin-bottom: 14px;
    letter-spacing: -0.03em;
    line-height: 1.3;
}

.modal-desc {
    color: #cbd5e1;
    font-size: clamp(0.88rem, 2vw, 0.98rem);
    line-height: 1.85;
    margin-bottom: 22px;
    font-weight: 400;
}

.modal-tags { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 20px; }
.modal-tag {
    background: rgba(56,189,248,0.08); color: #38bdf8;
    border: 1px solid rgba(56,189,248,0.18); border-radius: 8px;
    padding: 5px 14px; font-size: 0.78rem; font-weight: 600;
    display: inline-flex; align-items: center; gap: 5px;
}
.modal-tag svg { width: 14px; height: 14px; opacity: 0.8; }

.modal-detail-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 24px; }
.modal-detail-item {
    background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.06);
    border-radius: 12px; padding: 12px 14px; display: flex; align-items: center; gap: 10px;
}
.modal-detail-icon {
    width: 34px; height: 34px; border-radius: 9px;
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0;
}
.modal-detail-icon svg { width: 16px; height: 16px; }
.modal-detail-icon.blue { background: rgba(56,189,248,0.12); color: #38bdf8; }
.modal-detail-icon.purple { background: rgba(99,102,241,0.12); color: #818cf8; }
.modal-detail-icon.emerald { background: rgba(52,211,153,0.12); color: #34d399; }
.modal-detail-icon.amber { background: rgba(251,191,36,0.12); color: #fbbf24; }
.modal-detail-text { font-size: 0.75rem; color: #64748b; font-weight: 500; }
.modal-detail-value { color: #e2e8f0; font-weight: 700; font-size: 0.85rem; display: block; margin-top: 2px; }

.modal-btn {
    display: flex; align-items: center; justify-content: center; gap: 10px;
    background: linear-gradient(135deg, #38bdf8, #6366f1);
    color: white; padding: 14px 30px; border-radius: 14px;
    text-decoration: none; font-weight: 700; font-size: 0.95rem;
    border: none; cursor: pointer; transition: all 0.3s ease;
    width: 100%; font-family: 'Inter', sans-serif; letter-spacing: 0.3px;
}
.modal-btn svg { width: 18px; height: 18px; }
.modal-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 35px rgba(56,189,248,0.4);
    filter: brightness(1.1);
}

.ambient-glow {
    position: fixed; border-radius: 50%; pointer-events: none;
    filter: blur(80px); z-index: 0; opacity: 0.04;
}
.glow-1 { width: 400px; height: 400px; background: #38bdf8; top: 10%; left: -5%; animation: floatGlow 15s ease-in-out infinite; }
.glow-2 { width: 350px; height: 350px; background: #6366f1; bottom: 10%; right: -5%; animation: floatGlow 18s ease-in-out infinite reverse; }
@keyframes floatGlow {
    0%, 100% { transform: translate(0, 0); }
    33% { transform: translate(30px, -20px); }
    66% { transform: translate(-20px, 30px); }
}

.scroll-top {
    position: fixed; bottom: 30px; right: 30px;
    background: rgba(15, 23, 42, 0.85); backdrop-filter: blur(15px);
    color: #38bdf8; width: 48px; height: 48px; border-radius: 14px;
    display: flex; align-items: center; justify-content: center; cursor: pointer;
    border: 1px solid rgba(56,189,248,0.2);
    opacity: 0; transition: all 0.3s ease; z-index: 1000;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}
.scroll-top svg { width: 20px; height: 20px; }
.scroll-top.visible { opacity: 1; }
.scroll-top:hover { transform: translateY(-3px); border-color: #38bdf8; }

@keyframes fadeSlideUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

.modal-box::-webkit-scrollbar { width: 5px; }
.modal-box::-webkit-scrollbar-track { background: transparent; }
.modal-box::-webkit-scrollbar-thumb { background: linear-gradient(180deg, #38bdf8, #6366f1); border-radius: 10px; }

@media (max-width: 600px) {
    .modal-box { padding: 16px; }
    .modal-detail-grid { grid-template-columns: 1fr; }
    .modal-project-img { max-height: 30vh; }
    .stats-bar { grid-template-columns: repeat(2, 1fr); }
}
</style>
""", unsafe_allow_html=True)

# ── Data ──
projects = [f"Assets/Projects/P{i}.png" for i in range(1, 6)]
data = [
    {
        "name": "TaskFlow",
        "desc": "NLP-powered conversational agent with context memory and real-time responses. Built using transformer models for intent recognition and response generation. Features include multi-turn conversation handling, sentiment analysis, and integration with external APIs for dynamic content retrieval. The system was trained on custom datasets and optimized for low-latency inference.",
        "tags": ["Python", "Transformers", "Streamlit"],
        "complexity": 95,
        "category": "AI/ML"
    },
    {
        "name": "ContactMS",
        "desc": "Full-stack CRUD application with role-based access control and reporting. Supports student enrollment, grade management, attendance tracking, and automated report generation. Includes admin dashboard, teacher portal, and student view with real-time notifications. Database optimized for quick queries and data integrity.",
        "tags": ["Flask", "SQL", "HTML/CSS"],
        "complexity": 85,
        "category": "Web App"
    },
    {
        "name": "CALCULATOR",
        "desc": "Interactive analytics dashboard for real-time datasets with dynamic filtering. Features customizable charts, drill-down capabilities, and export functionality. Supports multiple data sources including CSV, JSON, and live API feeds. Built with responsive design principles for seamless viewing across all devices.",
        "tags": ["Pandas", "Plotly", "REST API"],
        "complexity": 88,
        "category": "Data"
    },
    {
        "name": "MyAPP",
        "desc": "Responsive shopping platform with cart, checkout flow, and payment simulation. Includes product catalog with search and filters, user authentication, order history, and admin inventory management. Implements secure session handling and mock payment gateway integration for testing purposes.",
        "tags": ["JavaScript", "React", "Firebase"],
        "complexity": 90,
        "category": "Web App"
    },
    {
        "name": "ExpenseTrack",
        "desc": "Step-by-step sorting and pathfinding animation tool built for educational purposes. Visualizes algorithms like QuickSort, MergeSort, Dijkstra, and A* with adjustable speed controls. Features interactive graph editing, algorithm comparison mode, and educational tooltips explaining each step of the process in detail.",
        "tags": ["Python", "Canvas API", "UX"],
        "complexity": 80,
        "category": "Education"
    }
]

# ── Ambient Glow ──
st.markdown("""
<div class="ambient-glow glow-1"></div>
<div class="ambient-glow glow-2"></div>
""", unsafe_allow_html=True)

# ── Heading ──
st.markdown(f"""
<div class="typing-wrapper">
    <div class="section-title-container">
        <div class="section-icon">{svg_icon("code-box", 24)}</div>
        <div class="section-title">Featured Projects</div>
    </div>
    <p class="subtitle-text">
        {svg_icon("rocket", 18)}
        Innovative solutions built with modern technologies
    </p>
    <div class="subtitle-divider"></div>
</div>
""", unsafe_allow_html=True)

# ── Stats ──
st.markdown(f"""
<div class="stats-bar">
    <div class="stat-item">
        <div class="stat-icon-wrap blue">{svg_icon("folder-open", 20)}</div>
        <span class="stat-number" id="cnt-projects">0</span>
        <span class="stat-label">Projects</span>
    </div>
    <div class="stat-item">
        <div class="stat-icon-wrap purple">{svg_icon("stack", 20)}</div>
        <span class="stat-number" id="cnt-tech">0</span>
        <span class="stat-label">Technologies</span>
    </div>
    <div class="stat-item">
        <div class="stat-icon-wrap emerald">{svg_icon("git-branch", 20)}</div>
        <span class="stat-number" id="cnt-commits">0</span>
        <span class="stat-label">Commits</span>
    </div>
    <div class="stat-item">
        <div class="stat-icon-wrap amber">{svg_icon("star", 20)}</div>
        <span class="stat-number" id="cnt-stars">0</span>
        <span class="stat-label">GitHub Stars</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Filter Buttons ──
st.markdown(f"""
<div class="filter-section">
    <button class="filter-btn active" onclick="filterProjects('all', this)">
        {svg_icon("apps", 16)} All
    </button>
    <button class="filter-btn" onclick="filterProjects('AI/ML', this)">
        {svg_icon("robot", 16)} AI/ML
    </button>
    <button class="filter-btn" onclick="filterProjects('Web App', this)">
        {svg_icon("globe", 16)} Web App
    </button>
    <button class="filter-btn" onclick="filterProjects('Data', this)">
        {svg_icon("pie-chart", 16)} Data
    </button>
    <button class="filter-btn" onclick="filterProjects('Education', this)">
        {svg_icon("book-open", 16)} Education
    </button>
</div>
""", unsafe_allow_html=True)

# ── Gallery + Modals ──
st.markdown('<div class="project-gallery" id="projectGallery">', unsafe_allow_html=True)

cat_icons = {
    "AI/ML": "robot",
    "Web App": "globe", 
    "Data": "pie-chart",
    "Education": "book-open"
}

for i, (path, d) in enumerate(zip(projects, data)):
    b64 = get_base64_image(path)
    if b64:
        tags_html = "".join(
            f'<span class="modal-tag">{svg_icon("tag", 14)}{t}</span>'
            for t in d['tags']
        )
        skill_chips = "".join(
            f'<span class="skill-chip">{t}</span>'
            for t in d['tags'][:3]
        )
        complexity = d.get('complexity', 85)
        category = d.get('category', 'General')
        cat_icon = cat_icons.get(category, "code-box")

        st.markdown(f"""
        <!-- Project Card -->
        <div class="project-item" data-category="{category}" data-index="{i}"
             onclick="openModal({i})" style="--progress:{complexity}%;">
            <span class="project-badge">{svg_icon("check", 14)} Completed</span>
            <div class="project-img-wrapper">
                <img src="{b64}" class="project-img" alt="{d['name']}" loading="lazy">
                <div class="project-overlay">
                    <div class="overlay-icon-wrap">
                        {svg_icon("eye", 24)}
                    </div>
                    <span class="overlay-text">View Details</span>
                </div>
            </div>
            <div class="project-info">
                <h3>{d['name']}</h3>
                <div class="project-meta">
                    <div class="project-meta-left">
                        <span>{svg_icon("time", 14)} 2024</span>
                        <span>{svg_icon("git-commit", 14)} Active</span>
                    </div>
                    <span class="project-category-tag">
                        {svg_icon(cat_icon, 12)} {category}
                    </span>
                </div>
                <div class="skill-chips">{skill_chips}</div>
                <div class="skill-progress">
                    <div class="progress-label">
                        <span>Complexity</span>
                        <span>{complexity}%</span>
                    </div>
                    <div class="progress-bar-bg">
                        <div class="progress-bar-fill" id="bar-{i}" style="width:0%;"></div>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ── Modals (rendered OUTSIDE the gallery grid) ──
for i, (path, d) in enumerate(zip(projects, data)):
    b64 = get_base64_image(path)
    if b64:
        tags_html = "".join(
            f'<span class="modal-tag">{svg_icon("tag", 14)}{t}</span>'
            for t in d['tags']
        )
        complexity = d.get('complexity', 85)
        category = d.get('category', 'General')

        st.markdown(f"""
        <div class="modal-overlay" id="modal{i}">
            <div class="modal-box" id="modal-box-{i}" onclick="event.stopPropagation()">
                <button class="modal-close" onclick="closeModal({i})">
                    {svg_icon("close", 18)}
                </button>

                <div class="modal-img-container">
                    <img src="{b64}" class="modal-project-img" alt="{d['name']}">
                </div>

                <div class="modal-header">
                    <span class="modal-verified">
                        {svg_icon("check-double", 14)} Production Ready
                    </span>
                </div>

                <div class="modal-title">{d['name']}</div>

                <p class="modal-desc">{d['desc']}</p>

                <div class="modal-tags">{tags_html}</div>

                <div class="modal-detail-grid">
                    <div class="modal-detail-item">
                        <div class="modal-detail-icon blue">{svg_icon("git-branch", 16)}</div>
                        <div>
                            <span class="modal-detail-text">Status</span>
                            <span class="modal-detail-value">Completed</span>
                        </div>
                    </div>
                    <div class="modal-detail-item">
                        <div class="modal-detail-icon purple">{svg_icon("calendar", 16)}</div>
                        <div>
                            <span class="modal-detail-text">Year</span>
                            <span class="modal-detail-value">2024</span>
                        </div>
                    </div>
                    <div class="modal-detail-item">
                        <div class="modal-detail-icon emerald">{svg_icon("tag", 16)}</div>
                        <div>
                            <span class="modal-detail-text">Category</span>
                            <span class="modal-detail-value">{category}</span>
                        </div>
                    </div>
                    <div class="modal-detail-item">
                        <div class="modal-detail-icon amber">{svg_icon("bar-chart", 16)}</div>
                        <div>
                            <span class="modal-detail-text">Complexity</span>
                            <span class="modal-detail-value">{complexity}%</span>
                        </div>
                    </div>
                </div>

                <button class="modal-btn" onclick="window.open('https://github.com', '_blank')">
                    {svg_icon("github", 18)}
                    View Source Code
                </button>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ── Scroll to Top ──
st.markdown(f"""
<button class="scroll-top" id="scrollTopBtn"
    onclick="window.scrollTo({{top:0,behavior:'smooth'}})">
    {svg_icon("arrow-up", 20)}
</button>
""", unsafe_allow_html=True)

# ── JavaScript ──
st.markdown("""
<script>
(function() {

    // ── Counter Animation ──
    function animateCounter(id, target, suffix) {
        suffix = suffix || '';
        const el = document.getElementById(id);
        if (!el) return;
        let start = 0;
        const steps = 60;
        const increment = target / steps;
        let count = 0;
        const timer = setInterval(function() {
            count++;
            start += increment;
            if (count >= steps) {
                el.textContent = target + suffix;
                clearInterval(timer);
            } else {
                el.textContent = Math.floor(start) + suffix;
            }
        }, 35);
    }

    setTimeout(function() {
        animateCounter('cnt-projects', 5, '+');
        animateCounter('cnt-tech', 12, '+');
        animateCounter('cnt-commits', 350, '+');
        animateCounter('cnt-stars', 89, '');
    }, 3300);

    // ── Modal Functions ──
    window.openModal = function(i) {
        const modal = document.getElementById('modal' + i);
        if (!modal) {
            console.warn('Modal not found:', i);
            return;
        }
        // Close any open modals first
        document.querySelectorAll('.modal-overlay.open').forEach(function(m) {
            m.classList.remove('open');
        });
        // Force display then add class for animation
        modal.style.display = 'flex';
        setTimeout(function() {
            modal.classList.add('open');
        }, 10);
        document.body.style.overflow = 'hidden';
        
        // Close on overlay click
        modal.onclick = function(e) {
            if (e.target === modal) {
                closeModal(i);
            }
        };
    };

    window.closeModal = function(i) {
        const modal = document.getElementById('modal' + i);
        if (modal) {
            modal.classList.remove('open');
            setTimeout(function() {
                modal.style.display = 'none';
            }, 300);
            document.body.style.overflow = '';
        }
    };

    // ── ESC key to close ──
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            document.querySelectorAll('.modal-overlay.open').forEach(function(m) {
                m.classList.remove('open');
                setTimeout(function() {
                    m.style.display = 'none';
                }, 300);
            });
            document.body.style.overflow = '';
        }
    });

    // ── Filter ──
    window.filterProjects = function(cat, btn) {
        document.querySelectorAll('.filter-btn').forEach(function(b) {
            b.classList.remove('active');
        });
        btn.classList.add('active');

        const cards = document.querySelectorAll('.project-item');
        cards.forEach(function(card, idx) {
            const match = cat === 'all' || card.dataset.category === cat;
            if (match) {
                card.style.display = '';
                card.style.opacity = '0';
                card.style.transform = 'translateY(20px)';
                setTimeout(function() {
                    card.style.transition = 'all 0.4s ease';
                    card.style.opacity = '1';
                    card.style.transform = 'translateY(0)';
                }, 60 + idx * 70);
            } else {
                card.style.transition = 'all 0.3s ease';
                card.style.opacity = '0';
                card.style.transform = 'scale(0.9)';
                setTimeout(function() {
                    card.style.display = 'none';
                }, 320);
            }
        });
    };

    // ── Progress Bars on Hover ──
    function setupProgressBars() {
        document.querySelectorAll('.project-item').forEach(function(card) {
            const idx = card.dataset.index;
            const bar = document.getElementById('bar-' + idx);
            if (!bar) return;

            const progress = card.style.getPropertyValue('--progress') || '85%';

            card.addEventListener('mouseenter', function() {
                if (bar) bar.style.width = progress;
            });
            card.addEventListener('mouseleave', function() {
                if (bar) bar.style.width = '0%';
            });
        });
    }
    setupProgressBars();

    // ── Scroll to Top ──
    window.addEventListener('scroll', function() {
        const btn = document.getElementById('scrollTopBtn');
        if (btn) {
            if (window.scrollY > 300) {
                btn.classList.add('visible');
            } else {
                btn.classList.remove('visible');
            }
        }
    });

    // ── Intersection Observer for Cards ──
    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.08 });

        document.querySelectorAll('.project-item').forEach(function(el) {
            observer.observe(el);
        });
    }

    console.log('Projects page JS loaded. Modals ready.');

})();
</script>
""", unsafe_allow_html=True)