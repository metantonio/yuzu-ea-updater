Este script en python funciona como un actualizador automático de la última versión disponible de [EA Pinneaple de Yuzu](https://github.com/pineappleEA/pineapple-src/releases).

Está hecho pensando en usuarios que no conocen de programación.

Descargar los archivos en una misma carpeta. 
<a href="https://github.com/metantonio/yuzu-ea-updater/archive/refs/heads/main.zip">
	<img src="https://img.shields.io/github/repo-size/metantonio/yuzu-ea-updater"/>
</a>

## Qué se necesita si soy usuario de Windows 10?

Se necesita tener instalado Python 3.9 (preferiblemente), el cual puede descargarse desde la tienda oficial de Microsoft de forma gratuita.

- [Python 3.9](https://www.microsoft.com/store/productId/9P7QFQMJRFP7)


También es necesario instalar algunas dependencias de Python la primera vez para el correcto funcionamiento del script, para esto tan sólo se debe dar doble click al archivo: `instalar dependencias.bat`. Si por el contrario, se desean instalar las dependencias de Python de forma manual, es necesario ejecutar las siguientes líneas de código en el prompt:

```sh
pip3 install requests
python3 -m pip install requests
python3 -m pip install urllib.request
python3 -m pip install urllib2
```

## Cómo ejecuto el script de Python?
 
Para ejecutar el script, basta con darle doble click al archivo: `Yuzu Updater.bat`. Aunque si se desea ejecutar el script manualmente, hay que abrir el prompt de Windows, navegar hasta la dirección en que están contenidos los archivos, y ejecutar:

```sh
python3 YuzuUpdate.py
```


## Próximas Mejoras
<ol>
    <li>
      <a href="#">Descomprimir el archivo después de decargado</a>      
    </li>
    <li>
	<a href="#">Verificación si la descarga se completó al 100% (hasta ahora la verificación la hace el usuario visualmente comprobando que llegue a 100%)</a>
    </li>
</ol>