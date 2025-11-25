# app.py - Virtual Lab FPB KPK
# Versi ringkas siap deploy Streamlit

import streamlit as st
import math
from functools import reduce
from typing import List, Tuple
import random
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

st.set_page_config(page_title="Virtual Lab FPB-KPK", layout="wide")

def prime_factors(n: int):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    p = 3
    while p * p <= n:
        while n % p == 0:
            factors.append(p)
            n //= p
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
