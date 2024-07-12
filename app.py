import streamlit as st

# Title with emoji
st.title('CAVTEN APK :sunglasses:')

# Custom divider (violet color)
st.markdown("<hr style='border:2px solid violet'>", unsafe_allow_html=True)

# Header
st.header('Menentukan Bilangan Genap atau Bilangan Ganjil')

# Input for user to enter a number
number = st.number_input("Masukkan sebuah bilangan bulat:", min_value=0, step=1)

# Determine if the number is even or odd
if number % 2 == 0:
    st.write(f"Bilangan {number} adalah bilangan genap.")
else:
    st.write(f"Bilangan {number} adalah bilangan ganjil.")

# Additional content
st.markdown("<br>", unsafe_allow_html=True)  # Add some space
st.write('Pembuat aplikasi ini adalah cavten')
