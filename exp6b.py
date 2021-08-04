import numpy as np
import matplotlib.pyplot as plt
from scipy import special
import math


# Generation of random binary signal function
def binary(symbol, samples):
    rand_n = np.random.rand(symbol)
    rand_n[np.where(rand_n >= 0.5)] = 1
    rand_n[np.where(rand_n < 0.5)] = 0

    sig = np.zeros(int(symbol * samples))

    # generate symbols
    id_1 = np.where(rand_n == 1)

    for i in id_1[0]:
        temp = int(i * samples)
        sig[temp:temp + samples] = 1

    return sig


Fs = 10000  # Sampling frequency
Td = 0.1  # BIT DURATION
T = 1  # simulation time (sec)
t = np.arange(0, T, 1 / Fs)
samples = int(Td * Fs)  # samples in one bit
sym = int(Fs / samples)
sig = binary(sym, samples)

sigmap = np.zeros(len(sig))
sigmap[np.where(sig == 1)] = -1
sigmap[np.where(sig == 0)] = 1
plt.subplot(2,2,1)
plt.title('binary sequence')
plt.xlabel('time(s)')
plt.ylabel('AMPLITUDE')
plt.plot(t, sig)
plt.grid()
plt.show()
plt.subplot(2,2,2)
plt.title('mapped sequence')
plt.xlabel('time(s)')
plt.ylabel('AMPLITUDE')
plt.plot(t, sigmap)
plt.grid()
plt.show()


# Q-function using erfc function
def qFunc(x):
    q = 0.5 * special.erfc(x / np.sqrt(2))
    return q


SNRindB1 = np.arange(0, 10, 1)  # simulation SNR in dB
SNRindB2 = np.arange(0, 10, 0.1)  # theoritical SNR in dB
SNR_B1 = np.zeros(len(SNRindB1))  # storing linear SNR value of SNRindB1
SNR_B2 = np.zeros(len(SNRindB2))  # storing linear SNR value of SNRindB2
sigma = np.zeros(len(SNRindB1))  # store Variance values

# defining probability of error arrays
sim_err_prb = np.zeros(len(SNRindB1))
the_err_prb = np.zeros(len(SNRindB2))

N = 10000
# probability of error calculation using simulation
for k in range(len(SNRindB1)):
    E = 1  # Bit energy (Considering it to be 1)
    snr_in_linear = 1 * np.power(10, (SNRindB1[k] / 10))  # converting dB to linear scale
    SNR_B1[k] = snr_in_linear
    sigma[k] = np.sqrt(E / SNR_B1[k])  # calculating the variance
    # SNR = E/Var => Var (sigma^2) = E/SNR
    dsource = sigmap

    # dsource is now transmitted

    numoferr = 0  # error counter

    # Adding noise to transmitted

    # DEMODULATOR
    for i in range(N):
        if dsource[i] == 1:
            # random.normal generates a random no. from gaussian distribution
            # noise has mean zero and variance No/2
            y = np.sqrt(E) + np.random.normal(0, sigma[k])
        else:
            y = (-1)*np.sqrt(E) + np.random.normal(0, sigma[k])

        # DETECTOR
        if y < 0:
            decision = 1
        else:
            decision = 0
        if decision != sig[i]:
            numoferr += 1

        sim_err_prb[k] = numoferr / N
print(sim_err_prb)
# Error function calculation using Q-func
# this is theoretical calculation
for i in range(len(SNRindB2)):
    snr_in_linear = 1 * np.power(10, (SNRindB2[i] / 10))  # converting dB to linear scale
    SNR_B2[k] = snr_in_linear
    the_err_prb[i] = qFunc(math.sqrt(snr_in_linear))  # SNR = E/Var

# to show the plot and labeling it
plt.figure()
plt.title("B-PAM System Simulation for 10,000 bits", fontsize=28)
plt.ylabel("Error Probability", fontsize=20)
plt.xlabel("SNR (dB)", fontsize=20)
plt.semilogy(SNRindB2, the_err_prb, label='Theoretical')
plt.semilogy(SNRindB1, sim_err_prb, 'o', label='Simulation', color='red')
plt.legend(prop={"size": 20})
plt.grid()
plt.show()