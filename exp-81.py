
import numpy as np

n = np.arange(11)
x = 0.5 ** n
h = 0.5 ** n

y = np.zeros(11)

for i in range(11):
    for j in range(i + 1):
        y[i] += x[j] * h[i - j]

print("Manual Convolution:")
print(np.round(y, 4))
