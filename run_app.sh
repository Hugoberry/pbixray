#!/bin/bash

# PBIXRay Flask App Launcher
# This script starts the Flask application on localhost for secure local analysis

echo "======================================"
echo "  PBIXRay Local Flask Application"
echo "======================================"
echo ""

# Check if Flask is installed
if ! python3 -c "import flask" &> /dev/null; then
    echo "Flask is not installed. Installing dependencies..."
    pip install -r requirements.txt
    echo ""
fi

echo "Starting the application..."
echo "The app will be available at: http://127.0.0.1:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Run the Flask application
python3 app.py
