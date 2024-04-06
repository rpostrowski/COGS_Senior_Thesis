import argparse
import os

def create_folders(input_folder):
    # Create output folders if they don't exist

    output_folder = os.path.join(input_folder, 'output')
    os.makedirs(output_folder, exist_ok=True)

    control = os.path.join(output_folder, 'control')

    m1boost_m2control_3dB_q0 = os.path.join(output_folder, 'm1boost_m2control_3dB_q0')
    m1boost_m2control_7dB_q0 = os.path.join(output_folder, 'm1boost_m2control_7dB_q0')
    
    m1cut_m2control_3dB_q0 = os.path.join(output_folder, 'm1cut_m2control_3dB_q0')
    m1cut_m2control_7dB_q0 = os.path.join(output_folder, 'm1cut_m2control_7dB_q0')
    
    m1control_m2boost_3dB_q0 = os.path.join(output_folder, 'm1control_m2boost_3dB_q0')
    m1control_m2boost_7dB_q1 = os.path.join(output_folder, 'm1control_m2boost_7dB_q1')
    
    m1control_m2cut_3dB_q0 = os.path.join(output_folder, 'm1control_m2cut_3dB_q0')
    m1control_m2cut_7dB_q1 = os.path.join(output_folder, 'm1control_m2cut_7dB_q1')
    
    m1boost_m2cut_3dB_q0 = os.path.join(output_folder, 'm1boost_m2cut_3dB_q0')
    m1boost_m2cut_7dB_q1 = os.path.join(output_folder, 'm1boost_m2cut_7dB_q1')
    
    m1cut_m2boost_3dB_q0 = os.path.join(output_folder, 'm1cut_m2boost_3dB_q0')
    m1cut_m2boost_7dB_q1 = os.path.join(output_folder, 'm1cut_m2boost_7dB_q1')


    os.makedirs(control, exist_ok=True)
    
    os.makedirs(m1boost_m2control_3dB_q0, exist_ok=True)
    os.makedirs(m1boost_m2control_7dB_q0, exist_ok=True)
    
    os.makedirs(m1cut_m2control_3dB_q0, exist_ok=True)
    os.makedirs(m1cut_m2control_7dB_q0, exist_ok=True)

    os.makedirs(m1control_m2boost_3dB_q0, exist_ok=True)
    os.makedirs(m1control_m2boost_7dB_q1, exist_ok=True)
    
    os.makedirs(m1control_m2cut_3dB_q0, exist_ok=True)
    os.makedirs(m1control_m2cut_7dB_q1, exist_ok=True)
    
    os.makedirs(m1boost_m2cut_3dB_q0, exist_ok=True)
    os.makedirs(m1boost_m2cut_7dB_q1, exist_ok=True)

    os.makedirs(m1cut_m2boost_3dB_q0, exist_ok=True)
    os.makedirs(m1cut_m2boost_7dB_q1, exist_ok=True)



def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('input_folder', type=str, help='Input folder containing WAV files.')

    # Parse arguments
    args = parser.parse_args()

    # Call batch_eq with provided arguments
    create_folders(args.input_folder)


if __name__ == "__main__":
    main()