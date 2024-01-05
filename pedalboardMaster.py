from pedalboard import Pedalboard, Compressor, Limiter
from pedalboard.io import AudioFile

# reads in audio and resamples to desired sample rate
samplerate = 44100.0
with AudioFile('AUDIOFILE.wav').resampled_to(samplerate) as f:
    audio = f.read(f.frames)

# intial pedalboard structure
board = Pedalboard ([
    Compressor(threshold_db=-50, ratio=25),

])