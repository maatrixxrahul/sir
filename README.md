# SIR Epidemic Model Simulator

A simulation tool that models the spread of infectious diseases using the classic **SIR (Susceptible Infected Recovered)** compartmental model, built to explore epidemic dynamics through mathematical modeling and interactive visualization.



## 📖 Overview

The SIR model divides a population into three compartments:

- **S (Susceptible)** — individuals who can contract the disease
- **I (Infected)** — individuals currently infected and capable of spreading the disease
- **R (Recovered)** — individuals who have recovered and gained immunity (or been removed)

This simulator solves the SIR system of differential equations numerically and visualizes how an outbreak evolves over time based on user-defined parameters such as transmission rate, recovery rate, and initial population size.



##  Features

- Simulates disease spread using the SIR differential equation model
- Adjustable parameters: infection rate (β), recovery rate (γ), population size, and initial infected count
- Visualizes S, I, R curves over time
- Calculates key epidemic metrics (e.g., basic reproduction number R₀, peak infection point)
- Interactive interface for experimenting with different outbreak scenarios

---

##  Model Equations

The simulator is based on the standard SIR differential equations:

```
dS/dt = -β * S * I / N
dI/dt =  β * S * I / N - γ * I
dR/dt =  γ * I
```

Where:
- `N` = total population
- `β` = transmission rate
- `γ` = recovery rate
- `R₀ = β / γ` = basic reproduction number

---

## 🛠️ Tech Stack

- **Python**
- **NumPy** — numerical computation
