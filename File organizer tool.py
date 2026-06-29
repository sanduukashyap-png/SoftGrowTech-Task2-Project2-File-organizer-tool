import os
import shutil

# Folder path
folder_path = input("Enter folder path: ")

# File type categories
file_types = {
    "Images": [".jpg", ".png", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"]
}

# Scan all files in folder
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    # Check if it is a file
    if os.path.isfile(file_path):

        # Get file extension
        extension = os.path.splitext(file)[1].lower()

        # Match file type
        for folder_name, extensions in file_types.items():
            if extension in extensions:

                # Create folder if not exists
                target_folder = os.path.join(folder_path, folder_name)
                os.makedirs(target_folder, exist_ok=True)

                # Move file
                shutil.move(file_path, os.path.join(target_folder, file))

                print(f"{file} moved to {folder_name}")

print("Files organized successfully!")