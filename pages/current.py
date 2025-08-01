import streamlit as st
from current_account import CurrentAccount

saving=CurrentAccount(1000)

st.set_page_config(page_title="Bank APP",layout="centered")


with st.form ("Current Account"):
    amount=st.number_input("Please Enter Amont",step=100)
    operation=st.selectbox("Deposite","Withdraw",["Deposit","Withdraw"])
    sumbit=st.form_sumbit_button("Sumbit")

    if sumbit:
        if operation =="Withdraw":
            with st.spinner("Processing"):
                if amount<saving.balance:
                    saving.withdraw(amount)
                    st.success(f"New Balance is {saving.balance}")
                else:
                    st.error("Insufficient Funds")

        else:
            operation=="Deposit"
            with st.spinner("Processing"):
                    saving.deposit(amount)
                    st.success(f"New Balance is {saving.balance}")




        