import streamlit as st

# Streamlit app title
st.title("Simple Addition App by Talha")
#hello
# Input fields for two numbers
number1 = st.number_input("Enter the first number:", value=0)
number2 = st.number_input("Enter the second number:", value=0)

# Button to trigger the addition
if st.button("Add"):
    # Perform addition
    result = number1 + number2
    st.success(f"The sum is: {result}")
