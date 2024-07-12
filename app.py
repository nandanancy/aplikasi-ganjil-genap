import streamlit as st

st.title("Define Number Type apps")
st.header("Define Number Typs apps", divider ="blue")
st.write("ini adalah aplikasi untuk menentukan bilangan genap atau ganjil")

number = st.number_input("Insert a Number")
st.write("The Number Is",number)

import streamlit as st


st.write("Ini adalah aplikasi untuk menentukan bilangan genap atau ganjil.")

# Input untuk angka
number = st.number_input("Masukkan Angka", value=0)

# Tampilkan angka yang dimasukkan
st.write("Angka yang dimasukkan adalah:", number)

# Menentukan apakah angka genap atau ganjil
if number % 2 == 0:
    st.write("Angka {number} adalah **Genap**.")
else:
    st.write("Angka {number} adalah **Ganjil**.")


import streamlit as st

# Judul aplikasi
st.title("Aplikasi Penentu Bilangan Genap/Ganjil dan Perkalian")

# Deskripsi aplikasi
st.write("Aplikasi ini menentukan apakah sebuah bilangan genap atau ganjil dan melakukan perkalian.")

# Input untuk angka pertama
number = st.number_input("Masukkan Angka Pertama", value=0)

# Menentukan apakah angka genap atau ganjil
if number % 2 == 0:
    st.write(f"Angka {number} adalah **Genap**.")
else:
    st.write(f"Angka {number} adalah **Ganjil**.")

# Input untuk angka kedua untuk perkalian
multiplier = st.number_input("Masukkan Angka Kedua untuk Perkalian", value=1)

# Melakukan perkalian
result = number * multiplier
st.write(f"Hasil perkalian {number} x {multiplier} = {result}")

# Menentukan apakah hasil perkalian genap atau ganjil
if result % 2 == 0:
    st.write(f"Hasil {result} adalah **Genap**.")
else:
    st.write(f"Hasil {result} adalah **Ganjil**.")
