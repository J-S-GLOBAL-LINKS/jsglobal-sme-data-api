import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="J.S.GLOBAL LINKS", page_icon="logo.png", layout="wide")

# CSS DON KYAU
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
    
    # KYC Status Badge
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
    
    if st.button("👤 My Profile", use_container_width=True):
        st.session_state.page = 'profile'
        st.rerun()
    
    if st.button("🔐 KYC Verification", use_container_width=True):
        st.session_state.page = 'kyc'
        st.rerun()
    
    if st.button("📞 USSD Codes", use_container_width=True):
        st.session_state.page = 'ussd'
        st.rerun()
    
    if st.button("📜 Transactions", use_container_width=True):
        st.session_state.page = 'history'
        st.rerun()
    
    if st.button("💰 Commission", use_container_width=True):
        st.info("Coming Soon")
    
    if st.button("⚙️ Settings", use_container_width=True):
        st.info("Coming Soon")
    
    if st.button("📞 Support", use_container_width=True):
        st.session_state.page = 'support'
        st.rerun()
    
    st.markdown("---")
    if st.button("🚪 Logout", use_container_width=True):
        st.info("Logout feature coming soon")
    
    st.markdown("---")
    st.caption("📍 Kano, Nigeria")
    st.caption("📞 07062589825")

# HEADER
col1, col2 = st.columns([1, 8])
with col1:
    st.image("logo.png", width=50)
with col2:
    st.markdown("### J.S.GLOBAL LINKS AND SERVICES")
    st.caption("CAC: RC 8984371 | GENERAL MERCHANDISE")

# BACK BUTTON
if st.session_state.page != 'dashboard':
    if st.button("← Back to Dashboard"):
        st.session_state.page = 'dashboard'
        st.rerun()
    st.markdown("---")

# KYC WARNING
if st.session_state.kyc_status == 'pending' and st.session_state.page == 'dashboard':
    st.markdown('<div class="kyc-warning">', unsafe_allow_html=True)
    st.warning("⚠️ **KYC Required:** Ka kammala KYC Verification don amfani da duk services. Danna 'KYC Verification' a menu.")
    if st.button("Verify KYC Now", type="primary"):
        st.session_state.page = 'kyc'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.write("")

# DASHBOARD
if st.session_state.page == 'dashboard':
    st.markdown('<div class="wallet-container">', unsafe_allow_html=True)
    st.markdown("##### WALLET BALANCE")
    col1, col2, col3 = st.columns([6,1,1])
    with col1:
        if st.session_state.show_balance:
            st.markdown(f"## ₦{balance}")
        else:
            st.markdown("## ******")
    with col2:
        if st.button("👁️", key="eye"):
            st.session_state.show_balance = not st.session_state.show_balance
            st.rerun()
    with col3:
        if st.button("🔄", key="refresh"):
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="fund-btn">', unsafe_allow_html=True)
    if st.button("+ Fund Wallet", use_container_width=True):
        st.info("Za a tura ka zuwa SMEPlug don cika wallet. Ko ka tuntube mu: 07062589825")
    st.markdown('</div>', unsafe_allow_html=True)
    st.write("")

    st.info("**Upgrade Membership** - Unlock more discounts and other benefits >")
    st.write("")

    st.markdown("#### What would you like to do?")
    st.write("")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("📞\n\nAirtime", use_container_width=True):
            if st.session_state.kyc_status != 'approved':
                st.error("Dole ka yi KYC tukuna")
            else:
                st.session_state.page = 'airtime'
                st.rerun()
    with col2:
        if st.button("📱\n\nData", use_container_width=True):
            if st.session_state.kyc_status != 'approved':
                st.error("Dole ka yi KYC tukuna")
            else:
                st.session_state.page = 'data'
                st.rerun()
    
    st.write("")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📺\n\nCable TV", use_container_width=True):
            if st.session_state.kyc_status != 'approved':
                st.error("Dole ka yi KYC tukuna")
            else:
                st.session_state.page = 'cable'
                st.rerun()
    with col2:
        if st.button("⚡\n\nElectricity", use_container_width=True):
            if st.session_state.kyc_status != 'approved':
                st.error("Dole ka yi KYC tukuna")
            else:
                st.session_state.page = 'electricity'
                st.rerun()

    st.write("")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("📝\n\nWAEC ePIN", use_container_width=True):
            if st.session_state.kyc_status != 'approved':
                st.error("Dole ka yi KYC tukuna")
            else:
                st.session_state.page = 'waec'
                st.rerun()
    with col2:
        if st.button("📝\n\nJAMB ePIN", use_container_width=True):
            if st.session_state.kyc_status != 'approved':
                st.error("Dole ka yi KYC tukuna")
            else:
                st.session_state.page = 'jamb'
                st.rerun()

    st.write("")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("📞\n\nUSSD Codes", use_container_width=True):
            st.session_state.page = 'ussd'
            st.rerun()
    with col2:
        if st.button("📜\n\nTransactions", use_container_width=True):
            st.session_state.page = 'history'
            st.rerun()

# USSD CODES PAGE - SABON WANNAN
elif st.session_state.page == 'ussd':
    st.subheader("📞 USSD Codes - Saya ba tare da Internet ba")
    st.info("Danna code din don ya copy, sannan ka liƙa a wayarka ka kira")
    
    tab1, tab2, tab3, tab4 = st.tabs(["MTN", "GLO", "AIRTEL", "9MOBILE"])
    
    with tab1:
        st.markdown("### MTN USSD Codes")
        
        st.markdown('<div class="ussd-card">', unsafe_allow_html=True)
        st.markdown("**Check Balance**")
        st.code("*556#", language="text")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="ussd-card">', unsafe_allow_html=True)
        st.markdown("**Buy Airtime for Self**")
        st.code("*556*Amount# e.g *556*100#", language="text")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="ussd-card">', unsafe_allow_html=True)
        st.markdown("**Buy Airtime for Others**")
        st.code("*556*Phone*Amount# e.g *556*08012345678*100#", language="text")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="ussd-card">', unsafe_allow_html=True)
        st.markdown("**Buy Data**")
        st.code("*312#", language="text")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="ussd-card">', unsafe_allow_html=True)
        st.markdown("**Check Data Balance**")
        st.code("*323*4#", language="text")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### GLO USSD Codes")
        
        st.markdown('<div class="ussd-card">', unsafe_allow_html=True)
        st.markdown("**Check Balance**")
        st.code("#124*1#", language="text")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="ussd-card">', unsafe_allow_html=True)
        st.markdown("**Buy Airtime**")
        st.code("*124*Amount# e.g *124*100#", language="text")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="ussd-card">', unsafe_allow_html=True)
        st.markdown("**Buy Data**")
        st.code("*777#", language="text")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="ussd-card">', unsafe_allow_html=True)
        st.markdown("**Check Data Balance**")
        st.code("*127*0#", language="text")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab3:
        st.markdown("### AIRTEL USSD Codes")
        
        st.markdown('<div class="ussd-card">', unsafe_allow_html=True)
        st.markdown("**Check Balance**")
        st.code("*123#", language="text")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="ussd-card">', unsafe_allow_html=True)
        st.markdown("**Buy Airtime**")
        st.code("*123*Amount# e.g *123*
