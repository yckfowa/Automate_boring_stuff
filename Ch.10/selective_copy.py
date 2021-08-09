"""
select files from a folder tree  with specific extension name such as .pdf, and move them into a new folder
"""

import os
import shutil


def copy_to_folder(src, destination):

    for folder_name, subfolders, filenames in os.walk(src):

        for filename in filenames:
            if filename.endswith((".pdf")):
                shutil.copy(os.path.join(folder_name, filename), destination)

    print("Files copied")
