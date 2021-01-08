import numpy as np
import pylab as pl

#load file with data from attys
data = np.loadtxt('ECGch1_EMGch2_rightwristNoise_00.tsv')

#select data from ch1 (DIO1)
ecg=data[:,8]
np.savetxt("ecg_noise.dat",ecg)

#select data from cha2 noise (DIO2)
noise=data[:,9]
np.savetxt("just_noise.dat",ecg)