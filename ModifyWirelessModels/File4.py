import os

folderPath = r"C:\Users\SESA503669\OneDrive - Schneider Electric\D\D\ETPX\wirelessModels\Richa\CPAS\QuattroDevices\AddOn"

# Get all entries in the directory
entries = os.listdir(folderPath)

# Filter out entries that are directories and print their names
for entry in entries:
    if os.path.isdir(os.path.join(folderPath, entry)):
        print(entry)