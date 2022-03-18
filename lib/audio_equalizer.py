from scipy.signal import butter, lfilter


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

    def config_equalizer(
        self,
        gain1=0,
        gain2=0,
        gain3=0,
        gain4=0,
        gain5=0,
        gain6=0,
        gain7=0,
        gain8=0,
        gain9=0,
        gain10=0,
    ):
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
        b, a = butter(order, [low, high], btype="bandpass")
        filtered = lfilter(b, a, data)
        return filtered

    def equalizer_10band(self, data, fs):

        band_settings = [
            {"lower": 20, "upper": 39, "order": 2, "gain": self.gain1},
            {"lower": 40, "upper": 79, "order": 3, "gain": self.gain2},
            {"lower": 80, "upper": 159, "order": 3, "gain": self.gain3},
            {"lower": 160, "upper": 299, "order": 3, "gain": self.gain4},
            {"lower": 300, "upper": 599, "order": 3, "gain": self.gain5},
            {"lower": 600, "upper": 1199, "order": 3, "gain": self.gain6},
            {"lower": 1200, "upper": 2399, "order": 3, "gain": self.gain7},
            {"lower": 2400, "upper": 4999, "order": 3, "gain": self.gain8},
            {"lower": 5000, "upper": 9999, "order": 3, "gain": self.gain9},
            {"lower": 10000, "upper": 20000, "order": 3, "gain": self.gain10},
        ]
        bands = []
        for setting in band_settings:
            bands.append(
                self.__bandpass_filter(
                    data, setting["lower"], setting["upper"], fs, setting["order"]
                ) * 10 ** (setting["gain"] / 20)
            )
        return sum(bands)
