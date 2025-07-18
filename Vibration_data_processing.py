import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq

# --- Load CSV ---
df = pd.read_csv('vibration_data_normal_moter.csv')

# Convert timestamp to sample number (assuming fixed interval)
df['Sample'] = range(len(df))

# --- Plot Vibration Waveform ---
plt.figure(figsize=(12, 4))
plt.plot(df['Sample'], df['Vibration'], marker='o', linestyle='-', label='Vibration')
plt.title("Vibration Over Time")
plt.xlabel("Sample Number")
plt.ylabel("Vibration Magnitude (g)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# --- Calculate Statistics ---
mean_vib = df['Vibration'].mean()
std_vib = df['Vibration'].std()
max_vib = df['Vibration'].max()
min_vib = df['Vibration'].min()
rms_vib = np.sqrt(np.mean(df['Vibration'] ** 2))

print("\n--- Vibration Statistics ---")
print(f"Mean Vibration      : {mean_vib:.4f} g")
print(f"Standard Deviation  : {std_vib:.4f}")
print(f"Max Vibration       : {max_vib:.4f} g")
print(f"Min Vibration       : {min_vib:.4f} g")
print(f"RMS Vibration       : {rms_vib:.4f} g")

# --- Frequency Analysis (FFT) ---
# Parameters
sampling_rate = 50  # samples per second (if delay=20ms in Arduino)

# FFT needs even spacing
vibration_values = df['Vibration'].values
N = len(vibration_values)
yf = fft(vibration_values)
xf = fftfreq(N, 1 / sampling_rate)

# Plot only positive frequencies
plt.figure(figsize=(10, 4))
plt.plot(xf[:N//2], np.abs(yf[:N//2]), color='purple')
plt.title("Frequency Spectrum of Vibration (FFT)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()

# --- Optional: Check for Abnormal Vibration ---
vib_threshold = 1.8  # Change this based on your testing
abnormal_count = (df['Vibration'] > vib_threshold).sum()

print(f"\nSamples with Vibration > {vib_threshold}g: {abnormal_count}/{N}")
if abnormal_count > N * 0.2:
    print("⚠️ High vibration detected – possible imbalance or fault.")
else:
    print("✅ Vibration levels appear normal.")
