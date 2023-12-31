# -*- coding: utf-8 -*-
"""Untitled7 (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18ivyT_FPkb3AGeNOzldeM0VfCSBl1eW3
"""

import streamlit as st
import requests
from streamlit_lottie import st_lottie
import joblib
import numpy as np

st.set_page_config(page_title='Company Loan Eligibility', page_icon='::star::')

def load_lottie(url): # test url if you want to use your own lottie file 'valid url' or 'invalid url'
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def prepare_input_data_for_model(gender,age,annual_income,spending_score):

    if gender == 'Male':
        gender = 1
    else:
         gender = 0


    A = [gender]
    sample = np.array(A).reshape(-1,len(A))

    return sample



loaded_model = joblib.load("Customer_Segmentation")



st.write('# Customer Segmentation ')
st.header('Placement')

lottie_link = "https://lottie.host/6994bc3f-4f36-4ab6-9f44-4646cea87690/oVQQrhTlNb.json"
zanimation = load_lottie(lottie_link)

st.write('---')
st.subheader('Enter your details to predict what category you fit in')

with st.container():

    right_column, left_column = st.columns(2)

    with right_column:
        name = st.text_input('Your name')
        gender = st.radio('Your Gender: ', ['Male', 'Female'])
        age= st.number_input('Your Age:', min_value=0.0, max_value=100.0, value=0.0, step=0.1)
        annual_income= st.number_input('Your Annual Income (k$):', min_value=0.0, max_value=10000.0, value=0.0, step=0.1)
        spending_score= st.number_input('Your Spending Score:', min_value=0.0, max_value=100.0, value=0.0, step=0.1)

        sample = prepare_input_data_for_model(gender,age,annual_income,spending_score)





    if st.button('Predict'):
            pred_Y = loaded_model.predict(sample)

            if pred_Y >= 0.1 and pred_Y <= 0.3:
                #st.write("## Predicted Status : ", result)
                st.write('### You are a low spender.')
                st.balloons()
            elif pred_Y >= 0.3 and pred_Y <= 0.6:
                #st.write("## Predicted Status : ", result)
                st.write('### You are a moderate spender.')
                st.balloons()
            elif pred_Y >= 0.6 and pred_Y <= 1:
                #st.write("## Predicted Status : ", result)
                st.write('### You are a high spender.')
                st.balloons()