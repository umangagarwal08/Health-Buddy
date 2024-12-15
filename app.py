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
col1, col2 = st.columns([6, 1])  # Adjust column width ratio as needed
with col1:
    st.header("👨‍⚕️Health :blue[Buddy]", anchor=None)
with col2:
    logo_path = "logo.png"  # Path to your logo image file
    st.image(logo_path, width=500)  # Adjust width as needed
st.subheader("Your AI-powered wellness partner")


age=st.text_input("Enter you Age")
height= st.text_input("Enter your Height in cms")
Weight = st.text_input('Enter your weight in Kgs')
lifestyle=st.selectbox("Lifestyle" ,["Select Any","Sedentary","Active","Moderately"])
Diabetes=st.selectbox('Diabetes Stage',['Select Any','No Diabetes','Type I','Type II','Type III'],key='Select any')
bp = st.selectbox("Blood Pressure",['Select Any','Yes','No'],key='Select Any')
dietery=st.selectbox("Dietary Preferences", ["Select Any",'Vegetarian',"Non-vegetarian"])
gender=st.selectbox("Gender",['Select Any','Male','Female'])

input = st.text_input("Hi, I am your 💊Health Expert. Ask me anything")
sumbit_button = st.button("Submit")
if sumbit_button and input != "" and age != "" and height != "" and Diabetes != "" and bp != "" and Weight != "" \
    and lifestyle != "" and dietery != "" and gender != "":
    text=genai_response(input,age,Weight,lifestyle,height,Diabetes,bp,dietery,gender)
    st.markdown(text)


# Disclaimer
st.subheader("Disclaimer", divider=True)
notes = '''
1. This is an advisor providing guidance and should not be construed as medical advice.
2. Before taking any action, it is recommended to consult a Doctor.
'''
st.markdown(notes)
