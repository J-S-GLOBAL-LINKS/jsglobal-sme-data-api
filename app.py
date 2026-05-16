import streamlit as st
import requests

st.set_page_config(page_title="J.S.GLOBAL LINKS", page_icon="logo.png", layout="wide")

st.image("logo.png", width=200)
st.title("J.S.GLOBAL LINKS AND SERVICES")
st.subheader("Official Data, Airtime & Bills Reseller Platform")
st.markdown("---")

# API SETUP
api_key = st.secrets["SMEPLUG_API_KEY"]
BASE_URL = "https://smeplug.ng/api/v1"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# TABS 3: BALANCE | BUY DATA | BUY AIRTIME
tab1, tab2, tab3 = st.tabs(["💰 Wallet Balance", "📱 Buy Data", "📞 Buy Airtime"])

# TAB 1: BALANCE
with tab1:
    try:
        response = requests.get(f"{BASE_URL}/account/balance", headers=headers, timeout=10)
        if response.status_code == 200:
            st.success("✅ API YA HAUBA - An haɗa da SMEPlug")
            data = response.json()
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Wallet Balance", f"₦{data.get('balance', '0')}")
            with col2:
                st.metric("Account Name", data.get('account_name', 'J.S GLOBAL'))
        else:
            st.error(f"❌ Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"❌ Matsala: {e}")

# TAB 2: BUY DATA
with tab2:
    st.subheader("Sayi Data Bundle")
    
    try:
        # 1. Samo Networks
        net_response = requests.get(f"{BASE_URL}/networks", headers=headers, timeout=10)
        if net_response.status_code == 200:
            networks = net_response.json().get('data', [])
            network_options = {net['name']: net['id'] for net in networks}
            
            selected_network_name = st.selectbox("Zaɓi Network", list(network_options.keys()))
            selected_network_id = network_options[selected_network_name]
            
            # 2. Samo Data Plans na Network din
            plan_response = requests.get(f"{BASE_URL}/data/plans/{selected_network_id}", headers=headers, timeout=10)
            if plan_response.status_code == 200:
                plans = plan_response.json().get('data', [])
                plan_options = {f"{p['name']} - ₦{p['price']}": p['id'] for p in plans}
                
                selected_plan_name = st.selectbox("Zaɓi Data Plan", list(plan_options.keys()))
                selected_plan_id = plan_options[selected_plan_name]
                
                phone_number = st.text_input("Lambar Wayar Mai Karɓa", placeholder="08012345678")
                
                if st.button("Saya Data Yanzu", type="primary"):
                    if phone_number and len(phone_number) == 11:
                        payload = {
                            "network": selected_network_id,
                            "plan": selected_plan_id,
                            "mobile_number": phone_number,
                            "Ported_number": True
                        }
                        buy_response = requests.post(f"{BASE_URL}/data/purchase", headers=headers, json=payload, timeout=20)
                        if buy_response.status_code == 200:
                            st.success(f"✅ An saida data! {selected_plan_name} zuwa {phone_number}")
                            st.balloons()
                        else:
                            st.error(f"❌ Saye bai yi ba: {buy_response.text}")
                    else:
                        st.warning("Don Allah a shigar da lambar waya daidai mai lamba 11")
            else:
                st.error("Bai samu data plans ba")
        else:
            st.error("Bai samu networks ba")
    except Exception as e:
        st.error(f"Matsala wajen haɗawa: {e}")

# TAB 3: BUY AIRTIME
with tab3:
    st.subheader("Sayi Airtime VTU")
    
    try:
        # Samo Networks
        net_response = requests.get(f"{BASE_URL}/networks", headers=headers, timeout=10)
        if net_response.status_code == 200:
            networks = net_response.json().get('data', [])
            network_options = {net['name']: net['id'] for net in networks}
            
            selected_network_name = st.selectbox("Zaɓi Network", list(network_options.keys()), key="airtime_net")
            selected_network_id = network_options[selected_network_name]
            
            amount = st.number_input("Nawa ne Airtime?", min_value=50, max_value=50000, step=50)
            phone_number = st.text_input("Lambar Wayar Mai Karɓa", placeholder="08012345678", key="airtime_phone")
            
            if st.button("Saya Airtime Yanzu", type="primary"):
                if phone_number and len(phone_number) == 11:
                    payload = {
                        "network": selected_network_id,
                        "amount": amount,
                        "mobile_number": phone_number,
                        "Ported_number": True
                    }
                    buy_response = requests.post(f"{BASE_URL}/airtime/purchase", headers=headers, json=payload, timeout=20)
                    if buy_response.status_code == 200:
                        st.success(f"✅ An saida airtime ₦{amount} zuwa {phone_number}")
                        st.balloons()
                    else:
                        st.error(f"❌ Saye bai yi ba: {buy_response.text}")
                else:
                    st.warning("Don Allah a shigar da lambar waya daidai mai lamba 11")
        else:
            st.error("Bai samu networks ba")
    except Exception as e:
        st.error(f"Matsala wajen haɗawa: {e}")
