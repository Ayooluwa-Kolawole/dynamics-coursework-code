#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 17:00:32 2024

@author: ayooluwakolawole
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import numpy as np
# 1. Import the Data for Procedure 1
## 1. Import the Data for Procedure 1
data1 = pd.read_excel('/Users/ayooluwakolawole/Desktop/Dynamics Coursework/ExperimentalData_Dynamics.xlsx', sheet_name='Exp. 2 Procedure 1')
time1 = data1['Time (s)']
angle1 = data1['Disk Angle (rad)']

## 2. Plot the Angular Displacement for Procedure 1
plt.figure(figsize=(10, 6))
plt.plot(time1, angle1, label=r"Angular Displacement, $\theta$(t)")
plt.xlabel('Time, t (s)')
plt.ylabel(r"Angular Displacement, $\theta$ (rad)")
plt.title('Procedure 1: Undamped Free Oscillations')
plt.legend()
plt.grid(True)
plt.show()

## 3. Calculate Frequency and Period of Oscillation for the First Experiment
peaks1, _ = find_peaks(angle1)  # Identify peaks in the position data
peak_times1 = time1[peaks1]  # Get the time values at each peak

# Calculate the differences between successive peaks to get periods
periods1 = peak_times1.diff().dropna()  # Drop any NaN from the first diff
average_period1 = periods1.mean()  # Average of the periods
frequency1 = 1 / average_period1  # Frequency is the inverse of period

print("Procedure 1: Undamped Free Oscillations")
print(f"Average Period of Oscillation: {average_period1:.2f} seconds")
print(f"Experimental Natural Frequency: {frequency1:.2f} Hz")
print()
