#!/bin/bash

# Configuration
PROJECT_DIR="/home/allyan/Documents/Blogging_Platform"
VENV_PATH="$PROJECT_DIR/venv"
MANAGE_PY="$PROJECT_DIR/blogging_platform/manage.py"

echo "--- Starting Deployment ---"

# Navigate to project directory
cd "$PROJECT_DIR" || exit

# Install/Update dependencies
echo "Installing requirements..."
"$VENV_PATH/bin/pip" install -r requirements.txt

# Database migrations
echo "Running migrations..."
"$VENV_PATH/bin/python" "$MANAGE_PY" migrate --noinput

# Collect static files
echo "Collecting static files..."
"$VENV_PATH/bin/python" "$MANAGE_PY" collectstatic --noinput

# Restart services
echo "Restarting Gunicorn service..."
sudo systemctl restart gunicorn

echo "Reloading Nginx..."
sudo systemctl reload nginx

echo "--- Deployment Complete ---"
