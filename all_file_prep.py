import batch_eq
import combine_wavs
import create_coded_folders
import organize_files

def main():
    batch_eq.main()
    create_coded_folders.main()
    organize_files.main()
    combine_wavs.main()

if __name__ == "__main__":
    main()
