from tkinter import (
    Tk,
    Label,
    Button,
    Scale,
    HORIZONTAL,
    VERTICAL,
    IntVar,
    Frame,
)
import subprocess

process: subprocess.Popen = subprocess.Popen(
    ["python", "main.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    universal_newlines=True,
    bufsize=0,
)


def start_streaming():
    print("start streaming")
    process.stdin.write("stream start\n")


def stop_streaming():
    print("stop streaming")
    process.stdin.write("stream stop\n")


def set_stream_effect(self):
    cmd = "stream effect -s {} -n {} -v {}\n".format(
        num_semitones.get(),
        noise_percentage.get() / 100,
        volume.get() / 100,
    )
    print(cmd)
    process.stdin.write(cmd)


def set_stream_equalizer(self, band_num):
    print("stream equalizer -g{} {}\n".format(band_num, self))
    process.stdin.write("stream equalizer -g{} {}\n".format(band_num, self))


window = Tk()
window.title("Voice Transformation")
var1 = IntVar()


frame1 = Frame(window, padx=50, pady=50)
frame1.grid(column=1, row=1)
Label(frame1, text="num semitones").grid(row=1, column=1)
num_semitones = Scale(
    frame1,
    from_=0,
    to=20,
    length=200,
    orient=HORIZONTAL,
    command=set_stream_effect,
)
num_semitones.set(0)
num_semitones.grid(row=1, column=2)

Label(frame1, text="Noise Percentage").grid(row=3, column=1)
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
noise_percentage.grid(row=3, column=2)

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

Label(window, text="Equalizer").grid(row=0, column=2)
frame2 = Frame(window)
frame2.grid(column=2, row=1)


def vertical_scale(label, row, col, frame):
    def set_gain(self):
        set_stream_equalizer(self, col - 1)

    var = Scale(
        label=label,
        master=frame,
        from_=-200,
        to=200,
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


Button(frame1, text="START", width=20, height=3, command=start_streaming).grid(
    row=6, column=2
)
Button(frame1, text="Stop", width=20, height=3, command=stop_streaming).grid(
    row=7, column=2
)


window.mainloop()
