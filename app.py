import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="J.S.GLOBAL LINKS", page_icon="📱", layout="wide")

st.markdown("""
<style>
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
.cac-banner {
    background: #0d47a1;
    color: white;
    padding: 10px;
    text-align: center;
    font-weight: bold;
    margin: -1rem -1rem 1rem -1rem;
    font-size: 14px;
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
if "search_query" not in st.session_state:
    st.session_state.search_query = ""

try:
    response = requests.get(BASE_URL + "/account/balance", headers=headers, timeout=10)
    if response.status_code == 200:
        balance = response.json().get("balance", "0")
    else:
        balance = "0"
except Exception:
    balance = "0"

# CAC BANNER - YANA KAN KO WANE PAGE
st.markdown("""
<div class="cac-banner">
    J.S.GLOBAL LINKS AND SERVICES | CAC: RC 8984371 | Kano, Nigeria | 07062589825
</div>
""", unsafe_allow_html=True)

# SIDEBAR
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
        "jamb": "📝 JAMB ePIN",
        "kyc": "✅ KYC Verification",
        "admin": "🔐 Admin Panel"
    }
    
    for key, label in menu_items.items():
        if st.button(label, key=f"menu_{key}", use_container_width=True):
            st.session_state.page = key
            st.rerun()
    
    st.markdown("---")
    st.caption("J.S.GLOBAL LINKS AND SERVICES")
    st.caption("RC: 8984371")
    st.caption("Kano, Nigeria | 07062589825")

# HEADER
if st.session_state.page == "all_services":
    st.markdown("""
    <div class="main-header">
        <div style="font-size: 18px; font-weight: 600;">All Services</div>
        <div>Close</div>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="main-header">
        <div style="font-size: 18px; font-weight: 600;">☰ Dashboard</div>
        <div>🔔</div>
    </div>
    """, unsafe_allow_html=True)

# ALL SERVICES PAGE
if st.session_state.page == "all_services":
    search = st.text_input("", placeholder="🔍 Search", key="search_input", label_visibility="collapsed")
    st.session_state.search_query = search.lower()
    
    if st.button("← Back to Dashboard", key="back_from_all"):
        st.session_state.page = "dashboard"
        st.rerun()
    
    st.write("")
    
    all_services = [
        {"name": "Airtime", "icon": "📱", "key": "airtime"},
        {"name": "Data", "icon": "🌐", "key": "data"},
        {"name": "Cable TV", "icon": "📺", "key": "cable"},
        {"name": "Electricity", "icon": "⚡", "key": "electricity"},
        {"name": "Print Recharge", "icon": "🖨️", "key": "print"},
        {"name": "Fund Betting", "icon": "🎲", "key": "betting"},
        {"name": "Transfer Money", "icon": "💸", "key": "transfer"},
        {"name": "Withdraw Commission", "icon": "💰", "key": "withdraw"},
        {"name": "WAEC ePIN", "icon": "📝", "key": "waec"},
        {"name": "JAMB ePIN", "icon": "📝", "key": "jamb"},
        {"name": "Smile Internet", "icon": "📡", "key": "smile"}
    ]
    
    filtered_services = [s for s in all_services if st.session_state.search_query in s["name"].lower()]
    
    cols = st.columns(3)
    for idx, service in enumerate(filtered_services):
        with cols[idx % 3]:
            st.markdown('<div class="service-btn">', unsafe_allow_html=True)
            if st.button(f"{service['icon']}\n\n{service['name']}", key=f"all_{service['key']}", use_container_width=True):
                st.session_state.page = service['key']
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

# DASHBOARD PAGE
elif st.session_state.page == "dashboard":
    st.markdown(f"""
    <div class="wallet-card">
        <div style='display: flex; justify-content: space-between; margin-bottom: 10px;'>
            <div style='font-size: 13px; opacity: 0.9;'>WALLET BALANCE</div>
            <div style='font-size: 12px;'>1 of 2 ></div>
        </div>
        <div style='font-size: 32px; font-weight: bold; margin-bottom: 15px;'>{f'₦{balance}' if st.session_state.show_balance else '******'}</div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([3,1,3])
    with col1:
        if st.button("+ Fund Wallet", use_container_width=True):
            st.info("Contact: 07062589825 to fund wallet")
    with col3:
        if st.button("👁️" if st.session_state.show_balance else "👁️‍🗨️", key="toggle_bal"):
            st.session_state.show_balance = not st.session_state.show_balance
            st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)
    
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
    
    col1, col2 = st.columns([3,1])
    with col1:
        st.markdown("### What would you like to do?")
    with col2:
        if st.button("See all ›", key="see_all_btn"):
            st.session_state.page = "all_services"
            st.rerun()
    
    if st.session_state.kyc_status == "pending":
        st.warning("KYC Required: Go to Menu > KYC Verification to access all services")
    
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

# KYC PAGE
elif st.session_state.page == "kyc":
    if st.button("← Back"):
        st.session_state.page = "dashboard"
        st.rerun()
    st.subheader("KYC Verification - J.S.GLOBAL LINKS")
    st.markdown("**CAC: RC 8984371 | Complete this to access services**")
    
    if st.session_state.kyc_status == "approved":
        st.success("Your KYC has been approved")
    else:
        with st.form("kyc_form"):
            full_name = st.text_input("Full Name *", placeholder="Jamilu Sani")
            email = st.text_input("Email *", placeholder="example@gmail.com")
            phone = st.text_input("Phone *", placeholder="07062589825", max_chars=11)
            id_type = st.selectbox("ID Type *", ["NIN", "BVN", "Voter's Card"])
            id_number = st.text_input(f"ID Number *")
            address = st.text_area("Address *", placeholder="NO.278, LAYIN MAI UNGUWA KANO SAUNA")
            uploaded_file = st.file_uploader("Upload ID *", type=["png", "jpg", "jpeg"])
            agree = st.checkbox("I confirm information is accurate *")
            
            if st.form_submit_button("Submit KYC", type="primary", use_container_width=True):
                if all([full_name, email, phone, id_number, address, uploaded_file, agree]):
                    st.session_state.kyc_status = "submitted"
                    st.success("KYC submitted! Contact 07062589825 for approval")
                    st.rerun()
                else:
                    st.error("All fields are required")

# ADMIN PAGE
elif st.session_state.page == "admin":
    if st.button("← Back"):
        st.session_state.page = "dashboard"
        st.rerun()
    st.subheader("Admin Panel - J.S.GLOBAL LINKS RC 8984371")
    admin_pass = st.text_input("Enter Admin Password", type="password")
    if admin_pass == "Jamilu123":
        st.success("Welcome CEO Jamilu")
        if st.session_state.kyc_status == "submitted":
            st.warning("Pending KYC Request")
            if st.button("Approve KYC", type="primary"):
                st.session_state.kyc_status = "approved"
                st.success("KYC Approved!")
                st.rerun()
        else:
            st.info("No pending KYC")
    elif admin_pass != "":
        st.error("Wrong Password")

# Sauran pages
else:
    if st.button("← Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()
    st.subheader(st.session_state.page.title())
    if st.session_state.kyc_status != "approved":
        st.error("Complete KYC first: Menu > KYC Verification")
    else:
        st.info(f"{st.session_state.page.title()} service - Coming Soon. Contact 07062589825")
