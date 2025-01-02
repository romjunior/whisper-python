#!/bin/bash

echo "activating venv"
source whisper-python/bin/activate
echo "venv activated"
echo "preparing to run whisper"
fastapi run api.py
echo "whisper running"