import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft, fftfreq

L, R, C = 1, 6, 5


def H(t):
    return np.exp(-t / 3) - np.exp(-t / 2)


def y(w):
    return 1 / (1j * R * C * w - L * C * w**2 + 1)


def idfft(x):
    N = len(x)
    w0 = np.pi / N
    xi = np.zeros(N)
    for i in range(N):
        xi[i] = 1 / N * sum([x[k] * np.exp(1j * k * w0 * i) for k in range(N)])
    return xi

def dfft(x):
    N = len(x)
    w0 = np.pi / N
    xt = np.zeros(N)
    for i in range(N):
        xt[i] = sum([x[k] * np.exp(-1j * k * w0 * i) for k in range(N)])
    return xt


N = 100
t = np.linspace(0, 10, N)
h = H(t)
ht = fft(h)
n = ht.size
freq = fftfreq(n,d=0.1)


#plt.plot(t, H(t))
plt.plot(t, h)
plt.plot(freq, ht)
plt.grid()
plt.show()
