from ReadLoadDB import *
import numpy as np
import numpy.fft as nf
import matplotlib.pyplot as plt
import os

t = np.array(np.arange(0.0,10.0,0.02))
norm_para = len(t)/2
y = np.sin(2*np.pi*t+0.25*np.pi)
y = np.add(y, 3*np.sin(2*np.pi*7*t+0.05*np.pi))
#y = np.add(y, 5*np.cos(2*np.pi*7*t))

spectrum = nf.fft(y)
k = nf.fftfreq(len(t), d = 0.02)
#phase = np.angle(spectrum)

ReserveSpe = np.array([(spectrum[i]) for i in range(len(spectrum)) if k[i]>=0 and k[i]<=20])
ReserveAmp = np.abs(ReserveSpe/norm_para)
ReserveK = np.array([k[i] for i in range(len(k)) if k[i]>=0 and k[i]<=20])
ReservePhase = np.array([np.angle(spec) for spec in ReserveSpe])

sort_index = np.argsort(ReserveAmp)
pick_index = sort_index[:-11:-1]

print ReservePhase[pick_index]
print ReserveAmp[pick_index]

ReCov = np.zeros(len(t))
for idx in pick_index:
	ReCov = np.add(ReCov, ReserveAmp[idx]*np.sin(2*np.pi*ReserveK[idx]*t+ReservePhase[idx]))


plt.figure()
plt.subplot(211)
plt.plot(t,y)
plt.plot(t, ReCov, color='green')
plt.subplot(212)
plt.plot(k,abs(spectrum))
plt.show()



