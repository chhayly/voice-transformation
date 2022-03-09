import pyaudio as pa
import wave as wv

audio = pa.PyAudio()

# print('hello::',pa.PyAudio().get_default_input_device_info())

# stream = audio.open(format=pa.paInt16, channels=8, rate=44100, input=True, frames_per_buffer=1024)

# frames = []

# try:
#     while True:
#         data = stream.read(1024)
#         frames.append(data)
# except KeyboardInterrupt:
#     pass

# stream.stop_stream()
# stream.close()
# audio.terminate()

# sound_file = wv.open("output.wav", "wb")
# sound_file.setnchannels(1)
# sound_file.setsampwidth(audio.get_sample_size(pa.paInt16))
# sound_file.setframerate(44100)
# sound_file.writeframes(b''.join(frames))

# import matplotlib.pyplot as plt
# import librosa
# import librosa.display
# import soundfile as sf
# import numpy as np 
# from lib.pitch_shifter import time_stretch,pitch_scale
# import sys
# import pyaudio
# import wave
# import time



# #@title Filename
# filename = "input.m4a" #@param {type:"string"}
# filename = filename

# data,sample_rate=librosa.load(filename)

# print(data,sample_rate)

# #@title Pitch Shifter
# num_semitones = 11 #@param {type:"slider", min:0, max:20, step:1}
# time_stretch_rate = 1 #@param {type:"slider", min:0, max:5, step:0.1}
# augment=pitch_scale(data,sample_rate,num_semitones)
# augment1=time_stretch(augment,time_stretch_rate)
# sf.write("augmented_audio.wav", augment1, sample_rate)


# wf = wave.open('augmented_audio.wav', 'rb')

# # instantiate PyAudio (1)
# p = pyaudio.PyAudio()

# # define callback (2)
# def callback(in_data, frame_count, time_info, status):
#     data = wf.readframes(frame_count)
#     return (data, pyaudio.paContinue)

# # open stream using callback (3)
# stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
#                 channels=wf.getnchannels(),
#                 rate=wf.getframerate(),
#                 output=True,
#                 stream_callback=callback)

# # start the stream (4)
# stream.start_stream()

# # wait for stream to finish (5)
# while stream.is_active():
#     time.sleep(0.1)

# # stop stream (6)
# stream.stop_stream()
# stream.close()
# wf.close()

# # close PyAudio (7)
# p.terminate()
