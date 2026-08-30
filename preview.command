#!/usr/bin/env bash

# Move to the project root directory where the script is located
cd "$(dirname "$0")"

echo "========================================="
echo "   Co-creation Signage Slide Preview     "
echo "========================================="

# Check Node version
if ! command -v node >/dev/null 2>&1; then
    echo "Error: Node.js is not installed or not in PATH."
    echo "Please install Node.js (version >= 20) and try again."
    read -p "Press enter to exit..."
    exit 1
fi

# Ensure dependencies are installed
if [ ! -d "node_modules" ]; then
    echo "node_modules folder not found. Installing dependencies (npm ci)..."
    npm ci
    if [ $? -ne 0 ]; then
        echo "Error: 'npm ci' failed."
        read -p "Press enter to exit..."
        exit 1
    fi
fi

# Compile the slides
echo "Building slides..."
npm run build
if [ $? -ne 0 ]; then
    echo "Error: 'npm run build' failed."
    read -p "Press enter to exit..."
    exit 1
fi

# Open the browser automatically in the background
echo "Opening browser to http://127.0.0.1:4174 ..."
if command -v open >/dev/null 2>&1; then
    (sleep 1.5 && open "http://127.0.0.1:4174") &
fi

# Run the preview server
echo "Starting local preview server..."
npm run serve
