# Q2.4 – Damped Forced Oscillations Analysis (Procedure 3 Only)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# === Constants from Q2.1 ===
M = 118.4 / 1000       # kg
R = 4.76 / 100         # m
I = 0.5 * M * R**2     # kg·m^2
k_eq = 0.00259         # N·m/rad
b_theory = 9.68e-5     # N·m·s/rad (given)
omega_n_theory = np.sqrt(k_eq / I)           # rad/s
f_n_theory = omega_n_theory / (2 * np.pi)    # Hz
zeta_theory = b_theory / (2 * np.sqrt(k_eq * I))

# === Load Procedure 3 data ===
file_path = '/Users/ayooluwakolawole/Desktop/Dynamics Coursework/ExperimentalData_Dynamics.xlsx'
data = pd.read_excel(file_path, sheet_name='Exp. 2 Procedure 3')
time = data['Time (s)'].to_numpy()
theta = data['Disk Angle (rad)'].to_numpy()

# === Detect peaks ===
peaks, _ = find_peaks(theta, prominence=0.01)
peak_times = time[peaks]
peak_amplitudes = np.abs(theta[peaks])

# === Calculate period and damped frequency ===
periods = np.diff(peak_times)
T_exp = periods.mean()
f_d_exp = 1 / T_exp

# === Calculate logarithmic decrement, damping ratio, and damping coefficient ===
log_decrements = np.log(peak_amplitudes[:-1] / peak_amplitudes[1:])
delta = np.mean(log_decrements)
zeta_exp = delta / np.sqrt((2 * np.pi)**2 + delta**2)
b_exp = 2 * zeta_exp * np.sqrt(k_eq * I)

# === Plot displacement–time ===
plt.figure(figsize=(10, 6))
plt.plot(time, theta, label=r'$\theta(t)$')
# plt.plot(peak_times, theta[peaks], 'ro', label='Detected peaks')
plt.xlabel('Time, $t$ (s)')
plt.ylabel(r'Angular displacement, $\theta$ (rad)')
plt.title('Procedure 3: Damped Forced Oscillations')
plt.grid(True)
plt.legend()
plt.show()

# === Print results ===
print("=== Q2.4: Damped Forced Oscillations (Procedure 3) ===")
print(f"Average Period, T_exp: {T_exp:.3f} s")
print(f"Damped Natural Frequency, f_d_exp: {f_d_exp:.3f} Hz")
print(f"Logarithmic Decrement, δ: {delta:.4f}")
print(f"Damping Ratio, ζ_exp: {zeta_exp:.4f}")
print(f"Damping Coefficient, b_exp: {b_exp:.6e} N·m·s/rad")
print("--- Theoretical values ---")
print(f"f_n (theory): {f_n_theory:.3f} Hz")
print(f"ω_n (theory): {omega_n_theory:.3f} rad/s")
print(f"ζ (theory): {zeta_theory:.4f}")
print(f"b (theory): {b_theory:.6e} N·m·s/rad")
