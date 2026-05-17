import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="J.S.GLOBAL LINKS", page_icon="logo.png", layout="wide")

# CSS
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: #f8f9fa;
}
div[data-testid="stButton"] > button {
    height: 60px;
    background-color: white;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    font-size: 15px;
    font-weight: 600;
    text-align: left;
    padding-left: 15px;
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

# API SETUP
api_key = st.secrets["SMEPLUG_API_KEY"]
BASE_URL = "https://smeplug.ng/api/v1"
headers = {
    "Authorization": "Bearer " + api_key,
    "Content-Type": "application/json"
}

# SESSION STATE
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

# SAMO BALANCE
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
    st.toast(f"Copied {code} - Liqa a wayarka!", icon="✅")

# SIDEBAR
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

# HEADER
col1, col2 = st.columns([1, 8])
with col1:
    st.image("logo.png", width=50)
with col2:
    st.markdown("### J.S.GLOBAL LINKS AND SERVICES")
    st.caption("CAC: RC 8984371 | GENERAL MERCHANDISE")

# BACK BUTTON
if st.session_state.page != "dashboard":
    if st.button("← Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()
    st.markdown("---")

# DASHBOARD
if st.session_state.page == "dashboard":
    if st.session_state.kyc_status == "pending":
        st.markdown('<div class="kyc-warning">', unsafe_allow_html=True)
        st.warning("KYC Required: Ka kammala KYC Verification don amfani da duk services.")
        if st.button("Verify KYC Now", type="primary"):
            st.session_state.page = "kyc"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
        st.write("")

    st.markdown('<div class="wallet-container">', unsafe_allow_html=True)
    st.markdown("##### WALLET BALANCE")
    col1, col2, col3 = st.columns([6,1,1])
    with col1:
        if st.session_state.show_balance:
            st.markdown(f"## N{balance}")
        else:
            st.markdown("## ******")
    with col2:
        if st.button("👁️", key="eye"):
            st.session_state.show_balance = not st.session_state.show_balance
            st.rerun()
    with col3:
        if st.button("🔄", key="refresh"):
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="fund-btn">', unsafe_allow_html=True)
    if st.button("Fund Wallet", use_container_width=True):
        st.info("Za a tura ka zuwa SMEPlug don cika wallet. Ko ka tuntube mu: 07062589825")
    st.markdown("</div>", unsafe_allow_html=True)
    st.write("")

    st.markdown("#### What would you like to do?")
    st.write("")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("📱 Airtime", use_container_width=True):
            if st.session_state.kyc_status != "approved":
                st.error("Dole ka yi KYC tukuna")
            else:
                st.session_state.page = "airtime"
                st.rerun()
    with col2:
        if st.button("📶 Data", use_container_width=True):
            if st.session_state.kyc_status != "approved":
                st.error("Dole ka yi KYC tukuna")
            else:
                st.session_state.page = "data"
                st.rerun()
    
    st.write("")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📺 Cable TV", use_container_width=True):
            if st.session_state.kyc_status != "approved":
                st.error("Dole ka yi KYC tukuna")
            else:
                st.session_state.page = "cable"
                st.rerun()
    with col2:
        if st.button("💡 Electricity", use_container_width=True):
            if st.session_state.kyc_status != "approved":
                st.error("Dole ka yi KYC tukuna")
            else:
                st.session_state.page = "electricity"
                st.rerun()

    st.write("")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("📞 USSD Codes", use_container_width=True):
            st.session_state.page = "ussd"
            st.rerun()
    with col2:
        if st.button("📊 Transactions", use_container_width=True):
            st.session_state.page = "history"
            st.rerun()

# USSD CODES PAGE
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
                copy_code("*312#")
            st.markdown("</div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([3,1])
        with col1:
            st.markdown('<div class="ussd-card">', unsafe_allow_html=True)
            st.markdown("**Recharge Airtime**")
            st.code("*311*PIN#", language="text")
            st.caption("Misali: *311*123456789012345#")
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="copy-btn">', unsafe_allow_html=True)
            if st.button("Copy", key="mtn_recharge"):
                copy_code("*311*")
            st.markdown("</div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([3,1])
        with col1:
            st.markdown('<div class="ussd-card">', unsafe_allow_html=True)
            st.markdown("**Check Data Balance**")
            st.code("*323#", language="text")
            st.caption("Tsohon: *131*4#")
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="copy-btn">', unsafe_allow_html=True)
            if st.button("Copy", key="mtn_data_bal"):
                copy_code("*323#")
            st.markdown("</div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([3,1])
        with col1:
            st.markdown('<div class="ussd-card">', unsafe_allow_html=True)
            st.markdown("**Borrow Airtime/Data**")
            st.code("*303#", language="text")
            st.caption("Tsohon: *606#")
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="copy-btn">', unsafe_allow_html=True)
            if st.button("Copy", key="mtn_borrow"):
                copy_code("*303#")
            st.markdown("</div>", unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### 🟢 GLO USSD Codes - 2026")
        
        col1, col2 = st.columns([3,1])
        with col1:
            st.markdown('<div class="ussd-card">', unsafe_allow_html=True)
            st.markdown("**Check Airtime Balance**")
            st.code("*310#", language="text")
            st.caption("Tsohon: *124#")
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="copy-btn">', unsafe_allow_html=True)
            if st.button("Copy", key="glo_balance"):
                copy_code("*310#")
            st.markdown("</div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([3,1])
        with col1:
            st.markdown('<div class="ussd-card">', unsafe_allow_html=True)
            st.markdown("**Buy Data**")
            st.code("*312#", language="text")
            st.caption("Tsohon: *777#")
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="copy-btn">', unsafe_allow_html=True)
            if st.button("Copy", key="glo_data"):
                copy_code("*312#")
            st.markdown("</div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([3,1])
        with col1:
            st.markdown('<div class="ussd-card">', unsafe_allow_html=True)
            st.markdown("**Recharge Airtime**")
            st.code("*311*PIN#", language="text")
            st.caption("Tsohon: *123*PIN#")
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="copy-btn">', unsafe_allow_html=True)
            if st.button("Copy", key="glo_recharge"):
                copy_code("*311*")
            st.markdown("</div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([3,1])
        with col1:
            st.markdown('<div class="ussd-card">', unsafe_allow_html=True)
            st.markdown("**Check Data Balance**")
            st.code("*323#", language="text")
            st.caption("Tsohon: *127*0#")
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="copy-btn">', unsafe_allow_html=True)
            if st.button("Copy", key="glo_data_bal"):
                copy_code("*323#")
            st.markdown("</div>", unsafe_allow_html=True)
    
    with tab3:
        st.markdown("### 🔴 AIRTEL USSD Codes - 2026")
        
        col1, col2 = st.columns([3,1])
        with col1:
            st.markdown('<div class="ussd-card">', unsafe_allow_html=True)
            st.markdown("**Check Airtime Balance**")
            st.code("*310#", language="text")
            st.caption("Tsohon: *123#")
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="copy-btn">', unsafe_allow_html=True)
            if st.button("Copy", key="airtel_balance"):
                copy_code("*310#")
            st.markdown("</div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([3,1])
        with col1:
            st.markdown('<div class="ussd-card">', unsafe_allow_html=True)
            st.markdown("**Buy Data**")
            st.code("*312#", language="text")
            st.caption("Tsohon: *141#")
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="copy-btn">', unsafe_allow_html=True)
            if st.button("Copy", key="airtel_data"):
                copy_code("*312#")
            st.markdown("</div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([3,1])
        with col1:
            st.markdown('<div class="ussd-card">', unsafe_allow_html=True)
            st.markdown("**Recharge Airtime**")
            st.code("*311*PIN#", language="text")
            st.caption("Tsohon: *126*PIN#")
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="copy-btn">', unsafe_allow_html=True)
            if st.button("Copy", key="airtel_recharge"):
                copy_code("*311*")
            st.markdown("</div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([3,1])
        with col1:
            st.markdown('<div class="ussd-card">', unsafe_allow_html=True)
            st.markdown("**Check Data Balance**")
            st.code("*323#", language="text")
            st.caption("Tsohon: *140#")
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="copy-btn">', unsafe_allow_html=True)
            if st.button("Copy", key="airtel_data_bal"):
                copy_code("*323#")
            st.markdown("</div>", unsafe_allow_html=True)
    
    with tab4:
        st.markdown("### 🟡 9MOBILE USSD Codes - 2026")
        
        col1, col2 = st.columns([3,1])
        with col1:
            st.markdown('<div class="ussd-card">', unsafe_allow_html=True)
            st.markdown("**Check Airtime Balance**")
            st.code("*310#", language="text")
            st.caption("Tsohon: *232#")
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="copy-btn">', unsafe_allow_html=True)
            if st.button("Copy", key="9mobile_balance"):
                copy_code("*310#")
            st.markdown("</div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([3,1])
        with col1:
            st.markdown('<div class="ussd-card">', unsafe_allow_html=True)
            st.markdown("**Buy Data**")
            st.code("*312#", language="text")
            st.caption("Tsohon: *200#")
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="copy-btn">', unsafe_allow_html=True)
            if st.button("Copy", key="9mobile_data"):
                copy_code("*312#")
            st.markdown("</div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([3,1])
        with col1:
            st.markdown('<div class="ussd-card">', unsafe_allow_html=True)
            st.markdown("**Recharge Airtime**")
            st.code("*311*PIN#", language="text")
            st.caption("Tsohon: *222*PIN#")
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="copy-btn">', unsafe_allow_html=True)
            if st.button("Copy", key="9mobile_recharge"):
                copy_code("*311*")
            st.markdown("</div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([3,1])
        with col1:
            st.markdown('<div class="ussd-card">', unsafe_allow_html=True)
            st.markdown("**Check Data Balance**")
            st.code("*323#", language="text")
            st.caption("Tsohon: *228#")
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="copy-btn">', unsafe_allow_html=True)
            if st.button("Copy", key="9mobile_data_bal"):
                copy_code("*323#")
            st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.error("**Gargadi:** NCC ta hada codes su zama daya tun March 2026. Idan ka yi amfani da tsohon code kamar *556#, ba zai yi aiki ba!")
    st.success("**Tip:** Danna 'Copy' button, sannan liqa a wayarka ka kira. Ba sai ka rubuta da hannu ba!")

# KYC PAGE
elif st.session_state.page == "kyc":
    st.subheader("KYC Verification")
    st.markdown("**Dole ne ka cika wannan don amfani da services - CBN Regulation**")
    
    if st.session_state.kyc_status == "approved":
        st.success("KYC dinka an amince da shi. Za ka iya amfani da duk services")
        st.json(st.session_state.user_data)
    elif st.session_state.kyc_status == "submitted":
        st.warning("An karbi bayanan ka. Muna duba KYC dinka. Za mu tuntube ka cikin 24 hours.")
    else:
        with st.form("kyc_form"):
            st.markdown("#### 1. Personal Information")
            full_name = st.text_input("Cikakken Suna *", placeholder="Jamilu Sani")
            email = st.text_input("Email Address *", placeholder="example@gmail.com")
            phone = st.text_input("Phone Number *", placeholder="07062589825", max_chars=11)
            dob = st.date_input("Ranar Haihuwa *")
            
            st.markdown("#### 2. Identity Verification")
            id_type = st.selectbox("Nau'in ID *", ["NIN", "BVN", "Voter's Card", "Driver's License", "International Passport"])
            id_number = st.text_input(f"{id_type} Number *", placeholder="12345678901")
            
            st.markdown("#### 3. Address")
            address = st.text_area("Cikakken Address *", placeholder="NO.278, LAYIN MAI UNGUWA KANO SAUNA")
            state = st.selectbox("State *", ["Kano", "Lagos", "Abuja", "Kaduna", "Rivers", "Oyo", "Others"])
            lga = st.text_input("LGA *", placeholder="Kano Municipal")
            
            st.markdown("#### 4. Upload ID Document")
            uploaded_file = st.file_uploader("Hoton ID dinka *", type=["png", "jpg", "jpeg"])
            
            st.markdown("---")
            agree = st.checkbox("Na yarda cewa bayanan nan daidai ne *")
            
            submitted = st.form_submit_button("Submit KYC", type="primary", use_container_width=True)
            
            if submitted:
                if not all([full_name, email, phone, id_number, address, lga, uploaded_file, agree]):
                    st.error("Dole ka cika duka filin da *")
                else:
                    st.session_state.user_data = {
                        "full_name": full_name,
                        "email": email,
                        "phone": phone,
                        "dob": str(dob),
                        "id_type": id_type,
                        "id_number": id_number,
                        "address": address,
                        "state": state,
                        "lga": lga,
                        "submitted_date": str(datetime.now())
                    }
                    st.session_state.kyc_status = "submitted"
                    st.success("An karbi KYC dinka! Muna duba shi. Za mu tuntube ka cikin 24 hours.")
                    st.balloons()
                    st.rerun()

# ADMIN PANEL
elif st.session_state.page == "admin":
    st.subheader("Admin Panel - J.S.GLOBAL")
    admin_pass = st.text_input("Shigar da Admin Password", type="password")
    
    if admin_pass == "Jamilu123":
        st.success("Welcome CEO Jamilu")
        
        st.markdown("### Pending KYC Requests")
        if st.session_state.kyc_status == "submitted":
            st.write("**Suna:**", st.session_state.user_data.get("full_name"))
            st.write("**NIN/BVN:**", st.session_state.user_data.get("id_number"))
            st.write("**Phone:**", st.session_state.user_data.get("phone"))
            st.write("**Address:**", st.session_state.user_data.get("address"))
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Approve KYC", type="primary"):
                    st.session_state.kyc_status = "approved"
                    st.success("KYC Approved! Customer zai iya amfani da services yanzu")
                    st.rerun()
            with col2:
                if st.button("Reject KYC"):
                    st.session_state.kyc_status = "pending"
                    st.error("KYC Rejected")
        else:
            st.info("Babu Pending KYC tukuna")
            
        st.markdown("---")
        st.markdown("### Wallet Balance")
        st.metric("SMEPlug Balance", f"N{balance}")
        
    elif admin_pass != "":
        st.error("Wrong Password")

# PROFILE PAGE
elif st.session_state.page == "profile":
    st.subheader("My Profile")
    
    st.markdown("#### Business Information")
    st.markdown(f"""
    **Business Name:** J.S.GLOBAL LINKS AND SERVICES  
    **CAC Registration:** RC 8984371  
    **Business Type:** GENERAL MERCHANDISE  
    **Address:** NO.278, LAYIN MAI UNGUWA KANO SAUNA, KANO STATE  
    **Phone:** 07062589825  
    **Wallet Balance:** N{balance}
    """)
    st.success("Verified Business")
    
    st.markdown("---")
    
    st.markdown("#### Your KYC Information")
    if st.session_state.kyc_status == "approved":
        st.success("KYC Verified")
        st.json(st.session_state.user_data)
    elif st.session_state.kyc_status == "submitted":
        st.warning("KYC Under Review")
        st.json(st.session_state.user_data)
    else:
        st.error("KYC Not Submitted")
        if st.button("Complete KYC Now", type="primary"):
            st.session_state.page = "kyc"
            st.rerun()

# AIRTIME PAGE
elif st.session_state.page == "airtime":
    if st.session_state.kyc_status != "approved":
        st.error("Dole ka kammala KYC tukuna. Je zuwa Menu > KYC Verification")
        if st.button("Go to KYC"):
            st.session_state.page = "kyc"
            st.rerun()
    else:
        st.subheader("Buy Airtime VTU")
        try:
            net_response = requests.get(BASE_URL + "/networks", headers=headers)
            if net_response.status_code == 200:
                networks = net_response.json().get("data", [])
                network_options = {net["name"]: net["id"] for net in networks}
                selected_network_name = st.selectbox("Zaɓi Network", list(network_options.keys()))
                selected_network_id = network_options[selected_network_name]
                amount = st.number_input("Nawa Airtime?", min_value=50, max_value=50000, step=50)
                phone_number = st.text_input("Lambar Wayar", placeholder="08012345678", max_chars=11)
                
                if st.button("Saya Airtime Yanzu", type="primary", use_container_width=True):
                    if len(phone_number) == 11:
                        payload = {"network": selected_network_id, "amount": amount, "mobile_number": phone_number, "Ported_number": True}
                        buy_response = requests.post(BASE_URL + "/airtime/purchase", headers=headers, json=payload)
                        if buy_response.status_code == 200:
                            st.success(f"An saida airtime N{amount} zuwa {phone_number}")
                            st.balloons()
                        else:
                            st.error(f"Error: {buy_response.text}")
                    else:
                        st.error("Lambar waya ba daidai ba")
            else:
                st.error("An samu matsala wajen dauko networks")
        except Exception as e:
            st.error(f"Matsala: {e}")

# DATA PAGE
elif st.session_state.page == "data":
    if st.session_state.kyc_status != "approved":
        st.error("Dole ka kammala KYC tukuna")
        if st.button("Go to KYC"):
            st.session_state.page = "kyc"
            st.rerun()
    else:
        st.subheader("Buy Data Bundle")
        try:
            net_response = requests.get(BASE_URL + "/networks", headers=headers)
            if net_response.status_code == 200:
                networks = net_response.json().get("data", [])
                network_options = {net["name"]: net["id"] for net in networks}
                selected_network_name = st.selectbox("Zaɓi Network", list(network_options.keys()))
                selected_network_id = network_options[selected_network_name]
                
                plan_response = requests.get(BASE_URL + "/data/plans/" + str(selected_network_id), headers=headers)
                if plan_response.status_code == 200:
                    plans = plan_response.json().get("data", [])
                    plan_options = {f"{p['name']} - N{p['price']}": p["id"] for p in plans}
                    selected_plan_name = st.selectbox("Zaɓi Data Plan", list(plan_options.keys()))
                    selected_plan_id = plan_options[selected_plan_name]
                    phone_number = st.text_input("Lambar Wayar", placeholder="08012345678", max_chars=11)
                    
                    if st.button("Saya Data Yanzu", type="primary", use_container_width=True):
                        if len(phone_number) == 11:
                            payload = {"network": selected_network_id, "plan": selected_plan_id, "mobile_number": phone_number, "Ported_number": True}
                            buy_response = requests.post(BASE_URL + "/data/purchase", headers=headers, json=payload)
                            if buy_response.status_code == 200:
                                st.success(f"An saida {selected_plan_name} zuwa {phone_number}")
                                st.balloons()
                            else:
                                st.error(f"Error: {buy_response.text}")
                        else:
                            st.error("Lambar waya ba daidai ba")
                else:
                    st.error("An samu matsala wajen dauko data plans")
            else:
                st.error("An samu matsala wajen dauko networks")
        except Exception as e:
            st.error(f"Matsala: {e}")

# CABLE TV PAGE
elif st.session_state.page == "cable":
    if st.session_state.kyc_status != "approved":
        st.error("Dole ka kammala KYC tukuna")
    else:
        st.subheader("Pay DSTV / GOTV / Startimes")
        try:
            cable_response = requests.get(BASE_URL + "/cable/providers", headers=headers)
            if cable_response.status_code == 200:
                providers = cable_response.json().get("data", [])
                provider_options = {p["name"]: p["id"] for p in providers}
                selected_provider_name = st.selectbox("Zaɓi TV", list(provider_options.keys()))
                selected_provider_id = provider_options[selected_provider_name]
                
                smartcard_number = st.text_input("Smartcard / IUC Number")
                
                if st.button("Duba Sunan Mai TV"):
                    if smartcard_number:
                        verify_payload = {"provider": selected_provider_id, "smartcard_number": smartcard_number}
                        verify_response = requests.post(BASE_URL + "/cable/verify", headers=headers, json=verify_payload)
                        if verify_response.status_code == 200:
                            customer_name = verify_response.json().get("data", {}).get("name", "N/A")
                            st.session_state.cable_customer = customer_name
                            st.info(f"Sunan Mai TV: {customer_name}")
                            
                            plan_response = requests.get(BASE_URL + "/cable/plans/" + str(selected_provider_id), headers=headers)
                            if plan_response.status_code == 200:
                                plans = plan_response.json().get("data", [])
                                plan_options = {f"{p['name']} - N{p['price']}": p["id"] for p in plans}
                                st.session_state.cable_plans = plan_options
                        else:
                            st.error("Ba a sami sunan ba")
                
                if "cable_plans" in st.session_state:
                    selected_plan_name = st.selectbox("Zaɓi Package", list(st.session_state.cable_plans.keys()))
                    selected_plan_id = st.session_state.cable_plans[selected_plan_name]
                    
                    if st.button("Biya Cable TV Yanzu", type="primary", use_container_width=True):
                        pay_payload = {"provider": selected_provider_id, "smartcard_number": smartcard_number, "plan": selected_plan_id}
                        pay_response = requests.post(BASE_URL + "/cable/purchase", headers=headers, json=pay_payload)
                        if pay_response.status_code == 200:
                            st.success(f"An biya {selected_plan_name}")
                            st.balloons()
                        else:
                            st.error(f"Error: {pay_response.text}")
            else:
                st.error("An samu matsala wajen dauko cable providers")
        except Exception as e:
            st.error(f"Matsala: {e}")

# ELECTRICITY PAGE
elif st.session_state.page == "electricity":
    if st.session_state.kyc_status != "approved":
        st.error("Dole ka kammala KYC tukuna")
    else:
        st.subheader("Pay NEPA / Electricity Bills")
        try:
            disco_response = requests.get(BASE_URL + "/electricity/discos", headers=headers)
            if disco_response.status_code == 200:
                discos = disco_response.json().get("data", [])
                disco_options = {d["name"]: d["id"] for d in discos}
                selected_disco_name = st.selectbox("Zaɓi Kamfanin NEPA", list(disco_options.keys()))
                selected_disco_id = disco_options[selected_disco_name]
                
                meter_type = st.selectbox("Meter Type", ["prepaid", "postpaid"])
                meter_number = st.text_input("Meter Number")
                amount = st.number_input("Nawa Za Ka Biya?", min_value=500, step=100)
                
                if st.button("Duba Sunan Mai Meter"):
                    if meter_number:
                        verify_payload = {"disco": selected_disco_id, "meter_number": meter_number, "meter_type": meter_type}
                        verify_response = requests.post(BASE_URL + "/electricity/verify", headers=headers, json=verify_payload)
                        if verify_response.status_code == 200:
                            customer_name = verify_response.json().get("data", {}).get("name", "N/A")
                            st.session_state.electricity_customer = customer_name
                            st.info(f"Sunan Mai Meter: {customer_name}")
                        else:
                            st.error("Ba a sami sunan ba")
                
                if "electricity_customer" in st.session_state:
                    if st.button("Biya Kudin Wuta Yanzu", type="primary", use_container_width=True):
                        pay_payload = {"disco": selected_disco_id, "meter_number": meter_number, "meter_type": meter_type, "amount": amount}
                        pay_response = requests.post(BASE_URL + "/electricity/purchase", headers=headers, json=pay_payload)
                        if pay_response.status_code == 200:
                            token = pay_response.json().get("data", {}).get("token", "N/A")
                            st.success(f"An biya! Token: {token}")
                            st.balloons()
                        else:
                            st.error(f"Error: {pay_response.text}")
            else:
                st.error("An samu matsala wajen dauko discos")
        except Exception as e:
            st.error(f"Matsala: {e}")

# HISTORY PAGE
elif st.session_state.page == "history":
    st.subheader("Transaction History")
    st.info("Za a nuna tarihin cinikayyarka anan. API endpoint na history ba a haɗa ba tukuna.")
