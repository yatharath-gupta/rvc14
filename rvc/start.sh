#!/bin/bash
source "/f/RVC and stuff/apif/Retrieval-based-Voice-Conversion/venv/Scripts/activate"
export PYTHONPATH="/f/RVC and stuff/apif/Retrieval-based-Voice-Conversion/rvc:$PYTHONPATH"
python -m uvicorn main:app --host 0.0.0.0 --port 8000
