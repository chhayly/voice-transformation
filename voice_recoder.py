import streamlit as st
from pathlib import Path
import numpy as np
import soundfile as sf
import os
import librosa
import glob
from helper import  create_spectrogram, read_audio, record, save_record
from transform import add_white_noise,time_stretch,pitch_scale,invert_polarity




num_semitones=st.sidebar.slider("semitomes",max_value=50,min_value=-20)
time_stretch_rate =st.sidebar.slider("time_stretch",min_value=0.5,max_value=5.0,step=0.1)
white_noise_precent=st.sidebar.slider("noise_percent",min_value=0.0,max_value=20.0,step=0.5)
Inverse= st.sidebar.selectbox("Inverse Or Not",[True,False])
filename = st.text_input("Choose a filename: ")
show=0
if st.button(f"Click to Record"):
    if filename == "":
        st.warning("Choose a filename.")
    else:
        record_state = st.text("Recording...")
        duration = 5  # seconds
        fs = 22050
        myrecording = record(duration, fs)
        record_state.text(f"Saving sample as {filename}.mp3")

        path_myrecording = f"{filename}.mp3"
        # myrecording=pitch_scale(myrecording,22050,5)
        features=[]
        X = np.squeeze(myrecording)
        stft = np.abs(librosa.stft(X))
        augment = pitch_scale(X, fs, num_semitones)
        augment = time_stretch(augment, time_stretch_rate)
        if Inverse == True:
            augment = invert_polarity(augment)


        save_record(path_myrecording, augment, fs)
        record_state.text(f"Done! Saved sample as {filename}.mp3")
        # show=1
        #
        #
        st.audio(read_audio(path_myrecording))
        # fig = create_spectrogram(path_myrecording)
        # st.pyplot(fig)







#
# if st.button("Transform"):
#     if filename=="":
#         st.warning("Choose a filename.")
#     else:
#         data,sample_rate=librosa.load(f"{filename}.mp3")
#         augment = pitch_scale(data, sample_rate,num_semitones )
#         augment = time_stretch(augment,time_stretch_rate)
#         if Inverse==True:
#             augment= invert_polarity(augment)
#
#
#         sf.write("augmented_audio.wav", augment, sample_rate)
#
#         st.audio(read_audio("augmented_audio.wav"))




