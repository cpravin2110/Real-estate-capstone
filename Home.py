import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Gurgaon Real Estate Analytics App",
    page_icon="🏠",
    layout="wide"
)

# Main Title
st.title("🏠 Real Estate Price Prediction & Recommendation")

st.subheader("Welcome to our Gurgaon Real Estate Analytics Platform")

st.write(
    """
    This application analyzes real-estate properties across **100+ sectors of
    Gurgaon (Gurugram)** and helps users:

    • Predict property prices  
    • Explore real-estate market insights  
    • Analyze property data  
    • Find similar apartments
    """
)

st.divider()

# Features
st.header("🚀 Features")

st.subheader("💰 Price Prediction")
st.write(
    "Predict the estimated price of a property using our ML model."
)

st.subheader("📊 Analytics")
st.write(
    "Explore property prices, sectors, BHKs and other real-estate "
    "market insights across Gurgaon."
)

st.subheader("🏢 Apartment Recommendation")
st.write(
    "Find similar properties based on location and property characteristics."
)

st.divider()

# Dataset
st.header("📍 Dataset")

st.write(
    """
    The dataset contains Gurgaon real-estate properties covering **100+ sectors**,
    with information such as property type, BHK, bathrooms, built-up area,
    furnishing, location and other property characteristics.
    """
)

st.divider()

# Technologies
st.header("🛠️ Technologies")

st.write(
    "Python | Pandas | Scikit-learn | Plotly | Streamlit | Machine Learning"
)

st.divider()

# Developer
st.header("👨‍💻 Developed by")

st.write("**Pravin Chavan**")
st.write("Data Science | Machine Learning | GenAI Enthusiast")

# Sidebar
st.sidebar.success("Select a page from the sidebar.")
