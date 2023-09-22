#!/bin/bash
# Activate the virtual environment
source venv/bin/activate
# Run Gunicorn with Uvicorn workers
exec gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:app
