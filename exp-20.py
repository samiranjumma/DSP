
import numpy as np
import matplotlib.pyplot as plt

f = 50
t = np.linspace(0, 0.1, 1000)
x = 3 * np.cos(2 * np.pi * f * t)

for fs in [400, 100, 60]:
    ts = np.arange(0, 0.1, 1/fs)
    xs = 3 * np.cos(2 * np.pi * f * ts)

    plt.figure(figsize=(8, 3))
    plt.plot(t, x, label="Original Signal")
    plt.stem(ts, xs, linefmt="r-", markerfmt="ro",
             basefmt=" ", label="Sampled Signal")

    plt.title(f"Sampling at {fs} Hz")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid()
    plt.show()
