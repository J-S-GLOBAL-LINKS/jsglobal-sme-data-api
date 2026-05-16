import streamlit as st
import requests

st.set_page_config(page_title="J.S.GLOBAL LINKS", page_icon="logo.png")

st.image("logo.png", width=200)
st.title("J.S.GLOBAL LINKS AND SERVICES")
st.subheader("Official Data, Airtime & Bills Reseller Platform")
st.markdown("---")

try:
    api_key = st.secrets["SMEPLUG_API_KEY"]
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # URL DAIDAI DAGA POSTMAN DOCS: smeplug.ng + /account/balance
    response = requests.get("https://smeplug.ng/api/v1/account/balance", headers=headers, timeout=10)
    
    if response.status_code == 200:
        st.success("✅ API YA HAUBA - An haɗa da SMEPlug")
        data = response.json()
        st.write(f"**Wallet Balance: ₦{data.get('balance', '0')}**")
        st.write(f"**Account Name: {data.get('account_name', 'J.S GLOBAL')}**")
        st.write(f"**Account Number: {data.get('account_number', 'N/A')}**")
        st.write(f"**Bank: {data.get('bank_name', 'N/A')}**")
    else:
        st.error(f"❌ API BA YA AIKI - Code: {response.status_code}")
        st.code(f"URL: {response.url}")
        st.code(f"SMEPlug ya ce: {response.text}")
        
except Exception as e:
    st.error(f"❌ Matsala: {e}")
