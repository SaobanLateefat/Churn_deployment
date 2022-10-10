# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 13:36:01 2022

@author: SAOBAN
"""

#import numpy as np
#import pickle 
import joblib
import streamlit as st

## loading the saved model
#loaded_model = pickle.load(open('C:/Users/SAOBAN/Documents/Code_Basics/Deployment/trained_model.sev', 'rb'))

#pickle_in = open('C:/Users/SAOBAN/Documents/Code_Basics/Deployment/classifier.pkl', 'rb')
#loaded_model = pickle.load(pickle_in)
loaded_model = joblib.load(open('classifier.pkl', 'rb'))



@st.cache()

# Creationg a function for prediction

def churn_prediction(gender, SeniorCitizen, Partner, Dependents, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges, Tenure_cohort):
    # Pre-processing user input
    if gender == 'Female':
        gender = 0
    else:
        gender = 1
        
    if SeniorCitizen == 'No':
        SeniorCitizen = 0
    else:
        SeniorCitizen = 1
        
    if Partner == 'No':
        Partner = 0
    else:
        Partner = 1
        
    if Dependents == 'No':
        Dependents = 0
    else:
        Dependents = 1
        
    if PhoneService == 'No':
        PhoneService = 0
    else:
        PhoneService = 1
        
    if MultipleLines == 'No':
        MultipleLines = 0
    elif MultipleLines == 'No phone service':
        MultipleLines = 1
    else:
        MultipleLines = 2
        
    if InternetService == 'DSL':
        InternetService = 0
    elif InternetService == 'Fiber optic':
        InternetService = 1
    else:
        InternetService = 2
        
    if OnlineSecurity == 'No':
        OnlineSecurity = 0
    elif OnlineSecurity == 'No internet service':
        OnlineSecurity = 1
    else:
        OnlineSecurity = 2
        
    if OnlineBackup == 'No':
        OnlineBackup = 0
    elif OnlineBackup == 'No internet service':
        OnlineBackup = 1
    else:
        OnlineBackup = 2
        
    if DeviceProtection == 'No':
        DeviceProtection = 0
    elif DeviceProtection == 'No internet service':
        DeviceProtection = 1
    else:
        DeviceProtection = 2
        
    if TechSupport == 'No':
        TechSupport = 0
    elif TechSupport == 'No internet service':
        TechSupport = 1
    else:
        TechSupport = 2
        
    if StreamingTV == 'No':
        StreamingTV = 0
    elif StreamingTV == 'No internet service':
        StreamingTV = 1
    else:
        StreamingTV = 2
    
    if StreamingMovies =='No':
        StreamingMovies = 0
    elif StreamingMovies == 'No internet service':
        StreamingMovies = 1
    else:
        StreamingMovies = 2
        
    if Contract == 'Month-to-month':
        Contract = 0
    elif Contract == 'One year':
        Contract = 1
    else:
        Contract = 2
        
    if PaperlessBilling == 'No':
        PaperlessBilling = 0
    else:
        PaperlessBilling = 1
        
    if PaymentMethod == 'Bank transfer (automatic)':
        PaymentMethod = 0
    elif PaymentMethod == 'Credit card (automatic)':
        PaymentMethod = 1
    elif PaymentMethod == 'Electronic check':
        PaymentMethod = 2
    else:
        PaymentMethod = 3
    
    if Tenure_cohort == '0-12 Months':
        Tenure_cohort = 0
    elif Tenure_cohort == '12-24 Months':
        Tenure_cohort = 1
    elif Tenure_cohort == '24-48 Months':
        Tenure_cohort = 2
    else:
        Tenure_cohort = 3
    

    # Changing the input data to numpy
    #input_data_as_np_array = np.asarray(gender, SeniorCitizen, Partner, Dependents, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges, Tenure_cohort)

    # Reshape the array as we are predicting to one instance
    #input_data_reshaped = input_data_as_np_array.reshape(1,-1)

    prediction = loaded_model.predict([[gender, SeniorCitizen, Partner, Dependents, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges, Tenure_cohort]])
    print(prediction)
    if (prediction[0] == 'Yes'):
        return 'This person Churned'
    else:
        return 'This person did not churn'
    


    
# definng the function which will make the prediction using the data which the user inputs
#def prediction(gender, SeniorCitizen, Partner, Dependents, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges, Tenure_cohort):
    
    
        
    
        
        
        
    

def main():
    
    # giving a title
    st.title('Churn Prediction Web App')
    
    # getting the input data from the user using selct boxes and the likes

    gender = st.radio("What gender is this person", key="visibility", options=["Male", "Female"])
    SeniorCitizen = st.selectbox('Is the person a senior citizen', ('No', 'Yes'))
    Partner = st.selectbox('Did this person have a partner', ('No', 'Yes'))
    Dependents = st.selectbox('Is the person dependent', ('No', 'Yes'))
    PhoneService = st.selectbox('Does the person uses phone service', ('Yes', 'No'))
    MultipleLines = st.selectbox('Does this person uses multiple lines', ('No', 'Yes', 'No phone service'))
    InternetService = st.selectbox('What type of internet service does thie person use', ('fibre optic', 'DSL', 'None'))
    OnlineSecurity = st.selectbox('Does thie person have an online security', ('No', 'Yes', 'No internet service'))
    OnlineBackup = st.selectbox('Does this person have an online backup', ('No', 'Yes', 'No internet service'))
    DeviceProtection = st.selectbox('Does this person uses device protection', ('No', 'Yes', 'No interbet service'))
    TechSupport = st.selectbox('Is tech support available to this person', ('No', 'Yes', 'No internet service'))
    StreamingTV = st.selectbox('Does this person uses streming TV', ('No', 'Yes', 'No internet service'))
    StreamingMovies = st.selectbox('Does this person stream movies', ('No', 'Yes', 'No internet service'))
    Contract = st.selectbox('What type of contract did this person sign up for', ('Month-to-month', 'Two years', 'One year'))
    PaperlessBilling = st.selectbox('Does this person uses paperless billing', ('Yes', 'No'))
    PaymentMethod = st.selectbox('What payment method did this person use', ('Electronic ckeck', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'))
    MonthlyCharges = st.number_input('How much is this person charged monthly')
    TotalCharges = st.number_input('How much is this person charged in Total')
    Tenure_cohort = st.selectbox('What month range has this person partner with the company', ('0-12 Months', '12-24 Months', '24-48 Months', 'Over 48 Months'))
    
    
    # Code for Prediction
    prediction = ''
    
    # Creating a button for Prediction
    
    if st.button('Predict Churn'):
        prediction = churn_prediction(gender, SeniorCitizen, Partner, Dependents, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges, Tenure_cohort)
    
    st.success(prediction)
    
    
    
if __name__ == '__main__':
    main()
    
    

    
    
    
                                                
    
    
    
    
    
    
     
    
