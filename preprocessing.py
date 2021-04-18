import numpy as np
import pandas as pd
import pylab as pl
import scipy as sp
from scipy import signal 

def clean_matrix(file,name):
    data=np.loadtxt(file)
    fs=250.0 #same for both
    #clean ECG
    def butter_bandstop_filter(data, cfl, cfh, order):
        nyq = 0.5 * 250.0
        low = cfl / nyq
        high = cfh / nyq

        i, u = signal.butter(order, [low, high], btype='bandstop')
        y = signal.lfilter(i, u, data)
        return y
    ECG=data[:,7]
    h, f = signal.butter(4, 1/(fs*2), 'hp') 
    ecg_hp= sp.signal.lfilter(h,f,ECG)
    #ecg_hp=butter_bandstop_filter(ECG,0.5,1,4)
    ecg50=butter_bandstop_filter(ecg_hp,49,51,4)
    ecg=butter_bandstop_filter(ecg50,99,101,4)
    #clean EMG
    EMG=data[:,8]
    h, f = signal.butter(4, 10/(fs*2), 'hp') #different high pass filter
    emg_hp= sp.signal.lfilter(h,f,EMG)
    emg50=butter_bandstop_filter(emg_hp,49,51,4)
    emg=butter_bandstop_filter(emg50,99,101,4)
    '''emg9=butter_bandstop_filter(emg100,9.7,9.8,2)
    emg19=butter_bandstop_filter(emg9,19.5,19.6,2)
    emg29=butter_bandstop_filter(emg19,29.3,29.4,2)'''
    #emg=sp.signal.lfilter(b,a,emg_hp)
    #b, a = signal.iirnotch(100, 40.0, fs)
    #emg=sp.signal.lfilter(b,a,emg_50)
    #ecg=sp.signal.lfilter(b,a,ecg_50)

    #create matrix
    
    final = np.c_[ecg, emg]
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

samplingFrequency= 250
'''
clean_matrix('data/lastrecordings/armn.tsv','data/lastrecordings/armn.dat')
clean_matrix('data/lastrecordings/bicep.tsv','data/lastrecordings/bicep.dat')
clean_matrix('data/lastrecordings/cleanECGa.tsv','data/lastrecordings/cleanECGa.dat')'''
clean_matrix('data/lastrecordings/cleanECGb1.tsv','data/lastrecordings/cleanECGb1.dat')
'''
clean_matrix('data/lastrecordings/Weightarm.tsv','data/lastrecordings/Weightarm.dat')
clean_matrix('data/lastrecordings/WeightB.tsv','data/lastrecordings/WeightB.dat')
clean_matrix('data/data2.21/bicep.tsv','data/data2.21/bicep.dat')
clean_matrix('data/data2.21/bicep0.tsv','data/data2.21/bicep0.dat')
clean_matrix('data/data2.21/bicepf.tsv','data/data2.21/bicepf.dat')
clean_matrix('data/data1.06/cleanECGL2.tsv','data/data1.06/cleanECGL2.dat')
clean_matrix('data/data1.06/cleanECGL2t2.tsv','data/data1.06/cleanECGL2t2.dat')'''