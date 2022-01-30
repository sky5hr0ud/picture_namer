# picture_namer
This script prepends the directory name to each specified filetype along with a 5 digit number starting at "00000" eg: `<directory_name>_<xxxxx>_<filename>`. If there are already files with the `<directory_name>_<xxxxx>_<filename>` naming format in the directory then the script will count these files to prevent simultaneous use of the same numbers in the new filename. If there are more than 99999 files then the script will add more leading zeros. Spaces are changed into "_". Specified filetypes can be read from a text file or specified via the command line.

## picture_namer.py
This is the main script. I use Python 3.8.2 to run it. The script will ask for the path to where the files to be renamed are if no path is specified in the command line. If _list_of_filetypes.txt can't be found by the script the script will ask for a text file containing a list of filetypes. If the script cannot read the file in the location inputted it will run a default list of picture filetypes. The fallback default list of filetypes is: `'.jpg', '.png', '.mp4', '.jpeg', '.dng', '.gif', '.nef', '.bmp'` Default sort behavior is by date modified.

The following arguments can be used if desired:
- `-m` or `--moddate`: This sorts the files by modified date then prepends the directory name
- `-f` or `--filename`: This sorts the files by filename then prepends the directory name
- `-p <directory_path>` or `--folderpath <directory_path>`: Path to where files to be renamed are.

## _list_of_filetypes.txt
The script looks for this file in the same directory as the script then reads in the filetypes. I've populated it with picture and video filetypes and more can be appended. If this file is not present the script will ask for the location of a file. Comments can be included in the file using "#" or "//". 

**Warning:** If a filetype is missing in the list then the numbering of the files will be incorrect since the script will not search for that filetype.  

## picture_namer.exe
An executable is provided so the script doesn't have to be run via the command line using Python 3. This was built using Pyinstaller using the `--onefile` flag.
The `_list_of_filetypes.txt` is packaged inside the binary. Therefore to add additional filetypes the binary will have to be rebuilt after the `_list_of_filetypes.txt` is modified.

## build.bat
This runs the command that builds picture_namer.exe. Pyinstaller and Python are required. The *.spec files and the build directory are automatically removed to clean up files.
