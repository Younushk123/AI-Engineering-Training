# End-to-End ML Pipeline for Network Intrusion Detection

## Overview

This project demonstrates an end-to-end machine learning pipeline for detecting network intrusion by classifying network traffic as **BENIGN** or **DrDoS_DNS**. The workflow covers data preprocessing, exploratory data analysis, feature scaling, model training, evaluation, and deployment through an interactive Streamlit web application.

## Dataset

* **Dataset:** DrDoS_DNS Network Traffic Dataset
* **Task:** Binary Classification
* **Target Classes:**

  * BENIGN (Normal Traffic)
  * DrDoS_DNS (DNS-based DDoS Attack)

## Project Workflow

* Data Loading
* Data Cleaning & Preprocessing
* Exploratory Data Analysis (EDA)
* Feature Scaling
* Model Training
* Model Evaluation
* Cross Validation
* Model Serialization with Joblib
* Streamlit Deployment

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Joblib
* Matplotlib
* Seaborn

## Model Performance

* Accuracy: **99.97%**
* Precision: **99.97%**
* Recall: **99.97%**
* F1 Score: **99.97%**

## Project Structure

```text
├── data/
├── models/
│   ├── ddos_model.pkl
│   ├── scaler.pkl
│   └── label_encoder.pkl
├── notebook/
│   └── end-to-end-ml-pipeline-for-network-intrusion-detec.ipynb
├── app.py
├── requirements.txt
└── README.md
```

## Run the Project

1. Clone the repository

```bash
git clone <repository-url>
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Launch the Streamlit application

```bash
streamlit run app.py
```

## Results

The trained Logistic Regression model successfully classifies network traffic as either normal (BENIGN) or DNS-based DDoS attack (DrDoS_DNS). The application provides an easy-to-use interface for testing network traffic features and generating real-time predictions.

## Limitations

The selected dataset is highly separable for the chosen binary classes. Several backward-flow features remain constant for most DrDoS_DNS samples, resulting in very high classification performance. The project is intended to demonstrate an end-to-end machine learning workflow rather than serve as a production-ready intrusion detection system.

## Future Improvements

* Evaluate on multi-class intrusion detection datasets (e.g., NSL-KDD, CICIDS2017, UNSW-NB15).
* Compare multiple machine learning algorithms.
* Explore deep learning approaches for intrusion detection.
* Deploy the application to a cloud platform.

## Author

**Younus Hassan Khan**.
