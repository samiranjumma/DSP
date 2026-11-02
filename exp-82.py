
import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3]
h = [1, 1, 1]

y = np.convolve(x, h)

print("Convolution Output:", y)

plt.stem(range(len(y)), y)
plt.title("Linear Convolution")
plt.xlabel("n")
plt.ylabel("y[n]")
plt.grid()
plt.show()
