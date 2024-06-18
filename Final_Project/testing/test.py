import os
from zipfile import ZipFile


def upload_zip():
    with ZipFile("testing/tmp/zip/songs.zip", "w") as zip_object:
        # Traverse all files in directory
        for folder_name, sub_folders, file_names in os.walk("testing/tmp/songs"):
            for filename in file_names:
                # Create filepath of files in directory
                file_path = os.path.join(folder_name, filename)
                # Add files to zip file
                zip_object.write(file_path, os.path.basename(file_path))

        if os.path.exists("testing/tmp/zip/songs.zip"):
            print("ZIP file created")
        else:
            print("ZIP file not created")


upload_zip()
