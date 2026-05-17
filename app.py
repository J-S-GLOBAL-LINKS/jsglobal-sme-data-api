import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="J.S.GLOBAL LINKS", page_icon="logo.png", layout="wide")

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: #f8f9fa;
}
div[data-testid="stButton"] > button {
    height: 90px;
    background-color: white;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    font-size: 13px;
    font-weight: 600;
    text-align: center;
    padding: 10px 5px;
    white-space: pre-line;
    line-height: 1.2;
}
div[data-testid="stButton"] > button:hover {
    box-shadow: 0 4px 8px rgba(0,0.15);
    border: 1px solid #2a5298;
    color: #2a5298;
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
.copy-btn > button {
    background-color: #2a5298 !important;
    color: white !important;
    border: none !important;
    height: 35px !important;
    font-size: 13px !important;
    margin-top: 5px !important;
}
</style>
""", unsafe_allow_html=True)

api_key = st.secrets["SMEPLUG_API_KEY"]
BASE_URL = "https://smeplug.ng/api/v1"
headers = {
    "Authorization": "Bearer " + api_key,
    "Content-Type": "application/json"
}

if "page" not in st.session_state:
    st.session_state.page = "dashboard"
if "show_balance" not in st.session_state:
    st.session_state.show_balance = True
if "kyc_status" not in st.session_state:
    st.session_state.kyc_status = "pending"
if "user_data" not in st.session_state:
    st.session_state.user_data = {}
if "copied_code" not in st.session_state:
    st.session_state.copied_code = ""

try:
    response = requests.get(BASE_URL + "/account/balance", headers=headers, timeout=10)
    if response.status_code == 200:
        balance = response.json().get("balance", "0")
    else:
        balance = "0"
except Exception:
    balance = "0"

def copy_code(code):
    st.session_state.copied_code = code
    st.toast(f"Copied {code}", icon="✅")

with st.sidebar:
    st.image("logo.png", width=80)
    st.markdown("### J.S.GLOBAL LINKS")
    st.caption("RC: 8984371")
    
    if st.session_state.kyc_status == "approved":
        st.success("KYC Verified")
    elif st.session_state.kyc_status == "submitted":
        st.warning("KYC Pending")
    else:
        st.error("KYC Required")
    
    st.markdown("---")
    
    if st.button("🏠 Dashboard", use_container_width=True):
        st.session_state.page = "dashboard"
        st.rerun()
    
    if st.button("👤 My Profile", use_container_width=True):
        st.session_state.page = "profile"
        st.rerun()
    
    if st.button("✅ KYC Verification", use_container_width=True):
        st.session_state.page = "kyc"
        st.rerun()
    
    if st.button("📱 USSD Codes", use_container_width=True):
        st.session_state.page = "ussd"
        st.rerun()
    
    if st.button("📊 Transactions", use_container_width=True):
        st.session_state.page = "history"
        st.rerun()
    
    if st.button("🔐 Admin Panel", use_container_width=True):
        st.session_state.page = "admin"
        st.rerun()
    
    st.markdown("---")
    st.caption("Kano, Nigeria")
    st.caption("07062589825")

col1, col2 = st.columns([1, 8])
with col1:
    st.image("logo.png", width=50)
with col2:
    st.markdown("### J.S.GLOBAL LINKS AND SERVICES")
    st.caption("CAC: RC 8984371 | GENERAL MERCHANDISE")

if st.session_state.page != "dashboard":
    if st.button("← Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()
    st.markdown("---")

if st.session_state.page == "dashboard":
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); padding: 2rem; border-radius: 15px; color: white; margin-bottom: 1rem;'>
        <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;'>
            <div style='font-size: 14px; opacity: 0.9;'>WALLET BALANCE</div>
            <div style='font-size: 12px; opacity: 0.8;'>1 of 2 ></div>
        </div>
        <div style='font-size: 32px; font-weight: bold; margin-bottom: 1.5rem;'>{f'N{balance}' if st.session_state.show_balance else '******'}</div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([3, 1, 3])
    with col1:
        if st.button("➕ Fund Wallet", use_container_width=True):
            st.info("Za a tura ka zuwa SMEPlug don cika wallet. Ko ka tuntube mu: 07062589825")
    with col2:
        if st.button("🔄", key="refresh"):
            st.rerun()
    with col3:
        if st.button("👁️", key="eye"):
            st.session_state.show_balance = not st.session_state.show_balance
            st.rerun()
    
    st.write("")
    
    st.markdown("""
    <div style='background-color: #e8eaf6; padding: 15px; border-radius: 12px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;'>
        <div>
            <div style='font-weight: bold; color: #1e3c72; font-size: 16px;'>Upgrade Membership</div>
            <div style='font-size: 13px; color: #5c6bc0;'>Unlock more discounts and other benefits</div>
        </div>
        <div style='font-size: 24px; color: #1e3c72;'>›</div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("### What would you like to do?")
    with col2:
        st.markdown("<div style='text-align: right; color: #2a5298; font-weight: 600; padding-top: 10px;'>See all ›</div>", unsafe_allow_html=True)
    
    st.write("")
    
    if st.session_state.kyc_status == "pending":
        st.markdown('<div class="kyc-warning">', unsafe_allow_html=True)
        st.warning("KYC Required: Ka kammala KYC Verification don amfani da duk services.")
        if st.button("Verify KYC Now", type="primary"):
            st.session_state.page = "kyc"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
        st.write("")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("📞\n\nAirtime", use_container_width=True, key="btn_airtime"):
            if st.session_state.kyc_status != "approved":
                st.error("Dole ka yi KYC tukuna")
            else:
                st.session_state.page = "airtime"
                st.rerun()
    with col2:
        if st.button("🌐\n\nData", use_container_width=True, key="btn_data"):
            if st.session_state.kyc_status != "approved":
                st.error("Dole ka yi KYC tukuna")
            else:
                st.session_state.page = "data"
                st.rerun()
    with col3:
        if st.button("📺\n\nCable\nTV", use_container_width=True, key="btn_cable"):
            if st.session_state.kyc_status != "approved":
                st.error("Dole ka yi KYC tukuna")
            else:
                st.session_state.page = "cable"
                st.rerun()
    with col4:
        if st.button("💡\n\nElectricity", use_container_width=True, key="btn_electric"):
            if st.session_state.kyc_status != "approved":
                st.error("Dole ka yi KYC tukuna")
            else:
                st.session_state.page = "electricity"
                st.rerun()
    
    st.write("")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("🖨️\n\nPrint\nRecharge", use_container_width=True, key="btn_print"):
            st.info("Coming Soon")
    with col2:
        if st.button("🎲\n\nFund\nBetting", use_container_width=True, key="btn_betting"):
            st.info("Coming Soon")
    with col3:
        if st.button("💸\n\nTransfer\nMoney", use_container_width=True, key="btn_transfer"):
            st.info("Coming Soon")
    with col4:
        if st.button("💰\n\nWithdraw\nCommission", use_container_width=True, key="btn_withdraw"):
            st.info("Coming Soon")
    
    st.write("")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("📝\n\nWAEC\nePIN", use_container_width=True, key="btn_waec"):
            if st.session_state.kyc_status != "approved":
                st.error("Dole ka yi KYC tukuna")
            else:
                st.session_state.page = "waec"
                st.rerun()
    with col2:
        if st.button("📝\n\nJAMB\nePIN", use_container_width=True, key="btn_jamb"):
            if st.session_state.kyc_status != "approved":
                st.error("Dole ka yi KYC tukuna")
            else:
                st.session_state.page = "jamb"
                st.rerun()
    with col3:
        if st.button("📡\n\nSmile\nInternet", use_container_width=True, key="btn_smile"):
            st.info("Coming Soon")
    with col4:
        st.write("")
    
    st.write("")
    
    st.markdown("""
    <div style='background-color: #e8eaf6; padding: 15px; border-radius: 12px; display: flex; justify-content: space-between; align-items: center;'>
        <div style='display: flex; align-items: center; gap: 15px;'>
            <div style='font-size: 32px;'>❓</div>
            <div>
                <div style='font-weight: bold; color: #1e3c72; font-size: 16px;'>Need Help?</div>
                <div style='font-size: 13px; color: #5c6bc0;'>Try our self service or open a ticket</div>
            </div>
        </div>
        <div style='font-size: 24px; color: #1e3c72;'>›</div>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.page == "ussd":
    st.subheader("USSD Codes - NCC 2026")
    st.success("Sabbin codes da NCC ta hada su daya ga duk networks")
    
    if st.session_state.copied_code:
        st.info(f"Copied: {st.session_state.copied_code} - Yanzu liqa a wayarka ka kira!")
        st.session_state.copied_code = ""
    
    st.warning("Tsofaffin codes kamar *556#, *131#, *555* sun daina aiki!")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🟡 MTN", "🟢 GLO", "🔴 AIRTEL", "🟡 9MOBILE"])
    
    with tab1:
        st.markdown("### 🟡 MTN USSD Codes - 2026")
        col1, col2 = st.columns([3,1])
        with col1:
            st.markdown('<div class="ussd-card">', unsafe_allow_html=True)
            st.markdown("**Check Airtime Balance**")
            st.code("*310#", language="text")
            st.caption("Tsohon: *556#")
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="copy-btn">', unsafe_allow_html=True)
            if st.button("Copy", key="mtn_balance"):
                copy_code("*310#")
            st.markdown("</div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([3,1])
        with col1:
            st.markdown('<div class="ussd-card">', unsafe_allow_html=True)
            st.markdown("**Buy Data**")
            st.code("*312#", language="text")
            st.caption("Tsohon: *131#")
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="copy-btn">', unsafe_allow_html=True)
            if st.button("Copy", key="mtn_data"):
                copy_code("*
