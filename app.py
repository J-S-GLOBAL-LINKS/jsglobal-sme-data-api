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
    box-shadow: 0 4px 8px rgba(0,0,0,0.15);
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
        
        col1, col2 = st.columns([3,1])
        with col1:
            st.markdown('<div class="ussd-card">', unsafe_allow_html=True)
            st.markdown("**Link NIN**")
            st.code("*996#", language="text")
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="copy-btn">', unsafe_allow_html=True)
            if st.button("Copy", key="mtn_nin"):
                copy_code("*996#")
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
                
                if smartcard_number:
                    plan_response = requests.get(BASE_URL + f"/cable/plans/{selected_provider_id}", headers=headers)
                    if plan_response.status_code == 200:
                        plans = plan_response.json().get("data", [])
                        plan_options = {f"{p['name']} - N{p['price']}": p["id"] for p in plans}
                        selected_plan_name = st.selectbox("Zaɓi Package", list(plan_options.keys()))
                        selected_plan_id = plan_options[selected_plan_name]
                        
                        if st.button("Biya Cable Yanzu", type="primary", use_container_width=True):
                            payload = {"provider": selected_provider_id, "plan": selected_plan_id, "smartcard_number": smartcard_number}
                            buy_response = requests.post(BASE_URL + "/cable/purchase", headers=headers, json=payload)
                            if buy_response.status_code == 200:
                                st.success(f"An biya {selected_plan_name} na {smartcard_number}")
                                st.balloons()
                            else:
                                st.error(f"Error: {buy_response.text}")
        except Exception as e:
            st.error(f"Matsala: {e}")

elif st.session_state.page == "electricity":
    if st.session_state.kyc_status != "approved":
        st.error("Dole ka kammala KYC tukuna")
    else:
        st.subheader("Pay Electricity Bill")
        try:
            elec_response = requests.get(BASE_URL + "/electricity/discos", headers=headers)
