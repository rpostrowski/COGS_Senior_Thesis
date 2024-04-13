import argparse
import yodel.filter
import scipy.io.wavfile as wav
import os
from pydub import AudioSegment

def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

# Boost center_freq in m1, cut in everything else
def eq_tracks(input_folder, center_freq):

    # Get file list
    file_list = ["m1.wav", "m2.wav", "extraA.wav", "extraB.wav", "extraC.wav"]

    # Make output folder
    full_mix_folder = os.path.join(input_folder, "full_mix")
    os.makedirs(full_mix_folder, exist_ok=True)

    for filename in [filename for filename in file_list]:

        segment = AudioSegment.from_file(os.path.join(input_folder, filename))
        pre_eq_dB = segment.dBFS

        sample_rate, input_signal = wav.read(os.path.join(input_folder, filename))
        num_bands = 1
        eq = yodel.filter.ParametricEQ(sample_rate, num_bands)

        gain = 4 if filename == "m1.wav" else -4

        # Set parameters for the band
        eq.set_band(0, center_freq, 1.5, gain) # band, freq, q, dB

        output_signal = input_signal.copy()
        eq.process(input_signal, output_signal)

        # Write the processed signal to a new WAV file
        output_file_name = f"full_mix\eq_{filename}"
        output_path = os.path.join(input_folder, output_file_name)
        wav.write(output_path, sample_rate, output_signal)

    # EQ mix    
    eq_m1_segment = match_target_amplitude(AudioSegment.from_file(os.path.join(full_mix_folder, "eq_m1.wav")), pre_eq_dB)
    eq_m2_segment = match_target_amplitude(AudioSegment.from_file(os.path.join(full_mix_folder, "eq_m2.wav")), pre_eq_dB)
    eq_extraA_segment = match_target_amplitude(AudioSegment.from_file(os.path.join(full_mix_folder, "eq_extraA.wav")), pre_eq_dB)
    eq_extraB_segment = match_target_amplitude(AudioSegment.from_file(os.path.join(full_mix_folder, "eq_extraB.wav")), pre_eq_dB)
    eq_extraC_segment = match_target_amplitude(AudioSegment.from_file(os.path.join(full_mix_folder, "eq_extraC.wav")), pre_eq_dB)

    eq_full_mix = eq_m1_segment.overlay(eq_m2_segment.overlay(eq_extraA_segment.overlay(eq_extraB_segment.overlay(eq_extraC_segment))))
    eq_full_mix_norm = match_target_amplitude(eq_full_mix, -20.0)

    eq_full_mix_norm.export(os.path.join(full_mix_folder, "eq_full_mix_norm.wav"), format="wav")

    # Raw mix
    m1_segment = AudioSegment.from_file(os.path.join(input_folder, "m1.wav"))
    m2_segment = AudioSegment.from_file(os.path.join(input_folder, "m2.wav"))
    extraA_segment = AudioSegment.from_file(os.path.join(input_folder, "extraA.wav"))
    extraB_segment = AudioSegment.from_file(os.path.join(input_folder, "extraB.wav"))
    extraC_segment = AudioSegment.from_file(os.path.join(input_folder, "extraC.wav"))

    full_mix = m1_segment.overlay(m2_segment.overlay(extraA_segment.overlay(extraB_segment.overlay(extraC_segment))))
    full_mix_norm = match_target_amplitude(full_mix, -20.0)

    full_mix_norm.export(os.path.join(full_mix_folder, "full_mix_norm.wav"), format="wav")

def main(eq0, eq1, eq2):
    eq_tracks("audio\set0", eq0) # bass and kick
    eq_tracks("audio\set1", eq1) # electric and bass
    eq_tracks("audio\set2", eq2) # electric and electric

if __name__ == "__main__":
    main()