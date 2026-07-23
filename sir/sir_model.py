"""
sir_model.py
Core SIR (Susceptible-Infected-Recovered) epidemic model logic.
"""

import numpy as np
from scipy.integrate import odeint


def sir_deriv(y, t, N, beta, gamma):
    """
    Computes the derivatives (dS/dt, dI/dt, dR/dt) for the SIR model.

    Parameters:
        y (tuple): current (S, I, R) values
        t (float): time (required by odeint, not used directly here)
        N (int): total population
        beta (float): transmission rate
        gamma (float): recovery rate

    Returns:
        tuple: (dS/dt, dI/dt, dR/dt)
    """
    S, I, R = y
    dS_dt = -beta * S * I / N
    dI_dt = beta * S * I / N - gamma * I
    dR_dt = gamma * I
    return dS_dt, dI_dt, dR_dt


def run_sir_model(N, I0, R0, beta, gamma, days):
    """
    Runs the SIR simulation over a given number of days.

    Parameters:
        N (int): total population
        I0 (int): initial infected count
        R0 (int): initial recovered count
        beta (float): transmission rate
        gamma (float): recovery rate
        days (int): number of days to simulate

    Returns:
        t (np.ndarray): time points
        S, I, R (np.ndarray): compartment values over time
    """
    S0 = N - I0 - R0
    y0 = S0, I0, R0

    t = np.linspace(0, days, days)
    result = odeint(sir_deriv, y0, t, args=(N, beta, gamma))
    S, I, R = result.T

    return t, S, I, R


def calculate_r0(beta, gamma):
    """Calculates the basic reproduction number R0 = beta / gamma."""
    return beta / gamma if gamma != 0 else float("inf")


def peak_infection(I):
    """Returns the peak number of infected individuals and the day it occurs."""
    peak_day = int(np.argmax(I))
    peak_value = I[peak_day]
    return peak_day, peak_value