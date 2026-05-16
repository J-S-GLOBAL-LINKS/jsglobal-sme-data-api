import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="J.S.GLOBAL LINKS", page_icon="logo.png", layout="wide")

# CSS DON KYAU KAMAR VTU.NG
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: #f8f9fa;
}
div[data-testid="stButton"] > button {
    height: 110px;
    background-color: white;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    font-size: 16px;
    font-weight: 500;
}
div[data-testid="stButton"] > button:hover {
    box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    border: 1px solid #2a5298;
    color: #2a5298;
}
.wallet-container {
    background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
    padding: 1.5rem;
    border-radius: 15px;
    color: white;
    margin: 1rem 0;
}
.fund-btn > button {
    background-color: #ff4757 !important;
    color: white !important;
    border: none !important;
    height: 50px !important;
    font-weight: bold !important;
}
[data-testid="stSidebar"] {
    background-color: #1e3c72;
}
[data-testid="stSidebar"] * {
    color: white;
}
.kyc-warning {
    background-color: #fff3cd;
    padding: 15px;
    border-radius: 10px;
    border-left: 5px solid #ffc107;
}
.ussd-card {
    background-color: #e8f4fd;
    padding: 15px;
    border-radius: 10px;
    border-left: 5px solid #2a5298;
    margin: 10px 0;
}
</style>
""", unsafe_allow_html=True)

# API SETUP
api_key = st.secrets["SMEPLUG_API_KEY"]
BASE_URL = "https://smeplug.ng/api/v1"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# SESSION STATE
if 'page' not in st.session_state:
    st.session_state.page = 'dashboard'
if 'show_balance' not in st.session_state:
    st.session_state.show_balance = True
if 'kyc_status' not in st.session_state:
    st.session_state.kyc_status = 'pending'
if 'user_data' not in st.session_state:
    st.session_state.user_data = {}

# SAMO BALANCE
try:
    response = requests.get(f"{BASE_URL}/account/balance", headers=headers, timeout=10)
    balance = response.json().get('balance', '0') if response.status_code == 200 else '0'
except Exception:
    balance = '0'

# ===== SIDEBAR MENU =====
with st.sidebar:
    st.image("logo.png", width=80)
    st.markdown("### J.S.GLOBAL LINKS")
    st.caption("RC: 8984371")
    
    if st.session_state.kyc_status == 'approved':
        st.success("✅ KYC Verified")
    elif st.session_state.kyc_status == 'submitted':
        st.warning("⏳ KYC Pending")
    else:
        st.error("❌ KYC Required")
    
    st.markdown("---")
    
    if st.button("🏠 Dashboard", use_container_width=True):
        st.session_state.page = 'dashboard'
        st.rerun()
    
    if st.button("👤 My
