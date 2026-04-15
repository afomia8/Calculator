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
num1 = st.number_input('Enter the first number.')
num2 = st.number_input('Enter the second number.')
operator = st.selectbox('Select an operator',['+','-','*','/'] )

result = calculate(num1, num2, operator)
st.write('The result is:', result)
