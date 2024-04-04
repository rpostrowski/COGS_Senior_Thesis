import argparse
import yodel.filter
import scipy.io.wavfile as wav
import os

def batch_eq(input_folder, output_folder):

# input_folder = 'audio/set0/input'
# output_folder = 'audio/set0/output'

    file_list = os.listdir(input_folder)

    for filename in file_list:
        # Construct the full path to the file
        file_path = os.path.join(input_folder, filename)

        sample_rate, input_signal = wav.read(file_path)

        # Step 2: Create ParametricEQ instance
        num_bands = 2
        eq = yodel.filter.ParametricEQ(sample_rate, num_bands)

        # Step 3: Set parameters for each band
        eq.set_band(0, 300, 1.5, -10)  # Band 1: Center freq: 300Hz, Q-factor: 1.5, Gain: -10dB
        # eq.set_band(1, 2000, 1.5, 10)  # Band 2: Center freq: 2000Hz, Q-factor: 1.5, Gain: 10dB

        # Step 4: Process the input signal
        output_signal = input_signal.copy()
        eq.process(input_signal, output_signal)

        # Step 5: Write the processed signal to a new WAV file
        output_path = os.path.join(output_folder, "test.wav")
        wav.write(output_path, sample_rate, output_signal)

def main():
    parser = argparse.ArgumentParser(description='Apply batch equalization to WAV files in a folder.')

    parser.add_argument('input_folder', type=str, help='Input folder containing WAV files.')
    parser.add_argument('output_folder', type=str, help='Output folder to save processed WAV files.')

    # Parse arguments
    args = parser.parse_args()

    # Call batch_eq with provided arguments
    batch_eq(args.input_folder, args.output_folder)

if __name__ == "__main__":
    main()