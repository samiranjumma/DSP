
x = [1, 2, 3]
h = [1, 1, 1]

y = [0] * (len(x) + len(h) - 1)

for i in range(len(x)):
    for j in range(len(h)):
        y[i + j] += x[i] * h[j]
        print(f"y[{i+j}] += {x[i]} * {h[j]}")

print("Final Output:", y)
