import streamlit as st

st.title("INR Calculator")
st.markdown("""
This tool calculates **Ratio**, **Index**, and **INR** based on user input.
- **Ratio = Patient / Control**
- **Index = (Control × 100) / Patient**
- **INR = Ratio ^ ISI** (ISI = 1.2)
""")
st.sidebar.header("Input Values")
patient_value = st.sidebar.number_input("Patient Value", min_value=0.0, step=0.1, format="%.2f")
control_value = st.sidebar.number_input("Control Value", min_value=0.0, step=0.1, format="%.2f")

# Constants
ISI = 1.2
if patient_value > 0 and control_value > 0:
    ratio = patient_value / control_value
    index = (control_value * 100) / patient_value
    inr = ratio ** ISI
    st.subheader("Results")
    st.metric("Ratio", f"{ratio:.3f}")
    st.metric("Index", f"{index:.2f}")
    st.metric("INR", f"{inr:.3f}")

elif patient_value == 0 or control_value == 0:
    st.warning("Please enter values greater than 0 for both Patient and Control.")
else:
    st.info("Enter the values to see the calculations.")


st.markdown("""
Developed by Bipropod Das Shubro
""")
