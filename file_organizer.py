import os
import shutil
import datetime

def organize_files(directory):
    """Organizes files in a directory based on file type and date."""

    file_types = {
        "images": (".jpg", ".jpeg", ".png", ".gif", ".bmp"),
        "documents": (".pdf", ".docx", ".txt", ".csv", ".xlsx"),
        "videos": (".mp4", ".avi", ".mov", ".mkv"),
        "audio": (".mp3", ".wav", ".ogg"),
        "archives": (".zip", ".rar", ".7z"),
        "code": (".py", ".js", ".html", ".css")
    }

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        if os.path.isfile(filepath):
            file_extension = os.path.splitext(filename)[1].lower()

            # Organize by file type
            destination_folder = None
            for folder, extensions in file_types.items():
                if file_extension in extensions:
                    destination_folder = os.path.join(directory, folder)
                    break

            # Organize by date if no type match
            if destination_folder is None:
                try:
                    creation_time = datetime.datetime.fromtimestamp(os.path.getctime(filepath))
                    year_month = creation_time.strftime("%Y-%m")
                    destination_folder = os.path.join(directory, year_month)
                except OSError:
                    destination_folder = os.path.join(directory, "other") #For files where date cannot be retrieved.

            # Create destination folder if it doesn't exist
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            # Move the file
            try:
                shutil.move(filepath, os.path.join(destination_folder, filename))
                print(f"Moved {filename} to {destination_folder}")
            except shutil.Error as e:
                print(f"Error moving {filename}: {e}")
        elif os.path.isdir(filepath):
            #Optional: Add recursion here to organize subfolders.
            pass

if __name__ == "__main__":
    directory_to_organize = input("Enter the directory to organize: ")  # Get directory from user

    if os.path.exists(directory_to_organize):
        organize_files(directory_to_organize)
        print("File organization complete.")
    else:
        print("Directory not found.")
