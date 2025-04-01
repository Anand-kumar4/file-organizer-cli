import os
import sys
import shutil
import logging


# Configure logging
logging.basicConfig(
    filename='file_organizer.log',
    filemode='a',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def organize_files_by_extension(folder_path):
    if not os.path.isdir(folder_path):
        logging.error(f"Invalid directory: '{folder_path}'")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            ext = ext[1:] if ext else 'no_extension'
            dest_folder = os.path.join(folder_path, ext.upper())

            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)

            shutil.move(file_path, os.path.join(dest_folder, filename))
            logging.info(f"Moved '{filename}' to folder '{ext.upper()}'")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python file_organizer.py <folder_path>")
    else:
        organize_files_by_extension(sys.argv[1])