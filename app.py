import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def bell_fidelity(noise):
    p = noise/100
    return max(0, 1 - 0.75*p - 0.1*np.random.rand()*0.1)

st.title("Q-Verify - Quantum Chip Tester")
st.write("Testing Bell State under Noise")

col1, col2 = st.columns(2)
with col1:
    noise = st.slider("Noise %", 0, 50, 10)
with col2:
    st.metric("Current Test", f"{noise}%")

noises = np.arange(0,51,5)
fids = [bell_fidelity(n) for n in noises]

fig, ax = plt.subplots()
ax.plot(noises, fids, marker='o')
ax.set_xlabel("Noise %")
ax.set_ylabel("Fidelity")
ax.set_title("Fidelity vs Noise")
st.pyplot(fig)

current_fid = bell_fidelity(noise)
status = "PASS ✅" if current_fid>0.8 else "FAIL ❌"
st.success(f"Verification Result: At {noise}% noise, fidelity is {current_fid*100:.1f}% - {status}")

st.write("---")
st.write("**Q-Verify | Hyderabad | Founder: Chandu**")
st.write("Contact: LinkedIn DM")
st.write("---")
st.subheader("Real QPU Test - Upload CSV")
uploaded = st.file_uploader("Upload QPU counts (00,01,10,11 columns)")

if uploaded:
    import pandas as pd
    df = pd.read_csv(uploaded)
    total = df['00'].sum() + df['01'].sum() + df['10'].sum() + df['11'].sum()
    fid_real = (df['00'].sum() + df['11'].sum()) / total
    st.metric("Real Chip Fidelity", f"{fid_real*100:.1f}%")
    if fid_real > 0.9:
        st.balloons()