# AppCloser: you can close apps when you are not behind your system
You can restrict some sensitive applications that you do not want to be opened when you are not using your system.

This code helps you close applications when someone else (when you are not using the system) and put the system on the lock screen, and after three attempts, this script will put your system on sleep mode.

Furthermore, you can combine this script with a telegram bot and activate it remotely. 

![appCloser](./etc/pic1.png)
![appCloser](./etc/pic2.png)
 
 
## Install

### Dependencies

You need the following dependencies:

- python3
- ctypes
- pyautogui




### Install the repo and the requirements

Clone the repo and install 3rd-party libraries.

```bash
$ git clone 
$ cd AppCloser
$ pip3 install -r requirements.txt
```

 
## Run the code

You can run the the code with this:

```
python3 Desktop_Cleaner.py
```
After you run the code, the code starts observing the path and each time something changes you will see a desktop notification on your screen which is something like this:

![dektop](./etc/pic0.JPG)

And when you add a file to your "Watch Path":

![dektop](./etc/pic1.JPG)

The 'Destination Path' will be something like this:

 
![dektop](./etc/pic2.JPG)
 
![dektop](./etc/pic3.JPG)


## CODE

Importing libraries 
 
 ```
from time import sleep
from watchdog.observers import Observer
import shutil
from datetime import date
from pathlib import Path
from watchdog.events import FileSystemEventHandler
from ext import extension_paths
from win10toast import ToastNotifier 
 ```
 
 Desktop notification object
 
 ```
toaster = ToastNotifier() 
 ```

### "Rename file" Function
"Rename file" function renames file to reflect new path. If a file of the same name already exists in the destination folder, the file name is numbered and incremented until the filename is unique (prevents overwriting files).

```
def rename_file(source: Path, destination_path: Path):
    if Path(destination_path / source.name).exists():
        increment = 0

        while True:
            increment += 1
            new_name = destination_path / f'{source.stem}_{increment}{source.suffix}'

            if not new_name.exists():
                return new_name
    else:
        return destination_path / source.name

```


### "Add date to path" Function
this function adds current year/month to destination path. If the path doesn't already exist, it is created.

```
def add_date_to_path(path: Path):
    dated_path = path / f'{date.today().year}' / f'{date.today().month:02d}'
    dated_path.mkdir(parents=True, exist_ok=True)
    return dated_path

```


### "Extension"
This file is a switch case like function that determines the destination folder in the 'Destination Path':

```
extension_paths = {
        # audio
        '.aif':    'media/audio',
        '.cda':    'media/audio',
        '.mid':    'media/audio',
        '.midi':   'media/audio',
        '.mp3':    'media/audio',
        # text
        '.txt':    'text/text_files',
        '.doc':    'text/microsoft/word',
        '.pdf':    'text/pdf',
        # video
        '.m4v':    'media/video',
        '.mkv':    'media/video',
        '.mov':    'media/video',
        '.mp4':    'media/video',
        '.mpg':    'media/video',
        # images
        '.gif':    'media/images',
        '.JPG':    'media/images',
        '.jpeg':   'media/images',

....

```





 
 
 # Future 
 You can modify this project to obseve any folder anywhere in your system. Also,  if you implement this project in your work place, you can get a notification via any social media to get an update regarding any change in your files.



# Contact Me

Email: haratiank2@gmail.com

YouTube channel: https://www.youtube.com/channel/UCvf9_53f6n3YjNEA4NxAkJA?view_as=subscriber

GitHub: https://github.com/Kianoush-h

LinkedIn: https://www.linkedin.com/in/kianoush-haratiannejadi/



