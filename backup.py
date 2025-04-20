import os
import shutil
import sys
from datetime import datetime

def backup_files(source, destination):
    if not os.path.exists(source):
        print("Source directory does not exist.")
        return
    if not os.path.exists(destination):
        print("Destination directory does not exist.")
        return

    for filename in os.listdir(source):
        src_path = os.path.join(source, filename)
        dest_path = os.path.join(destination, filename)

        if os.path.isfile(src_path):
            if os.path.exists(dest_path):
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                name, ext = os.path.splitext(filename)
                new_filename = f"{name}_{timestamp}{ext}"
                dest_path = os.path.join(destination, new_filename)

            shutil.copy2(src_path, dest_path)
            print(f"Copied: {src_path} -> {dest_path}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python backup.py /path/to/source /path/to/destination")
    else:
        backup_files(sys.argv[1], sys.argv[2])