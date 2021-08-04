import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd


# GRAPH PLOT FUNCTION
def plot(x, y, title, x_name, y_name, color):
    plt.plot(x, y, color)
    plt.title(title)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.grid()
    plt.show()


# SAMPLING GRAPH FUNCTION
def stem(x, y, title, x_name, y_name, color):
    plt.stem(x, y, color, use_line_collection=True)
    plt.title(title)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.grid()
    plt.show()


# FINDING THE RANGE IN Q TABLE
def find_nearest(arr, x):
    k = 2
    left = 0
    right = len(arr) - 1

    while right - left >= k:
        if abs(arr[left] - x) > abs(arr[right] - x):
            left = left + 1
        else:
            right = right - 1

    return arr[left:left + k]


# QUANTIZATION FUNCTION
def Quantization(sampled, qtable):
    quantized = []
    for i in range(len(sampled)):
        arr1 = find_nearest(qtable, sampled[i])
        quantized.append(sum(arr1) / 2)
    return quantized


def main(Fs):
    print('FS = ', Fs)
    print("")
    # PARAMETERS
    f1 = 500
    f2 = 1500
    f3 = 750
    sample = 100
    # INDIVIDUAL SIGNAL GENERATION
    x = np.arange(0, sample, 0.01)
    y1 = np.sin(2 * np.pi * f1 * x / Fs)
    y2 = 2 * np.sin(2 * np.pi * f2 * x / Fs)
    y3 = 3 * np.sin(2 * np.pi * f3 * x / Fs)
    y = y1 + y2 + y3
    plt.figure(1)
    plot(x, y1, 'SIGNAL 1', 'TIME(t)', 'AMPLITUDE', 'green')
    plt.figure(2)
    plot(x, y2, 'SIGNAL 2', 'TIME(t)', 'AMPLITUDE', 'green')
    plt.figure(3)
    plot(x, y3, 'SIGNAL 3', 'TIME(t)', 'AMPLITUDE', 'green')
    plt.figure(4)
    plot(x, y, 'COMPOSITE SIGNAL ', 'TIME(t)', 'AMPLITUDE', 'red')
    # COMPOSITE SIGNAL GENERATION
    x1 = np.arange(0, sample + 1, 1)
    y11 = np.sin(2 * np.pi * f1 * x1 / Fs)
    y12 = 2 * np.sin(2 * np.pi * f2 * x1 / Fs)
    y13 = 3 * np.sin(2 * np.pi * f3 * x1 / Fs)
    ys = y11 + y12 + y13
    plt.figure(5)
    stem(x1, ys, 'SAMPLED SIGNAL', 'TIME(n)', 'AMPLITUDE', 'red')
    # QUANTIZATION LEVEL
    qlev = [64, 128, 256]
    for i in range(0, 3):
        Qlevel = qlev[i]
        print("Quantization Level :", Qlevel)
        print("")
        ysmin = min(ys)
        ysmax = max(ys)
        # Q-Table
        Q = round((abs(ysmin) + abs(ysmax)) / Qlevel, 2)
        minval = 0
        maxval = 0
        s = 0
        while True:
            if s == 0:
                minval = minval - Q
                if minval <= ysmin:
                    s = 1
            if s == 1:
                maxval = maxval + Q
                if maxval >= ysmax:
                    break
        minvalue = round(minval, 3)
        maxvalue = round(maxval, 3)
        qtable = np.arange(minvalue, maxvalue, Q)
        qtable = np.round(qtable, 2)
        print(qtable)
        print(Q)
        print(ysmin, ysmax)
        # QUANTIZED ARRAY GENERATION
        Quantized = Quantization(ys, qtable)
        qerror = ys - Quantized
        qerrorsq = qerror ** 2
        print((10 * math.log(((max(Quantized) * 2) / 2) / max(ys) * 2, 10)) + (6 * math.log(Qlevel, 2)) + 4.8)
    plt.figure(6)
    plot(x1, Quantized, 'QUANTIZED SIGNAL', 'TIME(n)', 'AMPLITUDE', 'orange')
    plt.plot(x1, ys, color='red')
    plt.legend(["Sampled Signal", "Quantized Signal"])
    plt.figure(7)
    plot(x1, qerrorsq, 'ERROR', 'TIME(n)', 'AMPLITUDE', 'purple')
    plt.show()
    print("")
    print("")


main(16000)