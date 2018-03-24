from ReadLoadDB import *
import numpy as np
import numpy.fft as nf
import matplotlib.pyplot as plt
import os
import wave
import scipy.signal as signal


def SaveReplay(WaveData, SampleRate,file = "replay.wav"):
	f = wave.open(file, "wb")

	# profile
	f.setnchannels(1)
	f.setsampwidth(2)
	f.setframerate(SampleRate)
	# write sound to file 
	sound = WaveData.astype(np.short)
	f.writeframes(sound.tostring())
	f.close()
	
	
def Replay():
	