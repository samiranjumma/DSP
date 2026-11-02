
import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
N = len(x)

X = np.zeros(N, dtype=complex)

# Manual DFT
for k in range(N):
    for n in range(N):
        X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)

magnitude = np.abs(X)
phase = np.angle(X)
power = magnitude ** 2

print("DFT:", np.round(X, 2))
print("Magnitude:", np.round(magnitude, 2))
print("Phase:", np.round(phase, 2))
print("Power:", np.round(power, 2))

# Plot results
plt.figure(figsize=(9, 7))

for i, (data, title) in enumerate([
    (magnitude, "Magnitude Spectrum"),
    (phase, "Phase Spectrum"),
    (power, "Power Spectrum")
], 1):
    plt.subplot(3, 1, i)
    plt.stem(range(N), data)
    plt.title(title)
    plt.xlabel("Frequency Bin (k)")
    plt.grid()

plt.tight_layout()
plt.show()
