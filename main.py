import audio_stream as st

audio = st.AudioStream()
# audio.audio_effect.config_parameters(num_semitones=11)
audio.audio_equalizer.config_equalizer(-100,-100,-100,-100,-100,-100)
audio.start()     # open the the stream
