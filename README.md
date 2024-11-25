# desktop-organiser

## Overview

This project is an automation file organization tool designed to declutter and organize files stored on your desktop.

The script scans your desktop directory, retrieves all files, and then organizes them into a structured folder system within a designated directory. 

Each file is sorted into subfolders based on its file extension, and further organized by the date the file was created. Additionally, the script identifies screenshot files and groups them into a dedicated 'Screenshots' subfolder within their respective extension and date folders.

## Features

- **Automatic Organization**: Quickly organizes files from your desktop into a structured folder system.
- **File Extension Sorting**: Categorizes files based on their file extensions for easier access.
- **Date-Based Subfolders**: Files are further organized into subfolders based on their creation date.
- **Special Handling for Screenshots**: Recognizes screenshot files and groups them into a separate 'Screenshots' subfolder within the appropriate structure.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/marccodess/auto-desktop-organiser.git
    ```

2. Navigate to the project directory:

    ```bash
    cd desktop-file-organizer
    ```

### Usage

*Project must to be stored on your Desktop for current config to run successfully. Otherwise, you will need to alter the path directories in the `__init__.py` file.*

1. Open a terminal or command prompt.

2. Once within the project directory, run the following:

    ```bash
    python3 main.py
    ```

3. Sit back and let the project organise your desktop for you!

## Support

For any issues, bugs, or feature requests, please create an issue on the [GitHub repository](https://github.com/marccodess/auto-desktop-organiser/issues).

<!-- 
## License

This project is licensed under the [MIT License](LICENSE). -->
