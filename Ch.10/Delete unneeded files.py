import os


def files_to_delete(src):

    for folder_name, subfolders, filenames in os.walk(src):

        for file in filenames:
            full_path = os.path.join(folder_name, file)
            size = os.path.getsize(full_path)

            if size > 100000000:
                print(full_path)
                # os.unlink(full_path)

