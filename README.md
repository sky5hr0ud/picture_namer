# picture_namer
This script prepends the directory name to each specified filetype along with a 5 digit number starting at "00000" eg: `<directory_name>_<xxxxx>_<filename>`. If there are already files with the `<directory_name>_<xxxxx>_<filename>` naming format in the directory then the script will count these files to prevent simultaneous use of the same numbers in the new filename. If there are more than 99999 files then the script will add more leading zeros. Spaces are changed into "_". Specified filetypes can be read from a text file or specified via the command line. I've only tested this using Windows 11.

## picture_namer.py
This is the main script. I use Python 3.8.2 to run it. The script will ask for the path to where the files to be renamed are if no path is specified in the command line. If _list_of_filetypes.txt can't be found by the script the script will ask for a text file containing a list of filetypes. If the script cannot read the file in the location inputted it will run a default list of picture filetypes. The fallback default list of filetypes is: `'.jpg', '.png', '.mp4', '.jpeg', '.dng', '.gif', '.nef', '.bmp'` Default sort behavior is by date modified.

The following CLI arguments can be used if desired:
- `-m` or `--moddate`: This sorts the files by modified date then prepends the directory name
- `-f` or `--filename`: This sorts the files by filename then prepends the directory name
- `-p <directory_path>` or `--folderpath <directory_path>`: Path to where files to be renamed are
- `-i` or `--input`: This disables user input. Required if script is ran unattended. The script has the ability to ask for user input for the folder path or incase a list of filetypes can't be found. Default behavior has user input enabled.
- `l <file_path>` or `--list <file_path>`: Specify a custom list of filetypes. Must be a `.txt` file containing one filetype per line. Comments can be included in the file using "#" or "//".
- `-e` or `--explicit`: Script will not ignore letter case in the filetypes list. Default behavior is to ignore case in filetypes list.

## picture_namer_gui.py
This contains the code used to for the GUI. The CLI arguments were copied into this file and slightly modified so they could be read by Gooey to create a GUI.

Check Gooey out here: https://github.com/chriskiehl/Gooey

## _list_of_filetypes.txt
The script looks for this file in the same directory as the script then reads in the filetypes. I've populated it with picture and video filetypes and more can be appended. If this file is not present the script will ask for the location of a file. Comments can be included in the file using "#" or "//". 

**Warning:** If a filetype is missing in the list then the numbering of the files will be incorrect since the script will not search for that filetype.  

## picture_namer_gui.exe
An executable is provided so the script doesn't have to be run via the command line using Python 3. This was built using Pyinstaller using the `--onefile` flag.
The `_list_of_filetypes.txt` is packaged inside the binary. Therefore to add additional filetypes the binary will have to be rebuilt after the `_list_of_filetypes.txt` is modified or a custom list will have to be inputted.

Check out this answer by James on stackoverflow for interesting Pyinstaller path behavior:  
https://stackoverflow.com/questions/51060894/adding-a-data-file-in-pyinstaller-using-the-onefile-option

## build.bat
This runs the command that builds picture_namer.exe using the parameters specified in `picture_namer_gui.spec`. Pyinstaller and Python are required. The the build directory is automatically removed to clean up files.

## picture_namer_gui.spec
This is the file that is used by Pyinstaller to build `picture_namer_gui.exe`. This has to be used due to the `image_overides` paramerter that allows Gooey to find the custom images.

## images Directory
Directory containing custom images used in the GUI.
