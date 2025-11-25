import streamlit as st
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
cross = np.cross(A, B)
angle = np.degrees(np.arccos(dot / (magA * magB + 1e-10)))


# ================= Hasil =================
st.subheader("📌 Hasil Perhitungan Vektor 3D")
col1, col2, col3 = st.columns(3)


with col1:
st.metric("‖A‖", f"{magA:.3f}")
st.metric("A · B (Dot Product)", f"{dot:.3f}")


with col2:
st.metric("‖B‖", f"{magB:.3f}")
st.metric("Sudut A-B", f"{angle:.3f}°")


with col3:
st.write("Cross Product (A × B):")
st.code(f"({cross[0]:.3f}, {cross[1]:.3f}, {cross[2]:.3f})")


# ================= Visualisasi =================
st.subheader("🎨 Visualisasi Vektor 3D")
fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(111, projection='3d')


# Sumbu
max_range = max(np.linalg.norm(A), np.linalg.norm(B)) + 2
ax.set_xlim([0, max_range])
ax.set_ylim([0, max_range])
ax.set_zlim([0, max_range])


# Plot vektor A
ax.quiver(0, 0, 0, A[0], A[1], A[2], color='blue', label='Vektor A')
# Plot vektor B
ax.quiver(0, 0, 0, B[0], B[1], B[2], color='red', label='Vektor B')
# Cross Product
ax.quiver(0, 0, 0, cross[0], cross[1], cross[2], color='green', label='A × B')


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
st.pyplot(fig)


# ================= Latihan Soal =================
st.subheader("📘 Latihan Soal Vektor 3D")
import random
if st.button("Generate Soal Baru"):
P = np.random.randint(-5, 6, size=3)
Q = np.random.randint(-5, 6, size=3)
st.write(f"Hitung dot product dan cross product dari vektor berikut:")
st.latex(f"P = ({P[0]}, {P[1]}, {P[2]})")
st.latex(f"Q = ({Q[0]}, {Q[1]}, {Q[2]})")
st.write("Coba hitung sendiri dulu ya!")
        p += 2
    if n > 1:
        factors.append(n)
    return factors

def factor_dict(n: int):
    d = {}
    for p in prime_factors(n):
        d[p] = d.get(p, 0) + 1
    return d

def all_factors(n: int):
    pf = factor_dict(n)
    primes = list(pf.items())
    def gen(i):
        if i == len(primes):
            return [1]
        p, exp = primes[i]
        rest = gen(i+1)
        res = []
        for e in range(exp+1):
            res += [r * (p**e) for r in rest]
        return res
    return sorted(gen(0))

def gcd_steps(a: int, b: int):
    steps = []
    x, y = a, b
    while y:
        q = x // y
        r = x % y
        steps.append(f"{x} = {y} × {q} + {r}")
        x, y = y, r
    steps.append(f"FPB = {x}")
    return x, steps

def lcm(a: int, b: int):
    return abs(a * b) // math.gcd(a, b) if a and b else 0

st.title("🌻 Virtual Lab Matematika: FPB, KPK, Faktor, Kelipatan")

col1, col2 = st.columns(2)
with col1:
    a = st.number_input("Bilangan pertama", min_value=1, value=36)
    b = st.number_input("Bilangan kedua", min_value=1, value=48)
    go = st.button("Hitung")

with col2:
    st.write("Opsi tampilan:")
    show_steps = st.checkbox("Langkah Euclidean FPB", True)
    show_factor = st.checkbox("Tampilkan faktor & faktorisasi", True)
    show_venn = st.checkbox("Venn diagram faktor", True)

if go:
    st.subheader("Hasil Perhitungan")
    colA, colB = st.columns(2)
    with colA:
        st.metric("FPB", math.gcd(a, b))
    with colB:
        st.metric("KPK", lcm(a, b))

    if show_factor:
        st.write("---")
        st.subheader("Faktorisasi & Faktor")
        c1, c2 = st.columns(2)
        with c1:
            st.write(f"Faktor dari {a}: {all_factors(a)}")
            st.write(f"Faktorisasi prima {a}: {prime_factors(a)}")
        with c2:
            st.write(f"Faktor dari {b}: {all_factors(b)}")
            st.write(f"Faktorisasi prima {b}: {prime_factors(b)}")

    if show_steps:
        st.write("---")
        st.subheader("Langkah Euclidean")
        g, steps = gcd_steps(a, b)
        for s in steps:
            st.code(s)

    if show_venn:
        st.write("---")
        st.subheader("Venn Diagram Faktor")
        fa = set(all_factors(a))
        fb = set(all_factors(b))
        only_a = fa - fb
        only_b = fb - fa
        common = fa & fb
        fig, ax = plt.subplots(figsize=(4, 4))
        venn2(subsets=(len(only_a), len(only_b), len(common)), set_labels=(a, b))
        st.pyplot(fig)

st.write("---")
st.subheader("Latihan Soal")
if st.button("Soal Baru"):
    x = random.randint(10, 200)
    y = random.randint(10, 200)
    st.write(f"FPB dari {x} dan {y} adalah ... ?")
