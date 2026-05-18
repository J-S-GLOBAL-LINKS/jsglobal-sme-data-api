import streamlit as st
import requests

# ==== PAGE CONFIG ====
st.set_page_config(
    page_title="JS Global",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==== SESSION STATE ====
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'page' not in st.session_state:
    st.session_state.page = "Dashboard"

# CSS - DESIGN FOR ANDROID
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {background-color: #ffffff;}
[data-testid="stHeader"] {background-color: #0d47a1;}
[data-testid="stSidebar"] {background-color: white !important;}

/* SIDEBAR BUTTONS */
[data-testid="stSidebar"] .stButton > button {
    background-color: white !important;
    color: #333333 !important;
    font-weight: 500 !important;
    border: none !important;
    text-align: left !important;
    padding: 2px 4px !important;
    font-size: 9px !important;
    border-radius: 4px !important;
    margin: 0px !important;
    line-height: 1 !important;
    height: 24px !important;
}

/* WANNAN SHINE SIRRIN ANDROID */
[data-testid="stSidebar"] .stButton > button * {
    font-size: 9px !important;
    transform: scale(0.65) !important;
    display: inline-block !important;
    transform-origin: left center !important;
}

[data-testid="stSidebar"] .stButton > button:hover {
    background-color: #0d47a1 !important;
    color: white !important;
}

.stButton > button {
    background-color: #0d47a1;
    color: white;
    border-radius: 8px;
    border: none;
    padding: 10px;
    font-weight: 600;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# ==== SIDEBAR MENU ====
with st.sidebar:
    st.markdown("### Menu")
    
    if st.button("📊 Dashboard"):
        st.session_state.page = "Dashboard"
        st.rerun()
    
    if st.button("📱 Data"):
        st.session_state.page = "Data"
        st.rerun()
    
    if st.button("📞 Airtime"):
        st.session_state.page = "Airtime"
        st.rerun()
    
    if st.button("💡 Electricity"):
        st.session_state.page = "Electricity"
        st.rerun()
    
    if st.button("📺 TV"):
        st.session_state.page = "TV"
        st.rerun()
    
    if st.button("🏦 Pay Bills"):
        st.session_state.page = "Pay Bills"
        st.rerun()
    
    if st.button("🎓 Education"):
        st.session_state.page = "Education"
        st.rerun()
    
    if st.button("👛 My Wallet"):
        st.session_state.page = "My Wallet"
        st.rerun()
    
    if st.button("💰 Commission"):
        st.session_state.page = "Commission"
        st.rerun()
    
    if st.button("📜 Transactions"):
        st.session_state.page = "Transactions"
        st.rerun()
    
    if st.button("⚙️ Settings"):
        st.session_state.page = "Settings"
        st.rerun()
    
    if st.button("🔒 Logout"):
        st.session_state.logged_in = False
        st.session_state.page = "Dashboard"
        st.rerun()

# ==== MAIN PAGE CONTENT ====
st.title(f"🌐 JS Global - {st.session_state.page}")

if st.session_state.page == "Dashboard":
    st.write("Welcome to JS Global Dashboard")
    st.info("Barka da zuwa JS Global. Zaɓi service daga Menu na hagu don fara transaction.")

elif st.session_state.page == "Data":
    st.write("Data Subscription Page")
    
elif st.session_state.page == "Airtime":
    st.write("Airtime Recharge Page")
    
elif st.session_state.page == "Electricity":
    st.write("Electricity Payment Page")
    
elif st.session_state.page == "TV":
    st.write("TV Subscription Page")
    
elif st.session_state.page == "Pay Bills":
    st.write("Pay Bills Page")
    
elif st.session_state.page == "Education":
    st.write("Education Payment Page")
    
elif st.session_state.page == "My Wallet":
    st.write("My Wallet Page")
    
elif st.session_state.page == "Commission":
    st.write("Commission Page")
    
elif st.session_state.page == "Transactions":
    st.write("Transaction History Page")
    
elif st.session_state.page == "Settings":
    st.write("Settings Page")
