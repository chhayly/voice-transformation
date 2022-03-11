import pyaudio as pa
import time
from lib.transformer import *

class AudioStream(object):
    def __init__(self):
        self.FORMAT = pa.paFloat32
        self.CHANNEL_INPUT = 1
        self.CHANNEL_OUTPUT = 1
        self.RATE = 44100
        self.CHUNK = 1024 * 10
        self.p = None
        self.in_stream = None
        self.audio_effect = AudioEffect()

    def configure_stream(self, FORMAT = pa.paFloat32, CHANNEL_INPUT = 1, CHANNEL_OUTPUT = 1, RATE = 44100, CHUNK = 1024 * 2):
        #Stop the stream
        self.stop(self)

        #Update the stream parameters
        self.FORMAT = FORMAT
        self.CHANNEL_INPUT = CHANNEL_INPUT
        self.CHANNEL_OUTPUT = CHANNEL_OUTPUT
        self.RATE = RATE
        self.CHUNK = CHUNK

        #Start the stream
        self.start(self)


    def start(self):
        try:
            # Initialize PyAudio for Output
            self.p_out = pa.PyAudio()
            self.out_stream = self.p_out.open(format=self.FORMAT, channels=self.CHANNEL_OUTPUT, rate=self.RATE,
                                                   output=True, frames_per_buffer=self.CHUNK)
            self.out_stream.start_stream()

            # Initialize PyAudio for Input
            self.p = pa.PyAudio()
            self.in_stream = self.p.open(format=self.FORMAT, channels=self.CHANNEL_INPUT, rate=self.RATE,
                                     input=True, frames_per_buffer=self.CHUNK, stream_callback=self._process_stream)
            self.in_stream.start_stream()
            while self.in_stream.is_active():
                time.sleep(0.1)
        except KeyboardInterrupt:
            self.stop()
            pass

        

    def stop(self):
        self.in_stream.close()
        self.p.terminate()
        self.out_stream.close()
        self.p_out.terminate()

    def _process_stream(self, in_data, frame_count, time_info, flag):
        data = np.frombuffer(in_data, dtype=np.float32)
        data = self.use_audio_effect(data)
        self.out_stream.write(np.array(data, dtype=np.float32).tobytes())
        return in_data, pa.paContinue

    def use_audio_effect(self, signal):
        signal = self.audio_effect.add_white_noise(signal)
        signal = self.audio_effect.time_stretch(signal)
        signal = self.audio_effect.pitch_scale(signal, self.CHUNK)
        signal = self.audio_effect.invert_polarity(signal)
        signal = self.audio_effect.set_volume(signal)
        return signal
