import numpy as np
import matplotlib.pyplot as plt
import math
import time
from quantiphy import Quantity as q


def Qfunct(x):
    y = float(
        np.multiply(0.5, math.erfc(np.divide(x, np.sqrt(2)))))  # erfc() is used to calculate the Gauss Error Function
    return y


start = time.time()

Sampling_Rate = [1, 0.1]  # Sampling Rate for Simulation

SNRindB2 = np.arange(0, 8, 0.1)  # SNR distributed from 0 to 8 in increments of 0.1 to calculate Theoretical BER
theo_p_ber = np.zeros(len(SNRindB2))  # Error Probability Obtained Theoretically

N = [1000, 10000, 100000]  # Different No.of bits to realise the its effect on SNR

E = float(2)  # Signal Energy per bit

for s in range(len(Sampling_Rate)):

    SNRindB1 = np.arange(0, 8, Sampling_Rate[
        s])  # SNR distributed from 0 to 8 in increments of Sampling Rate to calculate Simulation BER
    sim_p_ber = np.zeros(len(SNRindB1))  # Error Probability Obtained through Simulation

    for n in range(len(N)):
        dsource = np.zeros(N[n])

        # Generation of Binary Data Source.

        for k in range(len(SNRindB1)):
            SNR = np.exp(SNRindB1[k] * np.log(10) / 10)
            sigma = (np.sqrt(np.divide(E, SNR)))  # Extracting the Standard Deviation

            # Detection and Probability of Error Calculation

            for i in range(N[n]):
                temp = np.random.rand()  # Uniform Random Variable distributed over (0,1)
                if (temp < 0.5):
                    dsource[i] = (0)
                else:
                    dsource[i] = (1)

            numoferr = 0  # Number of Errors i.e., Error Counter

            for i in range(N[n]):
                if (dsource[i] == 0):
                    y = (-np.sqrt(E) + np.random.normal(0, sigma))  # random.normal(): Normal Gaussian Distribution
                else:
                    y = (np.sqrt(E) + np.random.normal(0, sigma))

                    # Detector Implementation
                if (y < 0):
                    decision = 0
                else:
                    decision = 1
                if (decision != dsource[i]):
                    numoferr += 1
                sim_p_ber[k] = numoferr / N[n]

        # Error Calculation using Error Function
        for i in range(len(SNRindB2)):
            SNR = np.exp(SNRindB2[i] * np.log(10) / 10)
            theo_p_ber[i] = Qfunct(np.sqrt(SNR))

        plt.figure(n + 1 + (len(N)) * s)
        plt.title('B-PAM System Sampling at ' + str(int(1 / Sampling_Rate[s])) + ' samples/sec with N:' + str(N[n]))
        plt.ylabel('Error Probability')
        plt.xlabel('SNR(dB)')
        plt.semilogy(SNRindB2, theo_p_ber, label='Theoretical')
        plt.semilogy(SNRindB1, sim_p_ber, 'o', label='Simulation')
        plt.legend()
        plt.grid()
        plt.show()

end = time.time()

execution_time = end - start
print('Execution Time', q(execution_time, 's'))
