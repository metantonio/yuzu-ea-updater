Este script en python funciona como un actualizador de la versión [EA Pinneaple de Yuzu](https://github.com/pineappleEA/pineapple-src/releases).

Está hecho pensando en usuarios que no conocen de programación.

Descargar los archivos en una misma carpeta.

## Qué se necesita si soy usuario de Windows 10?

Se necesita tener instalado Python 3.9 (preferiblemente), el cual puede descargarse desde la tienda oficial de Microsoft de forma gratuita.

- Python 3.9


También es necesario instalar algunas dependencias de Python, para esto tan sólo es necesario darle doble click al archivo: `instalar dependencias.bat`. Si por el contrario, se desean instalar las dependencias de Python de forma manual, es necesario ejecutar las siguientes líneas de código en el prompt:

```sh
pip3 install requests
python3 -m pip install requests
python3 -m pip install pandas
python3 -m pip install urllib.request
python3 -m pip install urllib2
```

## Cómo ejecuto el script de Python?
 
Para ejecutar el script, basta con darle doble click al archivo: `Yuzu Updater.bat`. Aunque si se desea ejecutar el script manualmente, hay que abrir el prompt de Windows, navegar hasta la dirección en que están contenidos los archivos, y ejecutar:

```sh
python3 YuzuUpdate.py
```