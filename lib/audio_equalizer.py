import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
from scipy import signal
from scipy.signal import butter, lfilter
import soundfile as sf


class AudioEqualizer(object):

    def __init__(self) -> None:
        self.gain1 = 0
        self.gain2 = 0
        self.gain3 = 0
        self.gain4 = 0
        self.gain5 = 0
        self.gain6 = 0
        self.gain7 = 0
        self.gain8 = 0
        self.gain9 = 0
        self.gain10 = 0
        pass

    def config_equalizer(self, gain1=0, gain2=0, gain3=0, gain4=0, gain5=0, gain6=0, gain7=0, gain8=0, gain9=0, gain10=0):
        self.gain1 = gain1
        self.gain2 = gain2
        self.gain3 = gain3
        self.gain4 = gain4
        self.gain5 = gain5
        self.gain6 = gain6
        self.gain7 = gain7
        self.gain8 = gain8
        self.gain9 = gain9
        self.gain10 = gain10

    def __bandpass_filter(self, data, lowcut, highcut, fs, order=5):
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        b, a = butter(order, [low, high], btype='bandpass')
        filtered = lfilter(b, a, data)
        return filtered

    def equalizer_10band(self, data, fs):
        band1 = self.__bandpass_filter(
            data, 20, 39, fs, order=2) * 10**(self.gain1/20)
        band2 = self.__bandpass_filter(
            data, 40, 79, fs, order=3)*10**(self.gain2/20)
        band3 = self.__bandpass_filter(
            data, 80, 159, fs, order=3)*10**(self.gain3/20)
        band4 = self.__bandpass_filter(
            data, 160, 299, fs, order=3) * 10**(self.gain4/20)
        band5 = self.__bandpass_filter(
            data, 300, 599, fs, order=3) * 10**(self.gain5/20)
        band6 = self.__bandpass_filter(
            data, 600, 1199, fs, order=3) * 10**(self.gain6/20)
        band7 = self.__bandpass_filter(
            data, 1200, 2399, fs, order=3) * 10**(self.gain7/20)
        band8 = self.__bandpass_filter(
            data, 2400, 4999, fs, order=3) * 10**(self.gain8/20)
        band9 = self.__bandpass_filter(
            data, 5000, 9999, fs, order=3) * 10**(self.gain9/20)
        band10 = self.__bandpass_filter(
            data, 10000, 20000, fs, order=3) * 10**(self.gain10/20)
        signal = band1 + band2 + band3 + band4 + \
            band5 + band6 + band7 + band8 + band9 + band10
        return signal
