@echo off
title W_Sound Control v1.2.0 Builder

cd /d "%~dp0"

echo ==========================================
echo   W_Sound Control v1.2.0 Build Start
echo ==========================================
echo.

py -3.14 -m pip install --upgrade pyinstaller
if errorlevel 1 (
    echo [ERROR] Failed to install/update PyInstaller
    pause
    exit /b 1
)

if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
del /q *.spec 2>nul

echo.
echo Building TrayApp_v1.2.0.exe ...
py -3.14 -m PyInstaller --clean --onefile --noconsole --name TrayApp_v1.2.0 tray_app.py
if errorlevel 1 goto build_error

echo.
echo Building SwitchByProfile_v1.2.0.exe ...
py -3.14 -m PyInstaller --clean --onefile --name SwitchByProfile_v1.2.0 switch_by_profile.py
if errorlevel 1 goto build_error

echo.
echo ==========================================
echo Build completed successfully.
echo ==========================================
echo Output:
dir dist
echo.
pause
exit /b 0

:build_error
echo.
echo [ERROR] Build failed.
pause
exit /b 1