import numpy as np
import pylab as pl
import pandas as pd
from scipy.fft import fft, fftfreq
from scipy import signal
from math import sqrt
# FFT function

def plot_FFT(data,column,figuren,samplingFrequency=250,range1=0,range2=-1):
    T= 1 / samplingFrequency

    N = len(data[range1:range2,column])
    # sample spacing
    yf = fft(data[range1:range2,column])
    xf = fftfreq(N, T)[:N//2]
    pl.figure(figuren)
    pl.plot(xf, 2.0/N * np.abs(yf[0:N//2]))

samplingFrequency= 250
def output(data,input,out,title,number,range=0):
    pl.figure(number)
    pl.plot(data[:,0],data[range:,input],label='prefiltered input')
    pl.plot( data[:,0],data[range:,out],label='output')
    pl.legend(bbox_to_anchor=(1.05, 1), borderaxespad=0.)
    pl.title(title)
    pl.xlabel('time/sec')

def canceller(data,column,title,number):
    pl.figure(number)
    pl.plot(data[:,0],data[:,column])
    pl.title(title)
    pl.xlabel('time/sec')


def signal_to_noise_rest():
    cleanbicep=np.loadtxt('data/lastrecordings/cleanECGb1.dat')
    start=10*250 #this is when the signal is cleanest and gives a better SNR 
    end=60*250
    signal=cleanbicep[start:end,1]
    noise=cleanbicep[start:end,2]
    dataLength=len(signal)
    #ECG signal can be found from 1Hz to 35-40Hz
    s= 1
    e= 100
    Start=int((s / samplingFrequency) * dataLength)
    End=int((e / samplingFrequency) * dataLength)
    #freqX = np.linspace(0, samplingFrequency / 2, int(dataLength / 2))
    fft_signal = np.abs(np.fft.fft(signal)[0:np.int(dataLength / 2)]) #FFT of signal
    fft_noise = np.abs(np.fft.fft(noise)[0:np.int(dataLength / 2)]) #FFT of noise (EMG)
    Noise = np.sum(fft_noise[Start:End]) #/ diff_noise # sum of FFT noise (EMG) over start and end
    Signal=np.sum(fft_signal[Start:End]) #/ diff_noise #sum of FFT signal over start and end
    SNR=Signal/Noise
    print(SNR)
    return SNR
signal_to_noise_rest()
def SNR(signalData):
    cleanbicep=np.loadtxt('data/lastrecordings/cleanECGb1.dat')
    start=10*250 #this is when the signal is cleanest and gives a better SNR 
    end=60*250
    refsignal=cleanbicep[start:end,1]
    refLength=len(refsignal)
    dataLength=len(signalData)
    #ECG signal can be found from 1Hz to 35-40Hz
    s= 1
    e= 100
    Start=int((s / samplingFrequency) * refLength)
    End=int((e / samplingFrequency) * refLength)
    startd=int((s / samplingFrequency) * dataLength)
    endd=int((e / samplingFrequency) * dataLength)
    #freqX = np.linspace(0, samplingFrequency / 2, int(dataLength / 2))
    fft_ref_ECG=np.abs(np.fft.fft(refsignal)[0:np.int(refLength / 2)])
    ref_ECG=np.sum(fft_ref_ECG[Start:End])# / diff_noise
 
    fft_signal = np.abs(np.fft.fft(signalData)[0:np.int(dataLength / 2)]) #FFT of signal
    signal=np.sum(fft_signal[startd:endd])# / diff_noise #sum of FFT signal over start and end
    SNR=ref_ECG/(signal-ref_ECG)#(signal-ref_ECG)
    #print(ref_ECG)
    #print(signal)
    print(SNR)
    return SNR

def cor_plot(data,columnECG,columnEMG,fignum,startecg=0,startemg=0):
    pl.figure(fignum)
    dataLength=len(data)
    cor= signal.correlate(data[startecg:,columnECG],data[startemg:,columnEMG])[0:np.int(dataLength / 2)]
    pl.plot(cor)
    return cor
def corr_coeffin(data,columnECG,columnEMG,startecg=0,startemg=0):
    corin=np.abs(np.corrcoef(data[startecg:,columnECG],data[startemg:,columnEMG])[0,1])
    print(corin)

def corr(Signal,noise):
    refLength=len(noise)
    dataLength=len(Signal)
    #ECG signal can be found from 1Hz to 35-40Hz
    s= 1
    e= 100
    Start=int((s / samplingFrequency) * dataLength)
    End=int((e / samplingFrequency) * dataLength)
    #freqX = np.linspace(0, samplingFrequency / 2, int(dataLength / 2))
    fft_ref=np.abs(np.fft.fft(noise)[0:np.int(refLength / 2)])
    
    fft_signal = np.abs(np.fft.fft(Signal)[0:np.int(dataLength / 2)]) #FFT of signal
    num=np.sum(fft_ref*fft_signal)# / diff_noise
    q=np.sum(fft_ref**2)*np.sum(fft_signal**2)
    cor=(num/sqrt(q))*100
    print(cor)
    return cor

start=6*250
#ARM 
cleanarm=np.loadtxt('data/lastrecordings/cleanECGa.dat')
#weight
weightarmlms=np.loadtxt('Results/Last_recordings/LMS/Weightarm.dat')
weightarmdnf=np.loadtxt('Results/Last_recordings/DNF/Weightarm.dat')
weightarm=np.loadtxt('data/lastrecordings/Weightarm.dat')
#noise
armnlms=np.loadtxt('Results/Last_recordings/LMS/armn.dat')
armndnf=np.loadtxt('Results/Last_recordings/DNF/armn.dat')
armn=np.loadtxt('data/lastrecordings/armn.dat')
#BICEP
cleanbicep=np.loadtxt('data/lastrecordings/cleanECGb1.dat')
#weight
weightb=np.loadtxt('data/lastrecordings/WeightB.dat')
weightblms=np.loadtxt('Results/Last_recordings/LMS/Weightb.dat')
weightbdnf=np.loadtxt('Results/Last_recordings/DNF/WeightB.dat')
#noise
bicepn=np.loadtxt('data/lastrecordings/bicep.dat')
bicepnlms=np.loadtxt('Results/Last_recordings/LMS/bicep.dat')
bicepndnf=np.loadtxt('Results/Last_recordings/DNF/bicep.dat')
#recordigs 2.21 usig bicep
biceplms=np.loadtxt('Results/2.21/LMS/bicep.dat')
bicep0lms=np.loadtxt('Results/2.21/LMS/bicep0.dat')
bicepflms=np.loadtxt('Results/2.21/LMS/bicepf.dat')
bicep0dnf=np.loadtxt('Results/2.21/DNF/bicep0.dat')

old_clean1=np.loadtxt('data/data1.06/cleanECGL2.dat')
old_clean2=np.loadtxt('data/data1.06/cleanECGL2.tsv')
def LMS_results():
    print('--------------------------')
    print('SNR with bicep noise=')
    SNR(bicepnlms[:,3])
    print('cor with bicep=')
    corr_coeffin(bicepnlms,3,4)
    corr(bicepnlms[:,3],bicepnlms[:,4])
    print('SNR bicep noise after LMS=')
    SNR(bicepnlms[:,1])
    print('cor with bicep after LMS=')
    corr_coeffin(bicepnlms,1,4)
    corr(bicepnlms[:,1],bicepnlms[:,4])
    print('--------------------------')
    print('--------------------------')
    print('SNR with wheight bicep noise=')
    SNR(weightblms[:,3])
    print('cor with wheight bicep=')
    corr_coeffin(weightblms,3,4)
    corr(weightblms[:,3],weightblms[:,4])
    print('SNR wheight bicep LMS=')
    SNR(weightblms[:,1])
    print('cor wheight bicep LMS=')
    corr_coeffin(weightblms,1,4)
    corr(weightblms[:,1],weightblms[:,4])
    print('--------------------------')
    print('--------------------------')
    print('--------------------------')
    print('SNR with arm noise=')
    SNR(armnlms[:,3])
    print('cor arm noise=')
    corr_coeffin(armnlms,4,3)
    corr(armnlms[:,3],armnlms[:,4])
    print('SNR with arm noise LMS=')
    SNR(armnlms[:,1])
    print('cor arm noise LMS=')
    corr_coeffin(armnlms,1,4)
    corr(armnlms[:,1],armnlms[:,4])
    print('--------------------------')
    print('--------------------------')
    print('SNR with wheight arm noise=')
    SNR(weightarmlms[:,3])
    print('cor arm wheight noise=')
    corr_coeffin(weightarmlms,3,4)
    corr(weightarmlms[:,3],weightarmlms[:,4])
    print('SNR wheight arm LMS=')
    SNR(weightarmlms[:,1])
    print('cor arm wheight noise LMS=')
    corr_coeffin(weightarmlms,1,4)
    corr(weightarmlms[:,1],weightarmlms[:,4])
    print('--------------------------')
    print('--------------------------')
    print('SNR with bicep0=')
    SNR(bicep0lms[:,3])
    print('cor with bicep0=')
    corr_coeffin(bicep0lms,3,4)
    corr(bicep0lms[:,3],bicep0lms[:,4])
    print('SNR bicep0 LMS=')
    SNR(bicep0lms[:,1])
    print('cor bicep0 LMS=')
    corr_coeffin(bicep0lms,1,4)
    corr(bicep0lms[:,1],bicep0lms[:,4])

    output(armnlms,3,1,'Output LMS arm',1)
    output(weightarmlms,3,1,'Output LMS w arm',2)
    output(bicepnlms,3,1,'Output LMS bicep',3)
    output(weightblms,3,1,'Output LMS w bicep',4)
    output(bicep0lms,3,1,'Output LMS bicep0',5)

def DNF_results():
    print('--------------------------')
    print('SNR with bicep noise=')
    SNR(bicepndnf[:,3])
    print('cor with bicep=')
    corr_coeffin(bicepndnf,3,4)
    corr(bicepndnf[:,3],bicepndnf[:,4])
    print('SNR bicep noise after LMS=')
    SNR(bicepndnf[:,1])
    print('cor with bicep after LMS=')
    corr_coeffin(bicepndnf,1,4)
    corr(bicepndnf[:,1],bicepndnf[:,4])
    print('--------------------------')
    print('--------------------------')
    print('SNR with wheight bicep noise=')
    SNR(weightbdnf[:,3])
    print('cor with wheight bicep=')
    corr_coeffin(weightbdnf,3,4)
    corr(weightbdnf[:,3],weightbdnf[:,4])
    print('SNR wheight bicep LMS=')
    SNR(weightbdnf[:,1])
    print('cor wheight bicep LMS=')
    corr_coeffin(weightbdnf,1,4)
    corr(weightbdnf[:,1],weightbdnf[:,4])
    print('--------------------------')
    print('--------------------------')
    print('--------------------------')
    print('SNR with arm noise=')
    SNR(armndnf[:,3])
    print('cor arm noise=')
    corr_coeffin(armndnf,4,3)
    corr(armndnf[:,3],armndnf[:,4])
    print('SNR with arm noise LMS=')
    SNR(armndnf[:,1])
    print('cor arm noise LMS=')
    corr_coeffin(armndnf,1,4)
    corr(armndnf[:,1],armndnf[:,4])
    print('--------------------------')
    print('--------------------------')
    print('SNR with wheight arm noise=')
    SNR(weightarmdnf[:,3])
    print('cor arm wheight noise=')
    corr_coeffin(weightarmdnf,3,4)
    corr(weightarmdnf[:,3],weightarmdnf[:,4])
    print('SNR wheight arm LMS=')
    SNR(weightarmdnf[:,1])
    print('cor arm wheight noise LMS=')
    corr_coeffin(weightarmdnf,1,4)
    corr(weightarmdnf[:,1],weightarmdnf[:,4])
    print('--------------------------')
    print('--------------------------')
    print('SNR with bicep0=')
    SNR(bicep0dnf[:,3])
    print('cor with bicep0=')
    corr_coeffin(bicep0dnf,3,4)
    corr(bicep0dnf[:,3],bicep0dnf[:,4])
    print('SNR bicep0 LMS=')
    SNR(bicep0dnf[:,1])
    print('cor bicep0 LMS=')
    corr_coeffin(bicep0dnf,1,4)
    corr(bicep0dnf[:,1],bicep0dnf[:,4])

    output(armndnf,3,1,'Output DNF arm',1)
    output(weightarmdnf,3,1,'Output DNF w arm',2)
    output(bicepndnf,3,1,'Output DNF bicep',3)
    output(weightbdnf,3,1,'Output DNF w bicep',4)
    output(bicep0dnf,3,1,'Output DNF bicep0',5)

#DNF_results()
#LMS_results()

'''
#fig, axs = pl.subplots(nrows=2, ncols=2, figsize=(10, 10))
# plot time signal:
axs[0, 0].set_title("ECG")
axs[0, 0].plot(weightarm[start:,0], weightarm[start:,1], color='C0')
axs[0, 0].set_xlabel("Time")
axs[0, 0].set_ylabel("Amplitude")

axs[0, 1].set_title("EMG")
axs[0, 1].plot(weightarm[start:,0], weightarm[start:,2], color='C0')
axs[0, 1].set_xlabel("Time")
axs[0, 1].set_ylabel("Amplitude")

# plot different spectrum types:
axs[1, 0].set_title("Magnitude Spectrum of ECG and EMG")
axs[1, 0].magnitude_spectrum(weightarm[start:,1], Fs=250, color='C0')
axs[1, 0].magnitude_spectrum(weightarm[start:,2], Fs=250, color='C1')
# plot different spectrum types:
#axs[1, 1].set_title("Magnitude Spectrum of EMG")
#axs[1, 1].magnitude_spectrum(armn[start:,2], Fs=250, color='C0')
fig.tight_layout()
#pl.plot(cleanbicep[11500:12000,1])
#pl.savefig('awesomeData.svg')'''
'''
ax1 = pl.subplot(313)
ax1.margins(0.05)           # Default margin is 0.05, value 0 means fit
ax1.magnitude_spectrum(weightarm[start:,1], Fs=250, color='C7')
ax1.magnitude_spectrum(weightarm[start:,2], Fs=250, color='C0')

ax2 = pl.subplot(311)      # Values >0.0 zoom out
ax2.set_title("ECG")
ax2.plot(weightarm[start:,0], weightarm[start:,1], color='C7')
ax2.set_xlabel("Time")
ax2.set_ylabel("Amplitude")

ax3 = pl.subplot(312)
ax3.set_title("EMG")
ax3.plot(weightarm[start:,0], weightarm[start:,2], color='C0')
ax3.set_xlabel("Time (s)")
ax3.set_ylabel("Amplitude")
fig.tight_layout()'''

fig, (ax1,ax2) = pl.subplots(nrows=2, sharex=True, subplot_kw=dict(frameon=False)) # frameon=False removes frames
pl.subplots_adjust(hspace=.0)
ax1.grid()
ax2.grid()
pl.xlim(60, 80)
ax1.plot(bicep0dnf[:,0], bicep0dnf[:,3], color='C0')
ax1.plot(bicep0dnf[:,0], bicep0dnf[:,1], color='C7')
ax2.plot(bicep0dnf[:,0], bicep0dnf[:,2], color='k')
pl.savefig('closerb0nDNF.svg')
'''
pl.grid()
pl.magnitude_spectrum(bicep0lms[:,3], Fs=250, color='C7')
pl.magnitude_spectrum(bicep0lms[:,4], Fs=250, color='C0')
pl.ylim(0, 6e-6)
pl.xlim(0, 125)
#pl.savefig('fft.svg')'''
'''
cor=cor_plot(bicep0lms,3,4,2)

fig, axs = pl.subplots(2, 1, subplot_kw=dict(frameon=False)) # frameon=False removes frames
pl.subplots_adjust(hspace=.0)

axs[0].plot(bicep0lms[:,0],bicep0lms[:,3],color='C0')
axs[0].plot(bicep0lms[:,0], bicep0lms[:,4],color='C7')
axs[0].set_xlabel('time')
axs[0].set_ylabel('s1 and s2')
axs[0].grid(True)
t=np.arange(0, len(cor), 250)
axs[1].plot(cor)
axs[1].set_ylabel('coherence')
axs[1].grid(True)
fig.tight_layout()
pl.savefig('cor.svg')'''

pl.show()

