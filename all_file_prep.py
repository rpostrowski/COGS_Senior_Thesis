import batch_eq
import combine_wavs
import create_coded_folders
import organize_files

def main():
    print("Starting: batch_eq")
    batch_eq.main()
    print("Finished: batch_eq")

    print("Starting: create_coded_folders")
    create_coded_folders.main()
    print("Finished: create_coded_folders")

    print("Starting: organize_files")
    organize_files.main()
    print("Finished: organize_files")

    print("Starting: combine_wavs")
    combine_wavs.main()
    print("Finished: combine_wavs")

if __name__ == "__main__":
    main()
