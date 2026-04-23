import streamlit as st
import base64
import os

def get_base64_image(image_path):
    """Convert image to base64 string for HTML embedding"""
    try:
        with open(image_path, "rb") as img_file:
            return f"data:image/png;base64,{base64.b64encode(img_file.read()).decode()}"
    except Exception:
        return None

def inject_plexus_bg():
    """Inject simple box-style background"""
    st.markdown("""
    <style>
    body { background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%); margin: 0; }
    .main .block-container { background: rgba(30, 41, 59, 0.8); border-radius: 15px; padding: 20px; margin: 20px auto; max-width: 1200px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); }
    </style>
    """, unsafe_allow_html=True)

def render_sidebar():
    """Render custom sidebar with SVG icons"""
    st.sidebar.markdown("""
    <style>
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%); border-right: 1px solid rgba(255,255,255,0.05); }
    .nav-container { padding: 20px 5px; font-family: 'Segoe UI', system-ui, sans-serif; }
    .nav-header { text-align: center; margin-bottom: 30px; padding-bottom: 20px; border-bottom: 1px solid rgba(255,255,255,0.1); }
    .nav-header h3 { color: #f8fafc; margin: 10px 0 5px; font-size: 1.3rem; }
    .nav-header p { color: #94a3b8; margin: 0; font-size: 0.85rem; }
    .nav-link { display: flex; align-items: center; gap: 12px; padding: 12px 15px; margin: 6px 0;
        border-radius: 10px; color: #cbd5e1; text-decoration: none; transition: all 0.3s ease; cursor: pointer; }
    .nav-link:hover { background: rgba(56,189,248,0.1); color: #38bdf8; transform: translateX(5px); }
    .nav-link svg { width: 20px; height: 20px; fill: currentColor; }
    .socials { position: absolute; bottom: 20px; left: 0; right: 0; display: flex; justify-content: center; gap: 15px; color: #64748b; }
    .socials a { color: inherit; text-decoration: none; transition: color 0.2s; }
    .socials a:hover { color: #38bdf8; }
    </style>
    """, unsafe_allow_html=True)

    st.sidebar.markdown("""
    <div class="nav-container">
        <div class="nav-header">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="#38bdf8"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg>
            <h3>Lloyd George Bibano</h3>
            <p>3rd Year CS Student</p>
        </div>
        <a href="/" class="nav-link"><svg viewBox="0 0 24 24"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg> Home</a>
        <a href="/1_About" class="nav-link"><svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg> About</a>
        <a href="/3_Skills" class="nav-link"><svg viewBox="0 0 24 24"><path d="M9 11.24V7.5a2.5 2.5 0 0 1 5 0v3.74c1.21-.81 2-2.18 2-3.74C16 4.46 13.54 2 10.5 2S5 4.46 5 7.5c0 1.56.79 2.93 2 3.74zm9.84 4.63l-4.54-2.26c-.17-.07-.35-.11-.54-.11H13v-6a1.5 1.5 0 0 0-3 0v9.02L5.14 19.2c-.38.2-.76.55-.76 1.15 0 .83.67 1.5 1.5 1.5h12.24c.83 0 1.5-.67 1.5-1.5 0-.43-.16-.84-.46-1.14l-.38-.34z"/></svg> Skills</a>
        <a href="/4_Certificate" class="nav-link"><svg viewBox="0 0 24 24"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z"/></svg> Certificates</a>
        <a href="/5_Project" class="nav-link"><svg viewBox="0 0 24 24"><path d="M22 9V7h-2V5a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-2h2v-2h-2v-2h2v-2h-2V9h2zm-4 10H4V5h14v14zM6 13h5v4H6v-4zm6-6h4v3h-4V7zM6 7h5v4H6V7zm6 4h4v3h-4v-3z"/></svg> Projects</a>
        <a href="/6_Contact" class="nav-link"><svg viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg> Contact</a>
        <div class="socials">
            <a href="#"><svg width="18" height="18" viewBox="0 0 24 24"><path d="M12 2.04c-5.5 0-10 4.49-10 10.02 0 5 3.66 9.15 8.44 9.9v-7H7.9v-2.9h2.54V9.85c0-2.51 1.49-3.89 3.78-3.89 1.09 0 2.24.2 2.24.2v2.46h-1.26c-1.24 0-1.63.77-1.63 1.56v1.88h2.78l-.45 2.9h-2.33v7a10 10 0 0 0 8.44-9.9c0-5.53-4.5-10.02-10-10.02z"/></svg></a>
            <a href="#"><svg width="18" height="18" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/></svg></a>
            <a href="#"><svg width="18" height="18" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm0 14.2c-2.5 0-4.71-1.28-6-3.22.03-1.99 4-3.08 6-3.08 1.99 0 5.97 1.09 6 3.08-1.29 1.94-3.5 3.22-6 3.22z"/></svg></a>
        </div>
    </div>
    """, unsafe_allow_html=True)