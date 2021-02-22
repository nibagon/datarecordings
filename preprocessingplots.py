import numpy as np
import pylab as pl
from scipy.fft import fft, fftfreq
def plot_in(doc):
    data = np.loadtxt(doc)
    time=data[:,0]
    ECG=data[:,1]
    pl.figure(1)
    pl.plot(time,ECG)
    pl.title('ECG')
    pl.xlabel('time/sec')

    pl.figure(2)
    EMG=data[:,2]
    pl.plot(time,EMG)
    pl.title('EMG')
    pl.xlabel('time/sec')

    #Fourier transform:
    samplingFrequency= 250
    T= 1 / samplingFrequency

    N = len(ECG)
    # sample spacing
    yf = fft(ECG)
    xf = fftfreq(N, T)[:N//2]
    pl.figure(3)
    pl.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
    pl.title('ECG fourier transform')
    N = len(EMG)
    yf = fft(EMG)
    xf = fftfreq(N, T)[:N//2]
    pl.figure(4)
    pl.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
    pl.title('EMG fourier transform')
    pl.show()

plot_in('data/data2.21/bicep0.dat')