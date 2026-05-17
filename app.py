import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="J.S.GLOBAL", layout="wide", initial_sidebar_state="expanded")

# === CONFIG ===
BASE_URL = st.secrets.get("BASE_URL", "")
API_KEY = st.secrets.get("API_KEY", "")
ADMIN_PASSWORD = st.secrets.get("ADMIN_PASSWORD", "change_me")
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

# === CSS ===
st.markdown("""
<style>
   .main.block-container {
        padding-top: 1rem;
        padding-left: 1rem;
        padding-right: 1rem;
        padding-bottom: 2rem;
    }

   .blue-header {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin-bottom: 1rem;
    }

    button[data-testid="baseButton-primary"] {
        background-color: #e91e63!important;
        color: white!important;
        border-radius: 25px!important;
        border: none!important;
        padding: 0.6rem 1.5rem!important;
        font-weight: 600!important;
    }

   .service-card {
        background: white;
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        cursor: pointer;
        transition: transform 0.2s, box-shadow 0.2s;
        min-height: 110px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        border: 1px solid #f0f0f0;
    }
   .service-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 6px 16px rgba(0,0,0,0.12);
    }
   .service-card p {
        margin: 0;
        font-size: 12px;
        font-weight: 500;
        color: #333;
    }

   .upgrade-card,.help-card {
        background-color: #e8eaf6;
        padding: 15px;
        border-radius: 12px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
    }

   .card-button > div > button {
        background: transparent!important;
        border: none!important;
        padding: 0!important;
        box-shadow: none!important;
        height: 0!important;
        margin: 0!important;
    }
</style>
""", unsafe_allow_html=True)

# === SESSION STATE ===
defaults = {
    "show_balance": True,
    "kyc_status": "pending",
    "user_data": {},
    "copied_code": "",
    "page": "dashboard",
    "cable_plans": None,
    "cable_customer": None,
    "cable_provider_id": None,
    "cable_smartcard": None,
    "electric_customer": None,
}
for k, v in defaults.items():
    st.session_state.setdefault(k, v)

# === API FUNCTIONS ===
@st.cache_data(ttl=60)
def get_balance():
    try:
        resp = requests.get(f"{BASE_URL}/account/balance", headers=headers, timeout=10)
        if resp.status_code == 200:
            return resp.json().get("balance", "0")
    except:
        pass
    return "0"

@st.cache_data(ttl=600)
def get_networks():
    try:
        resp = requests.get(f"{BASE_URL}/networks", headers=headers, timeout=10)
        return resp.json().get("data", []) if resp.status_code == 200 else []
    except:
        return []

@st.cache_data(ttl=600)
def get_data_plans(network_id):
    try:
        resp = requests.get(f"{BASE_URL}/data/plans/{network_id}", headers=headers, timeout=10)
        return resp.json().get("data", []) if resp.status_code == 200 else []
    except:
        return []

@st.cache_data(ttl=600)
def get_cable_providers():
    try:
        resp = requests.get(f"{BASE_URL}/cable/providers", headers=headers, timeout=10)
        return resp.json().get("data", []) if resp.status_code == 200 else []
    except:
        return []

@st.cache_data(ttl=600)
def get_cable_plans(provider_id):
    try:
        resp = requests.get(f"{BASE_URL}/cable/plans/{provider_id}", headers=headers, timeout=10)
        return resp.json().get("data", []) if resp.status_code == 200 else []
    except:
        return []

@st.cache_data(ttl=600)
def get_electricity_discos():
    try:
        resp = requests.get(f"{BASE_URL}/electricity/discos", headers=headers, timeout=10)
        return resp.json().get("data", []) if resp.status_code == 200 else []
    except:
        return []

def copy_code(code):
    st.session_state.copied_code = code
    st.toast(f"Copied {code}", icon="✅")

def check_kyc_or_block():
    if st.session_state.kyc_status!= "approved":
        st.error("Dole ka kammala KYC tukuna")
        if st.button("Go to KYC"):
            st.session_state.page = "kyc"
            st.rerun()
        st.stop()

# === SIDEBAR ===
with st.sidebar:
    st.image("logo.png", width=80)
    st.markdown("### J.S.GLOBAL LINKS")
    st.caption("RC: 8984371")

    status_map = {"approved": "success", "submitted": "warning"}
    status = status_map.get(st.session_state.kyc_status, "error")
    msg = {"approved": "KYC Verified", "submitted": "KYC Pending"}.get(st.session_state.kyc_status, "KYC Required")
    getattr(st, status)(msg)

    st.markdown("---")
    pages = [("🏠 Dashboard", "dashboard"), ("👤 My Profile", "profile"), ("✅ KYC Verification", "kyc"),
             ("📱 USSD Codes", "ussd"), ("📊 Transactions", "history"), ("🔐 Admin Panel", "admin")]
    for label, page in pages:
        if st.button(label, use_container_width=True):
            st.session_state.page = page
            st.rerun()

    st.markdown("---")
    st.caption("Kano, Nigeria")
    st.caption("07062589825")

# === HEADER ===
col1, col2 = st.columns([1, 8])
with col1:
    st.image("logo.png", width=50)
with col2:
    st.markdown("### J.S.GLOBAL LINKS AND SERVICES")
    st.caption("CAC: RC 8984371 | GENERAL MERCHANDISE")

if st.session_state.page!= "dashboard":
    if st.button("← Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()
    st.markdown("---")

balance = get_balance()

# === DASHBOARD ===
if st.session_state.page == "dashboard":
    st.markdown(f"""
    <div class="blue-header">
        <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
            <div style="font-size: 13px; opacity: 0.9;">WALLET BALANCE</div>
        </div>
        <div style="font-size: 32px; font-weight: bold; margin-bottom: 1rem;">
            {f'N{balance:,}' if st.session_state.show_balance else '******'}
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([3, 1, 3])
    with col1:
        if st.button("+ Fund Wallet", type="primary", use_container_width=True):
            st.info("Za a tura ka zuwa SMEPlug don cika wallet. Ko ka tuntube mu: 07062589825")
    with col2:
        if st.button("🔄"):
            st.cache_data.clear()
            st.rerun()
    with col3:
        if st.button("👁️"):
            st.session_state.show_balance = not st.session_state.show_balance
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="upgrade-card">
        <div>
            <div style="font-weight: bold; color: #1e3c72; font-size: 15px;">Upgrade Membership</div>
            <div style="font-size: 13px; color: #5c6bc0;">Unlock more discounts and other benefits</div>
        </div>
        <div style="font-size: 20px; color: #1e3c72;">›</div>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.kyc_status == "pending":
        st.warning("KYC Required: Ka kammala KYC Verification don amfani da duk services.")
        if st.button("Verify KYC Now", type="primary"):
            st.session_state.page = "kyc"
            st.rerun()

    services = [
        ("📞", "Airtime", "airtime", True), ("🌐", "Data", "data", True),
        ("📺", "Cable TV", "cable", True), ("💡", "Electricity", "electricity", True),
        ("🖨️", "Print Recharge", None, False), ("🎲", "Fund Betting", None, False),
        ("💸", "Transfer Money", None, False), ("💰", "Withdraw", None, False),
        ("📝", "WAEC ePIN", "waec", True), ("📝", "JAMB ePIN", "jamb", True),
        ("📡", "Smile Internet", None, False)
    ]

    for i in range(0, len(services), 4):
        cols = st.columns(4)
        for j, col in enumerate(cols):
            if i + j < len(services):
                icon, name, page, needs_kyc = services[i + j]
                with col:
                    st.markdown('<div class="card-button">', unsafe_allow_html=True)
                    if st.button("", key=f"card_{i+j}", use_container_width=True):
                        if page is None:
                            st.info("Coming Soon")
                        elif needs_kyc and st.session_state.kyc_status!= "approved":
                            st.error("Dole ka yi KYC tukuna")
                        else:
                            st.session_state.page = page
                            st.rerun()
                    st.markdown('</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="service-card"><div style="font-size:35px;">{icon}</div><p>{name}</p></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="help-card">
        <div style="display: flex; align-items: center; gap: 15px;">
            <div style="font-size: 30px;">❓</div>
            <div>
                <div style="font-weight: bold; color: #1e3c72; font-size: 15px;">Need Help?</div>
                <div style="font-size: 13px; color: #5c6bc0;">Try our self service or open a ticket</div>
            </div>
        </div>
        <div style="font-size: 20px; color: #1e3c72;">›</div>
    </div>
    """, unsafe_allow_html=True)

# === USSD ===
elif st.session_state.page == "ussd":
    st.subheader("USSD Codes - NCC 2026")
    st.success("Sabbin codes da NCC ta hada su daya ga duk networks")

    if st.session_state.copied_code:
        st.info(f"Copied: {st.session_state.copied_code}")
        st.session_state.copied_code = ""

    ussd_data = {
        "MTN": [("Check Airtime", "*310#"), ("Buy Data", "*312#"), ("Recharge", "*311*PIN#"), ("Check Data", "*323#")],
        "GLO": [("Check Airtime", "*310#"), ("Buy Data", "*312#"), ("Recharge", "*311*PIN#"), ("Check Data", "*323#")],
        "AIRTEL": [("Check Airtime", "*310#"), ("Buy Data", "*312#"), ("Recharge", "*311*PIN#"), ("Check Data", "*323#")],
        "9MOBILE": [("Check Airtime", "*310#"), ("Buy Data", "*312#"), ("Recharge", "*311*PIN#"), ("Check Data", "*323#")]
    }

    tabs = st.tabs(list(ussd_data.keys()))
    for tab, (network, codes) in zip(tabs, ussd_data.items()):
        with tab:
            for name, code in codes:
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown(f"**{name}**\n```{code}```")
                with col2:
                    if st.button("Copy", key=f"{network}_{code}"):
                        copy_code(code)

# === KYC ===
elif st.session_state.page == "kyc":
    st.subheader("KYC Verification")
    if st.session_state.kyc_status == "approved":
        st.success("KYC dinka an amince da shi")
        st.json(st.session_state.user_data)
    elif st.session_state.kyc_status == "submitted":
        st.warning("An karbi bayanan ka. Muna duba KYC dinka cikin 24 hours.")
    else:
        with st.form("kyc_form"):
            full_name = st.text_input("Cikakken Suna *")
            email = st.text_input("Email Address *")
            phone = st.text_input("Phone Number *", max_chars=11)
            id_type = st.selectbox("Nau'in ID *", ["NIN", "BVN", "Voter's Card", "Driver's License", "International Passport"])
            id_number = st.text_input(f"{id_type} Number *")
            address = st.text_area("Cikakken Address *")
            uploaded_file = st.file_uploader("Hoton ID dinka *", type=["png", "jpg", "jpeg"])
            agree = st.checkbox("Na yarda cewa bayanan nan daidai ne *")

            if st.form_submit_button("Submit KYC", type="primary"):
                if not all([full_name, email, phone, id_number, address, uploaded_file, agree]):
                    st.error("Dole ka cika duka filin da *")
                else:
                    st.session_state.user_data = {
                        "full_name": full_name, "email": email, "phone": phone,
                        "id_type": id_type, "id_number": id_number, "address": address,
                        "submitted_date": str(datetime.now())
                    }
                    st.session_state.kyc_status = "submitted"
                    st.success("An karbi KYC dinka!")
                    st.rerun()

# === ADMIN ===
elif st.session_state.page == "admin":
    st.subheader("Admin Panel")
    admin_pass = st.text_input("Shigar da Admin Password", type="password")

    if admin_pass == ADMIN_PASSWORD:
        st.success("Welcome CEO Jamilu")
        st.metric("SMEPlug Balance", f"N{balance:,}")

        if st.session_state.kyc_status == "submitted":
            st.write("**Pending KYC:**", st.session_state.user_data.get("full_name"))
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Approve KYC", type="primary"):
                    st.session_state.kyc_status = "approved"
                    st.rerun()
            with col2:
                if st.button("Reject KYC"):
                    st.session_state.kyc_status = "pending"
                    st.rerun()
        else:
            st.info("Babu Pending KYC tukuna")
    elif admin_pass:
        st.error("Wrong Password")

# === AIRTIME ===
elif st.session_state.page == "airtime":
    check_kyc_or_block()
    st.subheader("Buy Airtime VTU")
    networks = get_networks()
    if networks:
        network_options = {n["name"]: n["id"] for n in networks}
        selected = st.selectbox("Zaɓi Network", list(network_options.keys()))
        amount = st.number_input("Nawa Airtime?", min_value=50, max_value=50000, step=50)
        phone = st.text_input("Lambar Wayar", max_chars=11)

        if st.button("Saya Airtime Yanzu", type="primary"):
            if len(phone) == 11:
                payload = {"network": network_options[selected], "amount": amount, "mobile_number": phone}
                try:
                    resp = requests.post(f"{BASE_URL}/airtime/purchase", headers=headers, json=payload, timeout=15)
                    if resp.status_code == 200:
                        st.success(f"An saida airtime N{amount} zuwa {phone}")
                        st.cache_data.clear()
                        st.balloons()
                    else:
                        st.error(f"Error: {resp.text}")
                except Exception as e:
                    st.error(f"Matsala: {e}")
            else:
                st.error("Lambar waya ba daidai ba")

# === DATA ===
elif st.session_state.page == "data":
    check_kyc_or_block()
    st.subheader("Buy Data Bundle")
    networks = get_networks()
    if networks:
        network_options = {n["name"]: n["id"] for n in networks}
        selected_net = st.selectbox("Zaɓi Network", list(network_options.keys()))
        plans = get_data_plans(network_options[selected_net])
        if plans:
            plan_options = {f"{p['name']} - N{p['price']}": p["id"] for p in plans}
            selected_plan = st.selectbox("Zaɓi Data Plan", list(plan_options.keys()))
            phone = st.text_input("Lambar Wayar", max_chars=11)

            if st.button("Saya Data Yanzu", type="primary"):
                if len(phone) == 11:
                    payload = {"network": network_options[selected_net], "plan": plan_options[selected_plan], "mobile_number": phone}
                    try:
                        resp = requests.post(f"{BASE_URL}/data/purchase", headers=headers, json=payload, timeout=15)
                        if resp.status_code == 200:
                            st.success(f"An saida {selected_plan} zuwa {phone}")
                            st.cache_data.clear()
                            st.balloons()
                        else:
                            st.error(f"Error: {resp.text}")
                    except Exception as e:
                        st.error(f"Matsala: {e}")
                else:
                    st.error("Lambar waya ba daidai ba")

# === CABLE ===
elif st.session_state.page == "cable":
    check_kyc_or_block()
    st.subheader("Pay DSTV / GOTV / Startimes")
    providers = get_cable_providers()
    if providers:
        provider_options = {p["name"]: p["id"] for p in providers}
        selected_provider = st.selectbox("Zaɓi TV", list(provider_options.keys()))
        provider_id = provider_options[selected_provider]

        smartcard = st.text_input("Smartcard / IUC Number")

        if st.button("Duba Sunan Mai TV"):
            if smartcard:
                try:
                    payload = {"provider": provider_id, "smartcard_number": smartcard}
                    resp = requests.post(f"{BASE_URL}/cable/verify", headers=headers, json=payload, timeout=15)
                    if resp.status_code == 200:
                        name = resp.json().get("data", {}).get("name")
                        st.session_state.cable_customer = name
                        st.session_state.cable_smartcard = smartcard
                        st.session_state.cable_provider_id = provider_id
                        st.success(f"Sunan Mai TV: {name}")
                        st.session_state.cable_plans = get_cable_plans(provider_id)
                    else:
                        st.error("Ba a sami sunan ba")
                except Exception as e:
                    st.error(f"Matsala: {e}")

        if st.session_state.cable_plans:
            plan_options = {f"{p['name']} - N{p['price']}": p["id"] for p in st.session_state.cable_plans}
            selected_plan = st.selectbox("Zaɓi Package", list(plan_options.keys()))
            plan_id = plan_options[selected_plan]

            if st.button("Biya Kudin TV Yanzu", type="primary"):
                payload = {
                    "provider": st.session_state.cable_provider_id,
                    "plan": plan_id,
                    "smartcard_number": st.session_state.cable_smartcard
                }
                try:
                    resp = requests.post(f"{BASE_URL}/cable/purchase", headers=headers, json=payload, timeout=15)
                    if resp.status_code == 200:
                        st.success(f"An biya {selected_plan} ga {st.session_state.cable_customer}")
                        st.cache_data.clear()
                        st.balloons()
                        st.session_state.cable_plans = None
                    else:
                        st.error(f"Error: {resp.text}")
                except Exception as e:
                    st.error(f"Matsala: {e}")

# === ELECTRICITY ===
elif st.session_state.page == "electricity":
    check_kyc_or_block()
    st.subheader("Pay Electricity Bill")
    discos = get_electricity_discos()
    if discos:
        disco_options = {d["name"]: d["id"] for d in discos}
        selected_disco = st.selectbox("Zaɓi Disco", list(disco_options.keys()))
        meter_number = st.text_input("Meter Number")
        meter_type = st.selectbox("Meter Type", ["Prepaid", "Postpaid"])
        amount = st.number_input("Amount", min_value=100, step=100)

        if st.button("Verify Meter"):
            try:
                payload = {"disco": disco_options[selected_disco], "meter_number": meter_number}
                resp = requests.post(f"{BASE_URL}/electricity/verify", headers=headers, json=payload, timeout=15)
                if resp.status_code == 200:
                    customer = resp.json().get("data", {}).get("name", "Customer")
                    st.session_state.electric_customer = customer
                    st.session_state.electric_meter = meter_number
                    st.session_state.electric_disco = disco_options[selected_disco]
                    st.success(f"Customer: {customer}")
                else:
                    st.error("Ba a sami meter ba")
            except Exception as e:
                st.error(f"Matsala: {e}")

        if st.session_state.electric_customer:
            st.info(f"Customer: {st.session_state.electric_customer}")
            if st.button("Biya Bill Yanzu", type="primary"):
                payload = {
                    "disco": st.session_state.electric_disco,
                    "meter_number": st.session_state.electric_meter,
                    "meter_type": meter_type.lower(),
                    "amount": amount
                }
                try:
                    resp = requests.post(f"{BASE_URL}/electricity/purchase", headers=headers, json=payload, timeout=15)
                    if resp.status_code == 200:
                        st.success(f"An biya N{amount} ga {st.session_state.electric_customer}")
                        st.cache_data.clear()
                        st.balloons()
                        st.session_state.electric_customer = None
                    else:
                        st.error(f"Error: {resp.text}")
                except Exception as e:
                    st.error(f"Matsala: {e}")

# === PROFILE ===
elif st.session_state.page == "profile":
    st.subheader("My Profile")
    st.markdown(f"""
    **Business Name:** J.S.GLOBAL LINKS AND SERVICES
    **CAC Registration:** RC 8984371
    **Address:** NO.278, LAYIN MAI UNGUWA KANO SAUNA, KANO STATE
    **Phone:** 07062589825
    **Wallet Balance:** N{balance:,}
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

# === HISTORY ===
elif st.session_state.page == "history":
    st.subheader("Transaction History")
    st.info("Haɗa API endpoint na history nan")
