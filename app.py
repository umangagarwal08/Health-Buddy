import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
from propmpt import genai_response

# Set up the Gemini API Key

genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

# Streamlit Page
st.header("👨‍⚕️Health :blue[Buddy]", divider="green")

age=st.text_input("Enter you Age")
height= st.text_input("Enter your Height in cms")
Weight = st.text_input('Enter your weight in Kgs')
lifestyle=st.selectbox("Lifestyle" ,["Select Any","Sedentary","Active","Moderately"])
Diabetes=st.selectbox('Diabetes Stage',['Select Any','No Diabetes','Type I','Type II','Type III'],key='Select any')
bp = st.selectbox("Blood Pressure",['Select Any','Yes','No'],key='Select Any')
dietery=st.selectbox("Dietary Preferences", ['Vegetarian',"Non-vegetarian"])

input = st.text_input("Hi, I am your 💊Health Expert. Ask me anything")
sumbit_button = st.button("Submit")
if sumbit_button and input != "" and age != "" and height != "" and Diabetes != "" and bp != "" and Weight != "" and lifestyle != "" and dietery != "":
    text=genai_response(input,age,Weight,lifestyle,height,Diabetes,bp,dietery)
    st.markdown(text)


# Disclaimer
st.subheader("Disclaimer", divider=True)
notes = '''
1. This is an advisor providing guidance and should not be construed as medical advice.
2. Before taking any action, it is recommended to consult a Doctor.
'''
st.markdown(notes)
