@echo off

REM Check if running as administrator
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo You must run this script as an administrator!
    pause
    exit /b
)

REM Define variables
set "python_path=C:\Python312\python.exe"
set "script_path=%~dp0create_playlist.py"

REM Define registry keys
set reg_key=HKEY_CLASSES_ROOT\Directory\shell\GeneratePlaylist
set reg_key_command=%reg_key%\command

REM Set registry keys
reg add "%reg_key%" /ve /d "Generate Playlist" /f
reg add "%reg_key_command%" /ve /d "\"%python_path%\" \"%script_path%\" \"%%1\"" /f

echo Registry keys added. You should now see "Generate Playlist" in the context menu when you right-click on a folder in Windows Explorer.
pause
