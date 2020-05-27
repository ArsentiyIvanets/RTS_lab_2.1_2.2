from Lab_01.lab1 import n, wmax, N
from Lab_02.lab2 import generate_signal, generate_random_values

import matplotlib.pyplot as plt
from math import sin, cos, pi, sqrt
from numpy import fft


def show_graph(g):
    fig, ax = plt.subplots()
    ax.plot(g)
    ax.grid()
    plt.show()
    plt.close(fig)


def counter(N):
    values = {}
    for i in range(N):
        values[i] = (cos(2 * pi / N * i), sin(2 * pi / N * i))

    return values


def DFT(N, x):
    numpy_res = fft.fft(x)
    res = []
    for p in range(N - 1):
        Re = 0
        Im = 0
        for k in range(N - 1):
            Re += x[k] * cos(2 * pi / N * p * k)
            Im += x[k] * sin(2 * pi / N * p * k)
        F = sqrt((Re - numpy_res[p].real) ** 2 + (Im - numpy_res[p].imag) ** 2)
        res.append(F)

    return res


def DFT_t(N, x, values):
    res = []
    for p in range(N - 1):
        Re = 0
        Im = 0
        for k in range(N - 1):
            Re += x[k] * values[p * k % N][0]
            Im += x[k] * values[p * k % N][1]
        F = sqrt(Re ** 2 + Im ** 2)
        res.append(F)

    return res


if __name__ == '__main__':
    Ax, phix = generate_random_values(n)
    x = [generate_signal(n, wmax, t, Ax, phix) for t in range(N)]
    show_graph(x)

    from time import time
    # start = time()
    values = counter(N)
    # for k, v in values.items():
    #     print('{}: {}'.format(k, v))
    res = DFT(N, x)
    show_graph(res)
    # end = time()
    # print('time = %f' % (end - start))


print("Sum of all points signal = ", sum(x))

print("Sum of all points spectrum = ", sum(res))

