import streamlit as st

# Page configuration must be the first Streamlit command
st.set_page_config(
    page_title="Ground Truth Demo",
    layout="wide", # 开启宽屏模式，因为真实页面需要占据完整宽度
    initial_sidebar_state="collapsed"
)

# Inject global CSS styles
# 完全隐藏了 Streamlit 的侧边栏和顶部控制栏，使其看起来像一个纯粹的真实 App
st.markdown("""
<style>
.stApp {
    background-color: #F4F6F4;
    font-family: 'Inter', -apple-system, sans-serif;
}
[data-testid="collapsedControl"] { display: none; }
section[data-testid="stSidebar"] { display: none !important; }
header { visibility: hidden; }

.mobile-container {
    max-width: 480px;
    margin: 0 auto;
    background-color: #FFFFFF;
    min-height: 90vh;
    padding: 24px;
    border-radius: 12px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
}
.web-container {
    background-color: #FFFFFF;
    padding: 32px;
    border-radius: 12px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
}
.card { border: 1px solid #F0F2F0; border-radius: 16px; padding: 16px; margin-bottom: 16px; background: white; }
.card-dark { background-color: #0F1E2A; color: white; border-radius: 16px; padding: 16px; margin-bottom: 16px; }
.prog-bg { background-color: #E6EBE9; border-radius: 4px; height: 8px; width: 100%; margin: 6px 0 12px 0; }
.prog-fill-green { background-color: #2E9F64; border-radius: 4px; height: 100%; }
</style>
""", unsafe_allow_html=True)

# Define render functions for the three pages
def render_farmer_page():
    # Completely flattened HTML, removed fake status bar to act as a real app
    st.markdown("""
<div class="mobile-container">
<div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 24px;">
<div>
<div style="font-size: 13px; color: #666; margin-bottom: 2px;">Good morning, Kofi 👋</div>
<div style="font-size: 24px; font-weight: 800; color: #111C24;">Kofi's Farm</div>
<div style="font-size: 12px; color: #888; margin-top: 4px;">📍 Ashanti, Ghana · 4.2 ha</div>
</div>
<div style="background-color: #2E9F64; color: white; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 16px;">K</div>
</div>
<div class="card-dark" style="margin-bottom: 16px; border-radius: 20px;">
<div style="display: flex; justify-content: space-between; font-size: 11px; margin-bottom: 16px; color: #A0B0C0; font-weight: 600;">
<span style="color: white;">Field health · satellite</span><span>● Updated 2 days ago</span>
</div>
<svg width="100%" height="130" viewBox="0 0 200 100" preserveAspectRatio="none" style="border-radius: 8px;">
<polygon points="10,50 90,10 90,60 10,90" fill="#4ade80" />
<polygon points="90,10 190,20 180,80 90,60" fill="#86efac" />
<polygon points="10,90 90,60 100,95" fill="#fb923c" />
<polygon points="90,60 180,80 160,95 100,95" fill="#f87171" />
<text x="40" y="45" font-size="10" fill="#064e3b" font-weight="bold">Zone A</text>
<text x="130" y="40" font-size="10" fill="#064e3b" font-weight="bold">Zone B</text>
<text x="40" y="80" font-size="10" fill="#7c2d12" font-weight="bold">Zone C</text>
<text x="130" y="80" font-size="10" fill="#7f1d1d" font-weight="bold">Zone D</text>
</svg>
</div>
<div class="card" style="box-shadow: 0 4px 15px rgba(46,159,100,0.1); border-radius: 20px; border: none;">
<div style="font-size: 12px; font-weight: 700; color: #2E9F64; margin-bottom: 12px; letter-spacing: 0.5px;">THIS WEEK'S TIP <span style="color: #999; font-weight: normal;">Zone B</span></div>
<div style="display: flex; gap: 16px; align-items: flex-start;">
<div style="background-color: #E6F4EA; border-radius: 50%; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><span style="color: #2E9F64; font-size: 20px;">💧</span></div>
<div>
<div style="font-weight: 700; color: #111C24; font-size: 16px; margin-bottom: 6px;">Skip irrigation this week</div>
<div style="font-size: 14px; color: #555; line-height: 1.5; margin-bottom: 12px;">Zone B soil moisture is high after last week's rain. Hold off watering.</div>
<div style="background-color: #E6F4EA; color: #2E9F64; padding: 6px 12px; border-radius: 12px; font-size: 12px; font-weight: 700; display: inline-block;">↓ Saves ~15% water</div>
</div>
</div>
</div>
</div>
""", unsafe_allow_html=True)

def render_retailer_page():
    # Completely flattened HTML, removed browser top bar to act as a real dashboard
    st.markdown("""
<div class="web-container">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 32px;">
<div>
<div style="font-size: 28px; font-weight: 800; color: #111C24;">Supply Base</div>
<div style="font-size: 14px; color: #666; margin-top: 4px;">Cocoa programme · West Africa · 2026 season</div>
</div>
<div style="background-color: #E6F4EA; color: #2E9F64; padding: 8px 16px; border-radius: 20px; font-size: 13px; font-weight: 700;">● Live satellite feed</div>
</div>
<div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-bottom: 20px;">
<div class="card">
<div style="font-size: 13px; color: #666; margin-bottom: 8px;">Farms covered</div>
<div style="font-size: 32px; font-weight: 800; color: #111C24;">1,284</div>
<div style="font-size: 13px; color: #2E9F64; font-weight: bold; margin-top: 8px;">▲ 96 secured</div>
</div>
<div class="card">
<div style="font-size: 13px; color: #666; margin-bottom: 8px;">Hectares</div>
<div style="font-size: 32px; font-weight: 800; color: #111C24;">8,470</div>
<div style="font-size: 13px; color: #888; margin-top: 8px;">across 6 regions</div>
</div>
<div class="card">
<div style="font-size: 13px; color: #666; margin-bottom: 8px;">EUDR-ready</div>
<div style="font-size: 32px; font-weight: 800; color: #111C24;">91%</div>
<div style="font-size: 13px; color: #2E9F64; font-weight: bold; margin-top: 8px;">▲ 7 pts vs Q1</div>
</div>
<div class="card-dark" style="margin-bottom: 0;">
<div style="font-size: 13px; color: #A0B0C0; margin-bottom: 8px;">Supply-resilience score</div>
<div style="font-size: 32px; font-weight: 800;">82<span style="font-size: 16px; color: #A0B0C0;">/100</span></div>
<div style="font-size: 13px; color: #4ade80; font-weight: bold; margin-top: 8px;">▲ improving</div>
</div>
</div>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
<div class="card">
<div style="font-weight: 700; color: #111C24; font-size: 16px; margin-bottom: 20px;">Verification status</div>
<div style="display: flex; justify-content: space-between; font-size: 14px; margin-bottom: 4px;"><span>Deforestation-free</span><b>94%</b></div>
<div class="prog-bg" style="margin-bottom: 16px;"><div class="prog-fill-green" style="width: 94%;"></div></div>
<div style="display: flex; justify-content: space-between; font-size: 14px; margin-bottom: 4px;"><span>Verified-sustainable</span><b>86%</b></div>
<div class="prog-bg" style="margin-bottom: 16px;"><div class="prog-fill-green" style="width: 86%;"></div></div>
<div style="display: flex; justify-content: space-between; font-size: 14px; margin-bottom: 4px;"><span>EUDR-ready</span><b>91%</b></div>
<div class="prog-bg"><div class="prog-fill-green" style="width: 91%;"></div></div>
</div>
<div class="card">
<div style="font-weight: 700; color: #111C24; font-size: 16px; margin-bottom: 20px;">Regions Status</div>
<div style="display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid #eee; font-size: 14px;"><span>Ashanti (412 farms)</span><span style="color: #2E9F64; font-weight: bold;">● 97% Verified</span></div>
<div style="display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid #eee; font-size: 14px;"><span>Western (358 farms)</span><span style="color: #2E9F64; font-weight: bold;">● 92% Verified</span></div>
<div style="display: flex; justify-content: space-between; padding: 8px 0; font-size: 14px;"><span>Eastern (221 farms)</span><span style="color: #E79E4F; font-weight: bold;">● 78% Needs support</span></div>
</div>
</div>
</div>
""", unsafe_allow_html=True)

    # Add QR Code linking directly to the Consumer View
    st.markdown("""
<div style="margin-top: 24px; padding: 24px; background-color: #FFFFFF; border-radius: 12px; border: 1px dashed #ccc; display: flex; align-items: center; gap: 24px; max-width: 600px; margin-left: auto; margin-right: auto;">
<img src="https://api.qrserver.com/v1/create-qr-code/?size=120x120&data=https%3A%2F%2Fhss26-eudr-demo.streamlit.app%2F%3Fview%3Dconsumer" width="120" height="120" style="border-radius: 8px;">
<div>
<h3 style="margin: 0 0 8px 0; color: #111C24; font-size: 18px;">📲 Test the Consumer Journey</h3>
<p style="margin: 0; color: #666; font-size: 14px; line-height: 1.5;">Scan this QR code to access the <b>Consumer Proof</b> page directly.<br><i>(Ensure your phone is on the same local network, or change the URL parameter to your deployed domain.)</i></p>
</div>
</div>
    """, unsafe_allow_html=True)


def render_consumer_page():
    # Completely flattened HTML, real mobile responsive view
    st.markdown("""
<div class="mobile-container">
<div style="font-size: 13px; color: #888; margin-bottom: 24px; display: flex; align-items: center; gap: 8px;">
<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 7V5a2 2 0 0 1 2-2h2M17 3h2a2 2 0 0 1 2 2v2M21 17v2a2 2 0 0 1-2 2h-2M7 21H5a2 2 0 0 1-2-2v-2"/></svg>
Scanned just now
</div>
<div class="card" style="display: flex; gap: 16px; align-items: center; padding: 16px; border-radius: 16px; border: 1px solid #E6EBE9;">
<div style="background-color: #5C4033; color: white; width: 70px; height: 80px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: bold; text-align: center;">DARK<br>70%</div>
<div>
<div style="font-size: 11px; color: #888; font-weight: 700; letter-spacing: 0.5px;">ASANTE ORIGINS</div>
<div style="font-size: 18px; font-weight: 800; color: #111C24; line-height: 1.2; margin-top: 4px; margin-bottom: 12px;">Single-Origin Dark Chocolate</div>
<div style="background-color: #E6F4EA; color: #2E9F64; padding: 6px 12px; border-radius: 16px; font-size: 12px; font-weight: 700; display: inline-flex; align-items: center; gap: 6px;">
✓ Verified by Ground Truth
</div>
</div>
</div>
<div class="card-dark" style="border-radius: 16px; padding: 20px; margin-bottom: 16px;">
<div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 16px; font-weight: 600;">
<span style="color: white;">Traced to origin</span><span style="color: #A0B0C0;">Ashanti, Ghana</span>
</div>
<svg width="100%" height="110" viewBox="0 0 200 100" preserveAspectRatio="none">
<polygon points="10,40 80,20 100,70 30,90" fill="#2E9F64" />
<polygon points="80,20 180,30 160,80 100,70" fill="#1E8F50" />
<circle cx="50" cy="55" r="4" fill="#E79E4F"/>
<circle cx="130" cy="50" r="4" fill="#E79E4F"/>
</svg>
</div>
<div style="background-color: #FFF9F0; border-radius: 16px; padding: 20px; display: flex; gap: 16px; align-items: center; margin-bottom: 24px;">
<div style="background-color: #E79E4F; color: white; width: 44px; height: 44px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 18px; flex-shrink: 0;">K</div>
<div>
<div style="font-size: 14px; font-weight: 700; color: #111C24; margin-bottom: 4px;">Grown by Kofi Mensah</div>
<div style="font-size: 13px; color: #666; font-style: italic; line-height: 1.4;">"The satellite tips cut my water use and my beans sell for more now."</div>
</div>
</div>
<div style="background-color: #111C24; color: white; text-align: center; padding: 16px; border-radius: 30px; font-size: 15px; font-weight: 700; cursor: pointer;">
See the full origin story →
</div>
</div>
""", unsafe_allow_html=True)


# ========================================================
# --- Routing Logic (URL Query Parameters & Navigation) ---
# ========================================================

# Check if the URL contains "?view=consumer" (like when scanned via QR code)
target_view = st.query_params.get("view", "")

if target_view == "consumer":
    # If routed directly via QR code, render ONLY the consumer page
    render_consumer_page()
else:
    # Otherwise, show the presenter navigation on top
    st.markdown("""
        <div style='text-align: center; padding: 10px 0 30px 0;'>
            <h1 style='color: #111C24; font-size: 32px;'>Ground Truth Platform</h1>
            <p style='color: #666;'>Select a user role below to view their application.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Use standard Streamlit columns to center the radio buttons
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        page = st.radio(
            "Navigation",
            ["👨‍🌾 Farmer App", "🏢 Retailer Dashboard", "🍫 Consumer Proof"],
            horizontal=True,
            label_visibility="collapsed"
        )
        
    st.markdown("<hr style='margin-bottom: 40px;'>", unsafe_allow_html=True)
    
    # Render selected view
    if page == "👨‍🌾 Farmer App":
        render_farmer_page()
    elif page == "🏢 Retailer Dashboard":
        render_retailer_page()
    else:
        render_consumer_page()