from pathlib import Path

TARGET_FOLDER_NAME = "desktop_cleaned_folder"

DOCUMENT_PATH = Path(__file__).resolve().parents[3].joinpath("Documents")
DESKTOP_PATH = Path(__file__).resolve().parents[2]

TARGET_ROOT_DIR = DOCUMENT_PATH.joinpath(TARGET_FOLDER_NAME)
