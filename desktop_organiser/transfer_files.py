import time
import shutil
from pathlib import Path
from datetime import datetime


def move_files_by_suffix(source_directory: str, subfolder_directory: str) -> None:
    """
    Move files from source directory to target directory based on matching suffixes.

    Args:
    - source_directory (str): Path to the source directory.
    - subfolder_directory (str): Path to the subfolder directory.

    Returns:
    - None
    """
    files_to_move = [
        file
        for file in Path(source_directory).glob("*")
        if file.is_file() and file.suffix
    ]

    folder_extensions_list = [
        folder.name for folder in Path(subfolder_directory).iterdir() if folder.is_dir()
    ]

    for extension in folder_extensions_list:
        suffix = f".{extension.lower()}"

        for file in files_to_move:
            if file.suffix == suffix:
                date_folder = (
                    datetime.strptime(
                        time.ctime(file.stat().st_birthtime), "%a %b %d %H:%M:%S %Y"
                    )
                ).strftime("%Y%m")

                if file.suffix == ".png" and "Screenshot" in str(file):
                    folder_destination_path = Path(subfolder_directory).joinpath(
                        extension, date_folder, "Screenshots"
                    )
                else:
                    folder_destination_path = Path(subfolder_directory).joinpath(
                        extension, date_folder
                    )
                shutil.move(str(file), str(folder_destination_path))
                print(f"Moved '{file}' to '{folder_destination_path}'")
