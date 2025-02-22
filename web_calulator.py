import streamlit as st
import time

st.set_page_config(page_title="Talha Calculator" ,  page_icon="🧮")

with st.spinner("Processing..."):
    progress_bar = st.progress(0)
    
    for percent in range(100):
        time.sleep(0.05)
        progress_bar.progress(percent + 1)

st.success("Process Completed! Now Check out my web page")


st.title("Simple Calculator Web App")
st.caption("Created by ME(talha) with ❤️")

# User input
try:
    num1 = st.number_input("Enter first number:", step=1.0)
    num2 = st.number_input("Enter second number:", step=1.0)
except ValueError:
    st.error("Invalid input! Please enter a valid number.")


operation = st.selectbox("Select an operation:", 
                         ["Addition", "Subtraction", "Multiplication", "Division"])

#Calculation
if st.button("Calculate"):
    try:
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        st.success(f"Result: {result}")
    except ZeroDivisionError:
        st.error("Error: Cannot divide by zero.")
