from pydub import AudioSegment
import os
import wave
import matplotlib.pyplot as plt
import numpy as np
import numpy.fft as nf
import ReadLoadDB
import scipy.signal as signal

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
norm_para = len(time)/2

Spectrum_1 = nf.fft(Left)
k_1 = nf.fftfreq(NSample, d = 1.0/SampleRate)

Index_1 = [i for i in range(len(k_1)) if (k_1[i] >=20 and k_1[i]<=10001)]
ReserveSpec_1 = np.array([ Spectrum_1[i] for i in Index_1])
ReserveAmp_1 = [abs(Spectrum_1[i])/norm_para for i in Index_1]
ReserveK_1 = [k_1[i] for i in Index_1]
ReservePhase_1 = np.array([np.angle(spec) for spec in ReserveSpec_1])
#Prounce_1 = nf.ifft(ReserveAmp_1)

dF = NSample*1.0/SampleRate
Freq_List = [20,50,100,150,200,250,300,350,400,450,500,1000,2000,5000,10000]
Index = [int((a-20)*dF) for a in Freq_List]

sort_index = np.argsort(ReserveAmp_1)
pick_index = sort_index[:-1000:-1]

#pick_index.sort()
print len(pick_index)
#print [ReservePhase_1[i] for i in pick_index]

Prounce_1 = np.zeros(len(time))
for idx in pick_index:
	Prounce_1 = np.add(Prounce_1, ReserveAmp_1[idx]*np.sin(2*np.pi*ReserveK_1[idx]*time+ReservePhase_1[idx]))
print max(Prounce_1)


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
plt.plot(k_1, abs(Spectrum_1))
plt.subplot(212)
plt.plot(ReserveK_1, ReserveAmp_1)
plt.show()

print "writing"

# open wav file
f = wave.open("replay.wav", "wb")

# profile
f.setnchannels(1)
f.setsampwidth(2)
f.setframerate(SampleRate)
# write sound to file 
sound = Prounce_1.astype(np.short)
f.writeframes(sound.tostring())
f.close()