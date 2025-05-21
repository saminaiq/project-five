import streamlit as st  # for user-interface
import hashlib  # for hashing values
from cryptography.fernet import Fernet  # for encryption and decryption

# --- Page Setup ---
st.set_page_config(
    page_title="Secure Data System",
    page_icon="🔐",
    layout="centered"
)

st.title("Encrypt Your Data, Stay Protected")

# --- Custom CSS ---
def custom_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

        html, body, [class*="st-"] {
            font-family: Georgia, serif;
        }

        .stApp {
            background-image: url("https://plus.unsplash.com/premium_photo-1701179596614-9c64f50cda76?q=80&w=1374&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
            z-index:-1;
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            color: black;
            text-align: center;
        }

        .stApp > div {
            backdrop-filter: blur(5px); /* Prevents blur on text */
        }

        .stheader {
            font-family: Verdana, sans-serif !important;
            font-size: 30px;
            color: #4CAF50;
            text-align: left;
            
        }

        .stsubheader {
            font-family: 'Courier New', monospace !important;
            font-size: 30px;
            color: #4CAF50;
            text-align: left;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Apply the CSS
custom_css()

# --- Key Generation ---
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# --- Encryption Function ---
def encrypt_message(message):
    return cipher_suite.encrypt(message.encode()).decode()

# --- Decryption Function ---
def decrypt_message(token):
    return cipher_suite.decrypt(token.encode()).decode()

# --- Streamlit App Interface ---
st.subheader("🔐 Secure Encryption/Decryption System")

option = st.selectbox("Choose Action:", ["Encrypt", "Decrypt"])

user_input = st.text_input("Enter your message:")

if option == "Encrypt" and user_input:
    encrypted = encrypt_message(user_input)
    st.success("Encrypted Message:")
    st.code(encrypted)

elif option == "Decrypt" and user_input:
    try:
        decrypted = decrypt_message(user_input)
        st.success("Decrypted Message:")
        st.code(decrypted)
    except Exception as e:
        st.error("Decryption failed. Please enter a valid encrypted message.")


