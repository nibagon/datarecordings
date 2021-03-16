import numpy as np
import pylab as pl
from scipy.fft import fft, fftfreq
# FFT function

def plot_FFT(data,samplingFrequency):
    T= 1 / samplingFrequency

    N = len(data)
    # sample spacing
    yf = fft(data)
    xf = fftfreq(N, T)[:N//2]
    pl.plot(xf, 2.0/N * np.abs(yf[0:N//2]))

samplingFrequency= 250

#OUTPUT
datalms = np.loadtxt('LMSfiltered_ecg.dat')

lmsraw_ecg=datalms[:,5]
lmsin_ecg=datalms[:,4]
lmsout_ecg=datalms[:,1]

lmscanceller=datalms[:,2]
lmsraw_emg=datalms[:,6]
lmsin_emg=datalms[:,3]

lmstime=datalms[:,0]

'''
pl.figure(1)
plot_FFT(lmsraw_ecg,samplingFrequency)
plot_FFT(lmsin_ecg/1000,samplingFrequency)
pl.title('ECG fourier transform')

pl.figure(2)
plot_FFT(lmsraw_emg,samplingFrequency)
plot_FFT(lmsin_emg/1000,samplingFrequency)
pl.title('EMG fourier transform')

pl.figure(3)
pl.plot(lmstime,lmsin_ecg)
pl.plot(lmstime,lmsout_ecg)
pl.title('Output LMS vs input prefiltered ECG data')
pl.xlabel('time/sec')
'''
'''
pl.figure(1)
pl.plot(datalms[:,0],datalms[:,1])
pl.plot(datalms[:,0],datalms[:,4])
pl.title('Output of LMS filter vs input prefiltered ECG data')
pl.xlabel('time/sec')
'''

datadnf = np.loadtxt('ecg_filtered.dat')

raw_ecg=datadnf[:,5]
in_ecg=datadnf[:,4]
out_ecg=datadnf[:,1]

canceller=datadnf[:,2]
raw_emg=datadnf[:,6]
in_emg=datadnf[:,3]

time=datadnf[:,0]

'''
pl.figure(4)
plot_FFT(raw_ecg,samplingFrequency)
plot_FFT(in_ecg,samplingFrequency)

pl.title('ECG DNF fourier transform')

pl.figure(5)
plot_FFT(raw_emg,samplingFrequency)
plot_FFT(in_emg,samplingFrequency)
pl.title('EMG DNF fourier transform')
'''

pl.figure(1)
pl.plot(time,in_ecg)
pl.plot(time,out_ecg)
pl.title('Output DNF vs input prefiltered ECG data')
pl.xlabel('time/sec')


'''
pl.figure(2)
pl.plot(datadnf[:,0],datadnf[:,1])
pl.plot(datadnf[:,0],datadnf[:,4])
pl.title('Output DNF vs input prefiltered ECG data')
pl.xlabel('time/sec')
'''

"""
#CANCELER:
pl.figure(2)
pl.plot(data[:,0],data[:,2])
pl.title('Canceler')
pl.xlabel('time/sec')

#FILTERED EMG
pl.figure(3)
pl.plot(data[:,0],data[:,3])
pl.title('input EMG(clean)')
pl.xlabel('time/sec')

#FILTERED ECG
pl.figure(4)
pl.plot(data[:,0],data[:,4])
pl.title('filtered ECG')
pl.xlabel('time/sec')

#ECG
pl.figure(5)
pl.plot(data[:,0],data[:,5])
pl.title('Non filtered ECG')
pl.xlabel('time/sec')

#ECG

pl.figure(6)
pl.plot(data[:,0],data[:,6])
pl.title('Neural Output ECG')
pl.xlabel('time/sec')"""

pl.show()