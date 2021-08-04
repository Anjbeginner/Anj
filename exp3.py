import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import scipy.integrate as integrate
import scipy.special as special
from mpl_toolkits.mplot3d import Axes3D


def Grahm_Schmidt(matrix, orthogonality_check=False, automatic_check=False, error_tol=1.e-10):
    # matrix is a matrix whose rows are vectors to be turned into an ONbasis
    veclist = list(matrix)
    newbasis = []

    def orth_check(Matrix):

        # This fucntion check for the pairwise orthogonality of the new basis

        list_ = list(Matrix)
        dot_matrix = np.array([[m(item1, item2) for item1 in list_] for item2 in list_])
        if (dot_matrix - np.eye(dot_matrix.shape[0]) < error_tol).all():
            return True
        else:
            error = dot_matrix - np.eye(dot_matrix.shape[0])
            return False, np.max(error), np.min(error)

    def m(a, b):
        return np.matmul(a, b)

    def n(a):
        return np.linalg.norm(a)

    def proj(vector, ind):
        if ind == 0:
            new = vector / n(vector)
        else:
            l_ = np.array([newbasis[k] * m(newbasis[k], vector) for k in range(len(newbasis))])
            projections = np.sum(l_, axis=0)
            NEW = vector - projections
            new = NEW / n(NEW)
            newbasis.append(new)

    [proj(vector, ind) for ind, vector in enumerate(veclist)]
    newbasis_matrix = np.array(newbasis)
    if orthogonality_check and automatic_check == False:
        return orth_check(newbasis_matrix)
    elif automatic_check:
        return orth_check(matrix)
    else:
        return newbasis_matrix


if __name__ == '__main__':
    A = np.array([[2, -1, -1, -1], [-2, 1, 1, 0], [1, -1, 1, -1], [1, -2, -2, 2]])
    print(Grahm_Schmidt(A))


def c_value(s, p_arr, fs):  # Projection of Signal to ON Basis Function
    c_arr = []
    for i in range(len(p_arr)):
        c_arr.append(np.sum(s * p_arr[i]) / fs)
    return c_arr


def E(s):
    return sum(abs(s) ** 2.0) / 10


def d_value(s, c_arr, p_arr, length):  # Orthogonal Function to ON Basis
    d = np.zeros(length)
    for i in range(len(c_arr)):
        d -= c_arr[i] * p_arr[i]
    d += s
    return d


def comparison(a, b):  # To
    flag = 0
    for i in range(len(a)):
        if abs(a[i] - b[i]) > 10 ** (-5):
            flag = 1
            break

    if flag == 0:
        return True
    else:
        return False


def signal_vector(signals, orthogonal, fs):  # Generation of Rectangular Pulses
    result = []
    for i in range(len(signals)):
        l = []
        for j in range(len(orthogonal)):
            l.append(np.sum(signals[i] * orthogonal[j]) / fs)
        result.append(l)
    return result


########################################################################
fs = 10
time = np.arange(0, 2, 1 / fs)
long_time = np.arange(0, 4, 1 / fs)
s1 = np.zeros(len(long_time))
for i in range(len(time // 2)):
    s1[i] = 2.0
for i in range(len(time // 2)):
    s1[i + len(time) // 2] = -1
for i in range(len(time)):
    s1[i + len(long_time) // 2] = -1
s2 = np.zeros(len(long_time))
for i in range(len(time) // 2):
    s2[i] = -2
for i in range(len(time) // 2):
    s2[i + len(time) // 2] = 1
for i in range(len(long_time) // 2):
    s2[i + len(time) // 2] = 1
s3 = np.zeros(len(long_time))
for i in range(len(time) // 2):
    s3[i] = 1
for i in range(len(time)):
    s3[i + len(time) // 2] = -1
for i in range(len(time)):
    s3[i + len(long_time) // 2] = -1
for i in range(len(time) // 2):
    s3[i + len(long_time) // 2] = 1
s4 = np.zeros(len(long_time))
for i in range(len(time) // 2):
    s4[i] = 1
for i in range(len(time)):
    s4[i + len(time) // 2] = -2
for i in range(len(time)):
    s4[i + len(long_time) // 2] = 2
for i in range(len(time) // 2):
    s4[i + len(long_time) // 2] = -2

signals = [s1, s2, s3, s4]
signal_count = 4
#########################################################################
c_array = [0] * signal_count
p_array = [np.zeros(len(long_time))] * signal_count
orthogonal_signals = []
for i in range(signal_count):
    c_array = c_value(signals[i], p_array, fs)
    d = d_value(signals[i], c_array, p_array, len(long_time))
    energy = np.sqrt(E(d))
    p_array[i] = d / energy
    d = np.around(d, 4)
    if comparison(d, np.zeros(len(long_time))):
        continue
    orthogonal_signals.append(p_array[i])

    plt.figure(i + 1)
    plt.title("Input and $\psi$ signal")
    plt.ylabel("Amplitude")
    plt.xlabel("Time")
    plt.plot(long_time, signals[i], label='signal')
    plt.plot(long_time, p_array[i], label="$\psi$")
    plt.legend()
    plt.show()
for i in range(len(orthogonal_signals)):
    plt.figure(signal_count + i + 1)
    plt.title("Orthogonal Signals")
    plt.ylabel("Amplitude")
    plt.xlabel("Time")
    plt.plot(long_time, orthogonal_signals[i], label='signal')
    plt.legend()
    plt.show()
s_vector = signal_vector(signals, orthogonal_signals, fs)
s_vector = np.around(s_vector, 4)
start = [0, 0, 0]
limits = [-3, 3]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(len(s_vector)):
    ax.quiver(start[0], start[1], start[2], s_vector[i][0], s_vector[i][1],
              s_vector[i][2], color='b')
ax.set_xlim(limits)
ax.set_ylim(limits)
ax.set_zlim(limits)
ax.set_xlabel("$\psi_1$")
ax.set_ylabel("$\psi_2$")
ax.set_zlabel("$\psi_3$")
plt.draw()
plt.show()
