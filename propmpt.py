import streamlit as st
##import langchain 
import google.generativeai as genai
import os
import pandas as pd
from dotenv import load_dotenv
load_dotenv()


# Set up the Gemini API Key 
genai.configure(api_key=os.getenv('GOOGLE-API-KEY'))
model= genai.GenerativeModel('gemini-1.5-flash')




def genai_response(input,age,Weight,lifestyle,height,Diabetes,bp,Dietery):
    prompt=f'''You are a highly knowledgeable health advisor specializing in creating personalized wellness plans. Your expertise includes Indian diets, yoga practices, exercises, and natural remedies tailored to individual health profiles. Provide a comprehensive health plan for the user based on the following details:

Age: {age}
Height: {height}
Weight: {Weight}
Blood Pressure: {bp}
Diabetes Type: {Diabetes}
Lifestyle: {lifestyle}
Dietary Preferences: {Dietery}
Your response should include and based on this question {input} and the things has to be in detail for this question:

Diet Plan: Culturally appropriate meal suggestions with timings, emphasizing whole foods and traditional Indian ingredients.
Yoga Routine: A daily sequence of yoga asanas and pranayama techniques to promote overall health.
Exercise Plan: A balanced regimen of strength training, cardio, or low-impact exercises, adjusted for the individual's health and fitness level.
Natural Remedies: Home-based solutions or Ayurvedic recommendations for managing health concerns and boosting immunity.
Lifestyle Tips: Practical advice for maintaining long-term health, considering Indian culture and habits.
Ensure the plan is practical, safe, and easily implementable. Break the recommendations into morning, afternoon, and evening routines for clarity.


'''
    response = model.generate_content(prompt)


    return{st.write(response.text)}