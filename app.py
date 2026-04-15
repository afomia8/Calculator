import streamlit as st
import math

st.set_page_config(page_title="My Calculator", page_icon="🔢")
def calculate(num1, num2, operator):
  if operator == '+':
    return   num1 + num2
  elif operator == '-':
    return num1 - num2
  elif operator == '*':
    return num1*num2
  elif operator == '/':
    if num2 != 0:
      return num1/num2
    else:
      return'Cannot divide by zero.'
  elif operator == 'Power':
    return num1**num2  
  else:
    return 'Invalid Operator'

st.title('Calculator')
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input('Enter the first number.')
with col2:    
    num2 = st.number_input('Enter the second number.')
operator = st.selectbox('Select an operator',['+','-','*','/','Power'] )

if st.button('Calculate'):
    result = calculate(num1, num2, operator)
    st.write('The result is:', result)
