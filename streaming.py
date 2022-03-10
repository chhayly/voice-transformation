import pyaudio as pa
import time
from lib.transformer import *

class AudioHandler(object):
    def __init__(self):
        self.FORMAT = pa.paFloat32
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024 * 2
        self.p = None
        self.in_stream = None
        self.enablePitchShifting = True
        

    def start(self):
        try:
            # Initialize PyAudio for Output
            self.p_out = pa.PyAudio()
            self.out_stream = self.p_out.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE,
                                                   output=True, frames_per_buffer=self.CHUNK)
            self.out_stream.start_stream()

            # Initialize PyAudio for Input
            self.p = pa.PyAudio()
            self.in_stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE,
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
        num_semitones = 11
        time_stretch_rate =1

        data = np.frombuffer(in_data, dtype=np.float32)
        augment = pitch_scale(data, self.CHUNK, num_semitones)

        self.out_stream.write(np.array(augment, dtype=np.float32).tobytes())

        return in_data, pa.paContinue