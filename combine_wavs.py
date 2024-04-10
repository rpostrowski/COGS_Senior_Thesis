#!/bin/env python

import os
from pydub import AudioSegment
import os
import argparse


# combine_files("audio/set1/output")
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

        combined_track = m2_segment.overlay(m1_segment.overlay(extraB_segment.overlay(extraA_segment)))

        combined_track.export(os.path.join(folder_path, "hm.wav"), format="wav")


# FOR COMMAND LINE USE
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('parent_folder', type=str, help='Input folder containing WAV files.')
    args = parser.parse_args()

    # Call batch_eq with provided arguments
    combine_files(args.parent_folder)

if __name__ == "__main__":
    main()