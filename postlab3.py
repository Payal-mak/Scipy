import numpy as np
import matplotlib.pyplot as plt

# (c) Generate a 5 Hz sine wave signal and shift it in time by 0.1 seconds.
fs_c = 1000  # Sampling frequency
t_c = np.linspace(0, 1, fs_c, endpoint=False)  # Time vector
f1_c = 5  # Frequency of the sine wave (5 Hz)

# Generate the Original Sine Wave
sine_wave_5Hz_c = np.sin(2 * np.pi * f1_c * t_c)

# Generate the Shifted Sine Wave
shift_time_c = 0.1  # Time shift (0.1 seconds)
sine_wave_shifted_c = np.sin(2 * np.pi * f1_c * (t_c - shift_time_c))

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t_c, sine_wave_5Hz_c, label="Original 5 Hz Sine Wave", color='r')
plt.plot(t_c, sine_wave_shifted_c, label="Shifted 5 Hz Sine Wave (0.1 s)", color='m')
plt.title("Original and Time-Shifted 5 Hz Sine Wave - 1000 Hz Sampling for 1 second", fontsize=14)
plt.xlabel("Time [s]", fontsize=12)
plt.ylabel("Amplitude", fontsize=12)
plt.legend(loc="upper right")
plt.grid(True)
plt.show()
