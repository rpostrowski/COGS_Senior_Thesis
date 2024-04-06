import argparse
import os
import shutil

def sort_files(parent_folder):

    # List folders in folder
    folder_contents = os.listdir(parent_folder)
    file_list = [file for file in folder_contents if file.endswith(".wav")]
    sorted_folders = os.listdir(os.path.join(parent_folder, "output/"))

    for folder in sorted_folders:
        folder_path = os.path.join(parent_folder, "output", folder)

        # copy in extraA
        shutil.copy2("audio\set1\extraA.wav", os.path.join(folder_path, "extraA.wav"))
        
        # copy in extraB
        shutil.copy2("audio\set1\extraB.wav", os.path.join(folder_path, "extraB.wav"))

        if (folder == "control"):
            shutil.copy2("audio\set1\extraA.wav", os.path.join(folder_path, "extraA.wav"))
            shutil.copy2("audio\set1\extraB.wav", os.path.join(folder_path, "extraB.wav"))

        else:
            # extract useful info from folder name
            variables = folder.split("_")
            m1, m2, gain, qval = variables

            if (m1 == "m1control"):
                shutil.copy2("audio\set1\m1.wav", os.path.join(folder_path, "m1.wav"))
            else:
                # get the right m1 string
                m1_string = f"{m1}_{gain}_{qval}.wav"
                m1_path = os.path.join(parent_folder, m1_string)
                shutil.copy2(m1_path, os.path.join(folder_path, m1_string))


            if (m2 == "m2control"):
                shutil.copy2("audio\set1\m2.wav", os.path.join(folder_path, "m2.wav"))
            else:
                # get the right m2
                m2_string = f"{m2}_{gain}_{qval}.wav"
                m2_path = os.path.join(parent_folder, m2_string)
                shutil.copy2(m2_path, os.path.join(folder_path, m2_string))



def main():
    # parser = argparse.ArgumentParser()

    # parser.add_argument('input_folder', type=str, help='Input folder containing WAV files.')

    # # Parse arguments
    # args = parser.parse_args()

    sort_files("audio\set1")

if __name__ == "__main__":
    main()