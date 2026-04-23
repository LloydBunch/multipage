import streamlit as st
from sidebar import inject_plexus_bg

st.set_page_config(page_title="Contact Me", layout="wide", initial_sidebar_state="collapsed")
inject_plexus_bg()

st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<style>
/* Show sidebar toggle button */
button[kind="secondary"] { visibility: visible !important; }

<style>
    /* ===== GLOBAL RESET ===== */
    * { box-sizing: border-box; margin: 0; padding: 0; }

    .stApp {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
    }

    [data-testid="stForm"] {
        border: none !important;
        padding: 0 !important;
        background: transparent !important;
    }

    /* ===== MAIN CONTAINER ===== */
    .contact-master-wrap {
        max-width: 1200px;
        margin: 0 auto;
        padding: 10px 20px 80px;
        animation: masterFadeIn 0.9s cubic-bezier(0.16, 1, 0.3, 1);
    }

    @keyframes masterFadeIn {
        from { opacity: 0; transform: translateY(40px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* ===== HEADER ===== */
    .contact-hero {
        text-align: center;
        margin-bottom: 56px;
        position: relative;
        padding-top: 10px;
    }

    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        background: linear-gradient(135deg, rgba(56,189,248,0.08), rgba(129,140,248,0.08));
        border: 1px solid rgba(56, 189, 248, 0.2);
        padding: 10px 24px;
        border-radius: 50px;
        color: #38bdf8;
        font-size: 0.8rem;
        font-weight: 600;
        margin-bottom: 24px;
        letter-spacing: 1.2px;
        text-transform: uppercase;
        backdrop-filter: blur(10px);
    }

    .hero-badge i { font-size: 0.7rem; }

    .contact-hero h1 {
        color: #f1f5f9;
        font-size: clamp(2.2rem, 5.5vw, 3.2rem);
        font-weight: 800;
        margin: 0 0 18px;
        line-height: 1.1;
        letter-spacing: -0.04em;
    }

    .hero-gradient {
        background: linear-gradient(135deg, #38bdf8 0%, #818cf8 40%, #c084fc 80%, #f472b6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .contact-hero .hero-desc {
        color: #94a3b8;
        font-size: clamp(0.95rem, 2.2vw, 1.1rem);
        max-width: 580px;
        margin: 0 auto;
        line-height: 1.75;
        font-weight: 400;
    }

    .hero-line {
        width: 70px;
        height: 3px;
        background: linear-gradient(90deg, #38bdf8, #818cf8, #c084fc);
        margin: 28px auto 0;
        border-radius: 3px;
    }

    /* ===== TWO-COLUMN LAYOUT ===== */
    .contact-grid-main {
        display: grid;
        grid-template-columns: 1fr 1.5fr;
        gap: 28px;
        align-items: start;
    }

    /* ===== LEFT PANEL ===== */
    .left-panel { display: flex; flex-direction: column; gap: 16px; }

    /* Info Cards */
    .c-info-card {
        background: rgba(15, 23, 42, 0.55);
        backdrop-filter: blur(24px);
        -webkit-backdrop-filter: blur(24px);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 16px;
        padding: 22px 20px;
        display: flex;
        align-items: center;
        gap: 16px;
        transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        position: relative;
        overflow: hidden;
        cursor: default;
    }

    .c-info-card::after {
        content: '';
        position: absolute;
        inset: 0;
        border-radius: 16px;
        padding: 1px;
        background: linear-gradient(135deg, transparent 40%, rgba(56,189,248,0.2) 100%);
        -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        -webkit-mask-composite: xor;
        mask-composite: exclude;
        opacity: 0;
        transition: opacity 0.4s ease;
        pointer-events: none;
    }

    .c-info-card:hover {
        transform: translateY(-3px) scale(1.01);
        border-color: rgba(56, 189, 248, 0.15);
        box-shadow: 0 16px 48px rgba(0, 0, 0, 0.25),
                    0 4px 16px rgba(56, 189, 248, 0.06);
    }

    .c-info-card:hover::after { opacity: 1; }

    .c-icon-wrap {
        width: 50px;
        height: 50px;
        min-width: 50px;
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.1rem;
        transition: all 0.35s ease;
        position: relative;
    }

    .c-icon-wrap.ic-email {
        background: linear-gradient(135deg, rgba(56,189,248,0.1), rgba(56,189,248,0.18));
        color: #38bdf8;
        border: 1px solid rgba(56,189,248,0.15);
    }
    .c-icon-wrap.ic-phone {
        background: linear-gradient(135deg, rgba(52,211,153,0.1), rgba(52,211,153,0.18));
        color: #34d399;
        border: 1px solid rgba(52,211,153,0.15);
    }
    .c-icon-wrap.ic-location {
        background: linear-gradient(135deg, rgba(251,146,60,0.1), rgba(251,146,60,0.18));
        color: #fb923c;
        border: 1px solid rgba(251,146,60,0.15);
    }
    .c-icon-wrap.ic-clock {
        background: linear-gradient(135deg, rgba(192,132,252,0.1), rgba(192,132,252,0.18));
        color: #c084fc;
        border: 1px solid rgba(192,132,252,0.15);
    }

    .c-info-card:hover .ic-email { box-shadow: 0 0 20px rgba(56,189,248,0.15); }
    .c-info-card:hover .ic-phone { box-shadow: 0 0 20px rgba(52,211,153,0.15); }
    .c-info-card:hover .ic-location { box-shadow: 0 0 20px rgba(251,146,60,0.15); }
    .c-info-card:hover .ic-clock { box-shadow: 0 0 20px rgba(192,132,252,0.15); }

    .c-info-text h4 {
        color: #94a3b8;
        font-size: 0.7rem;
        font-weight: 700;
        margin: 0 0 4px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .c-info-text p {
        color: #e2e8f0;
        font-size: 0.92rem;
        margin: 0;
        line-height: 1.4;
        font-weight: 500;
    }

    .c-info-text a {
        color: #e2e8f0;
        text-decoration: none;
        transition: color 0.25s ease;
    }
    .c-info-text a:hover { color: #38bdf8; }

    /* Social Card */
    .social-panel {
        background: rgba(15, 23, 42, 0.55);
        backdrop-filter: blur(24px);
        -webkit-backdrop-filter: blur(24px);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 16px;
        padding: 22px 20px;
    }

    .social-panel h4 {
        color: #94a3b8;
        font-size: 0.72rem;
        font-weight: 700;
        margin: 0 0 16px;
        text-transform: uppercase;
        letter-spacing: 1px;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .social-panel h4 i { color: #64748b; font-size: 0.8rem; }

    .social-row {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 10px;
    }

    .soc-btn {
        display: flex;
        align-items: center;
        justify-content: center;
        aspect-ratio: 1;
        border-radius: 12px;
        background: rgba(30, 41, 59, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.05);
        color: #64748b;
        font-size: 1.15rem;
        text-decoration: none;
        transition: all 0.35s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }

    .soc-btn:hover { transform: translateY(-4px) scale(1.05); color: #f1f5f9; }

    .soc-btn.gh:hover {
        background: rgba(255,255,255,0.08);
        border-color: rgba(255,255,255,0.15);
        box-shadow: 0 8px 28px rgba(255,255,255,0.05);
    }
    .soc-btn.li:hover {
        background: rgba(10,102,194,0.12);
        border-color: rgba(10,102,194,0.25);
        color: #3b82f6;
        box-shadow: 0 8px 28px rgba(10,102,194,0.08);
    }
    .soc-btn.tw:hover {
        background: rgba(29,161,242,0.12);
        border-color: rgba(29,161,242,0.25);
        color: #38bdf8;
        box-shadow: 0 8px 28px rgba(29,161,242,0.08);
    }
    .soc-btn.dc:hover {
        background: rgba(88,101,242,0.12);
        border-color: rgba(88,101,242,0.25);
        color: #818cf8;
        box-shadow: 0 8px 28px rgba(88,101,242,0.08);
    }

    /* ===== RIGHT PANEL: FORM ===== */
    .form-wrapper {
        background: rgba(15, 23, 42, 0.55);
        backdrop-filter: blur(24px);
        -webkit-backdrop-filter: blur(24px);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 20px;
        padding: 38px 34px;
        position: relative;
        overflow: hidden;
    }

    .form-wrapper::before {
        content: '';
        position: absolute;
        top: 0;
        left: 20%;
        right: 20%;
        height: 2px;
        background: linear-gradient(90deg, transparent, #38bdf8 30%, #818cf8 50%, #c084fc 70%, transparent);
        border-radius: 2px;
    }

    .form-wrapper::after {
        content: '';
        position: absolute;
        top: -80px;
        right: -80px;
        width: 200px;
        height: 200px;
        background: radial-gradient(circle, rgba(56,189,248,0.04) 0%, transparent 70%);
        pointer-events: none;
    }

    .form-head {
        display: flex;
        align-items: center;
        gap: 14px;
        margin-bottom: 6px;
    }

    .form-head-icon {
        width: 40px;
        height: 40px;
        border-radius: 10px;
        background: linear-gradient(135deg, rgba(56,189,248,0.12), rgba(129,140,248,0.12));
        border: 1px solid rgba(56,189,248,0.15);
        display: flex;
        align-items: center;
        justify-content: center;
        color: #38bdf8;
        font-size: 1rem;
    }

    .form-head h3 {
        color: #f1f5f9;
        font-size: 1.35rem;
        font-weight: 700;
        margin: 0;
        letter-spacing: -0.02em;
    }

    .form-head-sub {
        color: #64748b;
        font-size: 0.88rem;
        margin: 0 0 30px;
        line-height: 1.6;
        padding-left: 54px;
    }

    .flabel {
        display: flex;
        align-items: center;
        gap: 6px;
        color: #cbd5e1;
        font-size: 0.78rem;
        font-weight: 600;
        margin-bottom: 8px;
        text-transform: uppercase;
        letter-spacing: 0.8px;
    }

    .flabel i { color: #475569; font-size: 0.7rem; }
    .flabel .req { color: #f87171; font-weight: 700; margin-left: 1px; }

    /* Streamlit Inputs */
    .form-wrapper .stTextInput > div > div > input,
    .form-wrapper .stTextArea > div > div > textarea {
        background: rgba(2, 6, 23, 0.6) !important;
        border: 1.5px solid rgba(71, 85, 105, 0.3) !important;
        border-radius: 12px !important;
        color: #e2e8f0 !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.95rem !important;
        padding: 14px 16px !important;
        transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94) !important;
    }

    .form-wrapper .stTextInput > div > div > input:hover,
    .form-wrapper .stTextArea > div > div > textarea:hover {
        border-color: rgba(71, 85, 105, 0.5) !important;
    }

    .form-wrapper .stTextInput > div > div > input:focus,
    .form-wrapper .stTextArea > div > div > textarea:focus {
        border-color: #38bdf8 !important;
        box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.1),
                    0 0 20px rgba(56, 189, 248, 0.04) !important;
        outline: none !important;
    }

    .form-wrapper .stTextInput > div > div > input::placeholder,
    .form-wrapper .stTextArea > div > div > textarea::placeholder {
        color: #374151 !important;
        font-weight: 400 !important;
    }

    .form-wrapper .stTextInput > label,
    .form-wrapper .stTextArea > label,
    .form-wrapper .stSelectbox > label {
        display: none !important;
    }

    .form-wrapper .stSelectbox > div > div {
        background: rgba(2, 6, 23, 0.6) !important;
        border: 1.5px solid rgba(71, 85, 105, 0.3) !important;
        border-radius: 12px !important;
        color: #e2e8f0 !important;
        transition: all 0.3s ease !important;
    }

    .form-wrapper .stSelectbox > div > div:hover {
        border-color: rgba(71, 85, 105, 0.5) !important;
    }

    /* Submit Button */
    .form-wrapper .stFormSubmitButton > button {
        background: linear-gradient(135deg, #38bdf8 0%, #818cf8 50%, #c084fc 100%) !important;
        color: #020617 !important;
        border: none !important;
        border-radius: 14px !important;
        padding: 16px 36px !important;
        font-size: 0.95rem !important;
        font-weight: 700 !important;
        font-family: 'Inter', sans-serif !important;
        letter-spacing: 0.4px !important;
        cursor: pointer !important;
        transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94) !important;
        width: 100% !important;
        position: relative !important;
        overflow: hidden !important;
        text-transform: uppercase !important;
    }

    .form-wrapper .stFormSubmitButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 12px 40px rgba(56, 189, 248, 0.25),
                    0 4px 16px rgba(129, 140, 248, 0.2) !important;
        filter: brightness(1.08) !important;
    }

    .form-wrapper .stFormSubmitButton > button:active {
        transform: translateY(-1px) !important;
    }

    .stAlert {
        border-radius: 12px !important;
    }

    /* ===== MAP SECTION ===== */
    .map-section {
        margin-top: 40px;
        animation: masterFadeIn 1s cubic-bezier(0.16, 1, 0.3, 1) 0.2s both;
    }

    .map-header {
        display: flex;
        align-items: center;
        gap: 14px;
        margin-bottom: 20px;
    }

    .map-header-icon {
        width: 42px;
        height: 42px;
        border-radius: 12px;
        background: linear-gradient(135deg, rgba(251,146,60,0.1), rgba(251,146,60,0.18));
        border: 1px solid rgba(251,146,60,0.15);
        display: flex;
        align-items: center;
        justify-content: center;
        color: #fb923c;
        font-size: 1rem;
    }

    .map-header-text h3 {
        color: #f1f5f9;
        font-size: 1.25rem;
        font-weight: 700;
        margin: 0;
        letter-spacing: -0.02em;
    }

    .map-header-text p {
        color: #64748b;
        font-size: 0.85rem;
        margin: 2px 0 0;
    }

    .map-container {
        display: grid;
        grid-template-columns: 1fr 340px;
        gap: 0;
        border-radius: 20px;
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, 0.06);
        background: rgba(15, 23, 42, 0.55);
        backdrop-filter: blur(24px);
        -webkit-backdrop-filter: blur(24px);
    }

    .map-embed {
        width: 100%;
        height: 360px;
        position: relative;
        overflow: hidden;
    }

    .map-embed iframe {
        width: 100%;
        height: 100%;
        border: none;
        filter: brightness(0.8) contrast(1.1) saturate(0.8);
        transition: filter 0.4s ease;
    }

    .map-embed:hover iframe {
        filter: brightness(0.85) contrast(1.1) saturate(0.9);
    }

    .map-info-side {
        padding: 32px 28px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        gap: 24px;
        border-left: 1px solid rgba(255, 255, 255, 0.05);
    }

    .map-detail-item {
        display: flex;
        align-items: flex-start;
        gap: 14px;
    }

    .map-detail-icon {
        width: 38px;
        height: 38px;
        min-width: 38px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.9rem;
    }

    .map-detail-icon.mdi-pin {
        background: rgba(251,146,60,0.12);
        color: #fb923c;
        border: 1px solid rgba(251,146,60,0.12);
    }
    .map-detail-icon.mdi-coords {
        background: rgba(56,189,248,0.12);
        color: #38bdf8;
        border: 1px solid rgba(56,189,248,0.12);
    }
    .map-detail-icon.mdi-region {
        background: rgba(52,211,153,0.12);
        color: #34d399;
        border: 1px solid rgba(52,211,153,0.12);
    }
    .map-detail-icon.mdi-country {
        background: rgba(192,132,252,0.12);
        color: #c084fc;
        border: 1px solid rgba(192,132,252,0.12);
    }

    .map-detail-text h5 {
        color: #94a3b8;
        font-size: 0.68rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin: 0 0 3px;
    }

    .map-detail-text p {
        color: #e2e8f0;
        font-size: 0.9rem;
        margin: 0;
        font-weight: 500;
        line-height: 1.4;
    }

    .map-open-link {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        color: #38bdf8;
        font-size: 0.82rem;
        font-weight: 600;
        text-decoration: none;
        padding: 10px 18px;
        border-radius: 10px;
        background: rgba(56,189,248,0.08);
        border: 1px solid rgba(56,189,248,0.15);
        transition: all 0.3s ease;
        margin-top: 4px;
        align-self: flex-start;
    }

    .map-open-link:hover {
        background: rgba(56,189,248,0.15);
        border-color: rgba(56,189,248,0.3);
        transform: translateX(3px);
        color: #7dd3fc;
    }

    .map-open-link i { font-size: 0.75rem; transition: transform 0.3s ease; }
    .map-open-link:hover i { transform: translateX(3px); }

    /* ===== STATUS BAR ===== */
    .avail-bar {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 12px;
        margin-top: 36px;
        padding: 18px 24px;
        background: rgba(15, 23, 42, 0.4);
        border-radius: 14px;
        border: 1px solid rgba(255, 255, 255, 0.04);
    }

    .avail-dot {
        width: 8px;
        height: 8px;
        background: #34d399;
        border-radius: 50%;
        animation: dotPulse 2.2s ease-in-out infinite;
        flex-shrink: 0;
    }

    @keyframes dotPulse {
        0%, 100% { box-shadow: 0 0 0 0 rgba(52,211,153,0.45); }
        50% { box-shadow: 0 0 0 8px rgba(52,211,153,0); }
    }

    .avail-bar p {
        color: #94a3b8;
        margin: 0;
        font-size: 0.88rem;
        font-weight: 400;
    }

    .avail-bar strong { color: #34d399; font-weight: 600; }

    /* ===== CTA SECTION ===== */
    .cta-block {
        margin-top: 36px;
        text-align: center;
        padding: 44px 30px;
        background: linear-gradient(135deg, rgba(56,189,248,0.04), rgba(129,140,248,0.04), rgba(192,132,252,0.04));
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        position: relative;
        overflow: hidden;
    }

    .cta-block::before {
        content: '';
        position: absolute;
        top: -120px;
        left: 50%;
        transform: translateX(-50%);
        width: 400px;
        height: 400px;
        background: radial-gradient(circle, rgba(56,189,248,0.03) 0%, transparent 60%);
        pointer-events: none;
    }

    .cta-icon-ring {
        width: 64px;
        height: 64px;
        border-radius: 50%;
        background: linear-gradient(135deg, rgba(56,189,248,0.08), rgba(129,140,248,0.08));
        border: 1px solid rgba(56,189,248,0.12);
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 20px;
    }

    .cta-icon-ring i {
        font-size: 1.5rem;
        color: #38bdf8;
    }

    .cta-block h3 {
        color: #f1f5f9;
        font-size: clamp(1.3rem, 3vw, 1.6rem);
        font-weight: 700;
        margin: 0 0 12px;
        letter-spacing: -0.02em;
    }

    .cta-block p {
        color: #94a3b8;
        font-size: 0.95rem;
        max-width: 520px;
        margin: 0 auto;
        line-height: 1.75;
    }

    /* ===== RESPONSIVE ===== */
    @media (max-width: 1024px) {
        .contact-grid-main {
            grid-template-columns: 1fr;
            gap: 22px;
        }

        .left-panel {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
        }

        .social-panel {
            grid-column: 1 / -1;
        }

        .map-container {
            grid-template-columns: 1fr;
        }

        .map-info-side {
            border-left: none;
            border-top: 1px solid rgba(255,255,255,0.05);
            flex-direction: row;
            flex-wrap: wrap;
            gap: 20px;
            padding: 24px;
        }

        .map-detail-item { min-width: calc(50% - 10px); }
        .map-open-link { width: 100%; justify-content: center; }
    }

    @media (max-width: 768px) {
        .contact-master-wrap { padding: 8px 14px 60px; }

        .contact-hero { margin-bottom: 40px; }

        .left-panel {
            grid-template-columns: 1fr;
            gap: 10px;
        }

        .form-wrapper { padding: 26px 20px; border-radius: 16px; }

        .form-head-sub { padding-left: 0; margin-top: 8px; }

        .map-embed { height: 280px; }

        .map-info-side {
            flex-direction: column;
            padding: 22px 20px;
        }

        .map-detail-item { min-width: 100%; }
    }

    @media (max-width: 480px) {
        .contact-master-wrap { padding: 4px 10px 50px; }

        .form-wrapper { padding: 22px 16px; }

        .c-info-card { padding: 18px 16px; gap: 12px; }

        .c-icon-wrap {
            width: 42px; height: 42px; min-width: 42px;
            font-size: 0.95rem;
            border-radius: 11px;
        }

        .social-row { grid-template-columns: repeat(4, 1fr); gap: 8px; }

        .map-container { border-radius: 14px; }
        .map-embed { height: 240px; }

        .cta-block { padding: 32px 18px; }
    }

    @media (max-width: 360px) {
        .social-row { grid-template-columns: repeat(2, 1fr); }
        .contact-hero h1 { font-size: 1.8rem; }
    }
</style>
""", unsafe_allow_html=True)

# ===== HEADER =====
st.markdown("""
<div class="contact-master-wrap">
    <div class="contact-hero">
        <div class="hero-badge">
            <i class="fas fa-paper-plane"></i>
            Contact
        </div>
        <h1>Get <span class="hero-gradient">In Touch</span></h1>
        <p class="hero-desc">Have a project in mind, a question, or want to collaborate? I would love to hear from you. Fill out the form below and I will respond promptly.</p>
        <div class="hero-line"></div>
    </div>
""", unsafe_allow_html=True)

# ===== MAIN GRID =====
st.markdown('<div class="contact-grid-main">', unsafe_allow_html=True)

# ===== LEFT PANEL =====
st.markdown("""
<div class="left-panel">
    <div class="c-info-card">
        <div class="c-icon-wrap ic-email"><i class="fas fa-envelope"></i></div>
        <div class="c-info-text">
            <h4>Email</h4>
            <p><a href="mailto:lloyd.bibano@email.com">lloyd.bibano@email.com</a></p>
        </div>
    </div>
    <div class="c-info-card">
        <div class="c-icon-wrap ic-phone"><i class="fas fa-phone-alt"></i></div>
        <div class="c-info-text">
            <h4>Phone</h4>
            <p><a href="tel:+1234567890">09518743282</a></p>
        </div>
    </div>
    <div class="c-info-card">
        <div class="c-icon-wrap ic-location"><i class="fas fa-map-marker-alt"></i></div>
        <div class="c-info-text">
            <h4>Location</h4>
            <p>Cabitan, Mandaon, Masbate</p>
        </div>
    </div>
    <div class="c-info-card">
        <div class="c-icon-wrap ic-clock"><i class="fas fa-clock"></i></div>
        <div class="c-info-text">
            <h4>Availability</h4>
            <p>Mon &ndash; Fri, 9 AM &ndash; 6 PM</p>
        </div>
    </div>
    <div class="social-panel">
        <h4><i class="fas fa-share-nodes"></i> Connect With Me</h4>
        <div class="social-row">
            <a href="https://github.com/" target="_blank" class="soc-btn gh" title="GitHub"><i class="fab fa-github"></i></a>
            <a href="https://linkedin.com/" target="_blank" class="soc-btn li" title="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
            <a href="https://twitter.com/" target="_blank" class="soc-btn tw" title="Twitter / X"><i class="fab fa-x-twitter"></i></a>
            <a href="https://discord.com/" target="_blank" class="soc-btn dc" title="Discord"><i class="fab fa-discord"></i></a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ===== RIGHT PANEL: FORM =====
st.markdown("""
<div class="form-wrapper">
    <div class="form-head">
        <div class="form-head-icon"><i class="fas fa-pen-nib"></i></div>
        <h3>Send a Message</h3>
    </div>
    <p class="form-head-sub">All fields marked with an asterisk are required. I typically respond within 24 hours.</p>
""", unsafe_allow_html=True)

with st.form(key="contact_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="flabel"><i class="fas fa-user"></i> Full Name <span class="req">*</span></div>', unsafe_allow_html=True)
        name = st.text_input("Full Name", placeholder="Sample", key="name", label_visibility="collapsed")
    with col2:
        st.markdown('<div class="flabel"><i class="fas fa-at"></i> Email Address <span class="req">*</span></div>', unsafe_allow_html=True)
        email = st.text_input("Email Address", placeholder="example.com", key="email", label_visibility="collapsed")

    col3, col4 = st.columns(2)
    with col3:
        st.markdown('<div class="flabel"><i class="fas fa-tag"></i> Subject <span class="req">*</span></div>', unsafe_allow_html=True)
        subject = st.text_input("Subject", placeholder="Project Inquiry", key="subject", label_visibility="collapsed")
    with col4:
        st.markdown('<div class="flabel"><i class="fas fa-list-check"></i> Inquiry Type</div>', unsafe_allow_html=True)
        inquiry = st.selectbox("Inquiry Type", [
            "General Inquiry",
            "Project Collaboration",
            "Job Opportunity",
            "Freelance Work",
            "Other"
        ], key="inquiry", label_visibility="collapsed")

    st.markdown('<div class="flabel"><i class="fas fa-message"></i> Message <span class="req">*</span></div>', unsafe_allow_html=True)
    message = st.text_area("Message", placeholder="Tell me about your project, goals, and how I can help...", height=140, key="message", label_visibility="collapsed")

    submitted = st.form_submit_button("Send Message", use_container_width=True)

    if submitted:
        if name and email and subject and message:
            st.success("Message sent successfully. I will get back to you within 24 hours.")
        else:
            st.warning("Please fill in all required fields before submitting.")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ===== MAP SECTION =====
st.markdown("""
<div class="map-section">
    <div class="map-header">
        <div class="map-header-icon"><i class="fas fa-location-dot"></i></div>
        <div class="map-header-text">
            <h3>My Location</h3>
            <p>Cabitan, Mandaon, Masbate, Philippines</p>
        </div>
    </div>
    <div class="map-container">
        <div class="map-embed">
            <iframe
                src="https://www.openstreetmap.org/export/embed.html?bbox=123.45%2C12.28%2C123.60%2C12.38&layer=mapnik&marker=12.33%2C123.53"
                loading="lazy"
                referrerpolicy="no-referrer-when-downgrade"
                title="Map showing Cabitan, Mandaon, Masbate"
                allowfullscreen>
            </iframe>
        </div>
        <div class="map-info-side">
            <div class="map-detail-item">
                <div class="map-detail-icon mdi-pin"><i class="fas fa-map-pin"></i></div>
                <div class="map-detail-text">
                    <h5>Barangay</h5>
                    <p>Cabitan</p>
                </div>
            </div>
            <div class="map-detail-item">
                <div class="map-detail-icon mdi-coords"><i class="fas fa-crosshairs"></i></div>
                <div class="map-detail-text">
                    <h5>Municipality</h5>
                    <p>Mandaon</p>
                </div>
            </div>
            <div class="map-detail-item">
                <div class="map-detail-icon mdi-region"><i class="fas fa-mountain-sun"></i></div>
                <div class="map-detail-text">
                    <h5>Province</h5>
                    <p>Masbate</p>
                </div>
            </div>
            <div class="map-detail-item">
                <div class="map-detail-icon mdi-country"><i class="fas fa-flag"></i></div>
                <div class="map-detail-text">
                    <h5>Country</h5>
                    <p>Philippines</p>
                </div>
            </div>
            <a href="https://www.openstreetmap.org/?mlat=12.33&mlon=123.53#map=13/12.33/123.53" target="_blank" class="map-open-link">
                <i class="fas fa-up-right-from-square"></i>
                Open in Maps
                <i class="fas fa-arrow-right"></i>
            </a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ===== STATUS BAR =====
st.markdown("""
<div class="avail-bar">
    <div class="avail-dot"></div>
    <p>Currently <strong>available</strong> for new projects and collaborations</p>
</div>
""", unsafe_allow_html=True)

# ===== CTA SECTION =====
st.markdown("""
<div class="cta-block">
    <div class="cta-icon-ring"><i class="fas fa-handshake-simple"></i></div>
    <h3>Let's Build Something Great Together</h3>
    <p>Whether it is a full-stack application, data science project, or a creative collaboration, I am always excited to work on meaningful projects that make a difference.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)