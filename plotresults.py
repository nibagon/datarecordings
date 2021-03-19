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


datadnf = np.loadtxt('ecg_filtered.dat') #output DNF
    #ECG DNF
raw_ecg=datadnf[:,5]
in_ecg=datadnf[:,4]
out_ecg=datadnf[:,1]
    #EMG DNF
canceller=datadnf[:,2]
raw_emg=datadnf[:,6]
in_emg=datadnf[:,3]
    #TIME DNF
time=datadnf[:,0]


#OUTPUT

datalms = np.loadtxt('LMSfiltered_ecg.dat') #output LMS
#ECG LMS
lmsraw_ecg=datalms[:,5]
lmsin_ecg=datalms[:,4]
lmsout_ecg=datalms[:,1]
#EMG LMS
lmscanceller=datalms[:,2]
lmsraw_emg=datalms[:,6]
lmsin_emg=datalms[:,3]
#TIME LMS
lmstime=datalms[:,0]


def fftecg(text,number):
    if text=='LMS':
        pl.figure(number)
        plot_FFT(lmsraw_ecg*1000,samplingFrequency)
        plot_FFT(lmsin_ecg,samplingFrequency)
        pl.title('ECG fourier transform')
    elif text=='DNF':
        pl.figure (number)
        plot_FFT(raw_ecg*0.0001,samplingFrequency)
        plot_FFT(in_ecg,samplingFrequency)
        pl.title('ECG DNF fourier transform')

def fftemg(text,number):
    if text=='LMS':
        pl.figure(number)
        plot_FFT(lmsraw_emg,samplingFrequency)
        plot_FFT(lmsin_emg/1000,samplingFrequency)
        pl.title('EMG fourier transform')
    elif text=='DNF':
        pl.figure (number)
        plot_FFT(raw_emg,samplingFrequency)
        plot_FFT(in_emg/0.0001,samplingFrequency)
        pl.title('EMG DNF fourier transform')

def output(text,number):
    if text=='LMS':
        pl.figure(number)
        pl.plot(lmstime,lmsin_ecg, label='prefiltered input')
        pl.plot(lmstime,lmsout_ecg, label='LMS output')
        pl.legend(bbox_to_anchor=(1.05, 1), borderaxespad=0.)
        pl.title('Output LMS vs input prefiltered ECG data')
        pl.xlabel('time/sec')
    elif text=='DNF':
        pl.figure(number)
        pl.plot(time,in_ecg)
        pl.plot(time,out_ecg)
        pl.title('Output DNF vs input prefiltered ECG data')
        pl.xlabel('time/sec')
'''
clean=np.loadtxt('data/data1.06/cleanECGL2.dat')
pl.figure(1)
pl.plot(clean[:,0],clean[:,1])
pl.title('Clean ECG')
pl.xlabel('time/sec')


preclean=np.loadtxt('data/data1.06/ECGL2.dat')
pl.figure(2)
pl.plot(preclean[:,0],preclean[:,1])
pl.title('Raw ECG')
pl.xlabel('time/sec')

raw=np.loadtxt('data/data2.09/bicepnoise.tsv')
pl.figure(3)
plot_FFT(raw[:,8],samplingFrequency)
#plot_FFT(raw[:,12],samplingFrequency)
pl.title('Power Spectrum Density EMG')
pl.xlabel('Frequency')

bclean= np.loadtxt('data/data2.09/bicepnoise.dat')
pl.figure(4)
plot_FFT(raw[:,7],samplingFrequency)
#plot_FFT(raw[:,11],samplingFrequency)
pl.title('Power Spectrum Density ECG')
pl.xlabel('Frequency')
'''
'''
fig, axs = pl.subplots(2, sharex=True, sharey=False)
fig.suptitle('Signal and canceller')

axs[0].plot(lmstime,lmsin_ecg, label='prefiltered input')
axs[0].plot(lmstime,lmsout_ecg, label='LMS output')
axs[0].legend(bbox_to_anchor=(1.05, 1), borderaxespad=0.)
#axs[0].title('Output LMS vs input prefiltered ECG data')
#axs[0].xlabel('time/sec')
axs[1].plot(lmstime,lmscanceller)
#axs[1].title('Canceller y(n)')'''


fig, axs = pl.subplots(2, sharex=True, sharey=False)
fig.suptitle('Signal and canceller')

axs[0].plot(time,in_ecg, label='prefiltered input')
axs[0].plot(time,out_ecg, label='LMS output')
axs[0].legend(bbox_to_anchor=(1.05, 1), borderaxespad=0.)
#axs[0].title('Output LMS vs input prefiltered ECG data')
#axs[0].xlabel('time/sec')
axs[1].plot(time,canceller)
#axs[1].title('Canceller y(n)')'''

#output('DNF',1)

pl.show()
