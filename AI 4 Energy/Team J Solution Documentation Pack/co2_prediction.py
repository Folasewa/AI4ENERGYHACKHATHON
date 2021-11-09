import streamlit as st
import pandas as pd
import numpy as np
import pickle
#from pycaret.regression import load_model, predict_model
raw_data = pd.read_excel('co2_emission_data_test.xlsx')

#defining prediction function
def predict_carbon(data):
    emissions = model_linear.predict(features_df)
    return emissions
model_linear = pickle.load(open('model_linear.sav', 'rb'))


st.title('CO2 Emission Prediction Web App')
st.write('This is a web app to predict the emission of CO2 based on the production of clinker')

limestone = st.sidebar.text_input('Limestone', "Input mass of limestone")
Shale = st.sidebar.text_input('Shale', "Input mass of Shale")
Iron_ore = st.sidebar.text_input('Iron Ore',"Input mass of Iron Ore" )
CaO = st.sidebar.text_input('CaO',"Input mass of CaO" )
SiO2 = st.sidebar.text_input('SiO2', "Input mass of SiO2")
Al2O3 = st.sidebar.text_input('Al2O3', "Input mass of Al2O3")
Fe2O3 = st.sidebar.text_input('Fe2O3', "Input mass of Fe2O3")

#mapping the features
features= {

    'Limestone': limestone,
    'Shale': Shale,
    'Iron_ore': Iron_ore,
    'CaO': CaO,
    'SiO2': SiO2,
    'Al2O3': Al2O3,
    'Fe2O3': Fe2O3


    }
features_df = pd.DataFrame([features])
st.table(features_df)

#predicting CO2
if st.button('Predict'):
   prediction = predict_carbon(features_df)
   prediction_conv = prediction/1000 
   st.write('Based on the feature values, the CO2 emission for this combination of raw materials is predicted to be: ' + str(int(prediction_conv)) + ' kg')
