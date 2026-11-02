
import numpy as np
import matplotlib.pyplot as plt

def fft(x):
    N = len(x)

    if N == 1:
        return x

    even = fft(x[::2])
    odd = fft(x[1::2])

    X = np.zeros(N, dtype=complex)

    for k in range(N // 2):
        W = np.exp(-2j * np.pi * k / N)
        X[k] = even[k] + W * odd[k]
        X[k + N//2] = even[k] - W * odd[k]

    return X

x = np.array([1, 2, 3, 4])
X = fft(x)

print("FFT Output:", np.round(X, 2))

plt.stem(range(len(X)), np.abs(X))
plt.title("FFT Magnitude Spectrum")
plt.xlabel("Frequency Bin (k)")
plt.ylabel("Magnitude")
plt.grid()
plt.show()
