
from lib.robot_voice import ConvertRobot
import numpy as np
import librosa
import parselmouth
from parselmouth.praat import call


class AudioEffect(object):
    def __init__(self):
        self.noise_percentage_factor = None
        self.time_stretch_rate = None
        self.num_semitones = None
        self.is_invert_polarity = False
        self.vol = None
        self.is_robot=False
        self.factor=2
        pass

    def config_parameters(
        self,
        noise_percentage_factor=None,
        time_stretch_rate=None,
        num_semitones=None,
        is_invert_polarity=0,
        vol=None,
        is_robot=False,
        factor=2
    ):
        self.noise_percentage_factor = noise_percentage_factor
        self.time_stretch_rate = time_stretch_rate
        self.num_semitones = num_semitones
        self.is_invert_polarity = is_invert_polarity
        self.vol = vol
        self.is_robot=is_robot
        self.factor=factor
        pass

    def add_white_noise(self, signal):
        if self.noise_percentage_factor is None:
            return signal
        noise = np.random.normal(0, signal.std(), signal.size)
        augmented_signal = signal + noise * self.noise_percentage_factor
        return augmented_signal

    def time_stretch(self, signal):
        if self.time_stretch_rate is None:
            return signal
        return librosa.effects.time_stretch(signal, self.time_stretch_rate)

    def pitch_scale(self, signal, sr):
        if self.num_semitones is None:
            return signal
        return librosa.effects.pitch_shift(signal, sr, self.num_semitones)

    def invert_polarity(self, signal):
        if self.is_invert_polarity == 1:
            return -signal
        return signal

    def set_volume(self, signal):
        if self.vol is None:
            return signal
        return signal * self.vol

    def convert_robot(self,fs,signal):
        if self.is_robot==True:
            signal=ConvertRobot(fs,signal)
        return signal
    

    def pitch_manipulation(self,signal):
        sound = parselmouth.Sound(signal)
        manipulation = call(sound, "To Manipulation", 0.01, 75, 600)
        pitch_tier = call(manipulation, "Extract pitch tier")

        call(pitch_tier, "Multiply frequencies", sound.xmin, sound.xmax, self.factor)

        call([pitch_tier, manipulation], "Replace pitch tier")
        sound_octave_up = call(manipulation, "Get resynthesis (overlap-add)")
        return sound_octave_up

    
