from desktop_organiser import (
    DOCUMENT_PATH,
    TARGET_FOLDER_NAME,
    DESKTOP_PATH,
    TARGET_ROOT_DIR,
)
from desktop_organiser.create_folders import (
    create_folder_if_not_exists,
    create_subfolders_for_extensions,
    create_date_folders,
    create_screenshots_folder,
)

from desktop_organiser.transfer_files import move_files_by_suffix


if __name__ == "__main__":
    # check if the target folder already exists, if not, create it
    create_folder_if_not_exists(DOCUMENT_PATH, TARGET_FOLDER_NAME)

    # look for all file extentions on desktop and create subfolder if doesn't already exist
    create_subfolders_for_extensions(DESKTOP_PATH, TARGET_ROOT_DIR)

    # create the date folder (format MMMYY)
    create_date_folders(DESKTOP_PATH, TARGET_ROOT_DIR)

    # create a screenshots folder within the PNG subfolder
    create_screenshots_folder(TARGET_ROOT_DIR)

    # transfer files from desktop to destination folders
    move_files_by_suffix(DESKTOP_PATH, TARGET_ROOT_DIR)
