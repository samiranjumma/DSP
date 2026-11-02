
import numpy as np
import matplotlib.pyplot as plt

N = 8
fs = 8
n = np.arange(N)
t = n / fs

x = np.sin(2 * np.pi * 2 * t)

X = np.zeros(N, dtype=complex)

for k in range(N):
    for i in range(N):
        X[k] += x[i] * np.exp(-2j * np.pi * k * i / N)

plt.stem(n, np.abs(X))
plt.title("DFT Magnitude Spectrum")
plt.xlabel("Frequency Bin (k)")
plt.ylabel("Magnitude")
plt.grid()
plt.show()

print("Magnitude:", np.round(np.abs(X), 2))
