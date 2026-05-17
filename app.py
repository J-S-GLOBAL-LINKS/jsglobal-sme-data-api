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
[data-testid="stSidebar"] {background-color: #0d47a1;}
[data-testid="stSidebar"] * {color: white;}
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
    color: #333;
    padding: 15px 10px;
}
.service-btn > button:hover {
    border: 1px solid #1976d2;
    box-shadow: 0 4px 8px rgba(0,0,0,0.15);
}
.bank-card {
    background-color: #fff3e0;
    padding: 15px;
    border-radius: 10px;
    border-left: 4px solid #ff9800;
    margin: 1rem 0;
}
</style>
""", unsafe_allow_html=True)

# SECRETS
api_key = st.secrets["SMEPLUG_API_KEY"]
PAYSTACK_SECRET = st.secrets.get("PAYSTACK_SECRET_KEY", "")
PAYSTACK_PUBLIC = st.secrets.get("PAYSTACK_PUBLIC_KEY", "")
SMS_API_KEY = st.secrets.get("TERMII_API_KEY", "")

# BANK DETAILS NA J.S.GLOBAL LINKS - KA CANZA WANNAN
COMPANY_BANK_NAME = "Access Bank"
COMPANY_ACCOUNT_NUMBER = "1234567890"  # SA ACCOUNT DINKA ANAN
COMPANY_ACCOUNT_NAME = "J.S.GLOBAL LINKS AND SERVICES"

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

def send_sms(to, message):
    try:
        if SMS_API_KEY:
            url = "https://api.ng.termii.com/api/sms/send"
            payload = {
                "to": to,
                "from": "JSGLOBAL",
                "sms": message,
                "type": "plain",
                "channel": "generic",
                "api_key": SMS_API_KEY
            }
            requests.post(url, json=payload, timeout=10)
    except:
        pass

balance = get_balance()

# CAC + BANK BANNER
st.markdown(f"""
<div class="cac-banner">
    J.S.GLOBAL LINKS AND SERVICES | CAC: RC 8984371 | {COMPANY_BANK_NAME}: {COMPANY_ACCOUNT_NUMBER} | 07062589825
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
        "fund": "💳 Fund Wallet",
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
    st.caption(f"{COMPANY_BANK_NAME}")
    st.caption(f"Acct: {COMPANY_ACCOUNT_NUMBER}")
    st.caption("Kano, Nigeria | 07062589825")

# HEADER
st.markdown("""
<div class="main-header">
    <div style="font-size: 18px; font-weight: 600;">☰ Dashboard</div>
    <div>🔔</div>
</div>
""", unsafe_allow_html=True)

# FUND WALLET PAGE - DA BANK DETAILS
if st.session_state.page == "fund":
    if st.button("← Back"): 
        st.session_state.page = "dashboard"
        st.rerun()
    st.subheader("Fund Wallet")
    
    tab1, tab2 = st.tabs(["🏦 Bank Transfer", "💳 Paystack Card"])
    
    with tab1:
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
        amount = st.number_input("Amount You Sent (₦)", min_value=100, key="bank_amount")
        if st.button("I Have Paid - Notify Admin", type="primary", use_container_width=True):
            send_sms("07062589825", f"ALERT: Customer paid ₦{amount} to {COMPANY_BANK_NAME}. Verify and credit.")
            st.success("Admin notified! Your wallet will be credited in 5 minutes")
    
    with tab2:
        st.info("Pay with ATM Card, Bank Transfer, or USSD via Paystack")
        with st.form("paystack_form"):
            email = st.text_input("Email", placeholder="your@email.com")
            amount = st.number_input("Amount (₦)", min_value=100, value=1000, key="ps_amount")
            if st.form_submit_button("Pay Now", type="primary", use_container_width=True):
                ref = generate_ref()
                paystack_url = f"https://paystack.com/pay/jsglobal?email={email}&amount={amount*100}&reference={ref}"
                st.success(f"[Click Here to Pay ₦{amount}]({paystack_url})")
                st.code(f"Reference: {ref}")

# DASHBOARD PAGE
elif st.session_state.page == "dashboard":
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
        if st.button("👁️" if st.session_state.show_balance else "👁️‍🗨️", key="toggle_bal"):
            st.session_state.show_balance = not st.session_state.show_balance
            st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Bank details card
    st.markdown(f"""
    <div class="bank-card">
        <div style='font-weight: bold; color: #e65100;'>💰 FUND VIA BANK TRANSFER</div>
        <div style='font-size: 13px; margin-top: 5px;'>
            <b>{COMPANY_BANK_NAME}</b> | {COMPANY_ACCOUNT_NUMBER} | {COMPANY_ACCOUNT_NAME}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([3,1])
    with col1:
        st.markdown("### What would you like to do?")
    with col2:
        if st.button("See all ›"):
            st.session_state.page = "all_services"
            st.rerun()
    
    if st.session_state.kyc_status == "pending":
        st.warning("KYC Required: Go to Menu > KYC Verification to access all services")
    
    # Services grid - kamar da
    col1, col2, col3, col4 = st.columns(4)
    services = [
        ("📱\n\nAirtime", "airtime"),
        ("🌐\n\nData", "data"),
        ("📺\n\nCable\nTV", "cable"),
        ("⚡\n\nElectricity", "electricity"),
        ("🖨️\n\nPrint\nRecharge", "print"),
        ("🎲\n\nFund\nBetting", "betting"),
        ("💸\n\nTransfer\nMoney", "transfer"),
        ("💰\n\nWithdraw\nCommission", "withdraw"),
        ("📝\n\nWAEC\nePIN", "waec"),
        ("📝\n\nJAMB\nePIN", "jamb"),
        ("📡\n\nSmile\nInternet", "smile")
    ]
    
    for i, (label, key) in enumerate(services):
        col = [col1, col2, col3, col4][i % 4]
        with col:
            st.markdown('<div class="service-btn">', unsafe_allow_html=True)
            if st.button(label, key=f"srv_{key}", use_container_width=True):
                st.session_state.page = key
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        if i % 4 == 3:
            st.write("")

# SAURAN PAGES - AIRTIME, DATA, ETC - DA SMS ALERT
elif st.session_state.page == "airtime":
    if st.button("← Back"): 
        st.session_state.page = "dashboard"
        st.rerun()
    st.subheader("Buy Airtime")
    if st.session_state.kyc_status != "approved":
        st.error("Complete KYC first")
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
                        send_sms(phone, f"JSGLOBAL: You received ₦{amount} {network} airtime. CAC: RC8984371")
                        send_sms("07062589825", f"SALE: ₦{amount} {network} to {phone}")
                        st.balloons()
                    else:
                        st.error("Failed: " + res.text)
                except Exception as e:
                    st.error(f"Error: {e}")

# ADMIN PAGE - DA BANK DETAILS EDIT
elif st.session_state.page == "admin":
    if st.button("← Back"):
        st.session_state.page = "dashboard"
        st.rerun()
    st.subheader("Admin Panel - J.S.GLOBAL LINKS RC 8984371")
    admin_pass = st.text_input("Enter Admin Password", type="password")
    if admin_pass == "Jamilu123":
        st.success("Welcome CEO Jamilu")
        st.metric("Total Commission", f"₦{st.session_state.commission}")
        
        st.subheader("Company Bank Details")
        st.info(f"Current: {COMPANY_BANK_NAME} - {COMPANY_ACCOUNT_NUMBER}")
        st.caption("To change, edit COMPANY_BANK_NAME and COMPANY_ACCOUNT_NUMBER in code")
        
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

# SAURAN PAGES KAMAR DA - DATA, CABLE, ETC
else:
    if st.button("← Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()
    st.info(f"{st.session_state.page.title()} service - Coming Soon")
