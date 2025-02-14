import wave
import matplotlib.pyplot as plt
import numpy as np
import os


f = wave.open("S1E5.wav", "rb")

# (nchannels, sampwidth, framerate, nframes, comptype, compname)
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]

str_data = f.readframes(nframes)
f.close()

wave_data = np.fromstring(str_data, dtype=np.short)
wave_data.shape = -1, 2
wave_data = wave_data.T
time = np.arange(0, nframes) * (1.0 / framerate)

figure = plt.gcf() # get current figure
figure.set_size_inches(8*20, 6)

duration = nframes/float(framerate)
xticks = np.arange(0, duration, 2)
plt.subplot(211).set_xticks(xticks)
plt.plot(time, wave_data[0])
plt.title('quit.playing.games.mp3 channel 1', loc='left')

plt.subplot(212).set_xticks(xticks)
plt.plot(time, wave_data[1], c="g")
plt.xlabel("time (seconds)")
plt.title('quit.playing.games.mp3 channel 2', loc='left')
plt.savefig('quit.playing.games.png', dpi=100, bbox_inches='tight', pad_inches=0.1)
plt.show()
plt.close(figure)