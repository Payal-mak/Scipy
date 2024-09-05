import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 500  # Sampling frequency (Hz)
duration = 2  # Duration of the signal (seconds)
t = np.linspace(0, duration, int(fs * duration))  # Time array

# Generate the sine wave (5 Hz) and cosine wave (10 Hz)
f_sine = 5
f_cosine = 10

sine_wave = np.sin(2 * np.pi * f_sine * t)
cosine_wave = np.cos(2 * np.pi * f_cosine * t)

# Multiply the signals element-wise
composite_signal = sine_wave * cosine_wave

# Plot the individual waves and the composite signal
plt.figure(figsize=(10, 6))

# Sine wave
plt.subplot(3, 1, 1)
plt.plot(t, sine_wave, label='5 Hz Sine Wave')
plt.title('Individual Sine and Cosine Waves')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()

# Cosine wave
plt.subplot(3, 1, 2)
plt.plot(t, cosine_wave, label='10 Hz Cosine Wave', color='orange')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()

# Composite signal
plt.subplot(3, 1, 3)
plt.plot(t, composite_signal, label='Composite Signal', color='cyan')
plt.title('Element-Wise Multiplication Result')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.show()
