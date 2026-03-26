import streamlit as st
from api import get_weather
from lstm_model import build_model, predict
from alerts import send_alert

# Page config
st.set_page_config(page_title="Crisis Monitoring System", layout="wide")

# Title
st.title("🚨 AI-Based Crisis Monitoring & Intelligent Alert System")

# Load model
@st.cache_resource
def load_model():
    return build_model()

model = load_model()

# Get real-time weather data
weather = get_weather()

# Prepare sequence for LSTM
sequence = [[
    weather["temperature"],
    weather["humidity"],
    weather["pressure"]
]] * 10

# Predict risk
risk = predict(model, sequence)

# Layout
col1, col2 = st.columns(2)

# 📊 Weather Data
with col1:
    st.subheader("🌦️ Real-Time Weather Data")

    st.metric("🌡 Temperature (°C)", weather["temperature"])
    st.metric("💧 Humidity (%)", weather["humidity"])
    st.metric("ضغط Pressure (hPa)", weather["pressure"])

# ⚠️ Risk Display
with col2:
    st.subheader("⚠️ Risk Level")

    if risk == 0:
        st.success("✅ LOW RISK")
    elif risk == 1:
        st.warning("⚠️ MEDIUM RISK")
    else:
        st.error("🚨 HIGH RISK ALERT")

        # Send SMS alert
        send_alert()

        st.markdown("""
        ### 🚨 Emergency Instructions:
        - Move to safe location
        - Avoid affected area
        - Contact emergency services
        """)

# 📍 Map Section
st.markdown("---")
st.subheader("📍 Live Location Map")

st.components.v1.html("""
<iframe
width="100%"
height="400"
src="https://maps.google.com/maps?q=chennai&t=&z=13&ie=UTF8&iwloc=&output=embed">
</iframe>
""", height=400)

# Footer
st.markdown("---")
st.caption("Developed as an AI-powered Disaster Monitoring System 🌍")
