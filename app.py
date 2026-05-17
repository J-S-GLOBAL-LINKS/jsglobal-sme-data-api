import streamlit as st
import requests
from datetime import datetime

# === CONFIG ===
BASE_URL = st.secrets.get("BASE_URL", "")
API_KEY = st.secrets.get("API_KEY", "")
ADMIN_PASSWORD = st.secrets.get("ADMIN_PASSWORD", "change_me")

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

# === SESSION STATE INIT ===
defaults = {
    "show_balance": True,
    "kyc_status": "pending",
    "user_data": {},
    "copied_code": "",
    "page": "dashboard",
    "cable_plans": None,
    "cable_customer": None,
    "cable_provider_id": None,
    "cable_smartcard": None,
}
for k, v in defaults.items():
    st.session_state.setdefault(k, v)

# === API FUNCTIONS ===
@st.cache_data(ttl=60)
def get_balance():
    try:
        resp = requests.get(f"{BASE_URL}/account/balance", headers=headers, timeout=10)
        if resp.status_code == 200:
            return resp.json().get("balance", "0")
    except requests.RequestException:
        pass
    return "0"

@st.cache_data(ttl=600)
def get_networks():
    try:
        resp = requests.get(f"{BASE_URL}/networks", headers=headers, timeout=10)
        return resp.json().get("data", []) if resp.status_code == 200 else []
    except requests.RequestException:
        return []

@st.cache_data(ttl=600)
def get_data_plans(network_id):
    try:
        resp = requests.get(f"{BASE_URL}/data/plans/{network_id}", headers=headers, timeout=10)
        return resp.json().get("data", []) if resp.status_code == 200 else []
    except requests.RequestException:
        return []

@st.cache_data(ttl=600)
def get_cable_providers():
    try:
        resp = requests.get(f"{BASE_URL}/cable/providers", headers=headers, timeout=10)
        return resp.json().get("data", []) if resp.status_code == 200 else []
    except requests.RequestException:
        return []

@st.cache_data(ttl=600)
def get_cable_plans(provider_id):
    try:
        resp = requests.get(f"{BASE_URL}/cable/plans/{provider_id}", headers=headers, timeout=10)
        return resp.json().get("data", []) if resp.status_code == 200 else []
    except requests.RequestException:
        return []

@st.cache_data(ttl=600)
def get_electricity_discos():
    try:
        resp = requests.get(f"{BASE_URL}/electricity/discos", headers=headers, timeout=10)
        return resp.json().get("data", []) if resp.status_code == 200 else []
    except requests.RequestException:
        return []

def verify_cable_smartcard(provider_id, smartcard):
    try:
        payload = {"provider": provider_id, "smartcard_number": smartcard}
        resp = requests.post(f"{BASE_URL}/cable/verify", headers=headers, json=payload, timeout=15)
        if resp.status_code == 200:
            return resp.json().get("data", {}).get("name")
    except requests.RequestException:
        pass
    return None

def copy_code(code):
    st.session_state.copied_code = code
    st.toast(f"Copied {code}", icon="✅")

def check_kyc_or_block():
    if st.session_state.kyc_status != "approved":
        st.error("Dole ka kammala KYC tukuna")
        if st.button("Go to KYC"):
            st.session_state.page = "kyc"
            st.rerun()
        st.stop()

def nav_button(label, page):
    if st.button(label, use_container_width=True):
        st.session_state.page = page
        st.rerun()

# === SIDEBAR ===
with st.sidebar:
    st.image("logo.png", width=80)
    st.markdown("### J.S.GLOBAL LINKS")
    st.caption("RC: 8984371")

    status_map = {
        "approved": ("success", "KYC Verified"),
        "submitted": ("warning", "KYC Pending"),
    }
    status_type, status_msg = status_map.get(st.session_state.kyc_status, ("error", "KYC Required"))
    getattr(st, status_type)(status_msg)

    st.markdown("---")
    pages = [
        ("🏠 Dashboard", "dashboard"),
        ("👤 My Profile", "profile"),
        ("✅ KYC Verification", "kyc"),
        ("📱 USSD Codes", "ussd"),
        ("📊 Transactions", "history"),
        ("🔐 Admin Panel", "admin"),
    ]
    for label, page in pages:
        nav_button(label, page)

    st.markdown("---")
