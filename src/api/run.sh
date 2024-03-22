#!/bin/bash

if [ "$1" == "dev" ]; then
    uvicorn main:app --host 0.0.0.0 --port 8080 --reload
elif [ "$1" == "start" ]; then
    uvicorn main:app --host 0.0.0.0 --port 8080
elif [ "$1" == "test" ]; then
    python -m unittest discover -s tests/unit
elif [ "$1" == "init" ]; then
    pip install --no-cache-dir --upgrade -r requirements.txt
    python index_generate.py
else
    echo "Invalid command. Usage: ./run.sh [dev|start|test|init]"
fi