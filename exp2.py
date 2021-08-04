import numpy as np
import matplotlib.pyplot as plt

# DM Transmitter
def delta(x, d):
 e = eq = mq = np.zeros(len(x))
 for i in range(len(x)):
    if i == 0:
         e[i] = x[i]
         eq[i] = d * np.sign(e[i])
         mq[i] = eq[i]
    else:
        e[i] = x[i] - mq[i - 1]
        eq[i] = d * np.sign(e[i])
        mq[i] = eq[i] + mq[i - 1]
 return mq
# given values
fm1 = 500
fs1 = 8000
t1 = np.arange(0, 1, 1 / fs1)
x = [(1.5 * (np.sin((2 * np.pi * fm1 / fs1) * t1))) for t1 in range(0, 100)]
# creating own signal
fm2 = 1000
fs2 = 9000
t2 = np.arange(0, 1, 1 / fs2)
x2 = [(3 * (np.cos((2 * np.pi * fm2 / fs2) * t2))) for t2 in range(0, 100)]
d1 = 0.25
d2 = 0.1
X1 = delta(x, d1)
X2 = delta(x, d2)
X3 = delta(x2, d1)
X4 = delta(x2, d2)
plt.figure(1)
plt.title('Quantized sine Signal using Delta Modulation with delta value 0.25')
plt.ylabel('Amplitude')
plt.xlabel('Time')
plt.plot(t1[:100], x[:100])
plt.step(t1[:100], X1[:100])
plt.show()
plt.figure(2)
plt.title('Quantized sine Signal using Delta Modulation with delta value 0.1')
plt.ylabel('Amplitude')
plt.xlabel('Time')
plt.plot(t1[:100], x[:100])
plt.step(t1[:100], X2[:100])
plt.show()
plt.figure(3)
plt.title('Quantized cosine Signal using Delta Modulation with delta value 0.25')
plt.ylabel('Amplitude')
plt.xlabel('Time')
plt.plot(t2[:100], x[:100])
plt.step(t2[:100], X3[:100])
plt.show()
plt.figure(4)
plt.title('Quantized cosine Signal using Delta Modulation with delta value 0.1')
plt.ylabel('Amplitude')
plt.xlabel('Time')
plt.plot(t2[:100], x[:100])
plt.step(t2[:100], X4[:100])
plt.show()
