#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 19:15:57 2024

@author: ayooluwakolawole
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib


# Given parameters
theta_0 = 0.362  # Static angular displacement in rad
omega_0 = 4.394  # Natural frequency in rad/s (from Q2.1)
b = 9.68e-5  # Damping coefficient in Nms/rad
keq = 0.00259  # Spring constant in Nm/rad
I = 0.000134  # Moment of inertia in kg.m^2

# Damping ratio
zeta = b / (2 * np.sqrt(keq * I))

# Frequency range for plotting
omega = np.linspace(0.1, 10, 500)  # Forcing frequencies in rad/s

# Magnitude of angular displacement
theta_magnitude = theta_0 / np.sqrt((1 - (omega / omega_0)**2)**2 + (2 * zeta * (omega / omega_0))**2)

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(omega, theta_magnitude, label=r"$|\theta(\omega)|$")
plt.axvline(omega_0, color='r', linestyle='--', label=r"$\omega_0 = 4.394$ rad/s")
plt.title("Theoretical Angular Displacement Magnitude vs Forcing Frequency")
plt.xlabel("Forcing Frequency, $\omega$ (rad/s)")
plt.ylabel(r"Magnitude of Angular Displacement, $|\theta(\omega)|$ (rad)")
plt.legend()
plt.grid(True)
plt.show()
