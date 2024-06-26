import argparse
import os

def create_folders(input_folder):
    # Create output folders if they don't exist

    output_folder = os.path.join(input_folder, 'output')
    os.makedirs(output_folder, exist_ok=True)

    # Make control folder
    control = os.path.join(output_folder, 'control')
    os.makedirs(control, exist_ok=True)

    m1_options = ["m1cut", "m1boost", "m1control"]
    db_levels = ["5dB", "8dB"]

    # Loop through each combination and create the directories
    for m1 in m1_options:

        # Define what the options are for m2
        if (m1 == "m1cut"):
            m2_options = ["m2boost", "m2control"]
        elif (m1 == "m1boost"):
            m2_options = ["m2cut", "m2control"]
        elif (m1 == "m1control"):
            m2_options = ["m2cut", "m2boost"]
        
        for m2 in m2_options:
            for db_level in db_levels:
                directory_path = os.path.join(output_folder, f"{m1}_{m2}_{db_level}")
                os.makedirs(directory_path, exist_ok=True)

    os.makedirs(os.path.join(output_folder, "mirrored_5dB"), exist_ok=True)
    os.makedirs(os.path.join(output_folder, "mirrored_8dB"), exist_ok=True)


# EXAMPLE - $ python3 create_coded_folders.py "audio\set1"
# def main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('input_folder', type=str, help='Input folder containing WAV files.')
#     args = parser.parse_args()
#     create_folders(args.input_folder)

def main(folder):
    create_folders(folder)

if __name__ == "__main__":
    main()