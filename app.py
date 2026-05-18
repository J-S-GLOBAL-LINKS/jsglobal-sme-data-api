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
</div>
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
    
    for
