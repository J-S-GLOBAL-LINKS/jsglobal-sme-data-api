import streamlit as st

st.set_page_config(
    page_title="J.S.GLOBAL",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# SESSION STATE
if 'page' not in st.session_state:
    st.session_state.page = "Dashboard"
if 'wallet_balance' not in st.session_state:
    st.session_state.wallet_balance = 0.00
if 'show_balance' not in st.session_state:
    st.session_state.show_balance = False

# CUSTOM CSS
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
   .block-container {padding: 0rem 1rem 1rem 1rem;}
    
   .top-bar {
        background: #1976D2;
        padding: 12px 15px;
        color: white;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin: -1rem -1rem 0rem -1rem;
        position: sticky;
        top: 0;
        z-index: 999;
    }
    
   .wallet-section {
        background: white;
        padding: 15px 20px 5px 20px;
        margin: 0 -1rem 10px -1rem;
    }
    
   .wallet-label {
        color: #666;
        font-size: 11px;
        font-weight: 500;
        letter-spacing: 0.5px;
    }
    
   .wallet-amount {
        font-size: 28px;
        font-weight: 700;
        color: #000;
        margin: 5px 0;
    }
    
   .upgrade-card {
        background: #E3F2FD;
        padding: 12px 15px;
        border-radius: 10px;
        margin: 15px 0;
        border: 1px solid #BBDEFB;
    }
    
   .help-float {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background: #1976D2;
        color: white;
        padding: 12px 20px;
        border-radius: 25px;
        font-weight: 600;
        font-size: 13px;
        box-shadow: 0 4px 12px rgba(25,118,210,0.4);
        z-index: 1000;
        border: none;
    }
</style>
""", unsafe_allow_html=True)

# TOP BAR
st.markdown("""
<div class='top-bar'>
    <div>☰</div>
    <div style='font-weight: 600; font-size: 16px;'>Dashboard</div>
    <div>🔔</div>
""", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    st.markdown("### JAMILU")
    st.caption("Free Member")
    st.caption("CK101278749 Upgrade >")
    
    st.markdown("---")
    
    menu_items = [
        ("🏠", "Dashboard"),
        ("📱", "Buy Airtime"),
        ("📶", "Buy Data"),
        ("📺", "Cable TV"),
        ("⚡", "Electricity"),
        ("🖨️", "Print Recharge"),
        ("🎰", "Fund Betting"),
        ("💸", "Transfer Money"),
        ("💰", "Withdraw Commission"),
        ("🎓", "WAEC ePIN"),
        ("📝", "JAMB ePIN"),
        ("🌐", "Smile Internet"),
    ]
    
    for icon, page in menu_items:
        if st.button(f"{icon} {page}", key=f"menu_{page}", use_container_width=True):
            st.session_state.page = page
            st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Sign Out →", key="signout", use_container_width=True):
        st.session_state.clear()
        st.rerun()

# MAIN DASHBOARD
if st.session_state.page == "Dashboard":
    
    # WALLET BALANCE
    st.markdown("<div class='wallet-section'>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([6, 1, 1])
    with col1:
        st.markdown("<div class='wallet-label'>WALLET BALANCE</div>", unsafe_allow_html=True)
        if st.session_state.show_balance:
            st.markdown(f"<div class='wallet-amount'>₦{st.session_state.wallet_balance:,.2f}</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='wallet-amount'>******</div>", unsafe_allow_html=True)
    with col2:
        if st.button("👁️", key="toggle_eye"):
            st.session_state.show_balance = not st.session_state.show_balance
            st.rerun()
    with col3:
        st.markdown("<div style='font-size: 12px; color: #666; text-align: right;'>1 of 2 ></div>", unsafe_allow_html=True)
    
    # FUND WALLET
    col1, col2 = st.columns([5, 1])
    with col1:
        if st.button("+ Fund Wallet", type="primary", use_container_width=True):
            st.session_state.wallet_balance += 1000
            st.rerun()
    with col2:
        if st.button("🔄", key="refresh"):
            st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # UPGRADE MEMBERSHIP
    st.markdown("""
    <div class='upgrade-card'>
        <div style='display: flex; justify-content: space-between; align-items: center;'>
            <div>
                <div style='font-weight: 700; font-size: 14px; color: #000;'>Upgrade Membership</div>
                <div style='font-size: 12px; color: #666; margin-top: 2px;'>Unlock more discounts and other benefits</div>
            </div>
            <div style='color: #1976D2; font-size: 20px;'>›</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # WHAT WOULD YOU LIKE TO DO
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown("<div style='font-weight: 600; font-size: 15px; margin: 15px 0 10px 0;'>What would you like to do?</div>", unsafe_allow_html=True)
    with col2:
        if st.button("See all >", key="see_all"):
            st.info("All Services")
    
    # SERVICES GRID
    services = [
        ("📱", "Airtime", "Buy Airtime"),
        ("📶", "Data", "Buy Data"),
        ("📺", "Cable\nTV", "Cable TV"),
        ("⚡", "Electricity", "Electricity"),
        ("🖨️", "Print\nRecharge", "Print Recharge"),
        ("🎰", "Fund\nBetting", "Fund Betting"),
        ("💸", "Transfer\nMoney", "Transfer Money"),
        ("💰", "Withdraw\nCommission", "Withdraw Commission"),
        ("🎓", "WAEC\nePIN", "WAEC ePIN"),
        ("📝", "JAMB\nePIN", "JAMB ePIN"),
        ("🌐", "Smile\nInternet", "Smile Internet"),
    ]
    
    # Display 4 columns
    for i in range(0, len(services), 4):
        cols = st.columns(4)
        for j in range(4):
            if i + j < len(services):
                icon, name, page = services[i + j]
                with cols[j]:
                    if st.button(f"{icon}\n{name}", key=f"service_{i+j}", use_container_width=True):
                        st.session_state.page = page
                        st.rerun()
    
    # NEED HELP
    st.markdown("""
    <div style='background: white; padding: 15px; border-radius: 10px; margin: 15px 0; border: 1px solid #E0E0E0;'>
        <div style='display: flex; align-items: center; gap: 10px;'>
            <div style='font-size: 24px;'>❓</div>
            <div>
                <div style='font-weight: 700; font-size: 14px;'>Need Help?</div>
                <div style='font-size: 12px; color: #666;'>Try our self service or open a ticket</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# SERVICE PAGES
elif st.session_state.page == "Buy Airtime":
    st.title("📱 Buy Airtime")
    network = st.selectbox("Select Network", ["MTN", "Airtel", "Glo", "9mobile"])
    phone = st.text_input("Phone Number", placeholder="08012345678")
    amount = st.number_input("Amount", min_value=50, step=50, value=100)
    if st.button("Buy Airtime", type="primary", use_container_width=True):
        if phone and len(phone) == 11:
            st.success(f"✅ Airtime ₦{amount:,} sent to {phone}")
            st.session_state.wallet_balance -= amount
            st.balloons()
        else:
            st.error("Enter valid phone number")

elif st.session_state.page == "Buy Data":
    st.title("📶 Buy Data")
    network = st.selectbox("Select Network", ["MTN", "Airtel", "Glo", "9mobile"])
    
    plans = {
        "MTN": ["1GB - 30 Days - ₦290", "2GB - 30 Days - ₦580", "5GB - 30 Days - ₦1,450"],
        "Airtel": ["1GB - 30 Days - ₦290", "2GB - 30 Days - ₦580", "5GB - 30 Days - ₦1,450"],
        "Glo": ["1GB - 30 Days - ₦270", "2GB - 30 Days - ₦540", "5GB - 30 Days - ₦1,350"],
        "9mobile": ["1GB - 30 Days - ₦280", "2GB - 30 Days - ₦560", "5GB - 30 Days - ₦1,400"]
    }
    
    plan = st.selectbox("Select Data Plan", plans[network])
    phone = st.text_input("Phone Number", placeholder="08012345678")
    
    if st.button("Buy Data", type="primary", use_container_width=True):
        if phone and len(phone) == 11:
            st.success(f"✅ Data {plan} sent to {phone}")
            st.balloons()
        else:
            st.error("Enter valid phone number")

else:
    st.title(st.session_state.page)
    st.info(f"{st.session_state.page} feature coming soon...")
    if st.button("← Back to Dashboard"):
        st.session_state.page = "Dashboard"
        st.rerun()

# FLOATING HELP BUTTON
st.markdown("""
<button class='help-float'>Need Help?</button>
""", unsafe_allow_html=True)
