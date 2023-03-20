import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image

pickle_in = open("poly.pkl","rb")
lasso=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def Height_and_Weight(Height(Inches)):
    
    """Let's Predict the sales of retail store 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: Height(Inches)
        in: query
        type: number
        required: true
      
    responses:
    200:
            description: The output values
            
    """
    prediction=lasso.predict([[Height(Inches)]])
    print(prediction)
    return prediction

def main():
    st.title("Height and Weight")
    wHeight(Inches) = st.text_input("Height(Inches)","Type Here")
    
  
    if st.button("Predict"):
        result=Sales_Of_Retail_Store([Height(Inches)])
    st.success('The output is {}')


if _name=='main_':
    main()