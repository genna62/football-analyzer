import os
import shutil

def delete_file_if_exists(file_path):
    """Delete the file at file_path if it exists."""
    if os.path.isfile(file_path):
        try:
            os.remove(file_path)
            print(f"Deleted existing file: {file_path}")
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")
    else:
        print(f"No file to delete at: {file_path}")


def delete_folder_and_contents(folder_path):
    """Delete a folder and all its contents if it exists."""
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        shutil.rmtree(folder_path)
        print(f"Deleted folder and all contents: {folder_path}")
    else:
        print(f"Folder does not exist: {folder_path}")

