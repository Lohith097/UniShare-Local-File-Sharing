@echo off
TITLE UniShare Local Hub
color 0A

:: Check if Python is actually installed on the classroom PC
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python is not installed on this PC, or it is not added to PATH.
    echo If you do not have Python, please use the standalone server.exe version instead.
    pause
    exit /b
)

echo [1/2] Checking requirements...
pip install qrcode >nul 2>&1

echo [2/2] Booting UniShare...
cls
python server.py

pause
