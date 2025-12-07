#!/bin/bash

echo "Starting Physical AI Book Backend..."

# Install dependencies
pip install -r requirements_simple.txt

# Start the server
uvicorn main_simple:app --host 0.0.0.0 --port ${PORT:-8000}
