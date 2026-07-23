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
- **SciPy** — ODE solving (`odeint`)
- **Matplotlib / Plotly** — visualization
- **Streamlit** — interactive web interface (if applicable)

---

##  Project Structure

```
sir/
│
├── app.py                 # Main application / entry point
├── sir_model.py            # Core SIR model logic and ODE solver
├── requirements.txt        # Project dependencies
├── README.md                # Project documentation
└── assets/                  # Screenshots, sample plots, etc.
```

---

##  Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/maatrixxrahul/sir.git
   cd sir
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```



##  Usage

1. Launch the app.
2. Set initial parameters — population size, initial infected count, transmission rate (β), and recovery rate (γ).
3. Run the simulation to view the S, I, R curves over the chosen time period.
4. Adjust parameters to compare different outbreak scenarios (e.g., effect of a lower transmission rate).



##  Example Output

The simulator generates a plot showing:
- Susceptible population declining over time
- Infected population rising to a peak, then falling
- Recovered population increasing as the outbreak resolves

*(Add a sample screenshot/plot here)*

---

##  Future Improvements

- Add SEIR (Exposed compartment) and other extended epidemic models
- Support for vaccination and intervention scenarios
- Real-world dataset calibration
- Multi-region / spatial simulation support

---

##  License

This project is open-source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Rahul Sah**
GitHub: [maatrixxrahul](https://github.com/maatrixxrahul)
Portfolio: [maatrixxrahul.netlify.app](https://maatrixxrahul.netlify.app)