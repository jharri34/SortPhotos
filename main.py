import os
import time
from PIL import Image as PImage
import pathlib 
import glob
import getopt, sys
from file_utils import collect_file_paths,display_directory_tree,simulate_directory_tree, display_simulated_tree, separate_files_by_type 
from data_processing import process_files_by_date, process_files_by_type

DATA_PATH = "/mnt/d/Pictures"
OUTPUT_PATH = "/mnt/d/Organize_Pictures"
# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[1:]

# Options
options = "hdt:"
# Long options
long_options = ["Help", "date", "type="]

def get_mode_selection():
    """Prompt the user to select a mode."""
    while True:
        print("Please choose the mode to organize your files:")
        print("1. By Date")
        print("2. By Type")
        response = input("Enter 1, or 2 (or type '/exit' to exit): ").strip()
        if response == '/exit':
            print("Exiting program.")
            exit()
        elif response == '1':
            return 'date'
        elif response == '2':
            return 'type'
        else:
            print("Invalid selection. Please enter 1, or 2. To exit, type '/exit'.")

def main():
    dry_run = True
    print("-" * 50)
    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)

         # checking each argument
        for currentArgument, currentValue in arguments:
            if currentArgument in ("-h", "--Help"):
                print ("Displaying Help")
            
            elif currentArgument in ("-d", "--date"):
                print ("Process files by date:", sys.argv[0])
                mode ='date' 
            
            elif currentArgument in ("-t", "--type"):
                print (("Process files by type (% s)") % (currentValue))
                mode = 'type'

    except getopt.error as err:
        print(str(err))

    # mode = get_mode_selection()
    file_paths = collect_file_paths(DATA_PATH)
    # Confirm successful output path
    output_path = os.path.join(os.path.dirname(DATA_PATH), 'organized_folder')
    print(f"Output path successfully set to: {output_path}")
    print("-" * 50)
    if mode == 'date':
        # Process files by date
        operations = process_files_by_date(file_paths, output_path, dry_run=False, silent=silent_mode, log_file=log_file)
    elif mode == 'type':
        # Process files by type
        operations = process_files_by_type(file_paths, output_path, dry_run=False, silent=silent_mode, log_file=log_file)
    # Simulate and display the proposed directory tree
    print("-" * 50)
    message = "Proposed directory structure:"
    print(message)
    print(os.path.abspath(output_path))
    simulated_tree = simulate_directory_tree(operations, output_path)
    display_simulated_tree(simulated_tree)
    print("-" * 50)

    # display_directory_tree(DATA_PATH)

    # separate_files_by_type()
    # Prepare for copying and renaming
    # renamed_files = set()
    # processed_files = set()
    pass
if __name__=="__main__":
    main()