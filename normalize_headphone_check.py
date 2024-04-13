import os
from pydub import AudioSegment

def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

def normalize_headphone_check(folder):
    files = os.listdir(folder)

    # for file in files:
    #     segment = AudioSegment.from_file(os.path.join(folder, file))
    #     output_file = match_target_amplitude(segment, -20.0)
    #     output_file.export(os.path.join(folder, "norm_" + file), format="wav")

    segment = AudioSegment.from_file(os.path.join(folder, "noise_calib_stim.wav"))
    output_file = match_target_amplitude(segment, -20.0)
    output_file.export(os.path.join(folder, "norm_noise_calib_stim.wav"), format="wav")

    

def main():
    normalize_headphone_check("headphone_check_files")

if __name__ == "__main__":
    main()