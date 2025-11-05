@echo off

REM PBIXRay Flask App Launcher (Windows)
REM This script starts the Flask application on localhost for secure local analysis

echo ======================================
echo   PBIXRay Local Flask Application
echo ======================================
echo.

REM Check if Flask is installed
python -c "import flask" 2>nul
if errorlevel 1 (
    echo Flask is not installed. Installing dependencies...
    pip install -r requirements.txt
    echo.
)

echo Starting the application...
echo The app will be available at: http://127.0.0.1:5000
echo.
echo Press Ctrl+C to stop the server
echo.

REM Run the Flask application
python app.py

pause
