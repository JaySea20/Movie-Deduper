#!/usr/bin/env python3

import os
import shutil
import sys

def list_files(folder):
    """List all files in the folder."""
    return [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

def prompt_user(files, folder):
    """Prompt the user to select a file to keep."""
    print(f"\nMultiple files found in: {folder}")
    for idx, file in enumerate(files, start=1):
        print(f"[{idx}] {file}")

    while True:
        try:
            selection = int(input("Select the file to keep (enter the number): "))
            if 1 <= selection <= len(files):
                return selection - 1
            else:
                print("Invalid selection. Please choose a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def deduplicate(media_dir):
    """Iterate through folders and deduplicate files."""
    for root, dirs, files in os.walk(media_dir):
        files = list_files(root)

        if len(files) > 1:
            keep_index = prompt_user(files, root)
            file_to_keep = files[keep_index]

            for idx, file in enumerate(files):
                if idx != keep_index:
                    file_path = os.path.join(root, file)
                    print(f"Deleting: {file}")
                    os.remove(file_path)

            print(f"Keeping: {file_to_keep}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 dedupe.py <MEDIA_DIR>")
        exit(1)

    MEDIA_DIR = sys.argv[1]
    if not os.path.exists(MEDIA_DIR):
        print(f"Error: Directory {MEDIA_DIR} does not exist.")
        exit(1)

    deduplicate(MEDIA_DIR)
