# 📈 Revenue Analysis & Interactive Dashboard

An end-to-end data analytics project that analyzes historical stock prices and company revenue using Python. The project combines API-based data collection, web scraping, data preprocessing, exploratory data analysis (EDA), and an interactive Streamlit dashboard to visualize financial performance.

---

##  Features

- Historical stock data collection using **Yahoo Finance (yFinance)**
- Revenue data extraction using **Web Scraping**
- Data cleaning and preprocessing with **Pandas**
- Exploratory Data Analysis (EDA)
- Interactive visualizations using **Plotly**
- Streamlit dashboard for company-wise financial analysis

---

## 📊 Companies Analyzed

- Tesla (TSLA)
- Amazon (AMZN)
- AMD
- GameStop (GME)

---

##  Technologies Used

- Python
- Pandas
- NumPy
- Plotly
- Streamlit
- yFinance
- BeautifulSoup
- Requests
- Matplotlib

---

##  Project Structure

```text
Revenue-Analysis-and-Interactive-Dashboard/
│
├── Revenue_Analysis_and_Interactive_Dashboard.ipynb
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── data/
│   ├── tesla_stock.csv
│   ├── amazon_stock.csv
│   ├── amd_stock.csv
│   ├── gamestop_stock.csv
│   ├── tesla_revenue.csv
│   ├── amazon_revenue.csv
│   ├── amd_revenue.csv
│   └── gamestop_revenue.csv
│
└── images/
    ├── dashboard_preview.png
    ├── tesla_dashboard.png
    └── amazon_dashboard.png
```

---

##  Installation

Clone the repository:

```bash
git clone https://github.com/younushk123/Revenue-Analysis-and-Interactive-Dashboard.git
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Launch the Streamlit dashboard:

```bash
streamlit run app.py
```

---

## 📈 Dashboard Preview

Add screenshots of your dashboard in the **images/** folder.

Example:

- Stock Price Trends
- Revenue Growth Charts
- Company Comparison Dashboard

---

##  Future Improvements

- Compare multiple companies simultaneously
- Add financial ratios and KPIs
- Deploy the dashboard using Streamlit Community Cloud
- Include additional financial metrics such as market capitalization and earnings

---

##  Author

**Younus Hassan Khan**

GitHub: https://github.com/Younushk123

---
