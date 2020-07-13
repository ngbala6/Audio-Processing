# Import packages
from pydub import AudioSegment
from pydub.playback import play


# Play audio
playaudio = AudioSegment.from_file("bala.wav", format="wav")
play(playaudio)