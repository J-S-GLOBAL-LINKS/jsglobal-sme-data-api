import streamlit as st

# ... wasu codes ...

if st.session_state.page == "Dashboard":
    st.title("Dashboard")
    # ... code din dashboard ...
    
elif st.session_state.page == "Data":
    st.title("Data Page")
    # ... code din data ...
