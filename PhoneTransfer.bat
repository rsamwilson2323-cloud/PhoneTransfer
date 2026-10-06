@echo off
setlocal EnableExtensions DisableDelayedExpansion
title LocalDrop - Phone to PC Transfer
color 0B

cd /d "%~dp0"

cls
echo.
echo ============================================================
echo.
echo                    LOCALDROP
echo.
echo                PHONE TO PC TRANSFER
echo.
echo ============================================================
echo.
echo   No cloud upload
echo   Local network transfer
echo   QR code pairing
echo   Multiple files
echo   Beautiful Chrome interface
echo.
echo ============================================================
echo.

echo [1/5] Checking Python...
python --version >nul 2>&1

if errorlevel 1 (
    echo.
    echo [ERROR] Python is not installed.
    echo.
    echo Install Python from:
    echo https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

python --version
echo.

echo [2/5] Installing required packages...
echo.

python -m pip install flask qrcode pillow --disable-pip-version-check

if errorlevel 1 (
    echo.
    echo [ERROR] Package installation failed.
    echo.
    pause
    exit /b 1
)

echo.
echo [OK] Required packages installed.
echo.

echo [3/5] Creating LocalDrop server...

set "PAYLOAD=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"

set "PAYLOAD=%PAYLOAD: =%"

python -c "import os,zlib,base64;open(r'%~dp0localdrop.py','wb').write(zlib.decompress(base64.b64decode(os.environ['PAYLOAD'])))"

if not exist "%~dp0localdrop.py" (
    echo.
    echo [ERROR] Could not create the server.
    pause
    exit /b 1
)

echo [OK] Server created.
echo.

echo [4/5] Opening LocalDrop...

start "" /min python "%~dp0localdrop.py"

timeout /t 3 /nobreak >nul

echo [5/5] Opening Chrome...
echo.

start "" chrome "http://127.0.0.1:8765/pc"

if errorlevel 1 (
    start "" "http://127.0.0.1:8765/pc"
)

echo.
echo ============================================================
echo.
echo                 LOCALDROP IS RUNNING
echo.
echo ============================================================
echo.
echo   PC dashboard:
echo   http://127.0.0.1:8765/pc
echo.
echo   Scan the QR code shown in Chrome.
echo.
echo   Received files:
echo   %~dp0Received_Files
echo.
echo   Keep this window open while transferring.
echo.
echo ============================================================
echo.
echo Press CTRL+C to stop the server.
echo.

python "%~dp0localdrop.py"

pause