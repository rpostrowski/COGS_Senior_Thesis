import argparse
import os
import shutil

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


def sort_files(parent_folder):

    # List folders in folder
    folder_contents = os.listdir(parent_folder)
    file_list = [file for file in folder_contents if file.endswith(".wav")]
    sorted_folders = os.listdir(os.path.join(parent_folder, "output/"))

    print(sorted_folders)

    for folder in sorted_folders:
        folder_path = os.path.join(parent_folder, "output", folder)
        print(folder_path)

        # copy in extraA
        shutil.copy2("audio\set1\extraA.wav", os.path.join(folder_path, "extraA.wav"))
        
        # copy in extraB
        shutil.copy2("audio\set1\extraB.wav", os.path.join(folder_path, "extraB.wav"))

        if (folder == "control"):
            print("control")

        else:
            # extract useful info from folder name
            variables = folder.split("_")
            m1, m2, gain, qval = variables

            # get the right m1
            if (m1 == "m1control"):
                print("copy m1.wav")
            elif (m1 == "m1cut"):
                print(f"{m1}_{gain}_{qval}.wav")

            # get the right m2
            if (m1 == "m1control"):
                print("copy m2.wav")

# # Copy and organize files
# for filename in file_list:
#     if filename.startswith('m1'):
#         shutil.copy2(os.path.join(input_folder, filename), m1_folder)
#     elif filename.startswith('m2'):
#         shutil.copy2(os.path.join(input_folder, filename), m2_folder)

def main():
    # parser = argparse.ArgumentParser()

    # parser.add_argument('input_folder', type=str, help='Input folder containing WAV files.')

    # # Parse arguments
    # args = parser.parse_args()

    # # Call batch_eq with provided arguments
    # create_folders(args.input_folder)

    sort_files("audio\set1")

if __name__ == "__main__":
    main()