#!/bin/bash

# Build script for Vercel deployment
echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "Copying static files to root static directory for Vercel..."
# Copy staticfiles to static directory so Vercel can find them
cp -r staticfiles/* static/ 2>/dev/null || mkdir -p static && cp -r staticfiles/* static/

echo "Build complete!"