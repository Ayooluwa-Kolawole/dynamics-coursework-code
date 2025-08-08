import numpy as np
import matplotlib.pyplot as plt

# Given parameters
x_0 = 0.05 * 100  # initial displacement in centimeters
m = 0.15  # mass in kg
k = 17  # spring constant in N/m
T_d = 0.59037  # damped period in seconds

# Natural frequency
omega_n = np.sqrt(k / m)

# Time array
t = np.linspace(0, 10, 1000)  # time from 0 to 10 seconds

# Displacement as a function of time for undamped case, converted to centimeters
x_t = x_0 * np.cos(omega_n * t)

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(t, x_t, label='Displacement $x(t)$')
plt.title('Ideal Mass-Spring System, Condition a) Response')
plt.xlabel('Time, t (s)')
plt.ylabel('Displacement, x (cm)')
plt.grid()

# Move the legend out of the way
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.show()
