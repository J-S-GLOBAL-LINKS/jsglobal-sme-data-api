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
    
    # SABON ENDPOINT DIN SMEPLUG V2
    response = requests.get("https://smeplug.com/api/v2/user", headers=headers, timeout=10)
    
    if response.status_code == 200:
        st.success("✅ API YA HAUBA - An haɗa da SMEPlug")
        data = response.json()
        st.write(f"**Sannu, {data.get('username', 'Jamilu')}**")
        st.write(f"**Balance: ₦{data.get('wallet', '0')}**")
        st.write(f"**Email: {data.get('email', 'N/A')}**")
    else:
        st.error(f"❌ API BA YA AIKI - Code: {response.status_code}")
        st.code(f"URL da aka gwada: {response.url}")
        st.code(f"SMEPlug ya ce: {response.text}")
        st.info("Idan 401 = API Key ba daidai ba. Idan 404 = URL ba daidai ba")
        
except KeyError:
    st.error("❌ API BA YA AIKI - Ba a samu API Key ba")
    st.warning("Ka je Streamlit > Settings > Secrets ka saka SMEPLUG_API_KEY")
except Exception as e:
    st.error(f"❌ Matsala: {e}")
