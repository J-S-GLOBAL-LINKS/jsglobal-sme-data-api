st.markdown("""
<style>
[data-testid="stAppViewContainer"] {background-color: #ffffff;}
[data-testid="stHeader"] {background-color: #0d47a1;}

/* GYARAN SIDEBAR - MU SA BAKI RUBUTU */
[data-testid="stSidebar"] {
    background-color: #0d47a1;
}
[data-testid="stSidebar"] .stButton > button {
    background-color: white !important;
    color: #333333 !important;
    font-weight: 600 !important;
    border: 1px solid #e0e0e0 !important;
}
[data-testid="stSidebar"] .stButton > button:hover {
    background-color: #f5f5f5 !important;
    color: #0d47a1 !important;
    border: 1px solid #0d47a1 !important;
}
[data-testid="stSidebar"] * {
    color: white;
}
[data-testid="stSidebar"] .stButton > button * {
    color: #333333 !important;
}

.cac-banner {
    background: #0d47a1;
    color: white;
    padding: 10px;
    text-align: center;
    font-weight: bold;
    margin: -1rem -1rem 1rem -1rem;
    font-size: 13px;
}
.main-header {
    background: #0d47a1;
    padding: 1rem;
    margin: 0 -1rem 1rem -1rem;
    color: white;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.wallet-card {
    background: linear-gradient(135deg, #0d47a1 0%, #1976d2 100%);
    padding: 1.5rem;
    border-radius: 12px;
    color: white;
    margin-bottom: 1rem;
}
.service-btn > button {
    height: 100px;
    background-color: white;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    font-size: 14px;
    font-weight: 500;
    color: #333 !important;
    padding: 15px 10px;
}
.service-btn > button:hover {
    border: 1px solid #1976d2;
    box-shadow: 0 4px 8px rgba(0,0,0,0.15);
}
.upgrade-card {
    background-color: #e3f2fd;
    padding: 15px;
    border-radius: 10px;
    border-left: 4px solid #1976d2;
    margin: 1rem 0;
}
.bank-card {
    background-color: #fff3e0;
    padding: 15px;
    border-radius: 10px;
    border-left: 4px solid #ff9800;
    margin: 1rem 0;
}
</style>
""", unsafe_allow_html=True)
