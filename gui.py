from tkinter import (
    Tk,
    Label,
    Button,
    Scale,
    HORIZONTAL,
    VERTICAL,
    IntVar,
    Frame,
    Checkbutton,
    StringVar,
    OptionMenu
)
from turtle import color
import lib.audio_stream as st
from lib.view_all_device import allInputDevices
"""The main AudioStream object"""
audio_stream: st.AudioStream = st.AudioStream()
ae: st.AudioEffect = audio_stream.audio_effect
aeq: st.AudioEqualizer = audio_stream.audio_equalizer


def start_streaming(device_index):
    print("start streaming")
    audio_stream.input_device=device_index

    audio_stream.start()


def stop_streaming():
    print("stop streaming")
    audio_stream.stop()

robot=False
def changeRobot(btn):
    global robot
    if robot==False:
        robot=True
        btn.configure(bg="green",fg="white")
    else:
        robot=False
        btn.configure(bg="white", fg="black")

def set_stream_effect(self):

    audio_stream.audio_effect.config_parameters(
        num_semitones=num_semitones.get(),
        noise_percentage_factor=noise_percentage.get() / 100,
        vol=volume.get() / 100,
        is_robot=robot,
        factor=pitch_tier.get()
    )


def set_stream_equalizer(self, band_num):
    setattr(aeq, "gain{}".format(band_num), int(self))




window = Tk()
window.title("Voice Transformation")



frame_header=Frame(window,padx=50,pady=50)
frame_header.grid(column=1,row=1)

selected_device = StringVar(window)

devices=allInputDevices()
OPTIONS =list(devices.keys())
selected_device.set(OPTIONS[0]) # default value

def changeMicrophone(event):
    stop_streaming()
    print("change microphone to "+str(event))
    start_streaming(devices[selected_device.get()])



Label(frame_header, text="Input Device").grid(row=1, column=1)
input_device_selector = OptionMenu(frame_header, selected_device,*OPTIONS,command=changeMicrophone)
input_device_selector.grid(row=1,column=2)


frame1 = Frame(window, padx=50, pady=50)
frame1.grid(column=1, row=2)
Label(frame1, text="num semitones").grid(row=1, column=1)
num_semitones = Scale(
    frame1,
    from_=-10,
    to=20,
    length=200,
    orient=HORIZONTAL,
    command=set_stream_effect,
)
num_semitones.set(0)
num_semitones.grid(row=1, column=2)

Label(frame1, text="Noise Percentage").grid(row=2, column=1)
noise_percentage = Scale(
    frame1,
    from_=0,
    to=100,
    length=200,
    resolution=0.5,
    orient=HORIZONTAL,
    command=set_stream_effect,
)
noise_percentage.set(0)
noise_percentage.grid(row=2, column=2)

Label(frame1, text="Pitch_tier").grid(row=3, column=1)
pitch_tier = Scale(
    frame1,
    from_=1,
    to=4,
    resolution=0.1,
    length=200,
    orient=HORIZONTAL,
    command=set_stream_effect,
)
pitch_tier.set(1)
pitch_tier.grid(row=3, column=2)

Label(frame1, text="Volume").grid(row=4, column=1)
volume = Scale(
    frame1,
    from_=0,
    to=100,
    length=200,
    orient=HORIZONTAL,
    command=set_stream_effect,
)
volume.set(100)
volume.grid(row=4, column=2)



robot_btn=Button(frame1, text="Robot", width=8, height=3, command=lambda:changeRobot(robot_btn),background="white")
robot_btn.grid(
    row=5, column=2
)
Label(window, text="Equalizer").grid(row=0, column=2)
frame2 = Frame(window)
frame2.grid(column=2, row=2)


def vertical_scale(label, row, col, frame):
    def set_gain(self):
        set_stream_equalizer(self, col - 1)

    var = Scale(
        label=label,
        master=frame,
        from_=20,
        to=-100,
        length=200,
        orient=VERTICAL,
        command=set_gain,
    )
    var.grid(row=row, column=col)
    return var


equalizer_band = [
    "20-40 Hz",
    "40-80 Hz",
    "80-160 Hz",
    "160-300 Hz",
    "300-600 Hz",
    "600-1200 Hz",
    "1200-2400 Hz",
    "2400-5000 Hz",
    "5000-10000 Hz",
    "10000-20000 Hz",
]
gain = []

for i in range(len(equalizer_band)):
    vertical_scale(equalizer_band[i], 1, i + 2, frame2)


Button(frame1, text="START", width=20, height=3, command=lambda:start_streaming(devices[selected_device.get()])).grid(
    row=6, column=2
)
Button(frame1, text="STOP", width=20, height=3, command=stop_streaming).grid(
    row=7, column=2
)


window.mainloop()
