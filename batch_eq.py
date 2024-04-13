import argparse
import yodel.filter
import scipy.io.wavfile as wav
import os

# We're expecting to receive a folder with four audio files, named in the following way:
# ["m1.wav", "m2.wav", "extraA.wav", "extraB.wav"]
   
def treat_prepped_folder(input_folder, m1_freq, m2_freq, q_factor):

    file_list = os.listdir(input_folder)

    # For both "m1.wav" and "m2.wav"...
    for filename in [filename for filename in file_list if filename.startswith('m')]:

        sample_rate, input_signal = wav.read(os.path.join(input_folder, filename))

        center_freq = m1_freq if filename == "m1.wav" else m2_freq

        # For the four gain options...
        for gain in [-7, -3, 3, 7]:
            
            # Create an instance of the custom equalizer
            num_bands = 1
            eq = yodel.filter.ParametricEQ(sample_rate, num_bands)

            # Set parameters for the band
            eq.set_band(0, center_freq, 1.5, gain)

            # Process the input signal
            output_signal = input_signal.copy()
            eq.process(input_signal, output_signal)

            # Prep the features for file coding
            which_file = "m1" if filename == "m1.wav" else "m2"
            boost_cut = "cut" if gain < 0 else "boost"
            dB = abs(gain)

            # Write the processed signal to a new WAV file
            output_file_name = f"{which_file}{boost_cut}_{dB}dB.wav"
            output_path = os.path.join(input_folder, output_file_name)
            wav.write(output_path, sample_rate, output_signal)


def equalize_file(input_path, output_path, center_freq, q_factor, gain):

    sample_rate, input_signal = wav.read(input_path)

    # Create ParametricEQ instance
    num_bands = 1
    eq = yodel.filter.ParametricEQ(sample_rate, num_bands)

    # Set parameters for the band
    eq.set_band(0, center_freq, q_factor, gain)

    # Process the input signal
    output_signal = input_signal.copy()
    eq.process(input_signal, output_signal)

    # Write the processed signal to a new WAV file
    output_path = "april4new.wav"
    wav.write(output_path, sample_rate, output_signal)

def equalize_folder(input_folder, output_folder, center_freq, q_factor, gain):

    file_list = os.listdir(input_folder)

    for filename in file_list:
        # Construct the full path to the file
        file_path = os.path.join(input_folder, filename)

        sample_rate, input_signal = wav.read(file_path)

        # Step 2: Create ParametricEQ instance
        num_bands = 2
        eq = yodel.filter.ParametricEQ(sample_rate, num_bands)

        # Step 3: Set parameters for each band
        eq.set_band(0, center_freq, q_factor, gain)

        # Step 4: Process the input signal
        output_signal = input_signal.copy()
        eq.process(input_signal, output_signal)

        # Step 5: Write the processed signal to a new WAV file
        output_path = os.path.join(output_folder, "april4new.wav")
        wav.write(output_path, sample_rate, output_signal)


# EXAMPLE - $ python3 batch_eq.py "set0" 202
# def main():
    # parser = argparse.ArgumentParser(description='Apply batch equalization to WAV files in a folder.')

    # parser.add_argument('input_folder', type=str, help='Input folder containing WAV files.')
    # parser.add_argument('center_freq', type=int)
    # args = parser.parse_args()

    # # Call batch_eq with provided arguments
    # treat_prepped_folder(args.input_folder, args.center_freq)

    # parser.add_argument('input_folder', type=str, help='Input folder containing WAV files.')
    # parser.add_argument('output_folder', type=str, help='Output folder to save processed WAV files.')
    # parser.add_argument('center_freq', type=int)
    # parser.add_argument('q_factor', type=float)
    # parser.add_argument('gain', type=int)
    # equalize_folder(args.input_folder, args.output_folder, args.center_freq, args.q_factor, args.gain)

def main():
    treat_prepped_folder("audio\set0", 100, 200, 1.5) # bass and kick
    treat_prepped_folder("audio\set1", 300, 400, 1.5) # electric and bass
    treat_prepped_folder("audio\set2", 500, 600, 1.5) # electric and electric

if __name__ == "__main__":
    main()