import streamlit as st
import requests

st.set_page_config(page_title="J.S.GLOBAL LINKS", page_icon="logo.png", layout="wide")

# CSS DON KYAU
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: #f8f9fa;
}
div[data-testid="stButton"] > button {
    height: 110px;
    background-color: white;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    font-size: 16px;
    font-weight: 500;
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
</style>
""", unsafe_allow_html=True)

# API SETUP
api_key = st.secrets["SMEPLUG_API_KEY"]
BASE_URL = "https://smeplug.ng/api/v1"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# SESSION STATE
if 'page' not in st.session_state:
    st.session_state.page = 'dashboard'
if 'show_balance' not in st.session_state:
    st.session_state.show_balance = True

# SAMO BALANCE
try:
    response = requests.get(f"{BASE_URL}/account/balance", headers=headers, timeout=10)
    balance = response.json().get('balance', '0') if response.status_code == 200 else '0'
except Exception:
    balance = '0'

# HEADER
col1, col2 = st.columns([1, 8])
with col1:
    st.image("logo.png", width=60)
with col2:
    st.markdown("### J.S.GLOBAL LINKS AND SERVICES")
    st.caption("CAC: RC 8984371 | GENERAL MERCHANDISE")

st.write("")

# WALLET BALANCE CARD
st.markdown('<div class="wallet-container">', unsafe_allow_html=True)
st.markdown("##### WALLET BALANCE")
col1, col2, col3 = st.columns([6,1,1])
with col1:
    if st.session_state.show_balance:
        st.markdown(f"## ₦{balance}")
    else:
        st.markdown("## ******")
with col2:
    if st.button("👁️", key="eye"):
        st.session_state.show_balance = not st.session_state.show_balance
        st.rerun()
with col3:
    if st.button("🔄", key="refresh"):
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# FUND WALLET BUTTON
st.markdown('<div class="fund-btn">', unsafe_allow_html=True)
if st.button("+ Fund Wallet", use_container_width=True):
    st.info("Za a tura ka zuwa SMEPlug don cika wallet. Ko ka tuntube mu: 07062589825")
st.markdown('</div>', unsafe_allow_html=True)
st.write("")

# UPGRADE MEMBERSHIP
st.info("**Upgrade Membership** - Unlock more discounts and other benefits >")
st.write("")

# BACK BUTTON
if st.session_state.page != 'dashboard':
    if st.button("← Back to Dashboard"):
        st.session_state.page = 'dashboard'
        st.rerun()
    st.markdown("---")

# DASHBOARD GRID
if st.session_state.page == 'dashboard':
    st.markdown("#### What would you like to do?")
    st.write("")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("📞\n\nAirtime", use_container_width=True):
            st.session_state.page = 'airtime'
            st.rerun()
    with col2:
        if st.button("📱\n\nData", use_container_width=True):
            st.session_state.page = 'data'
            st.rerun()
    
    st.write("")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📺\n\nCable TV", use_container_width=True):
            st.session_state.page = 'cable'
            st.rerun()
    with col2:
        if st.button("⚡\n\nElectricity", use_container_width=True):
            st.session_state.page = 'electricity'
            st.rerun()

    st.write("")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🧾\n\nPrint Recharge", use_container_width=True):
            st.info("Coming Soon")
    with col2:
        if st.button("🎰\n\nFund Betting", use_container_width=True):
            st.info("Coming Soon")
    
    st.write("")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("💸\n\nTransfer Money", use_container_width=True):
            st.info("Coming Soon")
    with col2:
        if st.button("💰\n\nWithdraw Commission", use_container_width=True):
            st.info("Coming Soon")

    st.write("")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("📝\n\nWAEC ePIN", use_container_width=True):
            st.session_state.page = 'waec'
            st.rerun()
    with col2:
        if st.button("📝\n\nJAMB ePIN", use_container_width=True):
            st.session_state.page = 'jamb'
            st.rerun()

    st.write("")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌐\n\nSmile Internet", use_container_width=True):
            st.info("Coming Soon")
    with col2:
        if st.button("📜\n\nTransactions", use_container_width=True):
            st.session_state.page = 'history'
            st.rerun()

# AIRTIME PAGE
elif st.session_state.page == 'airtime':
    st.subheader("📞 Buy Airtime VTU")
    try:
        net_response = requests.get(f"{BASE_URL}/networks", headers=headers)
        if net_response.status_code == 200:
            networks = net_response.json().get('data', [])
            network_options = {net['name']: net['id'] for net in networks}
            selected_network_name = st.selectbox("Zaɓi Network", list(network_options.keys()))
            selected_network_id = network_options[selected_network_name]
            amount = st.number_input("Nawa Airtime?", min_value=50, max_value=50000, step=50)
            phone_number = st.text_input("Lambar Wayar", placeholder="08012345678", max_chars=11)
            
            if st.button("Saya Airtime Yanzu", type="primary", use_container_width=True):
                if len(phone_number) == 11:
                    payload = {"network": selected_network_id, "amount": amount, "mobile_number": phone_number, "Ported_number": True}
                    buy_response = requests.post(f"{BASE_URL}/airtime/purchase", headers=headers, json=payload)
                    if buy_response.status_code == 200:
                        st.success(f"✅ An saida airtime ₦{amount} zuwa {phone_number}")
                        st.balloons()
                    else:
                        st.error(f"❌ Error: {buy_response.text}")
    except Exception as e:
        st.error(f"Matsala: {e}")

# DATA PAGE
elif st.session_state.page == 'data':
    st.subheader("📱 Buy Data Bundle")
    try:
        net_response = requests.get(f"{BASE_URL}/networks", headers=headers)
        if net_response.status_code == 200:
            networks = net_response.json().get('data', [])
            network_options = {net['name']: net['id'] for net in networks}
            selected_network_name = st.selectbox("Zaɓi Network", list(network_options.keys()))
            selected_network_id = network_options[selected_network_name]
            
            plan_response = requests.get(f"{BASE_URL}/data/plans/{selected_network_id}", headers=headers)
            if plan_response.status_code == 200:
                plans = plan_response.json().get('data', [])
                plan_options = {f"{p['name']} - ₦{p['price']}": p['id'] for p in plans}
                selected_plan_name = st.selectbox("Zaɓi Data Plan", list(plan_options.keys()))
                selected_plan_id = plan_options[selected_plan_name]
                phone_number = st.text_input("Lambar Wayar", placeholder="08012345678", max_chars=11)
                
                if st.button("Saya Data Yanzu", type="primary", use_container_width=True):
                    if len(phone_number) == 11:
                        payload = {"network": selected_network_id, "plan": selected_plan_id, "mobile_number": phone_number, "Ported_number": True}
                        buy_response = requests.post(f"{BASE_URL}/data/purchase", headers=headers, json=payload)
                        if buy_response.status_code == 200:
                            st.success(f"✅ An saida {selected_plan_name} zuwa {phone_number}")
                            st.balloons()
                        else:
                            st.error(f"❌ Error: {buy_response.text}")
    except Exception as e:
        st.error(f"Matsala: {e}")

# CABLE TV PAGE
elif st.session_state.page == 'cable':
    st.subheader("📺 Pay DSTV / GOTV / Startimes")
    try:
        cable_response = requests.get(f"{BASE_URL}/cable/providers", headers=headers)
        if cable_response.status_code == 200:
            providers = cable_response.json().get('data', [])
            provider_options = {p['name']: p['id'] for p in providers}
            selected_provider_name = st.selectbox("Zaɓi TV", list(provider_options.keys()))
            selected_provider_id = provider_options[selected_provider_name]
            
            smartcard_number = st.text_input("Smartcard / IUC Number")
            
            if st.button("Duba Sunan Mai TV"):
                if smartcard_number:
                    verify_payload = {"provider": selected_provider_id, "smartcard_number": smartcard_number}
                    verify_response = requests.post(f"{BASE_URL}/cable/verify", headers=headers, json=verify_payload)
                    if verify_response.status_code == 200:
                        customer_name = verify_response.json().get('data', {}).get('name', 'N/A')
                        st.session_state.cable_customer = customer_name
                        st.info(f"Sunan Mai TV: {customer_name}")
                        
                        plan_response = requests.get(f"{BASE_URL}/cable/plans/{selected_provider_id}", headers=headers)
                        if plan_response.status_code == 200:
                            plans = plan_response.json().get('data', [])
                            plan_options = {f"{p['name']} - ₦{p['price']}": p['id'] for p in plans}
                            st.session_state.cable_plans = plan_options
            
            if 'cable_plans' in st.session_state:
                selected_plan_name = st.selectbox("Zaɓi Package", list(st.session_state.cable_plans.keys()))
                selected_plan_id = st.session_state.cable_plans[selected_plan_name]
                
                if st.button("Biya Cable TV Yanzu", type="primary", use_container_width=True):
                    pay_payload = {"provider": selected_provider_id, "smartcard_number": smartcard_number, "plan": selected_plan_id}
                    pay_response = requests.post(f"{BASE_URL}/cable/purchase", headers=headers, json=pay_payload)
                    if pay_response.status_code == 200:
                        st.success(f"✅ An biya {selected_plan_name}")
                        st.balloons()
    except Exception as e:
        st.error(f"Matsala: {e}")

# ELECTRICITY PAGE
elif st.session_state.page == 'electricity':
    st.subheader("⚡ Pay NEPA / Electricity Bills")
    try:
        disco_response = requests.get(f"{BASE_URL}/electricity/discos", headers=headers)
        if disco_response.status_code == 200:
            discos = disco_response.json().get('data', [])
            disco_options = {d['name']: d['id'] for d in discos}
            selected_disco_name = st.selectbox("Zaɓi Kamfanin NEPA", list(disco_options.keys()))
            selected_disco_id = disco_options[selected_disco_name]
            
            meter_type = st.selectbox("Meter Type", ["prepaid", "postpaid"])
            meter_number = st.text_input("Meter Number")
            amount = st.number_input("Nawa Za Ka Biya?", min_value=500, step=100)
            
            if st.button("Duba Sunan Mai Meter"):
                if meter_number:
                    verify_payload = {"disco": selected_disco_id, "meter_number": meter_number, "meter_type": meter_type}
                    verify_response = requests.post(f"{BASE_URL}/electricity/verify", headers=headers, json=verify_payload)
                    if verify_response.status_code == 200:
                        customer_name = verify_response.json().get('data', {}).get('name', 'N/A')
                        st.session_state.customer_name = customer_name
                        st.info(f"Sunan Mai Meter: {customer_name}")

            if st.button("Biya NEPA Yanzu", type="primary", use_container_width=True):
                if meter_number and 'customer_name' in st.session_state:
                    pay_payload = {"disco": selected_disco_id, "meter_number": meter_number, "meter_type": meter_type, "amount": amount}
                    pay_response = requests.post(f"{BASE_URL}/electricity/purchase", headers=headers, json=pay_payload)
                    if pay_response.status_code == 200:
                        token = pay_response.json().get('data', {}).get('token', 'N/A')
                        st.success("✅ An biya NEPA!")
                        st.code(f"TOKEN: {token}")
                        st.balloons()
    except Exception as e:
        st.error(f"Matsala: {e}")

# WAEC PAGE
elif st.session_state.page == 'waec':
    st.subheader("📝 Buy WAEC ePIN")
    try:
        exam_response = requests.get(f"{BASE_URL}/education/exams", headers=headers)
        if exam_response.status_code == 200:
            exams = exam_response.json().get('data', [])
            waec = next((e for e in exams if 'waec' in e['name'].lower()), None)
            if waec:
                quantity = st.number_input("Quantity", min_value=1, max_value=10, value=1)
                if st.button("Buy WAEC ePIN", type="primary", use_container_width=True):
                    payload = {"exam": waec['id'], "quantity": quantity}
                    buy_response = requests.post(f"{BASE_URL}/education/purchase", headers=headers, json=payload)
                    if buy_response.status_code == 200:
                        pins = buy_response.json().get('data', {}).get('pins', [])
                        st.success(f"✅ An sayi {quantity} WAEC ePIN")
                        for pin in pins:
                            st.code(f"PIN: {pin}")
    except Exception as e:
        st.error(f"Matsala: {e}")

# JAMB PAGE
elif st.session_state.page == 'jamb':
    st.subheader("📝 Buy JAMB ePIN")
    try:
        exam_response = requests.get(f"{BASE_URL}/education/exams", headers=headers)
        if exam_response.status_code == 200:
            exams = exam_response.json().get('data', [])
            jamb = next((e for e in exams if 'jamb' in e['name'].lower()), None)
            if jamb:
                profile_code = st.text_input("JAMB Profile Code", max_chars=10)
                if st.button("Buy JAMB ePIN", type="primary", use_container_width=True):
                    if profile_code:
                        payload = {"exam": jamb['id'], "profile_code": profile_code}
                        buy_response = requests.post(f"{BASE_URL}/education/purchase", headers=headers, json=payload)
                        if buy_response.status_code == 200:
                            pin = buy_response.json().get('data', {}).get('pin', 'N/A')
                            st.success("✅ An sayi JAMB ePIN")
                            st.code(f"PIN: {pin}")
    except Exception as e:
        st.error(f"Matsala: {e}")

# TRANSACTIONS PAGE
elif st.session_state.page == 'history':
    st.subheader("📜 Tarihin Saye-Saye")
    try:
        trans_response = requests.get(f"{BASE_URL}/transactions", headers=headers)
        if trans_response.status_code == 200:
            transactions = trans_response.json().get('data', [])
            if transactions:
                st.dataframe(transactions, use_container_width=True)
            else:
                st.info("Babu transaction tukuna")
    except Exception as e:
        st.error(f"Matsala: {e}")

# FOOTER
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: grey; font-size: 12px;'>
<b>J.S.GLOBAL LINKS AND SERVICES</b><br>
CAC: RC 8984371 | WhatsApp: 07062589825<br>
NO.278, LAYIN MAI UNGUWA KANO SAUNA, KANO STATE<br>
© 2025 - Registered under CAMA 2020
</div>
""", unsafe_allow_html=True)
