import os
from pydub import AudioSegment
import glob

# if "audio" folder not exists, it will create
if not os.path.isdir("audio"):
    os.mkdir("audio")

# Grab the Audio files in "audio" folder
wavfiles  = glob.glob("./audio/*.wav")
print(wavfiles)

# Loopting each file and include in Audio Segment
wavs = [AudioSegment.from_wav(wav) for wav in wavfiles]

combined = wavs[0]

# Appending all the audio file
for wav in wavs[1:]:
    combined = combined.append(wav)

# Export Merged Audio File
combined.export("Mergedaudio.wav", format="wav")