:: This uses pyinstaller to build a executable. Requires Python and pyinstaller.
:: After the executable is created the build directory and .spec files are cleaned up.
REM Building picture_namer.exe using pyinstaller
pyinstaller .\picture_namer_gui.spec
REM Deleting files and directories.
rmdir build /s /q