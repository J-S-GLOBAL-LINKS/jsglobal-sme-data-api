import streamlit as st

st.set_page_config(
    page_title="J.S.GLOBAL",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# SESSION STATE
if 'page' not in st.session_state:
    st.session_state.page = "Dashboard"
if 'wallet_balance' not in st.session_state:
    st.session_state.wallet_balance = 0.00
if 'show_balance' not in st.session_state:
    st.session_state.show_balance = False
if 'show_sidebar' not in st.session_state:
    st.session_state.show_sidebar = False

# CUSTOM CSS - CLUBKONNECT STYLE
st.markdown("""
<style>
    /* Hide Streamlit Default */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Top Bar */
    .top-bar {
        background: #1976D2;
        padding: 15px 20px;
        color: white;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin: -1rem -1rem 1rem -1rem;
    }
    
    /* Wallet Card */
    .wallet-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 15px;
    }
    
    /* Fund Wallet Button */
    .fund-wallet-btn {
        background: #E91E63;
        color: white;
        padding: 12px 30px;
        border-radius: 25px;
        border: none;
        font-weight: bold;
        width: 100%;
        margin: 10px 0;
    }
    
    /* Upgrade Card */
    .upgrade-card {
        background: linear-gradient(135deg, #E3F2FD, #BBDEFB);
        padding: 15px;
        border-radius: 12px;
        margin: 15px 0;
        border: 1px solid #90CAF9;
    }
    
    /* Service Grid */
    .service-grid {
        display: grid;
        grid-template-columns: repeat(4,
