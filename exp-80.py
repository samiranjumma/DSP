
import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0, 11)
a = 0.5

x = a ** n
h = a ** n
y = (n + 1) * a ** n

print("n\t x[n]\t h[n]\t y[n]")
for i in n:
    print(f"{i}\t {x[i]:.4f}\t {h[i]:.4f}\t {y[i]:.4f}")

plt.figure(figsize=(9, 7))

for i, (signal, name) in enumerate(
    [(x, "Input x[n]"), (h, "Impulse Response h[n]"),
     (y, "Output y[n]")], 1):

    plt.subplot(3, 1, i)
    plt.stem(n, signal)
    plt.title(name)
    plt.xlabel("n")
    plt.grid()

plt.tight_layout()
plt.show()
