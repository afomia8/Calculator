import streamlit as st

def calculate(num1, num2, operator):
  if operator == '+':
    return   num1 + num2
  if operator == '-':
    return num1 - num2   
  if operator == '*':
    return num1*num2
  if operator == '/':
    return num1/num2   
  else:
    return 'Invalid Operator'

st.title('Calculator')  
