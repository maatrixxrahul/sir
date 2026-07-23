"""
app.py
Interactive Streamlit interface for the SIR Epidemic Model Simulator.
"""

import streamlit as st
import matplotlib.pyplot as plt

from sir_model import run_sir_model, calculate_r0, peak_infection

# ---------------- Page Config ----------------
st.set_page_config(page_title="SIR Epidemic Model Simulator", layout="wide")

st.title("🦠 SIR Epidemic Model Simulator")
st.markdown(
    "Simulate the spread of an infectious disease using the classic "
    "**SIR (Susceptible–Infected–Recovered)** compartmental model."
)

# ---------------- Sidebar Controls ----------------
st.sidebar.header("Simulation Parameters")

N = st.sidebar.number_input(
    "Total Population (N)", min_value=100, max_value=10_000_000,
    value=100_000, step=1000
)

I0 = st.sidebar.number_input(
    "Initial Infected (I0)", min_value=1, max_value=int(N),
    value=10, step=1
)

R0_initial = st.sidebar.number_input(
    "Initial Recovered (R0)", min_value=0, max_value=int(N),
    value=0, step=1
)

beta = st.sidebar.slider(
    "Transmission Rate (β)", min_value=0.0, max_value=1.0,
    value=0.3, step=0.01,
    help="Probability of disease transmission per contact, per day"
)

gamma = st.sidebar.slider(
    "Recovery Rate (γ)", min_value=0.01, max_value=1.0,
    value=0.1, step=0.01,
    help="Fraction of infected people recovering per day"
)

days = st.sidebar.slider(
    "Simulation Duration (days)", min_value=10, max_value=365,
    value=160, step=10
)

# ---------------- Run Simulation ----------------
t, S, I, R = run_sir_model(N, I0, R0_initial, beta, gamma, days)
r_naught = calculate_r0(beta, gamma)
peak_day, peak_value = peak_infection(I)

# ---------------- Key Metrics ----------------
col1, col2, col3 = st.columns(3)
col1.metric("Basic Reproduction Number (R₀)", f"{r_naught:.2f}")
col2.metric("Peak Infected", f"{int(peak_value):,}")
col3.metric("Peak Day", f"Day {peak_day}")

# ---------------- Plot ----------------
st.subheader("Epidemic Curve")

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(t, S, label="Susceptible", color="#2E5EAA", linewidth=2)
ax.plot(t, I, label="Infected", color="#D62728", linewidth=2)
ax.plot(t, R, label="Recovered", color="#2CA02C", linewidth=2)
ax.set_xlabel("Days")
ax.set_ylabel("Number of People")
ax.set_title("SIR Model — Disease Spread Over Time")
ax.legend()
ax.grid(alpha=0.3)

st.pyplot(fig)

# ---------------- Data Table (optional) ----------------
with st.expander("View Raw Simulation Data"):
    import pandas as pd
    df = pd.DataFrame({"Day": t, "Susceptible": S, "Infected": I, "Recovered": R})
    st.dataframe(df, use_container_width=True)

st.markdown("---")
st.caption("Built by Rahul Sah · github.com/maatrixxrahul")