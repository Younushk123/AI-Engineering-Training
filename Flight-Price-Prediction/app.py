import streamlit as st
import joblib
import pandas as pd

st.set_page_config(
    page_title="Flight Price Prediction",
    page_icon="✈️",
    layout="centered"
)

st.title("✈️ Flight Price Prediction")
st.write("Predict flight ticket prices using Machine Learning.")

st.sidebar.header("Enter Flight Details")

# Airline
airline = st.sidebar.selectbox(
    "Airline",
    ["AirAsia", "Air_India", "GO_FIRST", "Indigo",
     "SpiceJet", "Vistara"]
)

# Source City
source_city = st.sidebar.selectbox(
    "Source City",
    ["Bangalore", "Chennai", "Delhi",
     "Hyderabad", "Kolkata", "Mumbai"]
)

# Destination City
destination_city = st.sidebar.selectbox(
    "Destination City",
    ["Bangalore", "Chennai", "Delhi",
     "Hyderabad", "Kolkata", "Mumbai"]
)

# Departure Time
departure_time = st.sidebar.selectbox(
    "Departure Time",
    ["Early_Morning", "Morning", "Afternoon",
     "Evening", "Night", "Late_Night"]
)

# Arrival Time
arrival_time = st.sidebar.selectbox(
    "Arrival Time",
    ["Early_Morning", "Morning", "Afternoon",
     "Evening", "Night", "Late_Night"]
)

# Stops
stops = st.sidebar.selectbox(
    "Stops",
    ["zero", "one", "two_or_more"]
)

# Class
flight_class = st.sidebar.selectbox(
    "Class",
    ["Economy", "Business"]
)

# Duration
duration = st.sidebar.number_input(
    "Duration (Hours)",
    min_value=0.5,
    value=1.0,
    step=0.5
)

# Days Left
days_left = st.sidebar.number_input(
    "Days Left",
    min_value=1,
    step=1
)

@st.cache_resource
def load_model():
    model = joblib.load("model/flight_price_model.joblib")
    feature_names = joblib.load("model/feature_names.joblib")
    return model, feature_names
model, feature_names = load_model()

predict_button = st.button("Predict Price")
if predict_button:
    input_data = {
    "airline": airline,
    "source_city": source_city,
    "destination_city": destination_city,
    "departure_time": departure_time,
    "arrival_time": arrival_time,
    "stops": stops,
    "class": flight_class,
    "duration": duration,
    "days_left": days_left
    }

    # st.write(input_data)

    # Convert input dictionary to DataFrame
    input_df = pd.DataFrame([input_data])

    # Apply one-hot encoding
    input_df = pd.get_dummies(input_df)

    # Match training feature columns
    input_df = input_df.reindex(columns=feature_names, fill_value=0)

    # Display final input (for testing)
    # st.write(input_df)

    prediction = model.predict(input_df)

    st.success(f"✈️ Estimated Flight Price: ₹ {prediction[0]:,.2f}")