import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Revenue Dashboard")

st.title("📈 Revenue Analysis Dashboard")

company = st.selectbox(
    "Select Company",
    ["Tesla","Amazon","AMD","GameStop"]
)

stock = pd.read_csv(f"data/{company.lower()}_stock.csv")
revenue = pd.read_csv(f"data/{company.lower()}_revenue.csv")

fig = px.line(
    stock,
    x="Date",
    y="Close",
    title=f"{company} Stock Price"
)

st.plotly_chart(fig)

fig2 = px.bar(
    revenue,
    x="Year",
    y="Revenue",
    title=f"{company} Revenue"
)

st.plotly_chart(fig2)
# st.write(revenue.head())
# st.write(revenue.columns)