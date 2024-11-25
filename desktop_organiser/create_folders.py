import time
from pathlib import Path
from datetime import datetime


def create_folder_if_not_exists(base_directory: str, folder_name: str) -> None:
    """
    Check if a folder exists in the specified directory.
    If not, create the folder.

    Args:
    - base_directory (str): Path to the base directory.
    - folder_name (str): Name of the folder to be checked/created.

    Returns:
    - None
    """
    target_folder_path = Path(base_directory).joinpath(folder_name)

    if not target_folder_path.is_dir():
        target_folder_path.mkdir(parents=True, exist_ok=True)
        print(f"Folder '{folder_name}' created successfully in '{base_directory}'.")
    else:
        print(f"Folder '{folder_name}' already exists in '{base_directory}'.")


def create_subfolders_for_extensions(
    directory_path: str, target_directory: str
) -> None:
    """
    Get file extensions from files within a directory.
    Create subfolders for each unique file extension.

    Args:
    - directory_path (str): Path to the directory containing files.
    - target_directory (str): Path to the target directory.

    Returns:
    - None
    """
    files_with_extensions = [
        file
        for file in Path(directory_path).glob("*")
        if file.is_file() and file.suffix
    ]

    extensions = {file.suffix.upper().strip(".") for file in files_with_extensions}

    for extension in extensions:
        subfolder_path = Path(target_directory).joinpath(extension)
        if not subfolder_path.is_dir():
            subfolder_path.mkdir(parents=True, exist_ok=True)
            print(f"Subfolder '{subfolder_path}' created for extension '{extension}'.")
        else:
            print(
                f"Subfolder '{subfolder_path}' already exists for extension '{extension}'."
            )


def create_date_folders(base_directory: str, subfolder_directory: str) -> None:
    """
    Create date-based folders if they don't exist in the specified directory.

    Args:
    - base_directory (str): Path to the base directory.
    - subfolder_directory (str): Path to the extension subfolders directory.

    Returns:
    - None
    """
    extension_folders = [
        folder.name for folder in Path(subfolder_directory).iterdir() if folder.is_dir()
    ]

    for extension in extension_folders:
        date_folder_name_list = list(
            {
                (
                    datetime.strptime(
                        time.ctime(file.stat().st_birthtime), "%a %b %d %H:%M:%S %Y"
                    )
                ).strftime("%Y%m")
                for file in Path(base_directory).glob("*")
                if file.is_file() and file.suffix == f".{extension.lower()}"
            }
        )
        for date_folder in date_folder_name_list:
            subfolder_path = Path(subfolder_directory).joinpath(extension, date_folder)
            if not subfolder_path.exists():
                subfolder_path.mkdir(parents=True)
                print(
                    f"Subfolder '{subfolder_path}' created for extension '{extension}/{date_folder}'."
                )
            else:
                print(
                    f"Subfolder '{subfolder_path}' already exists for extension '{extension}/{date_folder}'."
                )


def create_screenshots_folder(base_directory: str) -> None:
    """
    Create a 'Screenshots' folder within the 'PNG' folder if it exists.

    Args:
    - base_directory (str): Path to the base directory.

    Returns:
    - None
    """
    screenshots_folder = "Screenshots"
    png_directory = Path(base_directory).joinpath("PNG")

    date_folders = [
        str(x).split("/")[-1] for x in png_directory.glob("*") if x.is_dir()
    ]
    for date_folder in date_folders:
        if png_directory.joinpath(date_folder).is_dir():
            screenshots_path = Path(
                png_directory.joinpath(date_folder, screenshots_folder)
            )
            if not screenshots_path.exists():
                screenshots_path.mkdir()
                print(
                    f"'Screenshots' folder created successfully in '{screenshots_path}'."
                )
            else:
                print(f"'Screenshots' folder already exists in '{screenshots_path}'.")
