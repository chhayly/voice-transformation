"""Handles the interactive shell for the user"""

import lib.audio_stream as st
import pash.shell
import pash.cmds
import pash.command as pcmd
import colorama as cr
from typing import List
cr.init()


"""The basic prompt for the voice-transformation shell"""
BPROMPT: str = cr.Fore.LIGHTBLUE_EX + 'voice-transformation' + \
    cr.Fore.LIGHTBLACK_EX + '$ ' + cr.Fore.RESET
"""The shell itself"""
sh: pash.shell.Shell = pash.shell.Shell(prompt=BPROMPT)
"""The main AudioStream object"""
audio_stream: st.AudioStream = st.AudioStream()


def audio_effect_config(cmd: pcmd.Command,
                        args: List[str],
                        noise_percentage_factor=audio_stream.audio_effect.noise_percentage_factor,
                        time_stretch_rate=audio_stream.audio_effect.time_stretch_rate,
                        num_semitones=audio_stream.audio_effect.num_semitones,
                        is_invert_polarity=audio_stream.audio_effect.is_invert_polarity,
                        vol=audio_stream.audio_effect.vol) -> None:
    audio_stream.audio_effect.config_parameters(
        noise_percentage_factor,
        time_stretch_rate,
        num_semitones,
        is_invert_polarity, vol)


def audio_equalizer_config(cmd: pcmd.Command,
                           args: List[str],
                           gain1=audio_stream.audio_equalizer.gain1,
                           gain2=audio_stream.audio_equalizer.gain2,
                           gain3=audio_stream.audio_equalizer.gain3,
                           gain4=audio_stream.audio_equalizer.gain4,
                           gain5=audio_stream.audio_equalizer.gain5,
                           gain6=audio_stream.audio_equalizer.gain6,
                           gain7=audio_stream.audio_equalizer.gain7,
                           gain8=audio_stream.audio_equalizer.gain8,
                           gain9=audio_stream.audio_equalizer.gain9,
                           gain10=audio_stream.audio_equalizer.gain10) -> None:

    audio_stream.audio_equalizer.config_equalizer(
        gain1, gain2, gain3, gain4, gain5, gain6, gain7, gain8, gain9, gain10)


def stop_stream(cmd: pcmd.Command,
                args: List[str]):
    audio_stream.stop()


def start_stream(cmd: pcmd.Command,
                 args: List[str]):
    audio_stream.start()	


def start() -> None:
    sh.add_cmd(pcmd.Command('clear', 'cls',
               callback=pash.cmds.clear, hint='clear the screen'))

    audio_effect = pcmd.Command(
        'effect', callback=audio_effect_config, hint='Configure the audio effect')
    audio_effect.add_arg('--noise_percentage_factor', '-n',
                         type=float, help='The noise percentage factor')
    audio_effect.add_arg('--time_stretch_rate', '-t',
                         type=float, help='The time stretch rate')
    audio_effect.add_arg('--num_semitones', '-s', type=int,
                         help='The number of semitones')
    audio_effect.add_arg('--is_invert_polarity', '-i',
                         type=bool, help='Invert the polarity')
    audio_effect.add_arg('--vol', '-v', type=float, help='The volume')

    audio_equalizer = pcmd.Command(
        'equalizer', callback=audio_equalizer_config, hint='Configure the audio equalizer')
    audio_equalizer.add_arg('--gain1', '-g1', type=float,
                            help='The gain for band 1')
    audio_equalizer.add_arg('--gain2', '-g2', type=float,
                            help='The gain for band 2')
    audio_equalizer.add_arg('--gain3', '-g3', type=float,
                            help='The gain for band 3')
    audio_equalizer.add_arg('--gain4', '-g4', type=float,
                            help='The gain for band 4')
    audio_equalizer.add_arg('--gain5', '-g5', type=float,
                            help='The gain for band 5')
    audio_equalizer.add_arg('--gain6', '-g6', type=float,
                            help='The gain for band 6')
    audio_equalizer.add_arg('--gain7', '-g7', type=float,
                            help='The gain for band 7')
    audio_equalizer.add_arg('--gain8', '-g8', type=float,
                            help='The gain for band 8')
    audio_equalizer.add_arg('--gain9', '-g9', type=float,
                            help='The gain for band 9')
    audio_equalizer.add_arg('--gain10', '-g10', type=float,
                            help='The gain for band 10')

    sh.add_cmd(
        pcmd.CascCommand('stream', cmds=[
            pcmd.Command('start', callback=start_stream,
                         hint='Start the audio stream'),
            pcmd.Command('stop', callback=stop_stream,
                         hint='Stop the audio stream'),
            audio_effect, audio_equalizer]))

    sh.prompt_until_exit()
