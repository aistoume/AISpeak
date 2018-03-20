# Record audio

from pyaudio import PyAudio, paInt16 
import numpy as np 
from datetime import datetime 
import wave 
import os

# Save file 
def save_wave_file(filename, data): 
    wf = wave.open(filename, 'wb') 
    wf.setnchannels(1) 
    wf.setsampwidth(2) 
    wf.setframerate(SAMPLING_RATE) 
    wf.writeframes("".join(data)) 
    wf.close() 



NUM_SAMPLES = 2000      # number of sample read in pyAudio
SAMPLING_RATE = 8000    # Sampling Rate
LEVEL = 1500            # Threshold
COUNT_NUM = 20          # 
SAVE_LENGTH = 8         # 

# Open the PyAudio function
pa = PyAudio() 
stream = pa.open(format=paInt16, channels=1, rate=SAMPLING_RATE, input=True, 
                frames_per_buffer=NUM_SAMPLES) 

save_count = 0
save_buffer = [] 

while True: 
	# Load NUM_SAMPLES sample
	string_audio_data = stream.read(NUM_SAMPLES) 
	audio_data = np.fromstring(string_audio_data, dtype=np.short) 
	large_sample_count = np.sum( audio_data > LEVEL ) 
	print np.max(audio_data), save_count, large_sample_count
	
	if large_sample_count > COUNT_NUM: 
		save_count = SAVE_LENGTH 
	else: 
		save_count -= 1 

	if save_count < 0: 
		save_count = 0 

	if save_count > 0: 
		save_buffer.append( string_audio_data ) 
	else: 
		if len(save_buffer) > 0: 
			filename = datetime.now().strftime("%Y-%m-%d_%H_%M_%S") + ".wav" 
			print filename
			filename = os.path.join('Sound_input', filename)
			print filename
			save_wave_file(filename, save_buffer) 
			save_buffer = [] 
			print filename, "saved" 