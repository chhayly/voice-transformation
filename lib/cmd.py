import lib.audio_stream as st
import pash.shell
import pash.cmds
import pash.command as pcmd
import colorama as cr
from typing import List

cr.init()


"""The basic prompt for the voice-transformation shell"""
BPROMPT: str = (
    cr.Fore.LIGHTBLUE_EX
    + "voice-transformation"
    + cr.Fore.LIGHTBLACK_EX
    + "$ "
    + cr.Fore.RESET
)
"""The shell itself"""
sh: pash.shell.Shell = pash.shell.Shell(prompt=BPROMPT)
"""The main AudioStream object"""
audio_stream: st.AudioStream = st.AudioStream()
ae: st.AudioEffect = audio_stream.audio_effect
aeq: st.AudioEqualizer = audio_stream.audio_equalizer


def audio_effect_config(
    cmd: pcmd.Command,
    args: List[str],
    noise_percentage_factor=ae.noise_percentage_factor,
    time_stretch_rate=ae.time_stretch_rate,
    num_semitones=ae.num_semitones,
    is_invert_polarity=ae.is_invert_polarity,
    vol=ae.vol,
    is_robot=ae.is_robot,
    factor=ae.factor

    
) -> None:
    ae.config_parameters(
        noise_percentage_factor,
        time_stretch_rate,
        num_semitones,
        is_invert_polarity,
        vol,
        is_robot,
        factor
    )


def audio_equalizer_config(
    cmd: pcmd.Command,
    args: List[str],
    gain1=aeq.gain1,
    gain2=aeq.gain2,
    gain3=aeq.gain3,
    gain4=aeq.gain4,
    gain5=aeq.gain5,
    gain6=aeq.gain6,
    gain7=aeq.gain7,
    gain8=aeq.gain8,
    gain9=aeq.gain9,
    gain10=aeq.gain10,
) -> None:
    aeq.config_equalizer(
        gain1, gain2, gain3, gain4, gain5, gain6, gain7, gain8, gain9, gain10
    )


def stop_stream(cmd: pcmd.Command, args: List[str]):
    audio_stream.stop()


def start_stream(cmd: pcmd.Command, args: List[str]):
    audio_stream.start()


def start() -> None:
    sh.add_cmd(
        pcmd.Command("clear", "cls", callback=pash.cmds.clear, hint="clear the screen")
    )

    audio_effect = pcmd.Command(
        "effect", callback=audio_effect_config, hint="Configure the audio effect"
    )
    audio_effect.add_arg(
        "--noise_percentage_factor",
        "-n",
        type=float,
        help="The noise percentage factor",
    )
    audio_effect.add_arg(
        "--time_stretch_rate", "-t", type=float, help="The time stretch rate"
    )
    audio_effect.add_arg(
        "--num_semitones", "-s", type=int, help="The number of semitones"
    )
    audio_effect.add_arg(
        "--is_invert_polarity", "-i", type=bool, help="Invert the polarity"
    )
    audio_effect.add_arg(
        "--is_robot", "-r", type=bool, help="add robot voice"
    )
    audio_effect.add_arg("--vol", "-v", type=float, help="The volume")
    audio_effect.add_arg("--pitch-tier", "-p", type=float, help="pitch tier")


    audio_equalizer = pcmd.Command(
        "equalizer",
        callback=audio_equalizer_config,
        hint="Configure the audio equalizer",
    )
    audio_equalizer.add_arg(
        "--gain1", "-g1", default=aeq.gain1, type=int, help="The gain for band 1"
    )
    audio_equalizer.add_arg(
        "--gain2", "-g2", default=aeq.gain2, type=int, help="The gain for band 2"
    )
    audio_equalizer.add_arg(
        "--gain3", "-g3", default=aeq.gain3, type=int, help="The gain for band 3"
    )
    audio_equalizer.add_arg(
        "--gain4", "-g4", default=aeq.gain4, type=int, help="The gain for band 4"
    )
    audio_equalizer.add_arg(
        "--gain5", "-g5", default=aeq.gain5, type=int, help="The gain for band 5"
    )
    audio_equalizer.add_arg(
        "--gain6", "-g6", default=aeq.gain6, type=int, help="The gain for band 6"
    )
    audio_equalizer.add_arg(
        "--gain7", "-g7", default=aeq.gain7, type=int, help="The gain for band 7"
    )
    audio_equalizer.add_arg(
        "--gain8", "-g8", default=aeq.gain8, type=int, help="The gain for band 8"
    )
    audio_equalizer.add_arg(
        "--gain9", "-g9", default=aeq.gain9, type=int, help="The gain for band 9"
    )
    audio_equalizer.add_arg(
        "--gain10", "-g10", default=aeq.gain10, type=int, help="The gain for band 10"
    )

    sh.add_cmd(
        pcmd.CascCommand(
            "stream",
            cmds=[
                pcmd.Command(
                    "start", callback=start_stream, hint="Start the audio stream"
                ),
                pcmd.Command(
                    "stop", callback=stop_stream, hint="Stop the audio stream"
                ),
                audio_effect,
                audio_equalizer,
            ],
        )
    )

    sh.prompt_until_exit()
