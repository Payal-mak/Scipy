import numpy as np
import matplotlib.pyplot as plt

# (e) Generate a 5 Hz sine wave and reverse it in time.
fs_e = 1000  # Sampling frequency
t_e = np.linspace(0, 1, fs_e, endpoint=False)  # Time vector
f1_e = 5  # Frequency of the sine wave (5 Hz)

# Generate the Original Sine Wave
sine_wave_5Hz_e = np.sin(2 * np.pi * f1_e * t_e)

# Reverse the Sine Wave
sine_wave_reversed_e = sine_wave_5Hz_e[::-1]  # Time-reversed signal

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t_e, sine_wave_5Hz_e, label="Original 5 Hz Sine Wave", color='k')
plt.plot(t_e, sine_wave_reversed_e, label="Reversed 5 Hz Sine Wave", color='purple')
plt.title("Original and Reversed 5 Hz Sine Wave - 1000 Hz Sampling for 1 second", fontsize=14)
plt.xlabel("Time [s]", fontsize=12)
plt.ylabel("Amplitude", fontsize=12)
plt.legend(loc="upper right")
plt.grid(True)
plt.show()
