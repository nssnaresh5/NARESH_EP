import os

# Replace with your parent directory path
parent_directory = r"C:\Users\SESA503669\Downloads\OneDrive_2024-05-22\Power meter v2"

# Get a list of all directories in the parent directory
directories = [d for d in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, d))]

# Iterate over each directory
for directory in directories:
    # Get the full directory path
    directory_path = os.path.join(parent_directory, directory)

    # Get a list of all files in the directory
    files = os.listdir(directory_path)

    # Iterate over each file
    for file in files:
        # Get the full file path
        file_path = os.path.join(directory_path, file)

        # Check if the file name contains "metadata" or "configurator"
        if "metadata" in file.lower():
            # Rename the file
            new_file_path = os.path.join(directory_path, directory + "_metadata.json")
            os.rename(file_path, new_file_path)
        elif "configurator" in file.lower():
            # Rename the file
            new_file_path = os.path.join(directory_path, directory + "_configurator.json")
            os.rename(file_path, new_file_path)