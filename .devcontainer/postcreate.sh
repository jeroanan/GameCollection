#!/bin/sh

python -m venv .venv
. .venv/bin/activate
pip install --upgrade setuptools pip
pip install -r requirements.txt
mkdir -p sessions/