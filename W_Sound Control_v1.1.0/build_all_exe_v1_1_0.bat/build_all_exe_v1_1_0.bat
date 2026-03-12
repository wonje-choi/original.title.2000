@echo off
title W_Sound Control v1.1.0 EXE Builder

cd /d "%~dp0"

echo ==========================================
echo   W_Sound Control v1.1.0 EXE Build Start
echo ==========================================
echo.

echo [1/7] Checking PyInstaller...
py -3.14 -m pip install --upgrade pyinstaller
if errorlevel 1 (
    echo.
    echo [ERROR] Failed to install or update PyInstaller.
    pause
    exit /b 1
)

echo.
echo [2/7] Cleaning old build files...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
del /q *.spec 2>nul

echo.
echo [3/7] Building SpeakerSwitch_v1.1.0.exe ...
py -3.14 -m PyInstaller --clean --onefile --noconsole --name SpeakerSwitch_v1.1.0 switch_to_speaker.py
if errorlevel 1 goto build_error

echo.
echo [4/7] Building EarphoneSwitch_v1.1.0.exe ...
py -3.14 -m PyInstaller --clean --onefile --noconsole --name EarphoneSwitch_v1.1.0 switch_to_earphone.py
if errorlevel 1 goto build_error

echo.
echo [5/7] Building HeadsetSwitch_v1.1.0.exe ...
py -3.14 -m PyInstaller --clean --onefile --name HeadsetSwitch_v1.1.0 switch_to_headset.py
if errorlevel 1 goto build_error

echo.
echo [6/7] Building AudioCycleSwitch_v1.1.0.exe ...
py -3.14 -m PyInstaller --clean --onefile --noconsole --name AudioCycleSwitch_v1.1.0 audio_cycle_switch.py
if errorlevel 1 goto build_error

echo.
echo [7/7] Building AudioSelector_v1.1.0.exe ...
py -3.14 -m PyInstaller --clean --onefile --name AudioSelector_v1.1.0 audio_selector.py
if errorlevel 1 goto build_error

echo.
echo ==========================================
echo   Build completed successfully.
echo ==========================================
echo Output folder:
echo %cd%\dist
echo.
dir dist
echo.
pause
exit /b 0

:build_error
echo.
echo [ERROR] Build failed.
echo Check the message above.
pause
exit /b 1