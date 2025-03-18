#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate

# Fetch books from Project Gutenberg
echo "Fetching books from Project Gutenberg..."
python manage.py fetch_gutenberg --num-books 5 --pages-per-book 5 || true 