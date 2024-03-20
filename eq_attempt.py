import yodel.filter
import scipy.io.wavfile as wav

# Step 1: Read the WAV file
# Replace 'input_file.wav' with the path to your WAV file
sample_rate, input_signal = wav.read('audio/bounce0.wav')

# Step 2: Create ParametricEQ instance
num_bands = 5  # Example: 5 frequency bands
eq = yodel.filter.ParametricEQ(sample_rate, num_bands)

# Step 3: Set parameters for each band
# Example parameters, you should adjust these based on your requirements
eq.set_band(0, 300, 1.5, -10)   # Band 1: Center freq: 100Hz, Resonance: 1.5, Gain: 3dB
eq.set_band(1, 2000, 1.5, 10)  # Band 5: Center freq: 5000Hz, Resonance: 1.5, Gain: 2dB

# Step 4: Process the input signal
output_signal = input_signal.copy()  # Make a copy to avoid modifying the original signal
eq.process(input_signal, output_signal)

# Step 5: Write the processed signal to a new WAV file
# Replace 'output_file.wav' with the desired output file path
wav.write('audio/output/output_bounce0.wav', sample_rate, output_signal)
