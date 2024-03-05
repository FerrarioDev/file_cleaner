# File Mover

File Mover is a Python script that automatically organizes files in your Downloads directory into specific folders based on their file types. It runs in the background and continuously monitors your Downloads folder for new files, moving them to appropriate destination folders.

## Features

- Automatically organizes files into folders based on their file types (e.g., audio, video, images, documents, etc.).
- Renames duplicate files to prevent overwriting.
- Runs in the background and continues to monitor the Downloads folder for new files.
- Provides a system tray icon for easy access to exit the program.

## Prerequisites

- Python 3.x
- Required Python packages: pystray, Pillow

## Usage

1. Clone this repository to your local machine.
2. Install the required Python packages by running:

```bash
pip install -r requirements.txt
```

3. Run the script by executing `file_cleaner.py`.

```bash
python3 file_cleaner.py
```

4. The program will start running in the background, monitoring your Downloads folder.
5. New files downloaded to the Downloads folder will be automatically organized into appropriate destination folders.
6. To exit the program, right-click on the system tray icon and select "Exit".

## Configuration

You can modify the file extensions and destination folders in the `file_mover.py` script to customize the behavior according to your preferences.
