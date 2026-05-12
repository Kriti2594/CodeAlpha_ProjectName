# Task Automation with Python Scripts
# Move all .jpg files from one folder to another

import os
import shutil

# Source and destination folders
source_folder = "source_images"
destination_folder = "moved_images"

# Create source folder if it does not exist
if not os.path.exists(source_folder):
    os.makedirs(source_folder)

# Create destination folder if it does not exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Move all .jpg files
for file_name in os.listdir(source_folder):
    if file_name.endswith(".jpg"):
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)

        shutil.move(source_path, destination_path)

        print(f"Moved: {file_name}")

print("All JPG files moved successfully!")
