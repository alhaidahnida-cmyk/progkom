iimport streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

st.set_page_config(page_title="Virtual Lab Vektor 3D", layout="wide")

st.title("🧭 Virtual Lab Matematika – Vektor 3D Interaktif")
st.write("Eksplorasi vektor 3D secara visual dan interaktif agar lebih mudah dipahami.")

# ================= Vektor Input =================
st.sidebar.header("Input Vektor 3D")
Ax = st.sidebar.number_input("A_x", value=1.0)
Ay = st.sidebar.number_input("A_y", value=2.0)
Az = st.sidebar.number_input("A_z", value=3.0)

Bx = st.sidebar.number_input("B_x", value=4.0)
By = st.sidebar.number_input("B_y", value=1.0)
Bz = st.sidebar.number_input("B_z", value=0.0)

A = np.array([Ax, Ay, Az])
B = np.array([Bx, By, Bz])

# ================= Perhitungan =================
dot = np.dot(A, B)
magA = np.linalg.norm(A)
magB = np.linalg.norm(B)
cross = np.cross(A
