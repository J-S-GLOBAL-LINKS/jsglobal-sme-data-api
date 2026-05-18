
import streamlit as st
import requests
from datetime import datetime
import random
import string

# ==== KARA WANNAN A NAN LINE 8 ====
if 'wallet_balance' not in st.session_state:
    st.session_state.wallet_balance = 0

if 'menu' not in st.session_state:
    st.session_state.menu = "Dashboard"
# =================================
15 
st.set_page_config(page_title="J.S.GLOBAL LINKS", page_icon="logo.png", layout="wide")

st.image("logo.png", width=200)

# PWA CODE - SA APP YA ZAMA INSTALLABLE
st.markdown("""
...


    # ==== BUTTONS SAU DAYA KAWAI ====
    services = [
        ("📱 Airtime", "Cajin Waya"),
        ("🧾 Print Recharge", "Print Recharge"),
        ("🎓 WAEC ePIN", "WAEC ePIN"),
        ("🌐 Data", "Sayar da Data"),
        ("🎲 Fund Betting", "Fund Betting"),
        ("📝 JAMB ePIN", "JAMB ePIN"),
        ("📺 Cable TV", "Biyan TV"),
        ("💸 Transfer Money", "Transfer Money"),
        ("📶 Smile Internet", "Smile Internet"),
        ("💡 Electricity", "Biyan NEPA"),
        ("💰 Withdraw Commission", "Withdraw Commission"),
    ]

    for i in range(0, len(services), 2):
        col1, col2 = st.columns(2)
        with col1:
            if st.button(services[i][0], key=f"btn_{i}", use_container_width=True):
                st.session_state.menu = services[i][1]
                st.rerun()
        if i+1 < len(services):
            with col2:
                if st.button(services[i+1][0], key=f"btn_{i+1}", use_container_width=True):
                    st.session_state.menu = services[i+1][1]
                    st.rerun()       
        
        
        
        
        
       
        
        
        
       
       
    

            
        
        
      
    
    
    
elif menu == "Sayar da Data":
    st.title("📊 Sayar da Data")
    st.info("Anan zaku sayi data mai rahusa")
    
elif menu == "Cajin Waya":
    st.title("💰 Cajin Waya / Airtime")
    
elif menu == "Biyan TV":
    st.title("📺 Biyan TV - GOTV/DSTV/Startimes")
    
elif menu == "Biyan NEPA":
    st.title("💡 Biyan NEPA / Lantarki")
    
elif menu == "Profile Dina":
    st.title("👤 Profile Dina")
    
elif menu == "Wallet Dina":
    st.title("💳 Wallet Dina")
    
elif menu == "Tarihin Ciniki":
    st.title("📋 Tarihin Ciniki")
    
elif menu == "Settings":
    st.title("⚙️ Settings")
    
elif menu == "Fita":
    st.session_state.logged_in = False
    st.rerun() 
api_key = st.secrets["SMEPLUG_API_KEY"]

# 🔥🔥🔥 CANZA WANNAN ZUWA BANK DINKA 🔥🔥🔥
COMPANY_BANK_NAME = "Access Bank"  
COMPANY_ACCOUNT_NUMBER = "1234567890"  # SA ACCOUNT DINKA ANAN
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

def generate_ref():
    return 'JSG' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

balance = get_balance()

# CAC + BANK BANNER
st.markdown(f"""
<div class="cac-banner">
    J.S.GLOBAL LINKS AND SERVICES | CAC: RC 8984371 | {COMPANY_BANK_NAME}: {COMPANY_ACCOUNT_NUMBER} | 07062589825
</div>
""", unsafe_allow_html=True)

# SIDEBAR
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
    
    st.markdown("<div style='text-align: center; color: #999; font-size: 12px; margin-top: 20px;'>J.S.GLOBAL v1.0</div>", unsafe_allow_html=True)

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
    
    if st.session_state.kyc_status == "pending":
        st.warning("KYC Required: Go to Menu > KYC Verification to access all services")
    
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

# FUND WALLET
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
    """, unsafe_allow_html=True)
    st.success("After payment, send proof to WhatsApp: 07062589825 for instant credit")

# AIRTIME PAGE - YANZU YANA AIKI
elif st.session_state.page == "airtime":
    if st.button("← Back"): 
        st.session_state.page = "dashboard"
        st.rerun()
    st.subheader("Buy Airtime")
    if st.session_state.kyc_status != "approved":
        st.error("Complete KYC first from Menu > KYC Verification")
    else:
        with st.form("airtime_form"):
            network = st.selectbox("Network", ["MTN", "Airtel", "Glo", "9mobile"])
            phone = st.text_input("Phone Number", max_chars=11)
            amount = st.number_input("Amount", min_value=50, max_value=50000)
            if st.form_submit_button("Buy Airtime", type="primary", use_container_width=True):
                payload = {"network": network, "phone": phone, "amount": amount, "ref": generate_ref()}
                try:
                    res = requests.post(BASE_URL + "/airtime/purchase", json=payload, headers=headers, timeout=30)
                    if res.status_code == 200:
                        st.success(f"Airtime ₦{amount} sent to {phone}")
                        st.balloons()
                    else:
                        st.error("Failed: " + res.text)
                except Exception as e:
                    st.error(f"Error: {e}")

# DATA PAGE
elif st.session_state.page == "data":
    if st.button("← Back"): 
        st.session_state.page = "dashboard"
        st.rerun()
    st.subheader("Buy Data")
    if st.session_state.kyc_status != "approved":
        st.error("Complete KYC first")
    else:
        with st.form("data_form"):
            network = st.selectbox("Network", ["MTN", "Airtel", "Glo", "9mobile"])
            phone = st.text_input("Phone Number", max_chars=11)
            plan = st.selectbox("Data Plan", ["1GB - 30 Days - ₦300", "2GB - 30 Days - ₦600", "5GB - 30 Days - ₦1500"])
            if st.form_submit_button("Buy Data", type="primary", use_container_width=True):
                payload = {"network": network, "phone": phone, "plan": plan, "ref": generate_ref()}
                try:
                    res = requests.post(BASE_URL + "/data/purchase", json=payload, headers=headers, timeout=30)
                    if res.status_code == 200:
                        st.success(f"Data {plan} sent to {phone}")
                        st.balloons()
                    else:
                        st.error("Failed: " + res.text)
                except Exception as e:
                    st.error(f"Error: {e}")

# KYC PAGE - YANZU YANA AIKI
elif st.session_state.page == "kyc":
    if st.button("← Back"):
        st.session_state.page = "dashboard"
        st.rerun()
    st.subheader("KYC Verification - J.S.GLOBAL LINKS")
    st.markdown("**CAC: RC 8984371 | Complete this to access services**")
    
    if st.session_state.kyc_status == "approved":
        st.success("✅ Your KYC has been approved! You can now use all services")
    elif st.session_state.kyc_status == "submitted":
        st.info("⏳ Your KYC is pending admin approval. Contact: 07062589825")
    else:
        with st.form("kyc_form"):
            st.write("**Personal Information**")
            full_name = st.text_input("Full Name *", placeholder="Jamilu Sani")
            email = st.text_input("Email *", placeholder="example@gmail.com")
            phone = st.text_input("Phone *", placeholder="07062589825", max_chars=11)
            id_type = st.selectbox("ID Type *", ["NIN", "BVN", "Voter's Card", "Driver's License"])
            id_number = st.text_input(f"{id_type} Number *")
            address = st.text_area("Residential Address *", placeholder="NO.278, LAYIN MAI UNGUWA KANO SAUNA")
            uploaded_file = st.file_uploader("Upload ID Card *", type=["png", "jpg", "jpeg"])
            agree = st.checkbox("I confirm all information is accurate *")
            
            if st.form_submit_button("Submit KYC", type="primary", use_container_width=True):
                if all([full_name, email, phone, id_number, address, uploaded_file, agree]):
                    st.session_state.kyc_status = "submitted"
                    st.success("KYC submitted successfully! Admin will approve within 24hrs")
                    st.balloons()
                    st.rerun()
                else:
                    st.error("All fields marked * are required")

# ADMIN PAGE
elif st.session_state.page == "admin":
    if st.button("← Back"):
        st.session_state.page = "dashboard"
        st.rerun()
    st.subheader("Admin Panel - J.S.GLOBAL LINKS RC 8984371")
    admin_pass = st.text_input("Enter Admin Password", type="password")
    if admin_pass == "Jamilu123":
        st.success("Welcome CEO Jamilu")
        st.metric("Total Commission", f"₦{st.session_state.commission}")
        st.info(f"Company Bank: {COMPANY_BANK_NAME} - {COMPANY_ACCOUNT_NUMBER}")
        
        if st.session_state.kyc_status == "submitted":
            st.warning("⏳ Pending KYC Request")
            if st.button("Approve KYC", type="primary"):
                st.session_state.kyc_status = "approved"
                st.success("KYC Approved!")
                st.rerun()
        else:
            st.info("No pending KYC requests")
    elif admin_pass != "":
        st.error("Wrong Password")

# SAURAN SERVICES - CABLE, ELECTRICITY, ETC
else:
    if st.button("← Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()
    st.subheader(f"{st.session_state.page.title()} Service")
    
    if st.session_state.kyc_status != "approved":
        st.error("Complete KYC first from Menu > KYC Verification")
    else:
        st.info(f"**{st.session_state.page.title()}** service is ready. API integration active.")
        st.write("Contact admin on 07062589825 to process your request")
