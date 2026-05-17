import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="J.S.GLOBAL", page_icon="📱", layout="wide")

st.markdown("""
<style>
/* Blue Theme kamar ClubKonnect */
[data-testid="stAppViewContainer"] {
    background-color: #ffffff;
}
[data-testid="stHeader"] {
    background-color: #0d47a1;
}
[data-testid="stSidebar"] {
    background-color: #0d47a1;
}
[data-testid="stSidebar"] * {
    color: white;
}
.main-header {
    background: #0d47a1;
    padding: 1rem;
    margin: -1rem -1rem 1rem -1rem;
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
    color: #333;
    padding: 15px 10px;
}
.service-btn > button:hover {
    border: 1px solid #1976d2;
    box-shadow: 0 4px 8px rgba(0,0,0,0.15);
}
.upgrade-card {
    background-color: #e3f2fd;
    padding: 15px;
    border-radius: 10px;
    border-left: 4px solid #1976d2;
    margin: 1rem 0;
}
.menu-item {
    padding: 12px 15px;
    border-radius: 8px;
    margin: 5px 0;
    cursor: pointer;
    color: white;
}
.menu-item:hover {
    background-color: rgba(255,255,255,0.1);
}
.menu-item-active {
    background-color: #1565c0;
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

try:
    response = requests.get(BASE_URL + "/account/balance", headers=headers, timeout=10)
    if response.status_code == 200:
        balance = response.json().get("balance", "0")
    else:
        balance = "0"
except Exception:
    balance = "0"

# SIDEBAR - KAMAR CLUBKONNECT
with st.sidebar:
    st.markdown("""
    <div style='text-align: center; padding: 20px 0;'>
        <div style='width: 60px; height: 60px; background: white; border-radius: 50%; margin: 0 auto 10px; display: flex; align-items: center; justify-content: center; font-size: 24px; color: #0d47a1; font-weight: bold;'>J</div>
        <div style='font-weight: bold; font-size: 16px;'>JAMILU</div>
        <div style='font-size: 12px; opacity: 0.8;'>Free Member</div>
        <div style='font-size: 11px; opacity: 0.7;'>CK1028749 Upgrade ></div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Menu Items
    menu_items = {
        "dashboard": "🏠 Dashboard",
        "airtime": "📱 Buy Airtime",
        "data": "🌐 Buy Data", 
        "cable": "📺 CableTV Subscription",
        "electricity": "⚡ Electricity Payment",
        "print": "🖨️ Print Recharge Card",
        "betting": "🎲 Fund Betting Wallet",
        "transfer": "💸 Transfer Money",
        "withdraw": "💰 Withdraw Commission",
        "smile": "📡 Smile Internet",
        "waec": "📝 WAEC ePIN",
        "jamb": "📝 JAMB ePIN"
    }
    
    for key, label in menu_items.items():
        if st.button(label, key=f"menu_{key}", use_container_width=True):
            st.session_state.page = key
            st.rerun()

# HEADER
st.markdown("""
<div class="main-header">
    <div style="font-size: 18px; font-weight: 600;">☰ Dashboard</div>
    <div>🔔</div>
</div>
""", unsafe_allow_html=True)

# DASHBOARD PAGE
if st.session_state.page == "dashboard":
    # Wallet Balance Card
    st.markdown(f"""
    <div class="wallet-card">
        <div style='display: flex; justify-content: space-between; margin-bottom: 10px;'>
            <div style='font-size: 13px; opacity: 0.9;'>WALLET BALANCE</div>
            <div style='font-size: 12px;'>1 of 2 ></div>
        </div>
        <div style='font-size: 32px; font-weight: bold; margin-bottom: 15px;'>{f'₦{balance}' if st.session_state.show_balance else '******'}</div>
        <div style='display: flex; gap: 10px;'>
            <div style='background: rgba(255,255,255,0.2); padding: 8px 15px; border-radius: 8px; font-size: 13px; cursor: pointer;'>+ Fund Wallet</div>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([4,1])
    with col2:
        if st.button("👁️" if st.session_state.show_balance else "👁️‍🗨️", key="toggle_bal"):
            st.session_state.show_balance = not st.session_state.show_balance
            st.rerun()
    
    # Upgrade Card
    st.markdown("""
    <div class="upgrade-card">
        <div style='display: flex; justify-content: space-between; align-items: center;'>
            <div>
                <div style='font-weight: bold; color: #0d47a1; font-size: 15px;'>Upgrade Membership</div>
                <div style='font-size: 12px; color: #555;'>Unlock more discounts and other benefits</div>
            </div>
            <div style='color: #0d47a1; font-size: 20px;'>›</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### What would you like to do?")
    
    # Services Grid
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="service-btn">', unsafe_allow_html=True)
        if st.button("📱\n\nAirtime", key="srv_airtime", use_container_width=True):
            st.session_state.page = "airtime"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="service-btn">', unsafe_allow_html=True)
        if st.button("🌐\n\nData", key="srv_data", use_container_width=True):
            st.session_state.page = "data"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="service-btn">', unsafe_allow_html=True)
        if st.button("📺\n\nCable\nTV", key="srv_cable", use_container_width=True):
            st.session_state.page = "cable"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="service-btn">', unsafe_allow_html=True)
        if st.button("⚡\n\nElectricity", key="srv_electric", use_container_width=True):
            st.session_state.page = "electricity"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="service-btn">', unsafe_allow_html=True)
        if st.button("🖨️\n\nPrint\nRecharge", key="srv_print", use_container_width=True):
            st.info("Coming Soon")
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="service-btn">', unsafe_allow_html=True)
        if st.button("🎲\n\nFund\nBetting", key="srv_betting", use_container_width=True):
            st.info("Coming Soon")
        st.markdown('</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="service-btn">', unsafe_allow_html=True)
        if st.button("💸\n\nTransfer\nMoney", key="srv_transfer", use_container_width=True):
            st.info("Coming Soon")
        st.markdown('</div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="service-btn">', unsafe_allow_html=True)
        if st.button("💰\n\nWithdraw\nCommission", key="srv_withdraw", use_container_width=True):
            st.info("Coming Soon")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="service-btn">', unsafe_allow_html=True)
        if st.button("📝\n\nWAEC\nePIN", key="srv_waec", use_container_width=True):
            st.session_state.page = "waec"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="service-btn">', unsafe_allow_html=True)
        if st.button("📝\n\nJAMB\nePIN", key="srv_jamb", use_container_width=True):
            st.session_state.page = "jamb"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="service-btn">', unsafe_allow_html=True)
        if st.button("📡\n\nSmile\nInternet", key="srv_smile", use_container_width=True):
            st.info("Coming Soon")
        st.markdown('</div>', unsafe_allow_html=True)
    with col4:
        st.write("")

# Sauran pages - Airtime, Data, etc
elif st.session_state.page == "airtime":
    st.subheader("Buy Airtime")
    if st.button("← Back"):
        st.session_state.page = "dashboard"
        st.rerun()
    st.info("Airtime purchase page - Add SMEPlug API integration here")

elif st.session_state.page == "data":
    st.subheader("Buy Data")
    if st.button("← Back"):
        st.session_state.page = "dashboard"
        st.rerun()
    st.info("Data purchase page - Add SMEPlug API integration here")

elif st.session_state.page == "cable":
    st.subheader("CableTV Subscription")
    if st.button("← Back"):
        st.session_state.page = "dashboard"
        st.rerun()
    st.info("Cable TV page - Add SMEPlug API integration here")

elif st.session_state.page == "electricity":
    st.subheader("Electricity Payment")
    if st.button("← Back"):
        st.session_state.page = "dashboard"
        st.rerun()
    st.info("Electricity page - Add SMEPlug API integration here")

else:
    if st.button("← Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()
    st.info("This service is coming soon")
