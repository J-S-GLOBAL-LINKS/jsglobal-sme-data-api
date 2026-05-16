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
        "Authorization": f"Token {api_key}",
        "Content-Type": "application/json"
    }
    
    # MU GWADA /me MAIMAKON /user
    response = requests.get("https://smeplug.com/api/v1/me", headers=headers, timeout=10)
    
    if response.status_code == 200:
        st.success("✅ API YA HAUBA - An haɗa da SMEPlug")
        data = response.json()
        st.write(f"**Sannu, {data.get('username', data.get('name', 'JSGlobal'))}**")
        st.write(f"**Balance: ₦{data.get('balance', data.get('wallet', '0'))}**")
        st.write(f"**Email: {data.get('email', 'N/A')}**")
    else:
        st.error(f"❌ API BA YA AIKI - Code: {response.status_code}")
        st.code(f"URL: {response.url}")
        st.code(f"SMEPlug ya ce: {response.text}")
        
except Exception as e:
    st.error(f"❌ Matsala: {e}")
