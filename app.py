import streamlit as st

# ==== PAGE CONFIG ====
st.set_page_config(
    page_title="SMEPlug",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==== SESSION STATE ====
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'page' not in st.session_state:
    st.session_state.page = "Dashboard"

# CSS - SMEPlug DESIGN
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {background-color: #f5f7fa;}
[data-testid="stHeader"] {background-color: #0d47a1;}
[data-testid="stSidebar"] {background-color: white !important; padding-top: 1rem;}

/* LOGO STYLE */
.sidebar-logo {
    text-align: center;
    padding: 10px 0px 20px 0px;
    border-bottom: 1px solid #e0e0e0;
    margin-bottom: 15px;
}
.sidebar-logo h1 {
    color: #0d47a1;
    font-size: 24px;
    font-weight: 800;
    margin: 0px;
    letter-spacing: -1px;
}
.sidebar-logo p {
    color: #666;
    font-size: 11px;
    margin: 0px;
}

/* SIDEBAR BUTTONS - PERFECT SIZE */
[data-testid="stSidebar"] .stButton > button {
    background-color: white !important;
    color: #333333 !important;
    font-weight: 500 !important;
    border: none !important;
    text-align: left !important;
    padding: 8px 12px !important;
    font-size: 14px !important;
    border-radius: 6px !important;
    margin: 3px 0px !important;
    line-height: 1.3 !important;
    height: 38px !important;
}

/* ICONS SIZE - ANDROID FIX */
[data-testid="stSidebar"] .stButton > button * {
    font-size: 14px !important;
    transform: scale(1) !important;
    display: inline-block !important;
    transform-origin: left center !important;
}

[data-testid="stSidebar"] .stButton > button:hover {
    background-color: #0d47a1 !important;
    color: white !important;
}

/* DASHBOARD CARDS */
.dashboard-card {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    margin-bottom: 15px;
}

.stButton > button {
    background-color: #0d47a1;
    color: white;
    border-radius: 8px;
    border: none;
    padding: 12px;
    font-weight: 600;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# ==== SIDEBAR MENU ====
with st.sidebar:
    # LOGO SMEPlug
    st.markdown("""
    <div class="sidebar-logo">
        <h1>⚡ SMEPlug</h1>
        <p>Your All-in-One Platform</p>
    </div>
    """, unsafe_allow_html=True)
    
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
    
    st.markdown("---")
    
    if st.button("🔒 Logout"):
        st.session_state.logged_in = False
        st.session_state.page = "Dashboard"
        st.rerun()

# ==== MAIN PAGE CONTENT ====
st.title(f"SMEPlug - {st.session_state.page}")

if st.session_state.page == "Dashboard":
    st.markdown("""
    <div class="dashboard-card">
        <h3>🎉 Barka da zuwa SMEPlug</h3>
        <p>Platform dinka na siyan Data, Airtime, da biyan Bills cikin sauki.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="dashboard-card">
            <h4>📱 Data</h4>
            <p>Siyan data MTN, Airtel, Glo, 9mobile</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="dashboard-card">
            <h4>💡 Bills</h4>
            <p>Biyan wuta, TV, ruwa da sauransu</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="dashboard-card">
            <h4>💰 Wallet</h4>
            <p>Saka kudi ka yi transaction</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.info("👈 Zaɓi service da kake so daga Menu na hagu don farawa.")

elif st.session_state.page == "Data":
    st.subheader("📱 Data Subscription")
    st.write("Zaɓi network da bundle da kake so.")
    
elif st.session_state.page == "Airtime":
    st.subheader("📞 Airtime Recharge")
    st.write("Saka number da amount.")
    
elif st.session_state.page == "Electricity":
    st.subheader("💡 Electricity Payment")
    st.write("Biyan NEPA/PHCN cikin sauki.")
    
elif st.session_state.page == "TV":
    st.subheader("📺 TV Subscription")
    st.write("DSTV, GOTV, Startimes renewal.")
    
elif st.session_state.page == "Pay Bills":
    st.subheader("🏦 Pay Bills")
    st.write("Biyan kudin ruwa da sauransu.")
    
elif st.session_state.page == "Education":
    st.subheader("🎓 Education Payment")
    st.write("WAEC, NECO, JAMB e-PIN.")
    
elif st.session_state.page == "My Wallet":
    st.subheader("👛 My Wallet")
    st.info("Balance: ₦0.00")
    st.button("Fund Wallet")
    
elif st.session_state.page == "Commission":
    st.subheader("💰 Commission")
    st.info("Commission: ₦0.00")
    
elif st.session_state.page == "Transactions":
    st.subheader("📜 Transaction History")
    st.write("Babu transaction tukuna.")
    
elif st.session_state.page == "Settings":
    st.subheader("⚙️ Settings")
    st.write("Canza password da profile.")
