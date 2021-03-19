import numpy as np
import pandas as pd
import pylab as pl
import scipy as sp
from scipy import signal

def clean_matrix(file,name):
    data=np.loadtxt(file)
    fs=250 #same for both
    #clean ECG
    ECG=data[:,11]
    l, p = signal.butter(4, 120/(fs*2), 'low') #create filters
    h, f = signal.butter(4, 1/(fs*2), 'hp') 
    ecg_low= sp.signal.lfilter(l,p,ECG) #clean signal
    ecg_hp= sp.signal.lfilter(h,f,ecg_low)
    #clean EMG
    EMG=data[:,12]
    h, f = signal.butter(4, 10/(fs*2), 'hp') #different high pass filter
    emg_hp= sp.signal.lfilter(h,f,EMG)
    emg_low= sp.signal.lfilter(l,p,emg_hp)
    #create matrix
    
    final = np.c_[ecg_hp, emg_low]
    final=np.c_[data[:,0], final]
    np.savetxt(name,final)
    return final

def extract_matrix(file,name):
    data=np.loadtxt(file)
    ECG=data[:,7]
    EMG=data[:,8]
    final = np.c_[ECG, EMG]
    final=np.c_[data[:,0], final]
    np.savetxt(name,final)
    return final

extract_matrix('data/data3.18/ECGarm2.tsv','data/data3.18/ECGarm2.dat')