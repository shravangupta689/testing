#!/bin/bash

MY_PATH=$(dirname "$0")

cd "$MY_PATH"
pip install -r req.txt
pytest
pytest --junitxml=report.xml
read -p "Press enter to continue"