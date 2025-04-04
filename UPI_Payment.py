import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

# Constants
UPI_ID = "jpeasal-8@okhdfcbank"
PAYEE_NAME = "Eashwar"

st.set_page_config(page_title="UPI Payment Link Generator", layout="centered")

# App Title
st.title("📱 UPI Payment Link & QR Generator")

# Input from user
amount = st.number_input("Enter Amount (INR)", min_value=1.0, step=1.0, format="%.2f")

# Generate UPI link
if st.button("Generate UPI Link"):
    upi_url = f"upi://pay?pa={UPI_ID}&pn={PAYEE_NAME}&am={amount:.2f}&cu=INR"
    
    st.markdown("### 🔗 UPI Payment Link")
    st.code(upi_url, language='text')

    # Generate QR Code
    qr = qrcode.make(upi_url)
    buf = BytesIO()
    qr.save(buf)
    buf.seek(0)
    img = Image.open(buf)

    st.markdown("### 📷 Scan QR to Pay")
    st.image(img, use_container_width=True, caption="Scan this with your UPI app")
