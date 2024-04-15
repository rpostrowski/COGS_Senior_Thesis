import batch_eq
import combine_wavs
import create_coded_folders
import organize_files
import normalize_headphone_check
import full_mix_eq

def main():
    # print("Starting: batch_eq")
    # # batch_eq.main("audio\set0", 75, 230, 1) # bass and kick
    # # batch_eq.main("audio\set1", 105, 1080, 1) # electric and bass
    # batch_eq.main("audio\set2", 600, 2200, 1) # electric and electric
    # print("Finished: batch_eq")

    print("Starting: create_coded_folders")
    create_coded_folders.main("audio\set0")
    create_coded_folders.main("audio\set1")
    create_coded_folders.main("audio\set2")
    print("Finished: create_coded_folders")

    print("Starting: organize_files")
    organize_files.main("audio\set0")
    organize_files.main("audio\set1")
    organize_files.main("audio\set2")
    print("Finished: organize_files")

    print("Starting: combine_wavs")
    combine_wavs.main("audio\set0\output")
    combine_wavs.main("audio\set1\output")
    combine_wavs.main("audio\set2\output")
    print("Finished: combine_wavs")

    print("Starting: normalizing headphone check files")
    normalize_headphone_check.main("headphone_check_files")
    print("Finished: normalizing headphone check files")
    
    # print("Starting: full_mix_eq")
    # full_mix_eq.main(75, 230, 105, 1080, 600, 2200)
    # print("Finished: full_mix_eq")

if __name__ == "__main__":
    main()
