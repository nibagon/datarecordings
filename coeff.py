import scipy.signal as sig
import numpy as np
import matplotlib.pylab as plt

# Sampling rate
fs = 250
cf = np.arange(0, 126, 1) / fs * 2

coeff = sig.firwin(249, [cf[2], cf[45], cf[55]], window='hamming', pass_zero=False)
np.savetxt('coeff.dat', coeff)