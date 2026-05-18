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

# CSS - DESIGN
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {background-color: #ffffff;}
[data-testid="stHeader"] {background-color: #0d47a1;}
[data-testid="stSidebar"] {background-color: white !important;}

/* SIDEBAR BUTTONS - KANKANAN */
[data-testid="stSidebar"] .stButton > button {
    background-color: white !important;
    color: #333333 !important;
    font-weight: 500 !important;
    border: none !important;
    text-align: left !important;
    padding: 4px 6px !important;
    font-size: 11px !important;
    border-radius: 5px !important;
    margin: 1px 0px !important;
    line-height: 1.1 !important;
    height: 30px !important;
}

/* RAGE GIRMAN EMOJI */
[data-testid="stSidebar"] .stButton > button p {
    font-size: 11px !important;
}

[data-testid="stSidebar"] button div[data-testid="stMarkdownContainer"] p {
    font-size: 11px !important;
}

[data-testid="stSidebar"] .stButton > button:hover {
    background-color: #0d47a1 !important;
    color: white !important;
}

/* SAURAN BUTTONS A CIKIN APP */
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
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Wallet Balance", "₦25,000")
    with col2:
        st.metric("Today Sales", "₦8,500")
    with col3:
        st.metric("Commission", "₦1,200")

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
