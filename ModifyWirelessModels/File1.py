import json
import os
from structures import findKeyvalue

# Replace with your parent directory path
parent_directory = r"C:\Users\SESA503669\OneDrive - Schneider Electric\D\D\ETPX\wirelessModels\Richa\ALL"

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
        # Convert the file name to lower case
        lower_file = file.lower()

        # Check if the file name is "metadata"
        if "metadata" in lower_file:
            # Get the full file path
            file_path = os.path.join(directory_path, file)

            # Open the JSON file
            with open(file_path, 'r+') as f:
                # Load the JSON content
                data = json.load(f)

                # Iterate over the "categories" list
                for category in findKeyvalue(data, 'device.configuration.categories')[0]:
                    for setting in category['settings']:
                        if setting['name'] == 'Device Label':
                            setting['fieldValidation'] = {'minLength': 0, 'maxLength': 5, 'regularExpression': ""}
                        if setting['name'] == 'Asset Name':
                            setting['fieldValidation'] = {'minLength': 0, 'maxLength': 32, 'regularExpression': ""}

                # Move the read cursor to the start of the file
                f.seek(0)

                # Write the modified content back into the JSON file
                json.dump(data, f, indent=4)

                # Truncate the file to remove leftover part
                f.truncate()
