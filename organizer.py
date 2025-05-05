import os
import shutil

# STEP 1: Automatically get the Downloads folder for the current user
from pathlib import Path
source_folder = str(Path.home() / "Downloads")

# STEP 2: Define folder categories
file_types = {
    'Executables': ['.exe', '.msi', '.app'],
    'Compressed': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.sh', '.bat'],
    'Code': ['.html', '.css', '.js', '.java', '.cpp', '.c'],
    'Databases': ['.sql', '.db', '.sqlite'],
    'Spreadsheets': ['.xls', '.xlsx', '.csv'],
    'Presentations': ['.ppt', '.pptx'],
    'PDFs': ['.pdf'],
    'Text Files': ['.txt', '.log'],
    'Markdown': ['.md'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.pptx'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.tar', '.gz'],
    'Fonts': ['.ttf', '.otf'],
    'Web Files': ['.html', '.css', '.js'],
    'Virtual Machines': ['.vmdk', '.vdi', '.ova'],
    '3D Models': ['.obj', '.fbx', '.stl'],
    'Design Files': ['.psd', '.ai', '.xd'],
    'Ebooks': ['.epub', '.mobi'],
    'Backup': ['.bak', '.tmp'],
    'Miscellaneous': ['.bin', '.iso', '.dmg'],
}

# STEP 3: Make folders if they don't exist
for folder in file_types.keys():
    folder_path = os.path.join(source_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Create "Others" folder
other_folder = os.path.join(source_folder, "Others")
if not os.path.exists(other_folder):
    os.makedirs(other_folder)

# STEP 4: Move files into the correct folder
for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)
    if os.path.isfile(file_path):
        moved = False
        for folder, extensions in file_types.items():
            if filename.lower().endswith(tuple(extensions)):
                dest_path = os.path.join(source_folder, folder, filename)
                shutil.move(file_path, dest_path)
                moved = True
                break
        if not moved:
            shutil.move(file_path, os.path.join(other_folder, filename))

# STEP 5: Clean up empty folders
for folder in file_types.keys():
    folder_path = os.path.join(source_folder, folder)
    if os.path.exists(folder_path) and not os.listdir(folder_path):
        os.rmdir(folder_path)

# Clean up the "Others" folder if empty
if os.path.exists(other_folder) and not os.listdir(other_folder):
    os.rmdir(other_folder)

# STEP 5: Print the results
print("Files have been organized into the following folders:")
for folder in file_types.keys():
    folder_path = os.path.join(source_folder, folder)
    if os.path.exists(folder_path):
        print(f"- {folder}: {len(os.listdir(folder_path))} files")
print(f"- Others: {len(os.listdir(other_folder))} files")
