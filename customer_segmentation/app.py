# ==========================================================
# Import Libraries
# ==========================================================

import streamlit as st
import pandas as pd
import joblib
import plotly.express as px


# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Customer Segmentation",
    page_icon="🛒",
    layout="wide"
)
st.markdown("""
<style>

div.stButton > button:first-child {
    background: linear-gradient(90deg, #2563EB, #06B6D4);
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 12px;
    padding: 12px 24px;
    border: none;
}

div.stButton > button:first-child:hover {
    background: linear-gradient(90deg, #1D4ED8, #0891B2);
    transform: scale(1.03);
    transition: all 0.2s ease;
}

</style>
""", unsafe_allow_html=True)


# ==========================================================
# Load Trained Model & Scaler
# ==========================================================

kmeans = joblib.load("models/kmeans_model.pkl")
scaler = joblib.load("models/scaler.pkl")


# ==========================================================
# Sidebar
# ==========================================================

with st.sidebar:

    st.title("📌 Project Overview")

    st.markdown("""
This application segments customers using **RFM Analysis** and **K-Means Clustering**.

### 🤖 Algorithm
- K-Means Clustering

### 📊 Features
- 📅 Recency
- 🔄 Frequency
- 💰 Monetary

### 🎯 Number of Clusters
- **5**

---
This project helps businesses understand customer behavior and design targeted marketing strategies.
""")


# ==========================================================
# Main Title
# ==========================================================

st.title("🛒 Customer Segmentation using K-Means")


st.markdown("""
Identify customer segments using **RFM Analysis** and **K-Means Clustering**.

Enter the customer's purchasing information to predict the customer segment and receive business recommendations.
""")

st.divider()


# ==========================================================
# Customer Information
# ==========================================================

st.subheader("📝 Customer Information")

col1, col2, col3 = st.columns(3)

# ----------------------------------------------------------
# Recency
# ----------------------------------------------------------

with col1:

    recency = st.number_input(
        "📅 Recency (Days)",
        min_value=1,
        value=30,
        help="Days since the customer's last purchase."
    )

# ----------------------------------------------------------
# Frequency
# ----------------------------------------------------------

with col2:

    frequency = st.number_input(
        "🔄 Frequency",
        min_value=1,
        value=5,
        help="Total number of purchases."
    )

# ----------------------------------------------------------
# Monetary
# ----------------------------------------------------------

with col3:

    monetary = st.number_input(
        "💰 Monetary ($)",
        min_value=0.0,
        value=1000.0,
        step=100.0,
        help="Total amount spent by the customer."
    )

st.divider()

# ==========================================================
# Predict Button
# ==========================================================

left, center, right = st.columns([2,3,2])

with center:

    predict = st.button(
        "Predict Customer Segment",
        use_container_width=True
    )

# ==========================================================
# RFM Guide
# ==========================================================

with st.expander("📖 What do these inputs mean?"):

    st.markdown("""
### 📅 Recency (Days)
Number of days since the customer's **last purchase**.

**Example:** `10` → Customer purchased **10 days ago**.

---

### 🔄 Frequency
Total number of purchases made by the customer.

**Example:** `25` → Customer has placed **25 orders**.

---

### 💰 Monetary ($)
Total amount of money spent by the customer.

**Example:** `15000` → Customer has spent **$15,000**.
""")

st.divider()

# ==========================================================
# Input Validation
# ==========================================================

if monetary <= 0:

    st.warning("⚠️ Monetary value should be greater than 0.")

if frequency <= 0:

    st.warning("⚠️ Frequency should be greater than 0.")

# ==========================================================
# Prediction
# ==========================================================

if predict:

    # ------------------------------------------------------
    # Create Input DataFrame
    # ------------------------------------------------------

    input_data = pd.DataFrame(
        [[recency, frequency, monetary]],
        columns=["Recency", "Frequency", "Monetary"]
    )

    # ------------------------------------------------------
    # Scale Input
    # ------------------------------------------------------

    input_scaled = scaler.transform(input_data)

    # ------------------------------------------------------
    # Predict Cluster
    # ------------------------------------------------------

    cluster = kmeans.predict(input_scaled)[0]

    # ------------------------------------------------------
    # Customer Segment Mapping
    # ------------------------------------------------------

    segment_map = {
        0: "🛍️ Regular Customer",
        1: "⚠️ At-Risk Customer",
        2: "💎 Loyal Customer",
        3: "⭐ High-Value Customer",
        4: "👑 VIP Customer"
    }

    segment = segment_map.get(cluster, "Unknown")

    st.divider()

    # ======================================================
    # Prediction Result
    # ======================================================

    st.subheader("Predicted Customer Segment")

    if cluster == 4:

        st.markdown("""
    <div style="
    background:linear-gradient(135deg,#FFD700,#FFA500);
    padding:20px;
    border-radius:12px;
    text-align:center;
    font-size:28px;
    font-weight:bold;
    color:black;">
    👑 VIP Customer
    </div>
    """, unsafe_allow_html=True)

    elif cluster == 3:

        st.markdown("""
    <div style="
    background:linear-gradient(135deg,#FF9800,#FF5722);
    padding:20px;
    border-radius:12px;
    text-align:center;
    font-size:28px;
    font-weight:bold;
    color:white;">
    ⭐ High-Value Customer
    </div>
    """, unsafe_allow_html=True)

    elif cluster == 2:

        st.success("💎 Loyal Customer")

    elif cluster == 0:

        st.info("🛍️ Regular Customer")

    else:

        st.error("⚠️ At-Risk Customer")

    # ======================================================
    # Customer Profile
    # ======================================================

    st.divider()

    st.subheader("📊 Customer Profile")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="📅 Recency",
            value=f"{recency} Days"
        )

    with col2:
        st.metric(
            label="🔄 Frequency",
            value=f"{frequency}"
        )

    with col3:
        st.metric(
            label="💰 Monetary",
            value=f"${monetary:,.2f}"
        )


    # ======================================================
    # Business Recommendations
    # ======================================================

    recommendations = {

        0: """
### 🛍️ Regular Customer

**Business Insight**
- Moderate purchasing behavior
- Average spending pattern
- Potential for upselling

**Recommended Actions**
- 🎯 Personalized recommendations
- 🎁 Bundle offers
- 🛒 Seasonal promotions
""",

        1: """
### ⚠️ At-Risk Customer

**Business Insight**
- Customer has not purchased recently
- Low purchase frequency
- Risk of churn

**Recommended Actions**
- 💌 Win-back email campaign
- 🎟️ Special discount coupons
- 🔔 Re-engagement offers
""",

        2: """
### 💎 Loyal Customer

**Business Insight**
- Frequently purchases products
- Strong customer loyalty
- Consistent revenue source

**Recommended Actions**
- ⭐ Loyalty rewards
- 🎁 Exclusive member offers
- 🤝 Referral programs
""",

        3: """
### ⭐ High-Value Customer

**Business Insight**
- High purchase frequency
- Significant revenue contribution
- Valuable long-term customer

**Recommended Actions**
- 🚀 Premium customer support
- 🎁 Early product access
- 🎯 Personalized recommendations
""",

        4: """
### 👑 VIP Customer

**Business Insight**
- Highest-value customer
- Exceptional spending behavior
- Top priority customer

**Recommended Actions**
- 👑 VIP Membership
- 💎 Exclusive Rewards
- 🤝 Dedicated Account Manager
"""
    }

    st.divider()

    st.subheader("💡 Business Recommendation")


    if cluster == 4:
        st.success(recommendations[cluster], icon="👑")

    elif cluster == 3:
        st.success(recommendations[cluster], icon="⭐")

    elif cluster == 2:
        st.success(recommendations[cluster], icon="💎")

    elif cluster == 0:
        st.info(recommendations[cluster], icon="🛍️")

    else:
        st.error(recommendations[cluster], icon="⚠️")

    # ======================================================
    # Customer RFM Visualization
    # ======================================================

    st.divider()

    st.subheader("📈 Customer RFM Profile")

    chart_data = pd.DataFrame({
        "Feature": ["📅 Recency", "🔄 Frequency", "💰 Monetary"],
        "Value": [recency, frequency, monetary]
    })

    fig = px.bar(
        chart_data,
        x="Feature",
        y="Value",
        color="Feature",
        text="Value",
        title="Customer RFM Analysis"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        template="plotly_dark",
        showlegend=False,
        height=450,
        title_x=0.5,
        xaxis_title="RFM Features",
        yaxis_title="Value"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # ======================================================
    # Input Summary
    # ======================================================

    st.divider()

    st.subheader("📋 Customer Input Summary")

    summary = pd.DataFrame({

        "Feature": [
            "Recency",
            "Frequency",
            "Monetary"
        ],

        "Value": [
            recency,
            frequency,
            monetary
        ]

    })

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True
    )


# ==========================================================
# About Customer Segments
# ==========================================================

# st.divider()

st.subheader("📚 About Customer Segments")

segment_info = pd.DataFrame({

        "Customer Segment":[
            "👑 VIP Customer",
            "⭐ High-Value Customer",
            "💎 Loyal Customer",
            "🛍️ Regular Customer",
            "⚠️ At-Risk Customer"
        ],

        "Description":[
            "Highest spending customers with exceptional purchase behavior.",
            "Frequent buyers contributing significant revenue.",
            "Customers who purchase regularly and remain highly engaged.",
            "Average customers with moderate purchasing activity.",
            "Inactive customers who require re-engagement strategies."
        ]

})

st.dataframe(
    segment_info,
    use_container_width=True,
    hide_index=True
    )

# ==========================================================
# Footer
# ==========================================================

st.divider()

st.markdown(
"""
<div style='text-align:center;'>

Developed by **Younus Khan**

Machine Learning Portfolio Project

</div>
""",
unsafe_allow_html=True
)

