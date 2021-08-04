import numpy as np
import math
import matplotlib.pyplot as plt
N = 10000
def Qfunct(x):
    y = float(np.multiply(0.5, math.erfc(np.divide(x, np.sqrt(2))))) # erfc() is used to calculate the Gauss Error Function
    return y
def Binary_Signal(N):
    signal = []
    for i in range(int(N / 10)):
        temp = np.random.randint(0, 2)
        for j in range(0, 10):
            signal.append(temp)
    return list(signal)
def Precoding_Duobinary(b):
    d = np.zeros(len(b))
    for i in range(len(b)):
         if i == 0:
            if b[i] == 1:
                d[i] = int(0)
            else:
                d[i] = int(1)
         else:
                d[i] = int(b[i]) ^ int(d[i - 1])
    return list(d)
def Level_Shifter(d):
    a = np.zeros(len(d))
    for i in range(len(a)):
        if d[i] == 1:
            a[i] = int(1)
        else:
            a[i] = int(-1)
    return list(a)
def Receiver_Signal(a):
    c = np.zeros(len(a))
    for i in range(len(c)):
        if i == 0:
         c[i] = int(a[i] + 1)
        else:
            c[i] = int(a[i] + a[i - 1])
    return list(c)
def Detector_Without_Noise(c):
    B = np.zeros(len(c))
    for i in range(len(B)):
        if np.abs(c[i]) > 1:
            B[i] = int(0)
        elif np.abs(c[i]) < 1:
                B[i] = int(1)
    return list(B)
def Detector_With_Noise(sample):
    B = np.zeros(len(c))
    for i in range(len(B)):
        if np.abs(sample[i]) > 1:
            B[i] = int(0)
        elif np.abs(sample[i]) < 1:
            B[i] = int(1)
    return list(B)
binary = Binary_Signal(N)
print('Binary Signal',binary[:20])
d = Precoding_Duobinary(binary)
print('Precoding Duobinary',d[:20])
a = Level_Shifter(d)
print('Level Shifter',a[:20])
c = Receiver_Signal(a)
print('Receiver_Signal',c[:20])
B1 = Detector_Without_Noise(c)
N_o = N
mu = 0
sigma = [np.sqrt(0.1), np.sqrt(0.5), np.sqrt(1)]
r = [np.random.normal(mu, sigma[i], N_o) for i in range(len(sigma))]
y1 = c + r[0]
y2 = c + r[1]
y3 = c + r[2]
B2 = Detector_With_Noise(y1)
B3 = Detector_With_Noise(y2)
B4 = Detector_With_Noise(y3)
yk = [B1, B2, B3, B4]
Result = []
for i in range(len(yk)):
    if i == 0:
     Result.append(B1)
    else:
        Result.append(yk[i])
print(Result[0][:20])
print(Result[1][:20])
print(Result[2][:20])
print(Result[3][:20])
count = []
for i in range(len(Result)):
    numoferr = 0
    for j in range(len(binary)):
        if int(binary[j]) ^ int(Result[i][j]) != 0:
            numoferr += 1
    count.append(numoferr)
print(count)
sim_ber = [(count[i] / N) for i in range(len(count))]
print(sim_ber)