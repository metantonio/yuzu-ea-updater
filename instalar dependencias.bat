echo Carpeta de Instalacion de dependencias

cd /d %~dp0
@echo off
cd %

@echo on
pip3 install requests
python3 -m pip install requests

python3 -m pip install urllib.request
python3 -m pip install urllib2

echo END
PAUSE