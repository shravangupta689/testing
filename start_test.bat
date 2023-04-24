@echo off
set MY_PATH=%~dp0
cd %MY_PATH%
pip install -r req.txt
pytest
pytest --junitxml=report.xml
pause
