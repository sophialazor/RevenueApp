import streamlit as st
from model.revenue_model import revenue

st.title("Revenue Calculator")
st.write("Enter a price and quantity to calculate revenue.")

with st.form("revenue_form"):
    price = st.number_input("Price ($)", min_value=0.0, step=0.01, format="%.2f")
    quantity = st.number_input("Quantity", min_value=0, step=1)
    run = st.form_submit_button("Run")

if run:
    revenue_value = revenue(price, quantity)
    st.metric("Revenue", f"${revenue_value:,.2f}")