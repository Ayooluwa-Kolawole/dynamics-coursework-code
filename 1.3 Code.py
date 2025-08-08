# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# 1. Import the Data for the First Experiment
data1 = pd.read_excel('/Users/ayooluwakolawole/Desktop/Dynamics Coursework/ExperimentalData_Dynamics.xlsx', sheet_name='Exp. 1.1 (no sliding block)')
time1 = data1['Time - Plot 0']
position1 = data1['Pulley Movement (cm) - Plot 0']

# 2. Plot the Oscillation Data for the First Experiment
plt.figure(figsize=(10, 6))
plt.plot(time1, position1, label='Condition a) Response x(t)')
plt.xlabel('Time, t (s)')
plt.ylabel('Pulley Movement, x (cm)')
plt.title('Mass Spring Damper Experiment, Condition a) Response x(t)')
plt.legend()
plt.grid(True)
plt.show()

# 3. Calculate Frequency and Period of Oscillation for the First Experiment
peaks1, _ = find_peaks(position1)  # Identify peaks in the position data
peak_times1 = time1[peaks1]  # Get the time values at each peak

# Calculate the differences between successive peaks to get periods
periods1 = peak_times1.diff().dropna()  # Drop any NaN from the first diff
average_period1 = periods1.mean()  # Average of the periods
frequency1 = 1 / average_period1  # Frequency is the inverse of period

print("Experiment 1 - Condition a)")
print(f"Average Period of Oscillation: {average_period1:.2f} seconds")
print(f"Frequency of Oscillation: {frequency1:.2f} Hz")

# 4. Import the Data for the Second Experiment
data2 = pd.read_excel('/Users/ayooluwakolawole/Desktop/Dynamics Coursework/ExperimentalData_Dynamics.xlsx', sheet_name='Exp. 1.2 (with sliding block)')
time2 = data2['Time - Plot 0']
position2 = data2['Pulley Movement (cm) - Plot 0']

# 5. Plot the Oscillation Data for the Second Experiment
plt.figure(figsize=(10, 6))
plt.plot(time2, position2, label='Condition b) Response x(t)', color='orange')
plt.xlabel('Time, t (s)')
plt.ylabel('Pulley Movement, x (cm)')
plt.title('Mass Spring Damper Experiment, Condition b) Response x(t)')
plt.legend()
plt.grid(True)
plt.show()

# 6. Calculate Frequency and Period of Oscillation for the Second Experiment
peaks2, _ = find_peaks(position2)  # Identify peaks in the position data
peak_times2 = time2[peaks2]  # Get the time values at each peak

# Calculate the differences between successive peaks to get periods
periods2 = peak_times2.diff().dropna()  # Drop any NaN from the first diff
average_period2 = periods2.mean()  # Average of the periods
frequency2 = 1 / average_period2  # Frequency is the inverse of period

print("\nExperiment 2 - Condition b)")
print(f"Average Period of Oscillation: {average_period2:.2f} seconds")
print(f"Frequency of Oscillation: {frequency2:.2f} Hz")
