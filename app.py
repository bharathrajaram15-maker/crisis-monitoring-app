import streamlit as st
import requests

st.set_page_config(layout="wide")

st.title("🚨 Crisis Monitoring Dashboard")

data = requests.get("http://127.0.0.1:8000/predict").json()

col1, col2 = st.columns(2)

with col1:
    st.metric("Temperature", data["weather"]["temperature"])
    st.metric("Humidity", data["weather"]["humidity"])

with col2:
    risk = data["risk"]

    if risk == 0:
        st.success("Low Risk")
    elif risk == 1:
        st.warning("Medium Risk")
    else:
        st.error("🚨 HIGH RISK")

st.markdown("### 📍 Location Map")

st.components.v1.html("""
<iframe
width="100%"
height="400"
src="https://maps.google.com/maps?q=chennai&t=&z=13&ie=UTF8&iwloc=&output=embed">
</iframe>
""", height=400)