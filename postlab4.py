import numpy as np
import matplotlib.pyplot as plt

# (d) Generate a 10 Hz sine wave and scale its amplitude by a factor of 3.
fs_d = 1000  # Sampling frequency
t_d = np.linspace(0, 1, fs_d, endpoint=False)  # Time vector
f2_d = 10  # Frequency of the sine wave (10 Hz)

# Generate the Original Sine Wave
sine_wave_10Hz_d = np.sin(2 * np.pi * f2_d * t_d)

# Scale the Sine Wave
sine_wave_scaled_d = 3 * sine_wave_10Hz_d  # Scale by a factor of 3

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t_d, sine_wave_10Hz_d, label="Original 10 Hz Sine Wave", color='c')
plt.plot(t_d, sine_wave_scaled_d, label="Scaled 10 Hz Sine Wave (Amplitude x 3)", color='hotpink')
plt.title("Original and Scaled 10 Hz Sine Wave - 1000 Hz Sampling for 1 second", fontsize=14)
plt.xlabel("Time [s]", fontsize=12)
plt.ylabel("Amplitude", fontsize=12)
plt.legend(loc="upper right")
plt.grid(True)
plt.show()
