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
    
    # WANNAN NE URL DAIDAI - API.SMEPLUG.COM
    response = requests.get("https://api.smeplug.com/api/v2/user", headers=headers, timeout=10)
    
    if response.status_code == 200:
        st.success("✅ API YA HAUBA - An haɗa da SMEPlug")
        data = response.json()
        st.write(f"**Sannu, {data.get('username', 'Jamilu')}**")
        st.write(f"**Balance: ₦{data.get('wallet', '0')}**")
        st.write(f"**Email: {data.get('email', 'N/A')}**")
        st.write(f"**Business: {data.get('business_name', 'JSGlobal')}**")
    else:
        st.error(f"❌ API BA YA AIKI - Code: {response.status_code}")
        st.code(f"URL: {response.url}")
        st.code(f"SMEPlug ya ce: {response.text}")
        
except KeyError:
    st.error("❌ API BA YA AIKI - Ba a samu API Key ba")
except Exception as e:
    st.error(f"❌ Matsala: {e}")
