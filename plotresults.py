import numpy as np
import pylab as pl
#OUTPUT
data = np.loadtxt('ecg_filtered.dat')
pl.figure(1)
pl.plot(data[:,0],data[:,1])
pl.plot(data[:,0],data[:,4])
pl.title('Output LMS')
pl.xlabel('time/sec')

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

pl.show()