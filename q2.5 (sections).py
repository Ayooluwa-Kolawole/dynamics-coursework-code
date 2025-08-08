import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# === Load data ===
file_path = '/Users/ayooluwakolawole/Desktop/Dynamics Coursework/ExperimentalData_Dynamics.xlsx'
data = pd.read_excel(file_path, sheet_name='Exp. 2 Procedure 3')

time = data['Time (s)'].to_numpy()
disk_vel = data['Disk Angular Velocity (rad/s)'].to_numpy()
driver_vel = data['Driver Angular Velocity (rad/s)'].to_numpy()

# === Function to plot zoomed windows ===
def plot_window(t_start, t_end, title):
    mask = (time >= t_start) & (time <= t_end)
    t_win = time[mask]
    disk_win = disk_vel[mask]
    driver_win = driver_vel[mask]
    
    plt.figure(figsize=(8, 4))
    plt.plot(t_win, disk_win, label="Disk Angular Velocity")
    plt.plot(t_win, driver_win, label="Driver Angular Velocity")
    plt.xlabel("Time (s)")
    plt.ylabel("Angular Velocity (rad/s)")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

# === Define time windows (adjust as needed) ===
plot_window(0, 5, "High Frequency (Start)")
plot_window(280, 285, "Resonance Frequency (Max Disk Amplitude)")
plot_window(420, 425, "Low Frequency (End)")

