from pydub import AudioSegment
import os
import wave
import matplotlib.pyplot as plt
import numpy as np
import numpy.fft as nf

#file = 'S1E5.mp3'

folder_path = "E:\MachineLearning\AudioProcess\LearningSample"
Noise_folder = os.path.join(folder_path,"Baba","txt")

file_name = os.path.join(Noise_folder, "baba01.txt")
print(file_name)
#sound = AudioSegment.from_mp3(file)
#sound.export(target_file, format="wav")

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
#print NSample*1.0/SampleRate
time = np.arange(0, NSample*1.0/SampleRate, 1.0/SampleRate)

Amp_1 = nf.fft(Left)
k_1 = nf.fftfreq(NSample, d = 1.0/SampleRate)
ReserveAmp_1 = [Amp_1[i] for i in range(len(Amp_1)) if (k_1[i] >20 and k_1[i]<10000)]
ReserveK_1 = [k_1[i] for i in range(len(k_1)) if (k_1[i] >20 and k_1[i]<10000)]
Prounce_1 = nf.ifft(ReserveAmp_1)

Amp_2 = nf.fft(Right)
k_2 = nf.fftfreq(NSample, d = 1.0/SampleRate)
ReserveAmp_2 = [Amp_2[i] for i in range(len(Amp_2)) if (k_2[i] >20 and k_2[i]<10000)]
ReserveK_2 = [k_1[i] for i in range(len(k_2)) if (k_2[i] >20 and k_2[i]<10000)]
Prounce_2 = nf.ifft(ReserveAmp_2)


print info
#print "Left",Left
#print "Right", Right

xticks = np.arange(0,60)
plt.subplot(211)
plt.plot(time, Left)
plt.title('Plot of Noise, Channels 1', loc='left')

plt.subplot(212)
plt.plot(Prounce_1)
plt.title('Mimic Nounce', loc='left')
plt.show()

plt.figure()
plt.subplot(211)
plt.plot(k_1, abs(Amp_1))
plt.subplot(212)
plt.plot(ReserveK_1, ReserveAmp_1)
plt.show()