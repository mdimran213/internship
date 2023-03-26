import numpy as np
import pickle
import pandas as pd
import streamlit as st 



pickle = open("poly.pkl","rb")
poly=pickle.load(pickle)

def welcome():
    return "Welcome All"

def Height_and_Weight(Height):
    
    """Let's Predict the Height_and_Weight 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: Height
        in: query
        type: number
        required: true
      
    responses:
    200:
            description: The output values
            
    """
    prediction=poly.predict([[Height]])
    print(prediction)
    return prediction

def main():
    st.title("Height and Weight")
    Weight = st.text_input("Height","Type Here")
    
  
    if st.button("Predict"):
        result=Height_and_Weight([Height])
    st.success('The predicted weight is {}'.format(result))


if _name=='main_':
    main()