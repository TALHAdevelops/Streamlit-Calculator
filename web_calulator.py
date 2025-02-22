import streamlit as st

st.set_page_config(page_title="Talha Calculator")


st.title("Simple Calculator Web App")

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
