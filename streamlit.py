import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
import streamlit as st

# Set the page title and description
st.title("Determine Your Cluster")
st.write("""
This app predicts which cluster a person falls into
""")

# # Optional password protection (remove if not needed)
# password_guess = st.text_input("Please enter your password?")
# # this password is stores in streamlit secrets
# if password_guess != st.secrets["password"]:
#     st.stop()

# Load the pre-trained model
km_pickle = open("models/Kmodel.pkl", "rb")
km_model = pickle.load(km_pickle)
km_pickle.close()


# Prepare the form to collect user inputs
with st.form("user_inputs"):
    st.subheader("User Details")
    
    # Gender input
    Age = st.number_input("How old are you?", 
                                       min_value=0,
                                       max_value=100 
                                       )
    # Annual Income
    ApplicantIncome = st.number_input("How much do you earn per year?", 
                                       min_value=0, 
                                       max_value=150)
    
    # Spending score
    Spending = st.number_input("Rate your spending score (0-100)", 
                                       min_value=0, 
                                       max_value=100)
    
    # Gender input
    Gender = st.selectbox("Gender", options=["Male", "Female"])
    
    
    
    # Submit button
    submitted = st.form_submit_button("Predict You cluster")


# Handle the dummy variables to pass to the model
if submitted:
    Gender_Male = 0 if Gender == "Female" else 1


    # Convert Loan Amount Term and Credit History to integers
    Age = int(Age)
    ApplicantIncome = int(ApplicantIncome)
    Spending = int(Spending)

    # Prepare the input for prediction. This has to go in the same order as it was trained
    prediction_input = [[Age, ApplicantIncome, Spending, Gender_Male
    ]]

    # Make prediction
    new_prediction = km_model.predict(prediction_input)[0]

    # Display result
    st.subheader("Prediction Result:")
    st.write(f"You belong to cluster{new_prediction}")
  
       

st.write(
    """We used a machine learning (Cluster Analysis) model to predict your cluster, the features used in this prediction are ranked by relative
    importance below."""
)
