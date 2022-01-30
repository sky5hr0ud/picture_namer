:: This uses pyinstaller to build a executable. Requires Python and pyinstaller.
:: After the executable is created the build directory and .spec files are cleaned up.
REM Building picture_namer.exe using pyinstaller
pyinstaller --onefile --add-data "_list_of_filetypes.txt;." picture_namer.py
REM Deleting files and directories.
del *.spec
rmdir build /s /q