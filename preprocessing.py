def clean_matrix(file):
    data=np.loadtxt(file)
    fs=250 #same for both
    #clean ECG
    ECG=data[:,11]
    l, p = signal.butter(4, 120/(fs*2), 'low') #create filters
    h, f = signal.butter(4, 10/(fs*2), 'hp') 
    ecg_low= sp.signal.lfilter(l,p,ECG) #clean signal
    ecg_hp= sp.signal.lfilter(h,f,ecg_low)
    #clean EMG
    EMG=data[:,12]
    h, f = signal.butter(4, 50/(fs*2), 'hp') #different high pass filter
    emg_hp= sp.signal.lfilter(h,f,EMG)
    emg_low= sp.signal.lfilter(l,p,emg_hp)
    #create matrix
    
    final = np.c_[ecg_hp, emg_low]
    final=np.c_[data[:,0], final]
    np.savetxt("filtered_data.dat",final)
    return final

def extract_matrix(file):
    data=np.loadtxt(file)
    ECG=data[:,11]
    EMG=data[:,12]
    final = np.c_[ECG, EMG]
    final=np.c_[data[:,0], final]
    np.savetxt("unfiltered_data.dat",final)
    return final