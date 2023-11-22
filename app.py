import streamlit as st
import joblib 
model = joblib.load('newsClassifier')
st.title('NEWS CLASSIFIER') # Creates a title with name SPAM-HAM CLASSIFIER
ip = st.text_input('Enter the news : ') # Creates a text box
op = model.predict([ip])
if st.button('Classify'):
  st.title(op[0])
