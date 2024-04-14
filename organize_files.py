import argparse
import os
import shutil

def sort_files(parent_folder):

    folder_contents = os.listdir(parent_folder)
    # file_list = [file for file in folder_contents if file.endswith(".wav")]
    sorted_folders = os.listdir(os.path.join(parent_folder, "output/"))

    for folder in sorted_folders:
        folder_path = os.path.join(parent_folder, "output", folder)

        # Copy in extraA.wav
        shutil.copy2(os.path.join(parent_folder, "extraA.wav"), os.path.join(folder_path, "extraA.wav"))
        
        # Copy in extraB.wav
        shutil.copy2(os.path.join(parent_folder, "extraB.wav"), os.path.join(folder_path, "extraB.wav"))

        # Copy in extraC.wav
        shutil.copy2(os.path.join(parent_folder, "extraC.wav"), os.path.join(folder_path, "extraC.wav"))

        # Handle control folder
        if (folder == "control"):
            shutil.copy2(os.path.join(parent_folder,"m1.wav"), os.path.join(folder_path, "m1.wav"))
            shutil.copy2(os.path.join(parent_folder, "m2.wav"), os.path.join(folder_path, "m2.wav"))
        elif (folder == "mirrored"):
            shutil.copy2(os.path.join(parent_folder,"m1_mirrored.wav"), os.path.join(folder_path, "m1_mirrored.wav"))
            shutil.copy2(os.path.join(parent_folder, "m2_mirrored.wav"), os.path.join(folder_path, "m2_mirrored.wav"))
        # For all other folders...
        else:
            # Extract useful info from folder name
            variables = folder.split("_")
            m1, m2, gain = variables

            # Copy in the correct version of the m1 file
            if (m1 == "m1control"):
                shutil.copy2(os.path.join(parent_folder,"m1.wav"), os.path.join(folder_path, "m1.wav"))
            else:
                m1_string = f"{m1}_{gain}.wav"
                m1_path = os.path.join(parent_folder, m1_string)
                shutil.copy2(m1_path, os.path.join(folder_path, m1_string))

            # Copy in the correct version of the m2 file
            if (m2 == "m2control"):
                shutil.copy2(os.path.join(parent_folder,"m2.wav"), os.path.join(folder_path, "m2.wav"))
            else:
                m2_string = f"{m2}_{gain}.wav"
                m2_path = os.path.join(parent_folder, m2_string)
                shutil.copy2(m2_path, os.path.join(folder_path, m2_string))


# EXAMPLE - $ python3 organize_files.py "audio\set1"
# def main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('input_folder', type=str, help='Input folder containing WAV files.')
#     args = parser.parse_args()
#     sort_files(args.input_folder)

def main(folder):
    sort_files(folder)

if __name__ == "__main__":
    main()