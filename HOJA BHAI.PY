import streamlit as st
import random
import string

def generate_password(length, include_uppercase, include_numbers, include_special_chars):
    chars = string.ascii_lowercase
    if include_uppercase:
        chars += string.ascii_uppercase
    if include_numbers:
        chars += string.digits
    if include_special_chars:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Streamlit UI
st.title("Password Generator")

# Input fields
length = st.slider("Select password length:", 8, 32, 12)
include_uppercase = st.checkbox("Include Uppercase")
include_numbers = st.checkbox("Include Numbers")
include_special_chars = st.checkbox("Include Special Characters")

# Generate button
if st.button("Generate Password"):
    password = generate_password(length, include_uppercase, include_numbers, include_special_chars)
    st.success(f"Your generated password: {password}")