import audio_stream as st
from tkinter import *

start_audio=False
audio = st.AudioStream()





window=Tk()
window.title("Voice Transformation")
var1 = IntVar()


frame1 = Frame(window,padx=50,pady=50)
frame1.grid(column=1,row=1)
Label(frame1,text="num semitones").grid(row=1,column=1)
numsentom= Scale(frame1, from_=-20, to=50,length=200, orient=HORIZONTAL)
numsentom.set(0)
numsentom.grid(row=1,column=2)

Label(frame1,text="time_stretch").grid(row=2,column=1)
time_stretch= Scale(frame1, from_=0.5, to=5.0,length=200, resolution=0.1,orient=HORIZONTAL)
time_stretch.set(0.0)
time_stretch.grid(row=2,column=2)

Label(frame1,text="Noise Percentage").grid(row=3,column=1)
noise_percentage= Scale(frame1, from_=0, to=20,length=200, resolution=0.5,orient=HORIZONTAL)
noise_percentage.set(0)
noise_percentage.grid(row=3,column=2)

Label(frame1,text="Volume").grid(row=4,column=1)
volume= Scale(frame1, from_=0, to=50,length=200, orient=HORIZONTAL)
volume.set(0)
volume.grid(row=4,column=2)

Label(frame1,text="Invert",pady=10).grid(row=5,column=1)
invert= Checkbutton(frame1,height=5,width=5,onvalue=True,offvalue=False,variable=var1)
# invert.set(0)
invert.grid(row=5,column=2)


Label(window,text="Unknown Title").grid(row=0,column=2)
frame2 = Frame(window)
frame2.grid(column=2,row=1)

def vertical_scale(row,col,frame):
    var = Scale(frame, from_=1, to=100, length=200, orient=VERTICAL)
    var.grid(row=row, column=col)
    return var


vertical_scale(1,2,frame2)
vertical_scale(1,3,frame2)
vertical_scale(1,4,frame2)
vertical_scale(1,5,frame2)
vertical_scale(1,6,frame2)
vertical_scale(1,7,frame2)
vertical_scale(1,8,frame2)
vertical_scale(1,9,frame2)
vertical_scale(1,10,frame2)
vertical_scale(1,11,frame2)




def PrintTest():
    print(var1)
def startAudio():
    audio.audio_effect.config_parameters(
        num_semitones=float(numsentom.get()),
        is_invert_polarity=var1,vol=float(volume.get()),
        noise_percentage_factor=float(noise_percentage.get()))

    audio.start()
def stopAudio():
    audio.stop()

Button(frame1,text="START",width=20,height=3,command=startAudio).grid(row=6,column=2)
Button(frame1,text="Stop",width=20,height=3,command=stopAudio).grid(row=7,column=2)



window.mainloop()






