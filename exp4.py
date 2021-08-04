import np as np
import numpy as np
import matplotlib.pyplot as plt
# module for generating binary sequence randomly
def binary(symbol, sym_len):
    rand_n = np.random.rand(symbol)
    rand_n[np.where(rand_n >= 0.5)] = 1
    rand_n[np.where(rand_n <= 0.5)] = 0
    sig = np.zeros(int(symbol * sym_len))
    id_1 = np.where(rand_n == 1)
    for i in id_1[0]:
         temp = int(i * sym_len)
         sig[temp:temp + sym_len] = 1
    return sig
fs = 100
fc = 10
T = 10
t = np.arange(0, T, 1 / fs)
x = np.sin(2 * np.pi * fc * t)
y = x = np.cos(2 * np.pi * fc * t)
td = 1
samples = int(td * fs)
sym = int(np.floor(np.size(t) / samples))
sig = binary(sym, samples)
plt.figure(1)
plt.xlabel("time(s)")
plt.ylabel("amplitude")
plt.title("random binary signal")
plt.plot(t, sig)
# generating ASK signal
ask = x * sig
plt.figure(2)
plt.xlabel("time(s)")
plt.ylabel("amplitude")
plt.title("ASK signal")
plt.plot(t, ask)
plt.tight_layout()
# generating FSK
f = fc - fc * sig / 2
fsk = np.cos(2 * np.pi * f * t)
plt.figure(3)
plt.xlabel("time(s)")
plt.ylabel("amplitude")
plt.title("FSK signal")
plt.plot(t, fsk)
plt.tight_layout()
psk=np.zeros(len(t))
for i in range(len(sig)):
    if sig[i]==0:
        psk[i]=np.sin(3*np.pi*t[i])
    else:
        psk[i]=np.cos(3*np.pi*t[i])
plt.figure(4)
plt.xlabel("time(s)")
plt.ylabel("amplitude")
plt.title("PSK signal")
plt.plot(t,psk)
plt.tight_layout()
plt.show()

qpsk = sig*np.cos(2*np.pi*fc *t) - (sig*np.sin(2*np.pi*fc *t))
plt.figure(5)
plt.xlabel("time(s)")
plt.ylabel("amplitude")
plt.title("QPSK signal")
plt.plot(t,qpsk)
plt.tight_layout()
plt.show()