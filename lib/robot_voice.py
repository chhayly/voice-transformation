import getopt
import numpy as np
import scipy.io.wavfile as wavfile
import math
import sys




"""
Constants
"""

class Waveshaper():
    def __init__(self, curve):
        self.curve = curve
        self.n_bins = self.curve.shape[0]

    def transform(self, samples):
        # normalize to 0 < samples < 2
        max_val = np.max(np.abs(samples))
        if max_val >= 1.0:
            result = samples/np.max(np.abs(samples)) + 1.0
        else:
            result = samples + 1.0
        result = result * (self.n_bins-1)/2
        return self.curve[result.astype(np.int)]

# Diode constants (must be below 1; paper uses 0.2 and 0.4)
VB = 0.2
VL = 0.4

# Controls distortion
H = 4

# Controls N samples in lookup table; probably leave this alone
LOOKUP_SAMPLES = 1024

# Frequency (in Hz) of modulating frequency
MOD_F = 50

def diode_lookup(n_samples):
    result = np.zeros((n_samples,))
    for i in range(0, n_samples):
        v = float(i - float(n_samples)/2)/(n_samples/2)
        v = abs(v)
        if v < VB:
            result[i] = 0
        elif VB < v <= VL:
            result[i] = H * ((v - VB)**2)/(2*VL - 2*VB)
        else:
            result[i] = H*v - H*VL + (H*(VL-VB)**2)/(2*VL-2*VB)

    return result

def raw_diode(signal):
    result = np.zeros(signal.shape)
    for i in range(0, signal.shape[0]):
        v = signal[i]
        if v < VB:
            result[i] = 0
        elif VB < v <= VL:
            result[i] = H * ((v - VB)**2)/(2*VL - 2*VB)
    else:
        result[i] = H*v - H*VL + (H*(VL-VB)**2)/(2*VL-2*VB)
    return result

def ConvertRobot(rate,data):
    """
    Program to make a robot voice by simulating a ring modulator;
    procedure/math taken from
    http://recherche.ircam.fr/pub/dafx11/Papers/66_e.pdf
    """


    n_samples = data.shape[0]



    d_lookup = diode_lookup(LOOKUP_SAMPLES)
    diode = Waveshaper(d_lookup)


    tone = np.arange(n_samples)
    tone = np.sin(2*np.pi*tone*MOD_F/rate)

    # Gain tone by 1/2
    tone = tone * 0.5

    # Junctions here
    tone2 = tone.copy() # to top path
    data2 = data.copy() # to bottom path

    # Invert tone, sum paths
    tone = -tone + data2 # bottom path
    data = data + tone2 #top path

    #top
    data = diode.transform(data) + diode.transform(-data)

    #bottom
    tone = diode.transform(tone) + diode.transform(-tone)

    result = data - tone
    print("robot")
    return result
# Convert()