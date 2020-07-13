from pydub import AudioSegment
sound = AudioSegment.from_file("chunk.wav")

print("----------Before Conversion--------")
print("Frame Rate", sound.frame_rate)
print("Channel", sound.channels)
print("Sample Width",sound.sample_width)

# Change Frame Rate
sound = sound.set_frame_rate(16000)

# Change Channel
sound = sound.set_channels(1)

# Change Sample Width
sound = sound.set_sample_width(2)

# Export the Audio to get the changed content
sound.export("convertedrate.wav", format ="wav")