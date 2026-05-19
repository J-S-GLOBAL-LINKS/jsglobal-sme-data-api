import streamlit as st
import requests
from datetime import datetime
from supabase import create_client, Client

# ===== CONFIG =====
st.set_page_config(
    page_title="J.S.GLOBAL",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ===== SECRETS =====
SMPLUG_API_KEY = st.secrets["SMPLUG_API_KEY"]
PAYSTACK_SECRET_KEY = st.secrets["PAYSTACK_SECRET_KEY"]
PAYSTACK_PUBLIC_KEY = st.secrets["PAYSTACK_PUBLIC_KEY"]
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
ADMIN_PASSWORD = st.secrets["ADMIN_PASSWORD"]
SMPLUG_BASE_URL = "https://smplug.ng/api"

# ===== SUPABASE INIT =====
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ===== SESSION STATE =====
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'current_user' not in st.session_state:
    st.session_state.current_user = None
if 'user_id' not in st.session_state:
    st.session_state.user_id = None
if 'page' not in st.session_state:
    st.session_state.page = "Dashboard"
if 'wallet_balance' not in st.session_state:
    st.session_state.wallet_balance = 0.00
if 'show_balance' not in st.session_state:
    st.session_state.show_balance = False
if 'kyc_status' not in st.session_state:
    st.session_state.kyc_status = "Not Submitted"
if 'account_type' not in st.session_state:
    st.session_state.account_type = "user"
if 'admin_logged_in' not in st.session_state:
    st.session_state.admin_logged_in = False

# ===== CSS =====
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
.block-container {padding: 0rem 1rem 1rem 1rem;}
.top-bar {background: #1976D2; padding: 12px 15px; color: white; display: flex; justify-content: space-between; align-items: center; margin: -1rem -1rem 0rem -1rem; position: sticky; top: 0; z-index: 999;}
.wallet-section {background: white; padding: 15px 20px 5px 20px; margin: 0 -1rem 10px -1rem;}
.wallet-label {color: #666; font-size: 11px; font-weight: 500; letter-spacing: 0.5px;}
.wallet-amount {font-size: 28px; font-weight: 700; color: #000; margin: 5px 0;}
.kyc-badge {background: #FF9800; color: white; padding: 2px 8px; border-radius: 12px; font-size: 10px; font-weight: 600;}
.upgrade-card {background: #E3F2FD; padding: 12px 15px; border-radius: 10px; margin: 15px 0; border: 1px solid #BBDEFB;}
</style>
""", unsafe_allow_html=True)

# ===== DATABASE FUNCTIONS =====
def get_user_data(email):
    try:
        response = supabase.table('users').select("*").eq('email', email).execute()
        return response.data[0] if response.data else None
    except:
        return None

def update_wallet(user_id, amount):
    try:
        supabase.table('users').update({'wallet_balance': amount}).eq('id', user_id).execute()
        st.session_state.wallet_balance = amount
    except:
        pass

def save_transaction(user_id, service, amount, status, ref, phone=""):
    try:
        supabase.table('transactions').insert({
            'user_id': user_id,
            'service': service,
            'amount': amount,
            'status': status,
            'reference': ref,
            'phone': phone,
            'date': datetime.now().isoformat()
        }).execute()
    except:
        pass

def add_commission(reseller_id, sub_user_id, service, amount):
    try:
        commission = amount * 0.02
        supabase.table('commissions').insert({
            'reseller_id': reseller_id,
            'sub_user_id': sub_user_id,
            'service': service,
            'amount': amount,
            'commission': commission,
            'date': datetime.now().isoformat()
        }).execute()

        reseller = supabase.table('users').select("total_earnings,wallet_balance").eq('id', reseller_id).execute()
        if reseller.data:
            new_earn = float(reseller.data[0]['total_earnings']) + commission
            new_wallet = float(reseller.data[0]['wallet_balance']) + commission
            supabase.table('users').update({'total_earnings': new_earn, 'wallet_balance': new_wallet}).eq('id', reseller_id).execute()
    except:
        pass

# ===== LOGIN / SIGNUP =====
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align: center; color: #1a237e;'>JS GLOBAL SME DATA</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>Welcome to your VTU Platform</p>", unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["🔐 Sign In", "📝 Sign Up"])

    with tab1:
        login_email = st.text_input("Email", key="login_email")
        login_pass = st.text_input("Password", type="password", key="login_pass")

        if st.button("Sign In", type="primary", use_container_width=True):
            user = get_user_data(login_email)
            if user and user['password'] == login_pass:
                st.session_state.logged_in = True
                st.session_state.current_user = login_email
                st.session_state.user_id = user['id']
                st.session_state.wallet_balance = float(user['wallet_balance'])
                st.session_state.kyc_status = user['kyc_status']
                st.session_state.account_type = user['account_type']
                st.rerun()
            else:
                st.error("Invalid email or password")

    with tab2:
        name = st.text_input("Full Name")
        signup_email = st.text_input("Email", key="signup_email")
        signup_pass = st.text_input("Password", type="password", key="signup_pass")
        signup_phone = st.text_input("Phone Number")

        if st.button("Sign Up", type="primary", use_container_width=True):
            try:
                supabase.table('users').insert({
                    'full_name': name,
                    'email': signup_email,
                    'password': signup_pass,
                    'phone': signup_phone,
                    'wallet_balance': 0,
                    'kyc_status': 'Not Submitted',
                    'account_type': 'user',
                    'commission_rate': 0,
                    'total_earnings': 0
                }).execute()
                st.success("Account created! Please Sign In")
                st.balloons()
            except Exception as e:
                st.error("Email already exists or error occurred")

# ===== MAIN APP =====
else:
    user_data = get_user_data(st.session_state.current_user)

    # TOP BAR
    st.markdown("""<div class='top-bar'><div>☰</div><div style='font-weight: 600; font-size: 16px;'>Dashboard</div><div>🔔</div></div>""", unsafe_allow_html=True)

    # SIDEBAR
    with st.sidebar:
        st.markdown(f"### {user_data['full_name'].upper()}")

        if st.session_state.kyc_status == "Approved":
            st.markdown("✅ <span class='kyc-badge'>TIER 3 VERIFIED</span>", unsafe_allow_html=True)
        elif st.session_state.account_type == "reseller":
            st.markdown("👑 <span class='kyc-badge'>RESELLER</span>", unsafe_allow_html=True)
        else:
            st.markdown("⚠️ <span class='kyc-badge'>TIER 1</span>", unsafe_allow_html=True)

        st.caption("CK101278749 Upgrade >")
        st.markdown("---")

        menu_items = [
            ("🏠", "Dashboard"),
            ("👤", "KYC Verification"),
            ("👥", "My Resellers"),
            ("💰", "Fund Wallet"),
            ("📱", "Buy Airtime"),
            ("📶", "Buy Data"),
            ("📺", "Cable TV"),
            ("⚡", "Electricity"),
            ("💸", "Transactions"),
            ("👑", "Admin Panel")
        ]

        for icon, page in menu_items:
            if st.button(f"{icon} {page}", key=f"menu_{page}", use_container_width=True):
                st.session_state.page = page
                st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🚪 Sign Out", use_container_width=True):
            for key in st.session_state.keys():
                del st.session_state[key]
            st.rerun()

    # ===== DASHBOARD =====
    if st.session_state.page == "Dashboard":
        st.markdown("<div class='wallet-section'>", unsafe_allow_html=True)
        col1, col2 = st.columns([6, 1])
        with col1:
            st.markdown("<div class='wallet-label'>WALLET BALANCE</div>", unsafe_allow_html=True)
            if st.session_state.show_balance:
                st.markdown(f"<div class='wallet-amount'>₦{st.session_state.wallet_balance:,.2f}</div>", unsafe_allow_html=True)
            else:
                st.markdown("<div class='wallet-amount'>******</div>", unsafe_allow_html=True)
        with col2:
            if st.button("👁️"):
                st.session_state.show_balance = not st.session_state.show_balance
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

        if st.session_state.kyc_status!= "Approved":
            st.warning("⚠️ Complete KYC to unlock ₦5,000,000 daily limit")

        if st.session_state.account_type == "reseller":
            st.markdown(f"""
            <div class='upgrade-card'>
                <div style='display: flex; justify-content: space-between; align-items: center;'>
                    <div>
                        <div style='font-weight: 700; font-size: 14px; color: #000;'>Reseller Account</div>
                        <div style='font-size: 12px; color: #666; margin-top: 2px;'>Total Earnings: ₦{user_data['total_earnings']:,.2f}</div>
                    </div>
                    <div style='color: #1976D2; font-size: 20px;'>›</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<div style='font-weight: 600; font-size: 15px; margin: 15px 0 10px 0;'>What would you like to do?</div>", unsafe_allow_html=True)

        services = [("📱", "Airtime", "Buy Airtime"), ("📶", "Data", "Buy Data"), ("📺", "Cable\nTV", "Cable TV"), ("⚡", "Electricity", "Electricity")]
        cols = st.columns(4)
        for i, (icon, name, page) in enumerate(services):
            with cols[i]:
                if st.button(f"{icon}\n{name}", key=f"srv_{i}", use_container_width=True):
                    st.session_state.page = page
                    st.rerun()

    # ===== KYC PAGE =====
    elif st.session_state.page == "KYC Verification":
        st.title("👤 KYC Verification")

        if st.session_state.kyc_status == "Approved":
            st.success("✅ KYC Approved - Tier 3 Limit: ₦5,000,000/day")
        elif st.session_state.kyc_status == "Pending":
            st.info("⏳ KYC Under Review - Please wait 24 hours")
        else:
            kyc_type = st.radio("Verification Type", ["Individual", "Business/CAC"], horizontal=True)

            with st.form("kyc_form"):
                if kyc_type == "Individual":
                    st.subheader("Personal Information")
                    col1, col2 = st.columns(2)
                    with col1:
                        first_name = st.text_input("First Name *")
                        last_name = st.text_input("Last Name *")
                        dob = st.date_input("Date of Birth *")
                    with col2:
                        phone = st.text_input("Phone Number *")
                        address = st.text_area("Home Address *")
                        state = st.selectbox("State *", ["Kano", "Lagos", "Abuja", "Kaduna", "Rivers", "Oyo"])

                    id_type = st.selectbox("ID Type *", ["NIN", "BVN", "Driver's License"])
                    id_number = st.text_input(f"{id_type} Number *")
                    id_front = st.file_uploader("Upload ID Front *", type=["jpg", "png", "pdf"])
                else:
                    st.subheader("Business Information")
                    business_name = st.text_input("Business Name *")
                    rc_number = st.text_input("RC Number *")
                    business_type = st.selectbox("Business Type *", ["Sole Proprietorship", "LLC", "Limited"])
                    cac_cert = st.file_uploader("CAC Certificate *", type=["jpg", "png", "pdf"])
                    director_name = st.text_input("Director Full Name *")
                    director_bvn = st.text_input("Director BVN *")

                if st.form_submit_button("Submit KYC", type="primary"):
                    supabase.table('users').update({'kyc_status': 'Pending'}).eq('id', st.session_state.user_id).execute()
                    st.session_state.kyc_status = "Pending"
                    st.success("KYC Submitted Successfully!")
                    st.balloons()
                    st.rerun()

    # ===== RESELLER PAGE =====
    elif st.session_state.page == "My Resellers":
        st.title("👥 My Resellers & Commission")

        if user_data['account_type'] == 'reseller':
            tab1, tab2, tab3 = st.tabs(["📊 Overview", "➕ Add Sub-User", "💸 Earnings"])

            with tab1:
                sub_users = supabase.table('users').select("*").eq('parent_id', st.session_state.user_id).execute()
                comm = supabase.table('commissions').select("commission").eq('reseller_id', st.session_state.user_id).execute()
                total_earn = sum([float(c['commission']) for c in comm.data])

                col1, col2, col3 = st.columns(3)
                col1.metric("Total Sub-Users", len(sub_users.data))
                col2.metric("Total Earnings", f"₦{total_earn:,.2f}")
                col3.metric("Commission Rate", "2%")

                st.subheader("Your Sub-Users")
                if sub_users.data:
                    st.dataframe(sub_users.data, use_container_width=True)
                else:
                    st.info("No sub-users yet")

            with tab2:
                with st.form("sub_user_form"):
                    sub_name = st.text_input("Full Name *")
                    sub_email = st.text_input("Email *")
                    sub_pass = st.text_input("Password *", type="password")
                    sub_phone = st.text_input("Phone Number *")

                    if st.form_submit_button("Create Sub-User", type="primary"):
                        try:
                            supabase.table('users').insert({
                                'full_name': sub_name,
                                'email': sub_email,
                                'password': sub_pass,
                                'phone': sub_phone,
                                'account_type': 'sub_user',
                                'parent_id': st.session_state.user_id,
                                'wallet_balance': 0,
                                'kyc_status': 'Not Submitted',
                                'commission_rate': 0,
                                'total_earnings': 0
                            }).execute()
                            st.success(f"Sub-User {sub_name} created!")
                            st.rerun()
                        except:
                            st.error("Email already exists")

            with tab3:
                comm_history = supabase.table('commissions').select("*").eq('reseller_id', st.session_state.user_id).order('date', desc=True).execute()
                if comm_history.data:
                    st.dataframe(comm_history.data, use_container_width=True)
                else:
                    st.info("No commissions yet")
        else:
            st.info("🚀 Upgrade to Reseller Account to earn 2% commission on all sub-users")
            if st.button("Upgrade to Reseller - ₦10,000", type="primary"):
                if st.session_state.wallet_balance >= 10000:
                    new_bal = st.session_state.wallet_balance - 10000
                    supabase.table('users').update({
                        'account_type': 'reseller',
                        'commission_rate': 2.0,
                        'wallet_balance': new_bal
                    }).eq('id', st.session_state.user_id).execute()
                    st.session_state.wallet_balance = new_bal
                    st.session_state.account_type = 'reseller'
                    st.success("Upgraded to Reseller!")
                    st.balloons()
                    st.rerun()
                else:
                    st.error("Insufficient balance. Fund wallet first")

    # ===== FUND WALLET - PAYSTACK =====
    elif st.session_state.page == "Fund Wallet":
        st.title("💰 Fund Wallet")
        amount = st.number_input("Amount (₦)", min_value=100, value=1000, step=100)

        if st.button("Pay with Paystack", type="primary", use_container_width=True):
            headers = {"Authorization": f"Bearer {PAYSTACK_SECRET_KEY}"}
            data = {
                "email": st.session_state.current_user,
                "amount": int(amount * 100),
                "callback_url": "https://yourapp.streamlit.app"
            }
            res = requests.post("https://api.paystack.co/transaction/initialize", headers=headers, json=data)

            if res.status_code == 200:
                url = res.json()['data']['authorization_url']
                st.success("Click below to pay")
                st.link_button("Pay Now", url)
                st.info("After successful payment, refresh this page to see updated balance")
            else:
                st.error("Payment initialization failed")

    # ===== BUY AIRTIME - SMEPLUG =====
    elif st.session_state.page == "Buy Airtime":
        st.title("📱 Buy Airtime")
        network = st.selectbox("Network", ["MTN", "AIRTEL", "GLO", "9MOBILE"])
        phone = st.text_input("Phone Number", placeholder="08012345678")
        amount = st.number_input("Amount", min_value=50, step=50, value=100)

        if st.button("Buy Airtime", type="primary", use_container_width=True):
            if phone and len(phone) == 11:
                if st.session_state.wallet_balance >= amount:
                    headers = {"Authorization": f"Token {SMPLUG_API_KEY}", "Content-Type": "application/json"}
                    payload = {"network": network, "mobile_number": phone, "amount": amount, "Ported_number": True}

                    with st.spinner("Processing..."):
                        res = requests.post(f"{SMPLUG_BASE_URL}/topup/", headers=headers, json=payload)

                        if res.json().get("status") == "success":
                            if user_data['parent_id']:
                                add_commission(user_data['parent_id'], st.session_state.user_id, "Airtime", amount)

                            new_bal = st.session_state.wallet_balance - amount
                            update_wallet(st.session_state.user_id, new_bal)
                            save_transaction(st.session_state.user_id, "Airtime", amount, "Success", res.json().get('id'), phone)
                            st.success(f"✅ Airtime ₦{amount:,} sent to {phone}")
                            st.balloons()
                        else:
                            st.error("Failed: " + str(res.json().get('message', 'Unknown error')))
                else:
                    st.error("Insufficient wallet balance")
            else:
                st.error("Enter valid 11-digit phone number")

    # ===== BUY DATA - SMEPLUG =====
    elif st.session_state.page == "Buy Data":
        st.title("📶 Buy Data")
        provider = st.selectbox("Network", ["MTN", "AIRTEL", "GLO", "9MOBILE"])
        phone = st.text_input("Phone Number", placeholder="08012345678")

        plans = {
            "MTN": {"1GB - ₦350": "2", "2GB - ₦700": "3", "5GB - ₦1,500": "5"},
            "AIRTEL": {"1.5GB - ₦500": "8", "3GB - ₦1,000": "9", "6GB - ₦1,500": "10"},
            "GLO": {"1GB - ₦300": "13", "2GB - ₦600": "14", "4.5GB - ₦1,000": "15"},
            "9MOBILE": {"1GB - ₦500": "20", "2GB - ₦1,000": "21", "7GB - ₦1,500": "22"}
        }

        plan_name = st.selectbox("Select Plan", list(plans[provider].keys()))
        plan_id = plans[provider][plan_name]
        amount = int(plan_name.split("₦")[1].replace(",", ""))

        if st.button("Buy Data", type="primary", use_container_width=True):
            if phone and len(phone) == 11:
                if st.session_state.wallet_balance >= amount:
                    headers = {"Authorization": f"Token {SMPLUG_API_KEY}", "Content-Type": "application/json"}
                    payload = {"network": provider, "mobile_number": phone, "plan": plan_id, "Ported_number": True}

                    with st.spinner("Processing..."):
                        res = requests.post(f"{SMPLUG_BASE_URL}/data", headers=headers, json=payload)

                        if res.json().get("status") == "success":
                            if user_data['parent_id']:
                                add_commission(user_data['parent_id'], st.session_state.user_id, "Data", amount)

                            new_bal = st.session_state.wallet_balance - amount
                            update_wallet(st.session_state.user_id, new_bal)
                            save_transaction(st.session_state.user_id, "Data", amount, "Success", res.json().get('id'), phone)
                            st.success(f"✅ {plan_name} sent to {phone}")
                            st.balloons()
                        else:
                            st.error("Failed: " + str(res.json().get('message', 'Unknown error')))
                else:
                    st.error("Insufficient wallet balance")
            else:
                st.error("Enter valid phone number")

    # ===== TRANSACTIONS =====
    elif st.session_state.page == "Transactions":
        st.title("💸 Transaction History")
        trans = supabase.table('transactions').select("*").eq('user_id', st.session_state.user_id).order('date', desc=True).limit(50).execute()
        if trans.data:
            st.dataframe(trans.data, use_container_width=True)
        else:
            st.info("No transactions yet")

    # ===== ADMIN PANEL =====
    elif st.session_state.page == "Admin Panel":
        st.title("👑 Admin Panel")

        if not st.session_state.admin_logged_in:
            admin_pass = st.text_input("Admin Password", type="password")
            if st.button("Login as Admin"):
                if admin_pass == ADMIN_PASSWORD:
                    st.session_state.admin_logged_in = True
                    st.rerun()
                else:
                    st.error("Wrong Password")
        else:
            if st.button("🚪 Logout Admin"):
                st.session_state.admin_logged_in = False
                st.rerun()

            tab1, tab2, tab3, tab4 = st.tabs(["📋 KYC Requests", "👥 All Users", "💰 Transactions", "📊 Stats"])

            with tab1:
                st.subheader("Pending KYC Verifications")
                users = supabase.table('users').select("*").eq('kyc_status', 'Pending').execute()
                for user in users.data:
                    st.write(f"**{user['full_name']}** - {user['email']} - {user['phone']}")
                    col1, col2, col3 = st.columns(3)
                    if col1.button("✅ Approve", key=f"app_{user['id']}"):
                        supabase.table('users').update({'kyc_status': 'Approved'}).eq('id', user['id']).execute()
                        st.success("Approved")
                        st.rerun()
                    if col2.button("❌ Reject", key=f"rej_{user['id']}"):
                        supabase.table('users').update({'kyc_status': 'Rejected'}).eq('id', user['id']).execute()
                        st.error("Rejected")
                        st.rerun()
                    st.markdown("---")

            with tab2:
                users = supabase.table('users').select("*").execute()
                st.dataframe(users.data, use_container_width=True)

            with tab3:
                trans = supabase.table('transactions').select("*").order('date', desc=True).limit(100).execute()
                st.dataframe(trans.data, use_container_width=True)

            with tab4:
                users = supabase.table('users').select("*").execute()
                trans = supabase.table('transactions').select("amount").execute()
                total_revenue = sum([float(t['amount']) for t in trans.data])

                col1, col2, col3, col4 = st.columns(4)
                col1.metric("Total Users", len(users.data))
                col2.metric("Resellers", len([u for u in users.data if u['account_type'] == 'reseller']))
                col3.metric("Verified", len([u for u in users.data if u['kyc_status'] == 'Approved']))
                col4.metric("Total Revenue", f"₦{total_revenue:,.2f}")

    # ===== SAURAN PAGES =====
    elif st.session_state.page in ["Cable TV", "Electricity"]:
        st.title(st.session_state.page)
        st.info("Feature coming soon... Integrate with SMEPlug API")
    else:
        st.title(st.session_state.page)
        st.info("Coming soon...")
