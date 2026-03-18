import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

# Title
st.title("INR Calculator")

st.markdown("""
This tool calculates **Ratio**, **Index**, and **INR** based on user input.

- **Ratio = Patient / Control**
- **Index = (Control × 100) / Patient**
- **INR = Ratio ^ ISI** (ISI = 1.2)
""")

# Input fields (no sidebar)
patient_value = st.number_input("Enter Patient Value", min_value=0.0, step=0.1, format="%.2f")
control_value = st.number_input("Enter Control Value", min_value=0.0, step=0.1, format="%.2f")

ISI = 1.2

# Function to generate PDF
def generate_pdf(patient, control, ratio, index, inr):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("INR Calculation Report", styles['Title']))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph(f"Patient Value: {patient}", styles['Normal']))
    elements.append(Paragraph(f"Control Value: {control}", styles['Normal']))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph(f"Ratio: {ratio:.3f}", styles['Normal']))
    elements.append(Paragraph(f"Index: {index:.2f}", styles['Normal']))
    elements.append(Paragraph(f"INR: {inr:.3f}", styles['Normal']))

    doc.build(elements)
    buffer.seek(0)
    return buffer

# Calculation
if patient_value > 0 and control_value > 0:
    ratio = patient_value / control_value
    index = (control_value * 100) / patient_value
    inr = ratio ** ISI

    st.subheader("Results")
    st.metric("Ratio", f"{ratio:.3f}")
    st.metric("Index", f"{index:.2f}")
    st.metric("INR", f"{inr:.3f}")

    # Generate PDF
    pdf_file = generate_pdf(patient_value, control_value, ratio, index, inr)

    st.download_button(
        label="Download Report as PDF",
        data=pdf_file,
        file_name="INR_Report.pdf",
        mime="application/pdf"
    )

elif patient_value == 0 or control_value == 0:
    st.warning("Please enter values greater than 0 for both Patient and Control.")
else:
    st.info("Enter the values to see the calculations.")

# Footer
st.markdown("---")
st.markdown("Developed by **Bipropod Das Shubro**")
