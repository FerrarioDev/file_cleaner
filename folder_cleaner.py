import os
import shutil
from pystray import MenuItem as item
import pystray
from PIL import Image
import threading
import time

EXT_AUDIO = ['mp3', 'wav', 'raw', 'wma', 'mid', 'midi']
EXT_VIDEO = ['mp4', 'avi', 'mov', 'wmv', 'mkv', 'flv']
EXT_IMGS = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tif', 'tiff']
EXT_DOCS = ['doc', 'docx', 'pdf', 'txt', 'xls', 'xlsx', 'ppt', 'pptx']
EXT_COMPR = ['zip', 'rar', '7z', 'tar', 'gz']
EXT_INSTL = ['exe', 'msi', 'dmg', 'pkg']

exit_event = threading.Event()

def process_files():
    while not exit_event.is_set():
        # Create directories
        BASE_PATH = os.path.expanduser('~')
        DEST_DIRS = {'Audio': EXT_AUDIO, 'Videos': EXT_VIDEO, 'Pictures': EXT_IMGS, 
                     'Documents': EXT_DOCS + EXT_COMPR, 'Applications': EXT_INSTL}

        for dir, extensions in DEST_DIRS.items():
            dir_path = os.path.join(BASE_PATH, dir)
            if not os.path.isdir(dir_path):
                os.mkdir(dir_path)

        # Map files from downloads folder
        DOWNLOADS_PATH = os.path.join(BASE_PATH, 'Downloads')
        files_list = os.listdir(DOWNLOADS_PATH)

        for filename in files_list:
            if filename[0] != '.':
                file_ext = filename.split('.')[-1].lower()
                src_path = os.path.join(DOWNLOADS_PATH, filename)
                for dir, extensions in DEST_DIRS.items():
                    if file_ext in extensions:
                        dst_path = os.path.join(BASE_PATH, dir, filename)
                        if os.path.exists(dst_path):
                            base, ext = os.path.splitext(filename)
                            index = 1
                            while os.path.exists(os.path.join(BASE_PATH, dir, f"{base}_{index}{ext}")):
                                index += 1
                            new_file_name = f"{base}_{index}{ext}"
                            dst_path = os.path.join(BASE_PATH, dir, new_file_name)
                        shutil.move(src=src_path, dst=dst_path)
                        break  # Move to the next file after finding the appropriate destination directory

        time.sleep(1)  # Adjust the polling interval as needed

def exit_program(icon, item):
    exit_event.set()
    icon.stop()

def create_system_tray_icon():
    # Create the icon
    image = Image.open("icon.png")  # Provide the path to your icon image
    menu = (item('Exit', exit_program),)

    # Create the tray icon
    icon = pystray.Icon("File Mover", image, "File Mover", menu)
    icon.run()

if __name__ == '__main__':
    # Start the file processing thread
    file_thread = threading.Thread(target=process_files)
    file_thread.daemon = True
    file_thread.start()

    # Start the system tray icon
    create_system_tray_icon()
