import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000  # Sampling frequency (Hz)
duration = 1  # Duration of the signal (seconds)
t = np.linspace(0, duration, int(fs * duration))  # Time array

# Generate sine waves
f1 = 5  # Frequency of the first sine wave (5 Hz)
f2 = 10  # Frequency of the second sine wave (10 Hz)

sine_wave1 = np.sin(2 * np.pi * f1 * t)
sine_wave2 = np.sin(2 * np.pi * f2 * t)

# Add the sine waves together
composite_signal = sine_wave1 + sine_wave2

# Plot the individual sine waves and the composite signal
plt.figure(figsize=(10, 6))

# First sine wave
plt.subplot(3, 1, 1)
plt.plot(t, sine_wave1, label='5 Hz Sine Wave')
plt.title('Individual Sine Waves')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()

# Second sine wave
plt.subplot(3, 1, 2)
plt.plot(t, sine_wave2, label='10 Hz Sine Wave', color='darkgreen')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()

# Composite signal
plt.subplot(3, 1, 3)
plt.plot(t, composite_signal, label='Composite Signal', color='brown')
plt.title('Composite Signal (Sum of Sine Waves)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.show()
