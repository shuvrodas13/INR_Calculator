import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from io import BytesIO

st.title("INR Calculator")

# ID Input (6 digits or more)
patient_id = st.text_input("Patient ID")

patient_value = st.number_input("Patient Value", min_value=0.0, step=0.1)
control_value = st.number_input("Control Value", min_value=0.0, step=0.1)

ISI = 1.2

# PDF Function
def generate_pdf(pid, patient, control, ratio, index, inr):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    # Styling
    styles['Title'].alignment = TA_CENTER
    styles['Title'].fontSize = 20
    styles['Normal'].fontSize = 14

    elements = []

    elements.append(Paragraph("INR Report", styles['Title']))
    elements.append(Spacer(1, 20))

    elements.append(Paragraph(f"Patient ID: {pid}", styles['Normal']))
    elements.append(Spacer(1, 10))
    
    elements.append(Paragraph(f"Patient Value: {patient}", styles['Normal']))
    elements.append(Paragraph(f"Control Value: {control}", styles['Normal']))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph(f"Ratio: {ratio:.3f}", styles['Normal']))
    elements.append(Paragraph(f"Index: {index:.2f}", styles['Normal']))
    elements.append(Paragraph(f"INR: {inr:.3f}", styles['Normal']))

    doc.build(elements)
    buffer.seek(0)
    return buffer

# Validation
valid_id = patient_id.isdigit() and len(patient_id) >= 6

if patient_id and not valid_id:
    st.error("Patient ID must be at least 6 digits.")

# Calculation
if valid_id and patient_value > 0 and control_value > 0:
    ratio = patient_value / control_value
    index = (control_value * 100) / patient_value
    inr = ratio ** ISI

    st.subheader("Results")
    st.metric("Ratio", f"{ratio:.3f}")
    st.metric("Index", f"{index:.2f}")
    st.metric("INR", f"{inr:.3f}")

    # Generate PDF
    pdf = generate_pdf(patient_id, patient_value, control_value, ratio, index, inr)

    st.download_button(
        "📄 Download Report",
        data=pdf,
        file_name=f"INR_Report_{patient_id}.pdf",
        mime="application/pdf"
    )

    # Print Button (browser print)
    st.markdown("""
        <button onclick="window.print()">🖨️ Print Report</button>
    """, unsafe_allow_html=True)

elif patient_value == 0 or control_value == 0:
    st.warning("Enter values greater than 0.")

st.markdown("---")
st.markdown("Developed by **Bipropod Das Shubro**")
