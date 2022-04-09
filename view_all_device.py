import pyaudio

# p = pyaudio.PyAudio()
# info = p.get_host_api_info_by_index(0)
# numdevices = info.get("deviceCount")
# for i in range(0, numdevices):
#     if (p.get_device_info_by_host_api_device_index(0, i).get("maxInputChannels")) > 0:
#         print(
#             "Input Device id ",
#             i,
#             " - ",
#             p.get_device_info_by_host_api_device_index(0, i).get("name"),
        # )
# import sounddevice as sd
# print(sd.query_devices())


# start pyaudio instance
pa = pyaudio.PyAudio()
import scipy.io.wavfile as wavfile
# print(pa.get_default_host_api_info())
# print(pa.get_default_output_device_info())
# print(pa.get_default_input_device_info())
# for id in range(pa.get_device_count()):
#   dev_dict = pa.get_device_info_by_index(id)
#   for key, value in dev_dict.items():
#       print(key, value)
stream_in = pa.open(
    rate=48000,
    channels=1,
    format=pyaudio.paInt16,
    input=True,                   # input stream flag
    input_device_index=1,         # input device index
    frames_per_buffer=1024
)

