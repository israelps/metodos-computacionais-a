import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft


def dirac_delta(r):
    return np.array([i if i == 0 else 0 for i in r])

N = 1000
T = 1 / 800
f = N*T
x = np.linspace(-f, f, N)

w = 2*np.pi

y = np.cos(w * x)

yt = fft(y)
f = 1/(2*T)
xt = np.linspace(-f, f , N/2)

fig, ax = plt.subplots(2, 1)
ax[0].plot(x,y)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Amplitude')
ax[1].plot(xt,2.0/N * yt[:N//2],'r') # plotting the spectrum
ax[1].set_xlabel(' w ')
ax[1].set_ylabel('|Y(w)|')
plt.show()
