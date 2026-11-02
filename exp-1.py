
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000)

# x(t)=A\sin(2 * pi * ft+ theta)
for A in [1, 2, 3]:
    x = A * np.sin(2 * np.pi * 5 * t)
    plt.plot(t, x, label=f"A = {A}")

plt.title("Amplitude Variation")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()
