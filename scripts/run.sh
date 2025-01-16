#!/bin/bash

# Get project root directory
ROOT_DIR=$(git rev-parse --show-toplevel)

# Change to root directory
cd "$ROOT_DIR"

# Check if virtual environment exists, create if it doesn't
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install/update requirements
echo "Installing/updating requirements..."
pip install -r requirements.txt

# Change to backend directory and run server
echo "Starting server..."
cd backend
python server.py 