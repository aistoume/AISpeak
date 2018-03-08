from pydub import AudioSegment
import os
#file = 'S1E5.mp3'

folder_path = "E:\MachineLearning\AudioProcess\LearningSample"
Noise_folder = os.path.join(folder_path,"Noise")
print(Noise_folder)
file_name = 'S1E5.mp3'
file = os.path.join("", file_name)
target_file = os.path.join("", 'S1E5.wav')
#sound = AudioSegment.from_mp3(file)
#sound.export(target_file, format="wav")