import batch_eq
import combine_wavs
import create_coded_folders
import organize_files
import normalize_headphone_check
import full_mix_eq

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

    print("Starting: normalizing headphone check files")
    normalize_headphone_check.main()
    print("Finished: normalizing headphone check files")
    
    print("Starting: full_mix_eq")
    full_mix_eq.main(eq0=0, eq1=0, eq2=0)
    print("Finished: full_mix_eq")

if __name__ == "__main__":
    main()
