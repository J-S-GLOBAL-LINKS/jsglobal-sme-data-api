elif st.session_state.page == "Flyer":
    st.title("📱 J.S.GLOBAL Premium Flyer")
    
    st.markdown("""
    <style>
    .flyer-container {
        width: 100%;
        max-width: 600px;
        margin: 0 auto;
        background: linear-gradient(135deg, #0A2463 0%, #1a3a7a 100%);
        padding: 40px 30px;
        border-radius: 25px;
        font-family: 'Poppins', sans-serif;
        color: white;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        position: relative;
        overflow: hidden;
    }
    .flyer-container::before {
        content: '';
        position: absolute;
        top: -50px;
        right: -50px;
        width: 200px;
        height: 200px;
        background: #FFD700;
        opacity: 0.1;
        border-radius: 50%;
    }
    .badge-new {
        background: linear-gradient(135deg, #FFD700, #FFA500);
        color: #0A2463;
        padding: 12px 24px;
        border-radius: 50px;
        font-weight: 900;
        font-size: 14px;
        display: inline-block;
        margin-bottom: 20px;
        box-shadow: 0 5px 15px rgba(255,215,0,0.4);
    }
    .headline-new {
        font-size: 42px;
        font-weight: 900;
        line-height: 1.1;
        margin-bottom: 15px;
        background: linear-gradient(135deg, #FFD700, #FFFFFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .subhead-new {
        font-size: 20px;
        color: #00A676;
        font-weight: 700;
        margin-bottom: 30px;
    }
    .feature-box {
        background: rgba(255,255,255,0.15);
        backdrop-filter: blur(10px);
        padding: 20px;
        border-radius: 15px;
        margin: 15px 0;
        border: 2px solid rgba(255,215,0,0.3);
    }
    .feature-title {
        color: #FFD700;
        font-size: 18px;
        font-weight: 800;
        margin-bottom: 12px;
    }
    .feature-item {
        font-size: 15px;
        margin: 8px 0;
        font-weight: 600;
    }
    .cta-new {
        background: linear-gradient(135deg, #FFD700, #FFA500);
        color: #0A2463;
        padding: 25px;
        border-radius: 18px;
        text-align: center;
        font-weight: 900;
        margin-top: 25px;
        box-shadow: 0 10px 30px rgba(255,215,0,0.5);
    }
    </style>
    
    <div class="flyer-container">
        <div style="text-align: center; font-size: 20px; font-weight: 900; color: #FFD700; margin-bottom: 25px; letter-spacing: 1px;">J.S.GLOBAL LINKS AND SERVICES</div>
        
        <div style="text-align: center;">
            <div class="badge-new">🚀 100% FREE APP</div>
        </div>
        
        <div class="headline-new">DATA CHEAP +<br>FREE ANDROID APP</div>
        <div class="subhead-new">Sayi Data Mai Rahusa, Ka Samu App Kyauta!</div>
        
        <div class="feature-box">
            <div class="feature-title">📊 DATA SELLING</div>
            <div class="feature-item">✅ MTN, Airtel, Glo, 9mobile</div>
            <div class="feature-item">✅ Cheap Data & Airtime</div>
            <div class="feature-item">✅ 24/7 Instant Delivery</div>
            <div class="feature-item">✅ Reseller Packages Available</div>
        </div>
        
        <div class="feature-box">
            <div class="feature-title">📱 FINTECH APP FEATURES</div>
            <div class="feature-item">✅ Fingerprint Login Security</div>
            <div class="feature-item">✅ Push Notifications</div>
            <div class="feature-item">✅ FREE CAC Registration</div>
            <div class="feature-item">✅ Google Playstore Publishing</div>
        </div>
        
        <div class="cta-new">
            <div style="font-size: 22px; margin-bottom: 8px;">📲 TUNTUBE MU YAU!</div>
            <div style="font-size: 20px; margin-bottom: 8px;">WhatsApp: +2347062589825</div>
            <div style="font-size: 16px;">Data + App = Nasar Kasuwancinka</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("💬 WhatsApp Yanzu", "https://wa.me/2347062589825")
    with col2:
        st.info("📸 Screenshot ka tura customers")
