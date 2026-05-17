st.markdown("""
<style>
    /* Hide default Streamlit padding */
   .main.block-container {
        padding-top: 1rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }

    /* Blue gradient header */
   .blue-header {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin-bottom: 1rem;
    }

    /* Pink fund button */
   .stButton > button[kind="primary"] {
        background-color: #e91e63;
        color: white;
        border-radius: 25px;
        border: none;
        padding: 0.5rem 1.5rem;
        font-weight: 600;
    }

    /* Service cards */
   .service-card {
        background: white;
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        cursor: pointer;
        transition: transform 0.2s;
        min-height: 110px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
   .service-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
   .service-card img {
        width: 40px;
        height: 40px;
        margin-bottom: 8px;
    }
   .service-card p {
        margin: 0;
        font-size: 12px;
        font-weight: 500;
        color: #333;
    }

    /* Upgrade membership card */
   .upgrade-card {
        background-color: #e8eaf6;
        padding: 15px;
        border-radius: 12px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
    }

    /* Need help card */
   .help-card {
        background-color: #e8eaf6;
        padding: 15px;
        border-radius: 12px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 1rem;
    }

    /* Hide Streamlit default button styling for cards */
    div[data-testid="column"] button {
        background: none;
        border: none;
        padding: 0;
    }
</style>
""", unsafe_allow_html=True)
