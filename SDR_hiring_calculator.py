import streamlit as st


def total_cost(num_sdr, rep_salary, open_headcount, tool_cost):
    total_rep_salary = num_sdr * rep_salary
    total_hiring_cost = open_headcount * (0.4 * rep_salary)
    total_tool_cost = tool_cost * num_sdr
    total_cost_team = total_rep_salary + total_hiring_cost + total_tool_cost
    return total_cost_team


st.set_option("client.showErrorDetails", True)
st.title(" Calculate your SDR team total cost of onwership")
st.write("use the sliders below to understand how many SDRs to hire")

num_sdr = st.number_input(
    "🙋 How many full-time SDRs do you have currently",
    min_value=0,
    max_value=100,
    step=1,
)
rep_salary = st.slider(
    "🤑 Average SDR Base Salary", min_value=0, max_value=100000, step=5000
)
open_headcount = st.slider(
    " 📈 Current Open Headcount", min_value=0, max_value=100, step=1
)
tool_cost = st.slider(
    " 💻 Average Tool Cost per Rep", min_value=0, max_value=100000, step=1000
)

total_cost_of_ownership = total_cost(num_sdr, rep_salary, open_headcount, tool_cost)

st.markdown("---")
st.metric("📊 Your Total Cost of Ownership", f"*${total_cost_of_ownership:,.0f}*")
