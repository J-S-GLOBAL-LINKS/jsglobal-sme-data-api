import streamlit as st
import requests
from datetime import datetime
import random
import string

#SMEPLUG API CONFIG
SMEPLUG_BASE_URL = "https://smeplug.ng/api/v1"
API_KEY = st.secrets["SMEPLUG_API_KEY"]

def buy_data(network, phone, plan_id):  # <--- Ba space a gaba
    url = f"{SMEPLUG_BASE_URL}/data"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "network": network,
        "phone": phone,
        "plan": plan_id
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()      
def get_data_plans(network):
   url = f"{SMEPLUG_BASE_URL}/data/plans"
   headers = {"Authorization": f"Bearer {API_KEY}"}
   params = {"network": network}
   response = requests.get(url, headers=headers, params=params)
   return response.json()
# ==== SESSION STATE - KADA KA TABA WANNAN ====
if 'wallet_balance' not in st.session_state:
    st.session_state.wallet_balance = 0

if 'commission' not in st.session_state:
    st.session_state.commission = 150.00

if 'menu' not in st.session_state:
    st.session_state.menu = "Dashboard"
# ==============================================

st.set_page_config(page_title="J.S.GLOBAL LINKS", page_icon="logo.png", layout="wide")

st.image("logo.png", width=200)

# PWA CODE - SA APP YA ZAMA INSTALLABLE
st.markdown("""
<link rel="manifest" href="./manifest.json">
<meta name="theme-color" content="#0d47a1">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="JSGlobal">
<link rel="apple-touch-icon" href="logo.png">
<script>
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('./sw.js');
}
# CSS - DESIGN
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {background-color: #ffffff;}
[data-testid="stHeader"] {background-color: #0d47a1;}
[data-testid="stSidebar"] {background-color: white !important;}

[data-testid="stSidebar"] .stButton > button {
    background-color: white !important;
    color: #333333 !important;
    font-weight: 500 !important;
    border: none !important;
    text-align: left !important;
    padding: 4px 6px !important;
    font-size: 11px !important;
    border-radius: 5px !important;
    margin: 1px 0px !important;
    line-height: 1.1 !important;
    height: 30px !important;
}

[data-testid="stSidebar"] .stButton > button p {
    font-size: 11px !important;
}

[data-testid="stSidebar"] button div[data-testid="stMarkdownContainer"] p {
    font-size: 11px !important;
}

[data-testid="stSidebar"] .stButton > button:hover {
    background-color: #0d47a1 !important;
    color: white !important;
}

.stButton > button {
    background-color: #0d47a1;
    color: white;
    border-radius: 8px;
    border: none;
    padding: 10px;
    font-weight: 600;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# ==== SIDEBAR MENU ====
with st.sidebar:
    st.markdown("### Menu")
    
    if st.button("🏠 Dashboard"):
        st.session_state.menu = "Dashboard"
    if st.button("💰 Fund Wallet"):
        st.session_state.menu = "Fund Wallet"
    if st.button("👤 KYC Verification"):
        st.session_state.menu = "KYC"
    if st.button("📱 Airtime"):
        st.session_state.menu = "Airtime"
    if st.button("🖨️ Print Recharge"):
        st.session_state.menu = "Print"
    if st.button("🎓 WAEC ePIN"):
        st.session_state.menu = "WAEC"
    if st.button("🌐 Data"):
        st.session_state.menu = "Data"
    if st.button("🎰 Fund Betting"):
        st.session_state.menu = "Betting"
    if st.button("🎓 JAMB ePIN"):
        st.session_state.menu = "JAMB"
    if st.button("📺 Cable TV"):
        st.session_state.menu = "Cable"
    if st.button("💸 Transfer Money"):
        st.session_state.menu = "Transfer"

# ==== DASHBOARD ====
if st.session_state.menu == "Dashboard":
    
    st.markdown(f"""
    <div class="wallet-card">
        <h3>J.S GLOBAL LINKS</h3>
        <p>WALLET BALANCE</p>
        <h1>₦{st.session_state.wallet_balance}</h1>
        <p>Commission: ₦{st.session_state.commission}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### What would you like to do?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📱 Airtime", key="dash_airtime"):
            st.session_state.menu = "Airtime"
        if st.button("🖨️ Print Recharge", key="dash_print"):
            st.session_state.menu = "Print"
        if st.button("🎓 WAEC ePIN", key="dash_waec"):
            st.session_state.menu = "WAEC"
        if st.button("🌐 Data", key="dash_data"):
            st.session_state.menu = "Data"
        if st.button("🎰 Fund Betting", key="dash_bet"):
            st.session_state.menu = "Betting"
            
    with col2:
        if st.button("🎓 JAMB ePIN", key="dash_jamb"):
            st.session_state.menu = "JAMB"
        if st.button("📺 Cable TV", key="dash_cable"):
            st.session_state.menu = "Cable"
        if st.button("💸 Transfer Money", key="dash_transfer"):
            st.session_state.menu = "Transfer"
        if st.button("😊 Smile Internet", key="dash_smile"):
            st.info("Coming Soon")
        if st.button("⚡ Electricity", key="dash_electric"):
            st.info("Coming Soon")

# ==== FUND WALLET ====
elif st.session_state.menu == "Fund Wallet":
    st.title("💰 Fund Wallet")
    st.info("KYC Required: Go to Menu > KYC Verification to access all services")
    
    st.markdown("""
    ### FUND VIA BANK TRANSFER
    **Access Bank: 1234567890**  
    **J.S.GLOBAL LINKS AND SERVICES**
    """)

# ==== DATA ====
elif st.session_state.menu == "Data":
    st.title("🌐 Buy Data")
    st.info("KYC Required: Go to Menu > KYC Verification to access all services")
    
    network = st.selectbox("Select Network", ["MTN", "Glo", "Airtel", "9mobile"])
    phone = st.text_input("Phone Number", placeholder="08012345678")
    plan = st.selectbox("Select Plan", ["1GB - ₦300", "2GB - ₦500", "5GB - ₦1000"])
    
    if st.button("Buy Data Now"):
        st.warning("Service coming soon. Integrate SMEPlug API to activate.")

# ==== AIRTIME ====
elif st.session_state.menu == "Airtime":
    st.title("📱 Buy Airtime")
    st.info("KYC Required: Go to Menu > KYC Verification to access all services")
    
    network = st.selectbox("Select Network", ["MTN", "Glo", "Airtel", "9mobile"], key="airtime_net")
    phone = st.text_input("Phone Number", placeholder="08012345678", key="airtime_phone")
    amount = st.number_input("Amount", min_value=50, max_value=50000, step=50)
    
    if st.button("Buy Airtime Now"):
        st.warning("Service coming soon. Integrate SMEPlug API to activate.")

# ==== SAURAN PAGES ====
elif st.session_state.menu == "KYC":
    st.title("👤 KYC Verification")
    st.info("Upload your documents to verify your account")
    st.warning("KYC system coming soon")

elif st.session_state.menu == "Print":
    st.title("🖨️ Print Recharge")
    st.warning("Service coming soon")

elif st.session_state.menu == "WAEC":
    st.title("🎓 WAEC ePIN")
    st.warning("Service coming soon")

elif st.session_state.menu == "Betting":
    st.title("🎰 Fund Betting")
    st.warning("Service coming soon")

elif st.session_state.menu == "JAMB":
    st.title("🎓 JAMB ePIN")
    st.warning("Service coming soon")

elif st.session_state.menu == "Cable":
    st.title("📺 Cable TV")
    st.warning("Service coming soon")

elif st.session_state.menu == "Transfer":
    st.title("💸 Transfer Money")
    st.warning("Service coming soon")

# ==== FOOTER ====
st.markdown("---")
st.markdown("J.S.GLOBAL LINKS AND SERVICES | CAC: RC 8984371 | Access Bank: 1234567890 | 07062589825")
