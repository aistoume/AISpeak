from ReadLoadDB import *
import numpy as np
import numpy.fft as nf
import matplotlib.pyplot as plt
import os
import wave
import scipy.signal as signal


folder_path = "E:\MachineLearning\AudioProcess\LearningSample"
Noise_folder = os.path.join(folder_path,"Baba","txt")
file_name = os.path.join(Noise_folder, "baba01.txt")

print(file_name)
Left = []
Right = []
info =[]

with open(file_name, "r") as f:
	n = 0
	for line in f:
		if n<5:
			info.append(line.strip().split("\t"))
			n+=1
		else:
			row = line.strip().split("\t")
			Left.append(float(row[0]))
			Right.append(float(row[1]))

NSample = int(info[0][1])
BitPerSample = int(info[1][1])
Channels = int(info[2][1])
SampleRate = int(info[3][1])

sound = np.asarray(Left)
sound = sound.astype(np.short)
			
# generate signal
time = 10
framerate = 40000
t = np.arange(0, time, 1.0/framerate)
wave_data = signal.chirp(t, 100, time, 1000, method='linear') * 10000
wave_data = wave_data.astype(np.short)

# open wav file
f = wave.open("sweep.wav", "wb")
plt.figure()
plt.plot(t,wave_data)
plt.show()

# profile
f.setnchannels(1)
f.setsampwidth(2)
f.setframerate(SampleRate)
# write sound to file 
f.writeframes(sound.tostring())
f.close()
