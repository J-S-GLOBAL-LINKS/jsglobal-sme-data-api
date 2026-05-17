import streamlit as st
import requests
from datetime import datetime
import random
import string

st.set_page_config(page_title="J.S.GLOBAL LINKS", page_icon="📱", layout="wide")

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {background-color: #ffffff;}
[data-testid="stHeader"] {background-color: #0d47a1;}

/* SIDEBAR KAMAR CLUBKONNECT */
[data-testid="stSidebar"] {
    background-color: white !important;
    padding-top: 0rem;
}
[data-testid="stSidebar"] .stButton > button {
    background-color: white !important;
    color: #333333 !important;
    font-weight: 500 !important;
    border: none !important;
    text-align: left !important;
    padding: 12px 20px !important;
    border-radius: 0px !important;
    justify-content: flex-start !important;
}
[data-testid="stSidebar"] .stButton > button:hover {
    background-color: #0d47a1 !important;
    color: white !important;
    border-radius: 0px 25px 25px 0px !important;
}
[data-testid="stSidebar"] .stButton > button:focus {
    background-color: #0d47a1 !important;
    color: white !important;
    border-radius: 0px 25px 25px 0px !important;
    box-shadow: none !important;
}
[data-testid="stSidebar"] * {color: #333333;}

.cac-banner {
    background: #0d47a1;
    color: white;
    padding: 10px;
    text-align: center;
    font-weight: bold;
    margin: -1rem -1rem 1rem -1rem;
    font-size: 13px;
}
.main-header {
    background: #0d47a1;
    padding: 1rem;
    margin: 0 -1rem 1rem -1rem;
    color: white;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.wallet-card {
    background: linear-gradient(135deg, #0d47a1 0%, #1976d2 100%);
    padding: 1.5rem;
    border-radius: 12px;
    color: white;
    margin-bottom: 1rem;
}
.service-btn > button {
    height: 100px;
    background-color: white;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    font-size: 14px;
    font-weight: 500;
    color: #333 !important;
    padding: 15px 10px;
}
.bank-card {
    background-color: #fff3e0;
    padding: 15px;
    border-radius: 10px;
    border-left: 4px solid #ff9800;
    margin: 1rem 0;
}
.signout-btn > button {
    background-color: #e91e63 !important;
    color: white !important;
    font-weight: bold !important;
    border-radius: 25px !important;
    padding: 12px !important;
    margin-top: 20px !important;
}
.help-btn {
    position: fixed;
    bottom: 80px;
    right: 20px;
    background-color: #00bcd4;
    color: white;
    border-radius: 50%;
    width: 60px;
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 12px;
    font-weight: bold;
    box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    z-index: 999;
}
</style>
""", unsafe_allow_html=True)

api_key = st.secrets["SMEPLUG_API_KEY"]

# BANK DETAILS NA J.S.GLOBAL LINKS - KA CANZA WANNAN
COMPANY_BANK_NAME = "Access Bank"
COMPANY_ACCOUNT_NUMBER = "1234567890"  # SA ACCOUNT DINKA
COMPANY_ACCOUNT_NAME = "J.S.GLOBAL LINKS AND SERVICES"

BASE_URL = "https://smeplug.ng/api/v1"
headers = {"Authorization": "Bearer " + api_key, "Content-Type": "application/json"}

if "page" not in st.session_state:
    st.session_state.page = "dashboard"
if "show_balance" not in st.session_state:
    st.session_state.show_balance = True
if "kyc_status" not in st.session_state:
    st.session_state.kyc_status = "pending"
if "commission" not in st.session_state:
    st.session_state.commission = "150.00"

def get_balance():
    try:
        response = requests.get(BASE_URL + "/account/balance", headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json().get("balance", "0")
        return "0"
    except:
        return "0"

balance = get_balance()

# CAC + BANK BANNER
st.markdown(f"""
<div class="cac-banner">
    J.S.GLOBAL LINKS AND SERVICES | CAC: RC 8984371 | {COMPANY_BANK_NAME}: {COMPANY_ACCOUNT_NUMBER} | 07062589825
</div>
""", unsafe_allow_html=True)

# SIDEBAR - KAMAR CLUBKONNECT
with st.sidebar:
    st.markdown("<div style='padding: 15px; font-weight: bold; color: #666;'>MENU</div>", unsafe_allow_html=True)
    
    menu_items = {
        "dashboard": "🏠 Dashboard",
        "airtime": "📱 Buy Airtime",
        "data": "🌐 Buy Data", 
        "cable": "📺 CableTV Subscription",
        "electricity": "⚡ Electricity Payment",
        "print": "📄 Print Recharge Card",
        "betting": "🎲 Fund Betting Wallet",
        "transfer": "🔄 Transfer Money",
        "withdraw": "⬇️ Withdraw Commission",
        "smile": "🌐 Smile Internet",
        "waec": "📝 WAEC ePIN",
        "jamb": "📝 JAMB ePIN",
        "kyc": "✅ KYC Verification",
        "admin": "🔐 Admin Panel"
    }
    
    for key, label in menu_items.items():
        if st.button(label, key=f"menu_{key}", use_container_width=True):
            st.session_state.page = key
            st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="signout-btn">', unsafe_allow_html=True)
    if st.button("Sign Out >", use_container_width=True):
        st.info("Signed out successfully")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<div style='text-align: center; color: #999; font-size: 12px; margin-top: 20px;'>J.S.GLOBAL v1.0</div>", unsafe_allow_html=True)

# NEED HELP BUTTON
st.markdown("""
<div class="help-btn">
    Need<br>Help?
</div>
""", unsafe_allow_html=True)

# HEADER
st.markdown("""
<div class="main-header">
    <div style="font-size: 18px; font-weight: 600;">☰ Dashboard</div>
    <div>🔔</div>
</div>
""", unsafe_allow_html=True)

# DASHBOARD
if st.session_state.page == "dashboard":
    st.markdown(f"""
    <div class="wallet-card">
        <div style='display: flex; justify-content: space-between; margin-bottom: 10px;'>
            <div style='font-size: 13px; opacity: 0.9;'>WALLET BALANCE</div>
            <div style='font-size: 12px;'>Commission: ₦{st.session_state.commission}</div>
        </div>
        <div style='font-size: 32px; font-weight: bold; margin-bottom: 15px;'>{f'₦{balance}' if st.session_state.show_balance else '******'}</div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([3,1,3])
    with col1:
        if st.button("+ Fund Wallet", use_container_width=True):
            st.session_state.page = "fund"
            st.rerun()
    with col3:
        if st.button("👁️" if st.session_state.show_balance else "👁️‍🗨️"):
            st.session_state.show_balance = not st.session_state.show_balance
            st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="bank-card">
        <div style='font-weight: bold; color: #e65100;'>💰 FUND VIA BANK TRANSFER</div>
        <div style='font-size: 13px; margin-top: 5px;'>
            <b>{COMPANY_BANK_NAME}</b> | {COMPANY_ACCOUNT_NUMBER} | {COMPANY_ACCOUNT_NAME}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### What would you like to do?")
    
    services = [
        ("📱\n\nAirtime", "airtime"),
        ("🌐\n\nData", "data"),
        ("📺\n\nCable\nTV", "cable"),
        ("⚡\n\nElectricity", "electricity"),
        ("📄\n\nPrint\nRecharge", "print"),
        ("🎲\n\nFund\nBetting", "betting"),
        ("🔄\n\nTransfer\nMoney", "transfer"),
        ("⬇️\n\nWithdraw\nCommission", "withdraw")
    ]
    
    cols = st.columns(4)
    for i, (label, key) in enumerate(services):
        with cols[i % 4]:
            st.markdown('<div class="service-btn">', unsafe_allow_html=True)
            if st.button(label, key=f"srv_{key}", use_container_width=True):
                st.session_state.page = key
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        if i % 4 == 3:
            st.write("")

# FUND WALLET PAGE
elif st.session_state.page == "fund":
    if st.button("← Back"): 
        st.session_state.page = "dashboard"
        st.rerun()
    st.subheader("Fund Wallet")
    
    st.markdown(f"""
    <div class="bank-card">
        <div style='font-weight: bold; font-size: 16px; color: #e65100; margin-bottom: 10px;'>J.S.GLOBAL LINKS BANK DETAILS</div>
        <div style='font-size: 14px; line-height: 1.8;'>
            <b>Bank Name:</b> {COMPANY_BANK_NAME}<br>
            <b>Account Number:</b> {COMPANY_ACCOUNT_NUMBER}<br>
            <b>Account Name:</b> {COMPANY_ACCOUNT_NAME}<br>
            <b>CAC Number:</b> RC 8984371
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.warning("After payment, send proof to WhatsApp: 07062589825 for instant credit")

# SAURAN PAGES
else:
    if st.button("← Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()
    st.info(f"{st.session_state.page.title()} service - Coming Soon")
