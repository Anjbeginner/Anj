
import numpy as np
import matplotlib.pyplot as plt
from scipy import special
import math


# Q-function using erf function
def qFunc(x):
    q = 0.5-(0.5 * special.erf(x / np.sqrt(2)))
    return q


SNRindB1 = np.arange(0, 7)  # simulation SNR in dB
SNRindB2 = np.arange(0, 7)  # theoritical SNR in dB
SNR_B1 = np.zeros(len(SNRindB1))  # storing linear SNR value of SNRindB1
SNR_B2 = np.zeros(len(SNRindB2))  # storing linear SNR value of SNRindB2
sigma = np.zeros(len(SNRindB1))  # store Variance values

# defining probability of error arrays
sim_err_prb = np.zeros(len(SNRindB1))
the_err_prb = np.zeros(len(SNRindB2))

N = 10000 # no. of bits transmitted

# probability of error calculation using simulation
for k in range(len(SNRindB1)):
    E = 2# Bit energy
    snr_in_linear = np.exp((SNRindB1[k]) * np.log(10 ^ 22) / 10)  # converting dB to linear scale
    SNR_B1[k] = snr_in_linear
    sigma[k] = np.sqrt(E / SNR_B1[k])  # calculating the variance

    # Generation of the binary data source
    # TRANSMITTER
    dsource = np.zeros(N)
    for i in range(N):
        temp = np.random.rand()  # generates a random number between 0 and 1
        if temp < 0.5:
            dsource[i] = 0
        else:
            dsource[i] = 1

    # dsource is now transmitted

    numoferr = 0  # error counter

    # Adding noise to transmitted bits

    # DEMODULATOR
    for i in range(N):
        if dsource[i] == 0:
            # random.normal generates a random no. from gaussian distribution
            # noise has mean zero and variance No/2
            y = (-1) * np.sqrt(E) + np.random.normal(0, sigma[k])
        else:
            y = np.sqrt(E) + np.random.normal(0, sigma[k])

        # DETECTOR
        if y < 0:
            decision = 0
        else:
            decision = 1
        if decision != dsource[i]:
            numoferr += 1

        sim_err_prb[k] = numoferr / N

# Error function calculation using Q-func
# this is theoretical calculation
for i in range(len(SNRindB2)):
    snr_in_linear = np.exp((SNRindB2[i]) * np.log(10 ^ 22) / 10)  # converting dB to linear scale
    SNR_B2[k] = snr_in_linear
    the_err_prb[i] = qFunc(math.sqrt((snr_in_linear)))

# to show the plot and labeling it
plt.figure()
plt.title("B-PAM System Simulation", fontsize=28)
plt.ylabel("Error Probability", fontsize=20)
plt.xlabel("SNR (dB)", fontsize=20)
plt.semilogy(SNRindB2, the_err_prb, label='Theoretical')
plt.semilogy(SNRindB1, sim_err_prb, 'o', label='Simulation', color='red')
plt.legend(prop={"size": 10})
plt.grid()
plt.show()
