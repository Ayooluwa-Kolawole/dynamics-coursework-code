# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file adjusted for torsional spring context.
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import numpy as np
"""
# Constants
M = 118.4 / 1000  # Mass of the disk in kg
R = 4.76 / 100  # Radius of the disk in meters
I = (1 / 2) * M * R**2  # Moment of inertia of the disk (kg·m²)

k_eq = 0.00259  # Equivalent torsional spring constant (Nm/rad)
natural_frequency = (k_eq / I)**0.5  # Natural frequency (rad/s)
b = 9.68e-5  # Torsional damping coefficient (Nms/rad)

# Print computed constants for verification
print(f"Mass of the disk, M: {M} kg")
print(f"Radius of the disk, R: {R} m")
print(f"Moment of inertia, I: {I} kg·m²")
print(f"Natural frequency, ω_n: {natural_frequency} rad/s")
print(f"Torsional damping coefficient, b: {b} Nms/rad")
print()

# Function to calculate damping ratio and coefficient
def calculate_damping(peak_amplitudes, torsional_damping, torsional_frequency):
    # Logarithmic decrement
    decrements = np.log(peak_amplitudes[:-1].values / peak_amplitudes[1:].values)
    delta = np.mean(decrements)
    
    # Damping ratio
    damping_ratio = delta / np.sqrt(4 * np.pi**2 + delta**2)
    
    # Damping coefficient (not used for torsional systems directly)
    damping_coefficient = torsional_damping / (2 * torsional_frequency * I)
    
    return damping_ratio, damping_coefficient
"""
# 1. Import the Data for Procedure 2
data1 = pd.read_excel('/Users/ayooluwakolawole/Desktop/Dynamics Coursework/ExperimentalData_Dynamics.xlsx', sheet_name='Exp. 2 Procedure 2')
time1 = data1['Time (s)']
angle1 = data1['Disk Angle (rad)']

# 2. Plot the Angular Displacement for Procedure 2
plt.figure(figsize=(10, 6))
plt.plot(time1, angle1, label=r"Angular Displacement, $\theta$(t)")
plt.xlabel('Time, t (s)')
plt.ylabel(r"Angular Displacement, $\theta$ (rad)")
plt.title('Procedure 2: Damped Free Oscillations')
plt.legend()
plt.grid(True)
plt.show()

# 3. Calculate Frequency and Period of Oscillation for the First Experiment
peaks1, _ = find_peaks(angle1)  # Identify peaks in the position data
peak_times1 = time1[peaks1]  # Get the time values at each peak

# Calculate the differences between successive peaks to get periods
periods1 = peak_times1.diff().dropna()  # Drop any NaN from the first diff
average_period1 = periods1.mean()  # Average of the periods
frequency1 = 1 / average_period1  # Frequency is the inverse of period

print("Procedure 2: Damped Free Oscillations")
print(f"Average Period of Oscillation: {average_period1:.2f} seconds")
print(f"Damped Frequency of Oscillation: {frequency1:.2f} Hz")
print()

"""
# Calculate Damping Ratio and Coefficient
peak_amplitudes1 = angle1.iloc[peaks1]  # Get amplitudes of the peaks
damping_ratio1, damping_coefficient1 = calculate_damping(peak_amplitudes1, b, natural_frequency)

print(f"Damping Ratio: {damping_ratio1:.4f}")
print(f"Damping Coefficient: {damping_coefficient1:.4f} Nms/rad")
print()

# 4. Import the Data for Procedure 3
data2 = pd.read_excel('/Users/ayooluwakolawole/Desktop/Dynamics Coursework/ExperimentalData_Dynamics.xlsx', sheet_name='Exp. 2 Procedure 3')
time2 = data2['Time (s)']
angle2 = data2['Disk Angle (rad)']

# 5. Plot the Angular Displacement for Procedure 3
plt.figure(figsize=(10, 6))
plt.plot(time2, angle2, label=r"Angular Displacement, $\theta$(t)")
plt.xlabel('Time, t (s)')
plt.ylabel(r"Angular Displacement, $\theta$ (rad)")
plt.title('Procedure 3: Damped Forced Oscillations')
plt.legend()
plt.grid(True)
plt.show()

# 6. Calculate Frequency and Period of Oscillation for Procedure 3
peaks2, _ = find_peaks(angle2)  # Identify peaks
peak_times2 = time2.iloc[peaks2]  # Get the time values at each peak

# Calculate the differences between successive peaks to get periods
periods2 = peak_times2.diff().dropna()  # Drop any NaN from the first diff
average_period2 = periods2.mean()  # Average of the periods
frequency2 = 1 / average_period2  # Frequency is the inverse of period

print("Procedure 3: Damped Forced Oscillations")
print(f"Average Period of Oscillation: {average_period2:.2f} seconds")
print(f"Damped Frequency of Oscillation: {frequency2:.2f} Hz")

# Calculate Damping Ratio and Coefficient
peak_amplitudes2 = angle2.iloc[peaks2]  # Get amplitudes of the peaks
damping_ratio2, damping_coefficient2 = calculate_damping(peak_amplitudes2, b, natural_frequency)

print(f"Damping Ratio: {damping_ratio2:.4f}")
print(f"Damping Coefficient: {damping_coefficient2:.4f} Nms/rad")

"""