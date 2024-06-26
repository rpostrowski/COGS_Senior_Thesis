import yodel.filter
import scipy.io.wavfile as wav

# Step 1: Read the WAV file
sample_rate, input_signal = wav.read('audio/bounce0.wav')

# Step 2: Create ParametricEQ instance
num_bands = 2
eq = yodel.filter.ParametricEQ(sample_rate, num_bands)

# Step 3: Set parameters for each band
eq.set_band(0, 300, 1.5, -10)  # Band 1: Center freq: 300Hz, Q-factor: 1.5, Gain: -10dB
eq.set_band(1, 2000, 1.5, 10)  # Band 2: Center freq: 2000Hz, Q-factor: 1.5, Gain: 10dB

# Step 4: Process the input signal
output_signal = input_signal.copy()
eq.process(input_signal, output_signal)

# Step 5: Write the processed signal to a new WAV file
wav.write('audio/output/output_bounce0.wav', sample_rate, output_signal)
