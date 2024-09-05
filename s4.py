import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
# Parameters for continuous and discrete signals
fs = 20  # Sampling frequency for discrete-time signal
t_continuous = np.linspace(0, 1, 1000)  # Time array for continuous signals
t_discrete = np.arange(0, 1, 1/fs)  # Discrete time array
f = 5  # Frequency of the signal

# Generate a continuous-time sine wave
continuous_signal = np.sin(2 * np.pi * f * t_continuous)

# Generate a discrete-time sine wave (sampled)
discrete_time_signal = np.sin(2 * np.pi * f * t_discrete)

# Discretize the amplitude (quantization) for the continuous-time signal
num_levels = 4  # Number of quantization levels
discrete_amplitude_signal = np.round(continuous_signal * (num_levels / 2)) / (num_levels / 2)

# Discretize both time and amplitude
discrete_time_amplitude_signal = np.round(discrete_time_signal * (num_levels / 2)) / (num_levels / 2)

# Plot the signals
plt.figure(figsize=(12, 10))

# Continuous-Time Signal
plt.subplot(4, 1, 1)
plt.plot(t_continuous, continuous_signal)
plt.title('Continuous-Time Signal (Sine Wave)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# Discrete-Time Signal
plt.subplot(4, 1, 2)
plt.stem(t_discrete, discrete_time_signal, use_line_collection=True)
plt.title('Discrete-Time Signal (Sampled Sine Wave)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# Discrete-Amplitude Signal
plt.subplot(4, 1, 3)
plt.plot(t_continuous, discrete_amplitude_signal, drawstyle='steps-pre')
plt.title('Discrete-Amplitude Signal (Quantized Sine Wave)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# Discrete-Time and Amplitude Signal
plt.subplot(4, 1, 4)
plt.stem(t_discrete, discrete_time_amplitude_signal, use_line_collection=True)
plt.title('Discrete-Time and Amplitude Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()

# Discrete signal operations (delay and advance)
n = np.arange(0, 20)  # Discrete time array (0 to 19)
signal = np.sin(0.2 * np.pi * n)  # Example discrete-time signal (sine wave)

# Delay the signal by 3 samples
delay = 3
delayed_signal = np.zeros_like(signal)
delayed_signal[delay:] = signal[:-delay]

# Advance the signal by 3 samples
advance = 3
advanced_signal = np.zeros_like(signal)
advanced_signal[:-advance] = signal[advance:]

# Plot the original and shifted signals
plt.figure(figsize=(12, 8))

# Original Signal
plt.subplot(3, 1, 1)
plt.stem(n, signal, use_line_collection=True)
plt.title('Original Signal')
plt.xlabel('n (Discrete Time)')
plt.ylabel('Amplitude')

# Delayed Signal
plt.subplot(3, 1, 2)
plt.stem(n, delayed_signal, use_line_collection=True)
plt.title(f'Delayed Signal (by {delay} samples)')
plt.xlabel('n (Discrete Time)')
plt.ylabel('Amplitude')

# Advanced Signal
plt.subplot(3, 1, 3)
plt.stem(n, advanced_signal, use_line_collection=True)
plt.title(f'Advanced Signal (by {advance} samples)')
plt.xlabel('n (Discrete Time)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
