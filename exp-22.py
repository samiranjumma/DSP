
import numpy as np
import matplotlib.pyplot as plt

fs = 15000

t = np.linspace(0, 0.005, 1000)
ts = np.arange(0, 0.005, 1/fs)

def signal(t):
    return (3*np.cos(2000*np.pi*t)
            + 5*np.sin(6000*np.pi*t)
            + 10*np.cos(12000*np.pi*t))

plt.plot(t, signal(t), label="Original Signal")
plt.stem(ts, signal(ts), linefmt="r-", markerfmt="ro",
         basefmt=" ", label="Sampled Signal")

plt.title("Sampling at 15000 Hz")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()

print("Maximum Frequency = 6000 Hz")
print("Nyquist Rate = 12000 Hz")
print("Sampling Frequency = 15000 Hz")
