import os
import time
import getopt, sys
from file_utils import collect_file_paths,display_directory_tree,simulate_directory_tree, display_simulated_tree, separate_files_by_type 
from data_processing import process_files_by_date, process_files_by_type

DATA_PATH = "/mnt/d/Pictures"
OUTPUT_PATH = "/mnt/d/Organize_Pictures"
# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[1:]

# Options
options = "hdt"
# Long options
long_options = ["Help", "date", "type"]



def main():
    dry_run = True
    mode=""
    output_path = os.path.join(os.path.dirname(DATA_PATH), 'organized_folder')

    print("-" * 50)
    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)

         # checking each argument
        for currentArgument, currentValue in arguments:
            if currentArgument in ("-h", "--Help"):
                print("Please choose the mode to organize your files:")
                print("-d, -date By Date")
                print("-t, -type By Type")
            
            elif currentArgument in ("-d", "--date"):
                print ("Process files by date:", sys.argv[0])
                mode ='date' 
            
            elif currentArgument in ("-t", "--type"):
                print (("Process files by type ") )
                mode = 'type'
            else:
                print("Something went wrong try agin")
                exit

    except getopt.error as err:
        print(str(err))
        exit
    
    # Start processing files
    start_time = time.time()
    file_paths = collect_file_paths(DATA_PATH)
    end_time = time.time()
    print("-" * 50)
    print("Directory tree before organizing:")
    # display_directory_tree(DATA_PATH)
    print("*" * 50)
    # Confirm successful output path
    message = f"Output path successfully set to: {output_path}"
    print("-" * 50)
    message = f"Time taken to load file paths: {end_time - start_time:.2f} seconds"
    print("-" * 50)
    
    if mode: 
        # mode = get_mode_selection()
        file_paths = collect_file_paths(DATA_PATH)
        # Confirm successful output path
        output_path = os.path.join(os.path.dirname(DATA_PATH), 'organized_folder')
        print(f"Output path successfully set to: {output_path}")
        print("-" * 50)
        if mode == 'date':
            # Process files by date
            operations = process_files_by_date(file_paths, output_path, dry_run=dry_run)
        if mode == 'type':
            # Process files by type
            operations = process_files_by_type(file_paths, output_path, dry_run=False)
        # Simulate and display the proposed directory tree
        print("-" * 50)
        message = "Proposed directory structure:"
        print(message)
        print(os.path.abspath(output_path))
        simulated_tree = simulate_directory_tree(operations, output_path)
        display_simulated_tree(simulated_tree)
        print("-" * 50)
   
if __name__=="__main__":
    main()