import streamlit as st
from supabase import create_client, Client
from datetime import datetime

# ===== PAGE CONFIG =====
st.set_page_config(
    page_title="JS GLOBAL SME DATA",
    page_icon="📱",
    layout="wide"
)

# ===== SUPABASE CONNECTION =====
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ===== SESSION STATE =====
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'current_user' not in st.session_state:
    st.session_state.current_user = None
if 'user_id' not in st.session_state:
    st.session_state.user_id = None
if 'account_type' not in st.session_state:
    st.session_state.account_type = 'user'
if 'wallet_balance' not in st.session_state:
    st.session_state.wallet_balance = 0.0
if 'full_name' not in st.session_state:
    st.session_state.full_name = ""

# ===== FUNCTIONS =====
def get_user_data(email):
    try:
        result = supabase.table('users').select("*").eq('email', email).execute()
        if result.data:
            return result.data[0]
        return None
    except:
        return None

def get_transactions(user_id):
    try:
        result = supabase.table('transactions').select("*").eq('user_id', user_id).order('created_at', desc=True).limit(10).execute()
        return result.data
    except:
        return []

# ===== LOGIN/SIGNUP/FORGOT PASSWORD PAGE =====
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align: center; color: #1E90FF;'>JS GLOBAL SME DATA</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Nigeria's #1 Data & Airtime Platform</p>", unsafe_allow_html=True)
    st.write("---")
    
    tab1, tab2, tab3 = st.tabs(["🔐 Sign In", "📝 Sign Up", "🔑 Forgot Password"])

    with tab1:
        st.subheader("Shiga Account Dinka")
        login_email = st.text_input("Email", key="login_email")
        login_pass = st.text_input("Password", type="password", key="login_pass")
        if st.button("Sign In", type="primary", use_container_width=True):
            if login_email and login_pass:
                user = get_user_data(login_email)
                if user and user['password'] == login_pass:
                    st.session_state.logged_in = True
                    st.session_state.current_user = login_email
                    st.session_state.user_id = user['id']
                    st.session_state.account_type = user['account_type']
                    st.session_state.wallet_balance = float(user['wallet_balance'])
                    st.session_state.full_name = user['full_name']
                    st.success("Login successful!")
                    st.rerun()
                else:
                    st.error("Invalid email or password")
            else:
                st.warning("Cika email da password")

    with tab2:
        st.subheader("Bude Sabon Account")
        name = st.text_input("Full Name", key="signup_name")
        signup_email = st.text_input("Email", key="signup_email")
        signup_pass = st.text_input("Password", type="password", key="signup_pass")
        signup_phone = st.text_input("Phone Number", key="signup_phone")
        if st.button("Sign Up", type="primary", use_container_width=True):
            if name and signup_email and signup_pass and signup_phone:
                try:
                    supabase.table('users').insert({
                        'full_name': name, 
                        'email': signup_email, 
                        'password': signup_pass,
                        'phone': signup_phone, 
                        'wallet_balance': 0, 
                        'kyc_status': 'pending',
                        'commission_rate': 0, 
                        'total_earnings': 0, 
                        'account_type': 'user'
                    }).execute()
                    st.success("Account created! Yanzu ka iya Sign In")
                    st.balloons()
                except Exception as e:
                    st.error("Email already exists ko akwai matsala")
            else:
                st.warning("Cika duka form din")

    with tab3:
        st.subheader("Canza Password")
        st.write("Shigar da email dinka don aiko maka link na canza password")
        reset_email = st.text_input("Email", key="reset_email")
        if st.button("Send Reset Link", type="primary", use_container_width=True):
            if reset_email:
                try:
                    supabase.auth.reset_password_for_email(reset_email)
                    st.success("An aiko link zuwa email dinka ✅")
                    st.info("Duba inbox ko spam folder")
                except Exception as e:
                    st.error("Email din nan ba a rajista ba")
            else:
                st.warning("Da fatan za a shigar da email")

# ===== DASHBOARD BAYAN LOGIN =====
else:
    # ===== SIDEBAR =====
    st.sidebar.markdown(f"**👤 {st.session_state.full_name}**")
    st.sidebar.markdown(f"**📧 {st.session_state.current_user}**")
    st.sidebar.markdown(f"**💰 Balance: ₦{st.session_state.wallet_balance:,.2f}**")
    st.sidebar.markdown(f"**👑 Type: {st.session_state.account_type.upper()}**")
    st.sidebar.write("---")
    
    if st.sidebar.button("🚪 Logout", use_container_width=True):
        st.session_state.logged_in = False
        st.rerun()
    
    st.title("📱 JS GLOBAL Dashboard")
    
    # ===== ADMIN DASHBOARD =====
    if st.session_state.account_type == 'admin':
        st.success("👑 Welcome Admin - Jamilu Haruna")
        
        admin_tab1, admin_tab2, admin_tab3 = st.tabs(["📊 Overview", "👥 Users", "💰 Transactions"])
        
        with admin_tab1:
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Total Users", "0")
            with col2:
                st.metric("Transactions", "0")
            with col3:
                st.metric("Revenue", "₦0")
            with col4:
                st.metric("Profit", "₦0")
        
        with admin_tab2:
            st.write("User Management zai zo anan")
            
        with admin_tab3:
            st.write("Duka transactions za su bayyana anan")
    
    # ===== USER DASHBOARD =====
    else:
        st.info(f"👤 Welcome {st.session_state.full_name}")
        
        tab1, tab2, tab3, tab4 = st.tabs(["📱 Buy Data", "📞 Buy Airtime", "💳 Fund Wallet", "📜 History"])
        
        with tab1:
            st.subheader("Buy Data Bundle")
            network = st.selectbox("Choose Network", ["MTN", "Glo", "Airtel", "9mobile"], key="data_network")
            
            if network == "MTN":
                plans = {"1GB - 30 Days - ₦300": 300, "2GB - 30 Days - ₦600": 600, "5GB - 30 Days - ₦1,500": 1500, "10GB - 30 Days - ₦3,000": 3000}
            elif network == "Glo":
                plans = {"1.2GB - 30 Days - ₦300": 300, "2.5GB - 30 Days - ₦600": 600, "5.8GB - 30 Days - ₦1,500": 1500, "10GB - 30 Days - ₦3,000": 3000}
            elif network == "Airtel":
                plans = {"1GB - 30 Days - ₦350": 350, "2GB - 30 Days - ₦700": 700, "5GB - 30 Days - ₦1,600": 1600, "10GB - 30 Days - ₦3,200": 3200}
            else:
                plans = {"1GB - 30 Days - ₦400": 400, "2GB - 30 Days - ₦800": 800, "5GB - 30 Days - ₦1,700": 1700, "10GB - 30 Days - ₦3,500": 3500}
            
            selected_plan = st.selectbox("Choose Data Plan", list(plans.keys()), key="data_plan")
            phone_number = st.text_input("Phone Number", placeholder="08012345678", key="data_phone")
            price = plans[selected_plan]
            
            st.info(f"**Price:** ₦{price:,}")
            
            if st.button("🚀 Buy Data Now", type="primary", use_container_width=True):
                if phone_number and len(phone_number) == 11:
                    if st.session_state.wallet_balance >= price:
                        new_balance = st.session_state.wallet_balance - price
                        supabase.table('users').update({'wallet_balance': new_balance}).eq('id', st.session_state.user_id).execute()
                        supabase.table('transactions').insert({
                            'user_id': st.session_state.user_id, 'type': 'data', 'network': network,
                            'phone_number': phone_number, 'amount': price, 'plan': selected_plan,
                            'status': 'success', 'description': f"{network} Data"
                        }).execute()
                        st.session_state.wallet_balance = new_balance
                        st.success(f"✅ Success! {selected_plan} sent to {phone_number}")
                        st.balloons()
                        st.rerun()
                    else:
                        st.error(f"❌ Insufficient Balance. Wallet: ₦{st.session_state.wallet_balance:,.2f}")
                else:
                    st.warning("Enter valid 11-digit phone number")
        
        with tab2:
            st.subheader("Buy Airtime VTU")
            airtime_network = st.selectbox("Choose Network", ["MTN", "Glo", "Airtel", "9mobile"], key="airtime_network")
            airtime_amount = st.number_input("Amount", min_value=50, max_value=50000, step=50, key="airtime_amount")
            airtime_phone = st.text_input("Phone Number", placeholder="08012345678", key="airtime_phone")
            
            st.info(f"**Amount:** ₦{airtime_amount:,}")
            
            if st.button("📞 Buy Airtime Now", type="primary", use_container_width=True):
                if airtime_phone and len(airtime_phone) == 11:
                    if st.session_state.wallet_balance >= airtime_amount:
                        new_balance = st.session_state.wallet_balance - airtime_amount
                        supabase.table('users').update({'wallet_balance': new_balance}).eq('id', st.session_state.user_id).execute()
                        supabase.table('transactions').insert({
                            'user_id': st.session_state.user_id, 'type': 'airtime', 'network': airtime_network,
                            'phone_number': airtime_phone, 'amount': airtime_amount, 'status': 'success',
                            'description': f"{airtime_network} Airtime"
                        }).execute()
                        st.session_state.wallet_balance = new_balance
                        st.success(f"✅ Success! ₦{airtime_amount:,} {airtime_network} Airtime sent to {airtime_phone}")
                        st.balloons()
                        st.rerun()
                    else:
                        st.error(f"
