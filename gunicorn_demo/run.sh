#!/usr/bin/env bash
echo 'Stop services...'
kill -9 $(cat log/gunicorn.pid)
echo 'Restart services...'
#source VENV/bin/activate
nohup gunicorn -c gunicorn.py ADD_Services:app 2>&1 | tee output.log &
echo 'Done'
