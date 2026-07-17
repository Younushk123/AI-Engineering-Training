import streamlit as st
import pandas as pd
import joblib

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="DDoS Attack Detection",
    page_icon="🛡️",
    layout="wide"
)

# ==========================================================
# Load Model
# ==========================================================

model = joblib.load("models/ddos_model.pkl")
scaler = joblib.load("models/scaler.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")

# ==========================================================
# Title
# ==========================================================

st.title("🛡️ DDoS Attack Detection")

st.write("""
Detect whether network traffic is **BENIGN** or **DrDoS_DNS**
using a trained **Logistic Regression** model.
""")

# ==========================================================
# Sidebar
# ==========================================================

st.sidebar.title("⚙️ Configuration")

scenario = st.sidebar.selectbox(
    "Select Traffic Scenario",
    [
        "Normal Browsing",
        "DNS Activity",
        "Possible DDoS Attack",
        "Custom Input"
    ]
)

# ==========================================================
# Scenario Values
# ==========================================================

if scenario == "Normal Browsing":

    protocol = 6
    flow_duration = 250000
    total_forward_packets = 30
    total_backward_packets = 25
    total_forward_packets_length = 3500
    total_backward_packets_length = 2800
    forward_packet_length_mean = 116
    backward_packet_length_mean = 112
    forward_packets_per_second = 120
    backward_packets_per_second = 100
    forward_iat_mean = 2000
    backward_iat_mean = 1800
    flow_iat_mean = 1900
    flow_packets_per_seconds = 220
    flow_bytes_per_seconds = 25000

elif scenario == "DNS Activity":

    protocol = 17
    flow_duration = 90000
    total_forward_packets = 8
    total_backward_packets = 8
    total_forward_packets_length = 650
    total_backward_packets_length = 700
    forward_packet_length_mean = 81
    backward_packet_length_mean = 87
    forward_packets_per_second = 95
    backward_packets_per_second = 95
    forward_iat_mean = 900
    backward_iat_mean = 850
    flow_iat_mean = 875
    flow_packets_per_seconds = 190
    flow_bytes_per_seconds = 16000

elif scenario == "Possible DDoS Attack":

    protocol = 17
    flow_duration = 15000
    total_forward_packets = 900
    total_backward_packets = 3
    total_forward_packets_length = 65000
    total_backward_packets_length = 150
    forward_packet_length_mean = 72
    backward_packet_length_mean = 50
    forward_packets_per_second = 65000
    backward_packets_per_second = 200
    forward_iat_mean = 10
    backward_iat_mean = 900
    flow_iat_mean = 15
    flow_packets_per_seconds = 65000
    flow_bytes_per_seconds = 4500000

else:

    st.sidebar.markdown("---")
    st.sidebar.subheader("Custom Network Features")

    protocol = st.sidebar.number_input(
        "Protocol",
        min_value=0,
        value=17,
        help="TCP = 6, UDP = 17, ICMP = 1"
    )

    flow_duration = st.sidebar.number_input(
        "Flow Duration",
        min_value=0.0,
        value=0.0
    )

    total_forward_packets = st.sidebar.number_input(
        "Total Forward Packets",
        min_value=0,
        value=0
    )

    total_backward_packets = st.sidebar.number_input(
        "Total Backward Packets",
        min_value=0,
        value=0
    )

    total_forward_packets_length = st.sidebar.number_input(
        "Total Forward Packets Length",
        min_value=0.0,
        value=0.0
    )

    total_backward_packets_length = st.sidebar.number_input(
        "Total Backward Packets Length",
        min_value=0.0,
        value=0.0
    )

    forward_packet_length_mean = st.sidebar.number_input(
        "Forward Packet Length Mean",
        min_value=0.0,
        value=0.0
    )

    backward_packet_length_mean = st.sidebar.number_input(
        "Backward Packet Length Mean",
        min_value=0.0,
        value=0.0
    )

    forward_packets_per_second = st.sidebar.number_input(
        "Forward Packets Per Second",
        min_value=0.0,
        value=0.0
    )

    backward_packets_per_second = st.sidebar.number_input(
        "Backward Packets Per Second",
        min_value=0.0,
        value=0.0
    )

    forward_iat_mean = st.sidebar.number_input(
        "Forward IAT Mean",
        min_value=0.0,
        value=0.0
    )

    backward_iat_mean = st.sidebar.number_input(
        "Backward IAT Mean",
        min_value=0.0,
        value=0.0
    )

    flow_iat_mean = st.sidebar.number_input(
        "Flow IAT Mean",
        min_value=0.0,
        value=0.0
    )

    flow_packets_per_seconds = st.sidebar.number_input(
        "Flow Packets Per Second",
        min_value=0.0,
        value=0.0
    )

    flow_bytes_per_seconds = st.sidebar.number_input(
        "Flow Bytes Per Second",
        min_value=0.0,
        value=0.0
    )

# ==========================================================
# Current Configuration
# ==========================================================

st.markdown("---")

col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("Current Configuration")
    st.write(f"**Scenario:** {scenario}")

with col2:
    predict = st.button(
        "Predict",
        use_container_width=True,
        type="primary"
    )

st.markdown("### Network Traffic Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Protocol", protocol)
    st.metric("Flow Duration", f"{flow_duration:,.0f}")

with col2:
    st.metric("Forward Packets", total_forward_packets)
    st.metric("Backward Packets", total_backward_packets)

with col3:
    st.metric("Flow Packets/sec", f"{flow_packets_per_seconds:,.2f}")
    st.metric("Flow Bytes/sec", f"{flow_bytes_per_seconds:,.2f}")

# ==========================================================
# Prediction
# ==========================================================

st.markdown("---")
st.subheader("Prediction")

if predict:

    input_data = pd.DataFrame({
        "protocol": [protocol],
        "flow_duration": [flow_duration],
        "total_forward_packets": [total_forward_packets],
        "total_backward_packets": [total_backward_packets],
        "total_forward_packets_length": [total_forward_packets_length],
        "total_backward_packets_length": [total_backward_packets_length],
        "forward_packet_length_mean": [forward_packet_length_mean],
        "backward_packet_length_mean": [backward_packet_length_mean],
        "forward_packets_per_second": [forward_packets_per_second],
        "backward_packets_per_second": [backward_packets_per_second],
        "forward_iat_mean": [forward_iat_mean],
        "backward_iat_mean": [backward_iat_mean],
        "flow_iat_mean": [flow_iat_mean],
        "flow_packets_per_seconds": [flow_packets_per_seconds],
        "flow_bytes_per_seconds": [flow_bytes_per_seconds]
    })

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(input_scaled)

    # Decode label
    result = label_encoder.inverse_transform(prediction)[0]

    st.markdown("---")
    st.subheader("Prediction Result")

    if result == "BENIGN":

        st.success("✅ BENIGN Traffic Detected")

        st.info("""
### Risk Level: LOW 🟢

This traffic appears to be normal network activity.

**Recommended Action**
- No immediate action required.
- Continue monitoring network traffic.
""")

    else:

        st.error("⚠️ DrDoS_DNS Attack Detected")

        st.warning("""
### Risk Level: HIGH 🔴

The traffic pattern matches a potential DNS-based DDoS attack.

**Recommended Action**
- Inspect suspicious source IP addresses.
- Monitor DNS requests.
- Review firewall and IDS/IPS logs.
- Block malicious traffic if confirmed.
""")

# ==========================================================
# Feature Reference
# ==========================================================

st.markdown("---")

with st.expander("📘 Feature Reference"):

    st.markdown("""

| Feature | Description |
|----------|-------------|
| Protocol | TCP = 6, UDP = 17, ICMP = 1 |
| Flow Duration | Total duration of the network flow |
| Total Forward Packets | Packets sent from source |
| Total Backward Packets | Packets returned from destination |
| Packet Length | Total transmitted bytes |
| Packets Per Second | Network traffic rate |
| IAT Mean | Average time between packets |
| Flow Bytes Per Second | Data transmitted per second |

""")

# ==========================================================
# About Project
# ==========================================================

st.markdown("---")

st.subheader("ℹ️ About")

st.write("""
This application predicts whether network traffic is **BENIGN** or **DrDoS_DNS**
using a Machine Learning model trained with **Logistic Regression**.

The model was trained on processed network traffic features and can assist
in identifying potential DNS-based DDoS attacks.
""")

# ==========================================================
# Footer
# ==========================================================

st.markdown("---")

st.caption("""
**End-to-End ML Pipeline for Network Intrusion Detection**

Built with **Python, Streamlit, Scikit-learn, and Logistic Regression**

Developed by **Younus Khan**
""")