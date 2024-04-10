#!/bin/env python

import os
from pydub import AudioSegment
import os
import argparse

def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

def combine_files(parent_folder):

    all_folders = os.listdir(parent_folder)

    for folder in all_folders:

        folder_path = os.path.join(parent_folder,folder)
        files = os.listdir(folder_path)
        
        extraA_segment = AudioSegment.from_file("audio/set1/output/control/extraA.wav")
        extraB_segment = AudioSegment.from_file("audio/set1/output/control/extraB.wav")

        audio_files = [f for f in files if f.startswith("m")]
        m1_segment = AudioSegment.from_file(os.path.join(folder_path, audio_files[0]))
        m2_segment = AudioSegment.from_file(os.path.join(folder_path, audio_files[1]))

        two_instr = m1_segment.overlay(m2_segment)
        one_extra = two_instr.overlay(extraA_segment)
        two_extra = one_extra.overlay(extraB_segment)

        two_instr_norm = match_target_amplitude(two_instr, -20.0)
        one_extra_norm = match_target_amplitude(one_extra, -20.0)
        two_extra_norm = match_target_amplitude(two_extra, -20.0)

        two_instr_norm.export(os.path.join(folder_path, "two_instr_norm.wav"), format="wav")
        one_extra_norm.export(os.path.join(folder_path, "one_extra_norm.wav"), format="wav")
        two_extra_norm.export(os.path.join(folder_path, "two_extra_norm.wav"), format="wav")


# EXAMPLE - $ python3 combine_wavs.py "audio\set1\output"
# def main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('parent_folder', type=str, help='Input folder containing WAV files.')
#     args = parser.parse_args()
#     combine_files(args.parent_folder)

def main():
    combine_files("audio\set0\output")
    combine_files("audio\set1\output")
    combine_files("audio\set2\output")

if __name__ == "__main__":
    main()