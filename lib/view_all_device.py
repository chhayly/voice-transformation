import pyaudio


def allInputDevices():
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get("deviceCount")
    devices={}
    for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get("maxInputChannels")) > 0:
            name=p.get_device_info_by_host_api_device_index(0, i).get("name")
            devices[name]=i
            # print(name)
    return devices



        

