import argparse
import os
import shutil

def create_folders(input_folder):
    # Create output folders if they don't exist

    output_folder = os.path.join(input_folder, 'output')
    os.makedirs(output_folder, exist_ok=True)

    control = os.path.join(output_folder, 'control')

    m1boost3dB_m2control_q0 = os.path.join(output_folder, 'm1boost3dB_m2control_q0')
    m1boost7dB_m2control_q1 = os.path.join(output_folder, 'm1boost7dB_m2control_q1')
    
    m1cut3dB_m2control_q0 = os.path.join(output_folder, 'm1cut3dB_m2control_q0')
    m1cut7dB_m2control_q1 = os.path.join(output_folder, 'm1cut7dB_m2control_q1')
    
    m1control_m2boost3dB_q0 = os.path.join(output_folder, 'm1control_m2boost3dB_q0')
    m1control_m2boost7dB_q1 = os.path.join(output_folder, 'm1control_m2boost7dB_q1')
    
    m1control_m2cut3dB_q0 = os.path.join(output_folder, 'm1control_m2cut3dB_q0')
    m1control_m2cut7dB_q1 = os.path.join(output_folder, 'm1control_m2cut7dB_q1')
    
    m1boost3dB_m2cut3dB_q0 = os.path.join(output_folder, 'm1boost3dB_m2cut3dB_q0')
    m1boost7dB_m2cut7dB_q1 = os.path.join(output_folder, 'm1boost7dB_m2cut7dB_q1')
    
    m1cut3dB_m2boost3dB_q0 = os.path.join(output_folder, 'm1cut3dB_m2boost3dB_q0')
    m1cut7dB_m2boost7dB_q1 = os.path.join(output_folder, 'm1cut7dB_m2boost7dB_q1')


    os.makedirs(control, exist_ok=True)
    
    os.makedirs(m1boost3dB_m2control_q0, exist_ok=True)
    os.makedirs(m1boost7dB_m2control_q1, exist_ok=True)
    
    os.makedirs(m1cut3dB_m2control_q0, exist_ok=True)
    os.makedirs(m1cut7dB_m2control_q1, exist_ok=True)

    os.makedirs(m1control_m2boost3dB_q0, exist_ok=True)
    os.makedirs(m1control_m2boost7dB_q1, exist_ok=True)
    
    os.makedirs(m1control_m2cut3dB_q0, exist_ok=True)
    os.makedirs(m1control_m2cut7dB_q1, exist_ok=True)
    
    os.makedirs(m1boost3dB_m2cut3dB_q0, exist_ok=True)
    os.makedirs(m1boost7dB_m2cut7dB_q1, exist_ok=True)

    os.makedirs(m1cut3dB_m2boost3dB_q0, exist_ok=True)
    os.makedirs(m1cut7dB_m2boost7dB_q1, exist_ok=True)

    # # List files in input folder
    # file_list = os.listdir(input_folder)

    # # Copy and organize files
    # for filename in file_list:
    #     if filename.startswith('m1'):
    #         shutil.copy2(os.path.join(input_folder, filename), m1_folder)
    #     elif filename.startswith('m2'):
    #         shutil.copy2(os.path.join(input_folder, filename), m2_folder)

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('input_folder', type=str, help='Input folder containing WAV files.')

    # Parse arguments
    args = parser.parse_args()

    # Call batch_eq with provided arguments
    create_folders(args.input_folder)

if __name__ == "__main__":
    main()