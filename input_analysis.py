import numpy as np
import pylab as pl
import scipy as sp
from scipy import signal
import matplotlib.pyplot as plt
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
    fs= 250
    T= 1 / fs

    #Filtering:
    #50 Hertz stopband:
    low = 48 / (fs*2)
    high = 52 / (fs*2)
    i, u = signal.butter(2, [low, high], btype='bandstop')

    ecg50=signal.lfilter(i, u, ECG)
    emg50=signal.lfilter(i, u, EMG)

    #100 Hertz stopband:
    low1 = 98 / (fs*2)
    high1 = 102 / (fs*2)
    b, a = signal.butter(2, [low1, high1], btype='bandstop')

    ecg100=signal.lfilter(b, a, ecg50)
    emg100=signal.lfilter(b, a, emg50)

    #Highpass ecg:
    h, f = signal.butter(2, 0.5/(fs*2), 'hp')

    ecgf=signal.lfilter(h, f, ecg100)

    #Highpass emg:
    e, m = signal.butter(4, 10/(fs*2), 'hp')

    emgf=signal.lfilter(e, m, emg100)

    #plot clean signal
    pl.figure(3)
    pl.plot(time,ecgf)
    pl.title('ECG after filtering')
    pl.xlabel('time/sec')

    pl.figure(4)
    pl.plot(time,emgf)
    pl.title('EMG after filtering')
    pl.xlabel('time/sec')


    #Correlations:
    corr = signal.correlate(emgf, ecgf, mode='same') / len(ecgf)
    pl.figure(5)
    pl.plot(corr)
    pl.title('cross corrrelation clean ECG and EMG')
    
    pl.show()

plot_in('data/data2.21/bicep0.dat')