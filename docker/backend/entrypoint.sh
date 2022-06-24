#!/bin/sh

# Create dirs if necessary
echo "Creating dirs"
./scripts/create_dirs.sh

# Apply database migrations
echo "Apply database migrations"
./examples/simple/manage.py migrate --noinput --settings=settings.docker

## Create test data
#echo "Create test data"
#./examples/simple/manage.py fobi_create_test_data --settings=settings.docker

# Start server
echo "Starting server"
python ./examples/simple/manage.py runserver 0.0.0.0:8000 --settings=settings.docker --traceback -v 3
