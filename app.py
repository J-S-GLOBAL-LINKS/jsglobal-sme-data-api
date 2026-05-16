
import streamlit as st
import requests

st.set_page_config(
    page_title="J.S.GLOBAL LINKS",
    page_icon="logo.png"
)

st.image("logo.png", width=200)
st.title("J.S.GLOBAL LINKS AND SERVICES")
st.subheader("Official Data, Airtime & Bills Reseller Platform")
st.markdown("---")

# DUBA API KEY A SECRETS
try:
    api_key = st.secrets["SMEPLUG_API_KEY"]
    
    # GWADA API KEY DIN
    headers = {"Authorization": f"Token {api_key}"}
    response = requests.get("https://smeplug.com/api/v1/user", headers=headers, timeout=10)
    
    if response.status_code == 200:
        st.success("✅ API YA HAUBA - An haɗa da SMEPlug")
        user_data = response.json()
        st.write(f"Sannu, {user_data.get('name', 'User')}")
        st.write(f"Balance: ₦{user_data.get('wallet_balance', 0)}")
    else:
        st.error(f"❌ API BA YA AIKI - Code: {response.status_code}")
        st.warning("Duba API Key dinka a Secrets ko kuma balance dinka")

except Exception as e:
    st.error("❌ API BA YA AIKI - Ba a samu API Key ba")
    st.info("Je zuwa 'Manage app' > 'Secrets' ka saka SMEPLUG_API_KEY")
    st.code('SMEPLUG_API_KEY = "key_dinka_anan"')