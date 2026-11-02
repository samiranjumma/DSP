
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000)

for phase in [0, np.pi/2, np.pi]:
    x = np.sin(2 * np.pi * 5 * t + phase)
    plt.plot(t, x, label=f"Phase = {phase:.2f}")

plt.title("Phase Variation")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()
