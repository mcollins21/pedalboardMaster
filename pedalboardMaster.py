from pedalboard import Pedalboard, Compressor, Limiter
from pedalboard.io import AudioFile

# reads in audio and resamples to desired sample rate
samplerate = 44100.0
with AudioFile('AUDIOFILE.wav').resampled_to(samplerate) as f:
    audio = f.read(f.frames)

# mixing pedalboard structure
board = Pedalboard ([
    Compressor(threshold_db=-50, ratio=25),
    # Limiter(threshold_db: float =-10.0, release_ms: float = 100.0) # limiter not functional
])

# running audio through pedalboard
effected = board(audio, samplerate)

# writing audio back as .wav file
with Audiofile('OUTPUTFILE.wav', 'w', samplerate, effected.shape[0]) as f:
    f.write(effected)