import streamlit as st
import requests

st.set_page_config(page_title="J.S.GLOBAL LINKS", page_icon="logo.png", layout="wide")

# HEADER DA CAC - REAL DATA DINKA
col1, col2 = st.columns([1, 4])
with col1:
    st.image("logo.png", width=150)
with col2:
    st.title("J.S.GLOBAL LINKS AND SERVICES")
    st.subheader("Official Data, Airtime & Bills Reseller Platform")
    st.success("✅ CAC REGISTERED: RC 8984371 | 📞 WhatsApp: 07062589825 | 📍 Nigeria")

st.markdown("---")

# API SETUP
api_key = st.secrets["SMEPLUG_API_KEY"]
BASE_URL = "https://smeplug.ng/api/v1"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# TABS 6
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "💰 Balance", "📱 Data", "📞 Airtime", "⚡ NEPA", "📺 Cable TV", "📜 History"
])

# TAB 1: BALANCE
with tab1:
    try:
        response = requests.get(f"{BASE_URL}/account/balance", headers=headers, timeout=10)
        if response.status_code == 200:
            st.success("✅ API YA HAUBA - An haɗa da SMEPlug")
            data = response.json()
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Wallet Balance", f"₦{data.get('balance', '0')}")
            with col2:
                st.metric("Account Name", data.get('account_name', 'J.S GLOBAL'))
            with col3:
                st.metric("CAC Status", "RC 8984371 ✅")
        else:
            st.error(f"❌ Error: {response.status_code}")
    except Exception as e:
        st.error(f"❌ Matsala: {e}")

# TAB 2: BUY DATA
with tab2:
    st.subheader("Sayi Data Mai Rahusa")
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
                    if len(phone_number) == 11 and phone_number.isdigit():
                        payload = {"network": selected_network_id, "plan": selected_plan_id, "mobile_number": phone_number, "Ported_number": True}
                        buy_response = requests.post(f"{BASE_URL}/data/purchase", headers=headers, json=payload)
                        if buy_response.status_code == 200:
                            st.success(f"✅ An saida {selected_plan_name} zuwa {phone_number}")
                            st.balloons()
                        else:
                            st.error(f"❌ Error: {buy_response.text}")
                    else:
                        st.warning("Lambar waya ba daidai ba")
    except Exception as e:
        st.error(f"Matsala: {e}")

# TAB 3: BUY AIRTIME
with tab3:
    st.subheader("Sayi Airtime VTU - Instant")
    try:
        net_response = requests.get(f"{BASE_URL}/networks", headers=headers)
        if net_response.status_code == 200:
            networks = net_response.json().get('data', [])
            network_options = {net['name']: net['id'] for net in networks}
            selected_network_name = st.selectbox("Zaɓi Network", list(network_options.keys()), key="airtime_net")
            selected_network_id = network_options[selected_network_name]
            amount = st.number_input("Nawa Airtime?", min_value=50, max_value=50000, step=50)
            phone_number = st.text_input("Lambar Wayar", placeholder="08012345678", key="airtime_phone", max_chars=11)
            
            if st.button("Saya Airtime Yanzu", type="primary", use_container_width=True):
                if len(phone_number) == 11 and phone_number.isdigit():
                    payload = {"network": selected_network_id, "amount": amount, "mobile_number": phone_number, "Ported_number": True}
                    buy_response = requests.post(f"{BASE_URL}/airtime/purchase", headers=headers, json=payload)
                    if buy_response.status_code == 200:
                        st.success(f"✅ An saida airtime ₦{amount} zuwa {phone_number}")
                        st.balloons()
                    else:
                        st.error(f"❌ Error: {buy_response.text}")
    except Exception as e:
        st.error(f"Matsala: {e}")

# TAB 4: NEPA / ELECTRICITY
with tab4:
    st.subheader("Biya Kuɗin NEPA / Lantarki")
    try:
        disco_response = requests.get(f"{BASE_URL}/electricity/discos", headers=headers)
        if disco_response.status_code == 200:
            discos = disco_response.json().get('data', [])
            disco_options = {d['name']: d['id'] for d in discos}
            selected_disco_name = st.selectbox("Zaɓi Kamfanin NEPA", list(disco_options.keys()))
            selected_disco_id = disco_options[selected_disco_name]
            
            meter_type = st.selectbox("Meter Type", ["prepaid", "postpaid"])
            meter_number = st.text_input("Meter Number", placeholder="12345678901")
            amount = st.number_input("Nawa Za Ka Biya?", min_value=500, max_value=50000, step=100)
            
            if st.button("Duba Sunan Mai Meter"):
                if meter_number:
                    verify_payload = {"disco": selected_disco_id, "meter_number": meter_number, "meter_type": meter_type}
                    verify_response = requests.post(f"{BASE_URL}/electricity/verify", headers=headers, json=verify_payload)
                    if verify_response.status_code == 200:
                        customer_name = verify_response.json().get('data', {}).get('name', 'N/A')
                        st.session_state.customer_name = customer_name
                        st.info(f"Sunan Mai Meter: {customer_name}")
                    else:
                        st.error("Meter Number ba daidai ba")

            if st.button("Biya NEPA Yanzu", type="primary", use_container_width=True):
                if meter_number and 'customer_name' in st.session_state:
                    pay_payload = {"disco": selected_disco_id, "meter_number": meter_number, "meter_type": meter_type, "amount": amount}
                    pay_response = requests.post(f"{BASE_URL}/electricity/purchase", headers=headers, json=pay_payload)
                    if pay_response.status_code == 200:
                        token = pay_response.json().get('data', {}).get('token', 'N/A')
                        st.success(f"✅ An biya NEPA! Token: {token}")
                        st.code(f"Token: {token}")
                        st.balloons()
                    else:
                        st.error(f"❌ Biyan bai yi ba: {pay_response.text}")
                else:
                    st.warning("Da farko ka duba sunan mai meter")
    except Exception as e:
        st.error(f"Matsala: {e}")

# TAB 5: CABLE TV
with tab5:
    st.subheader("Biya Kuɗin DSTV / GOTV / Startimes")
    try:
        cable_response = requests.get(f"{BASE_URL}/cable/providers", headers=headers)
        if cable_response.status_code == 200:
            providers = cable_response.json().get('data', [])
            provider_options = {p['name']: p['id'] for p in providers}
            selected_provider_name = st.selectbox("Zaɓi TV", list(provider_options.keys()))
            selected_provider_id = provider_options[selected_provider_name]
            
            smartcard_number = st.text_input("Smartcard / IUC Number", placeholder="1234567890")
            
            if st.button("Duba
