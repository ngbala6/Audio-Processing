from pydub import AudioSegment
import os

if not os.path.isdir("splitaudio"):
    os.mkdir("splitaudio")

audio = AudioSegment.from_file("02072018-083922_OUT_TATA_232_012156853818.gsm")
lengthaudio = len(audio)
print("Length of Audio File", lengthaudio)

start = 0
# In Milliseconds, this will cut 10 Sec of audio
threshold = 10000
end = 0
counter = 0

while start < len(audio):

    end += threshold

    print(start , end)

    chunk = audio[start:end]

    filename = f'bala/chunk{counter}.wav'

    chunk.export(filename, format="wav")

    counter +=1

    start += threshold





