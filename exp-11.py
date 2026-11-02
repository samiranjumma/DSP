
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000)

for f in [2, 5, 10]:
    x = np.sin(2 * np.pi * f * t)
    plt.plot(t, x, label=f"f = {f} Hz")

plt.title("Frequency Variation")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()
