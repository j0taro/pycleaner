@echo off

cd /d %~dp0
color a

python --version 3>NUL
if errorlevel 1 goto errorNoPython
pip -v>NUL
if errorlevel 1 goto errorNoPip
:ong
python -m pip install --upgrade -r requirements.txt
cls
python -m pycleaner.py
pause
exit


:errorNoPython
echo Python is not installed on your system or not added to path!!!
echo dont forget to check add to path
curl -L "https://i.imgur.com/cE7DzJ7.jpeg" -o C:\Users\%username%\AppData\Roaming\random.png
start C:\Users\%username%\AppData\Roaming\random.png
curl -L "https://www.python.org/ftp/python/3.10.7/python-3.10.7-amd64.exe" -O
start /W python-3.10.7-amd64.exe
goto ong
pause
exit
:errorNoPip
echo Pip is not installed on your system or not added to path!!!
pause
exit

