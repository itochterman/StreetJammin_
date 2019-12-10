#!/bin/bash
set +x
virtualenv venv --python python3
source ./venv/bin/activate
pip install -r requirements.txt
deactivate
