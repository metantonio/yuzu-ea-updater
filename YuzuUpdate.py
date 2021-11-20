from __future__ import ( division, absolute_import, print_function, unicode_literals )
import sys, tempfile, logging
import json, requests 
import http.client
import os
from zipfile import ZipFile
from pyunpack import Archive
import patoolib

if sys.version_info >= (3,):
    import urllib.request as urllib2
    import urllib.parse as urlparse
else:
    import urllib2
    import urlparse


url = requests.get("https://api.github.com/repos/pineappleEA/pineapple-src/releases/latest")
text = url.text

data = json.loads(text)
#print(data)

asset = data['assets']
#print(asset)

indexado=0
propiedadDos= asset[indexado]

#url2="https://atrevete.academy/blog/wp-content/uploads/2020/04/whatsapp-icon-design_23-2147900927-1.jpg"
url2= propiedadDos['browser_download_url']

url3 = requests.get("https://api.github.com/repos/pineappleEA/pineapple-src/releases")
text2 = url3.text
data2 = json.loads(text2)
#print(data2)
asset2 = data2[indexado]['assets']
propiedad2= asset2[0]


def unzip_file(file_name):
    wd = os.getcwd()
    print("working directory es ", wd)
    print("file name to unzip: ", file_name)
    #path_to_zip_file = wd
    directory_to_extract_to=wd
    with ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)
    print("extracción terminada")

def unzip_file_7z(file_name):
    wd = os.getcwd()
    #print("working directory es ", wd)
    print("Archivo a descomprimir: ", file_name)
    #path_to_zip_file = wd
    directory_to_extract_to = wd # + "\\test"
    Archive(file_name).extractall(directory_to_extract_to)
    print("Extraccion Finalizada")
    
def download_file(url, url3, dest=None):
    """ 
    Download and save a file specified by url to dest directory,
    """
    u = urllib2.urlopen(url)
    indexado=0
    scheme, netloc, path, query, fragment = urlparse.urlsplit(url)
    filename = os.path.basename(path)
    direccion = data2[indexado]['url']
    #url4=requests.get(str(direccion))
    #print(data2[indexado]['url'])
    if not filename:
        filename = url2.split('/')[-1]
    if dest:
        filename = os.path.join(dest, filename)
    ##Aquí podría ir un posible while si .7z no está en el nombre
    while '.7z' not in filename:
        url4 = requests.get(str(direccion))
        url=url4
        text = url.text
        data = json.loads(text)
        asset = data['assets']
        propiedadDos= asset[0]
        url2= propiedadDos['browser_download_url']
        print("url nueva: ", url2)
        u = urllib2.urlopen(url2)
        scheme, netloc, path, query, fragment = urlparse.urlsplit(url2)
        #url3= propiedad2['browser_download_url']
        filename = url2.split('/')[-1]
        print("\n Testing with: ", url2)
        print("Nombre del siguiente posible archivo a descargar: ", filename)
        indexado=indexado+1
        direccion = data2[indexado]['url']
        #url4=requests.get(str(direccion))
    if '.7z' in filename:
        print("Nombre del archivo correcto a descargar: ", filename)
        if not os.path.exists(filename):
            print("Comprobar porcentaje de descarga sea 100% \n")
            with open(filename, 'wb') as f:
                meta = u.info()
                meta_func = meta.getheaders if hasattr(meta, 'getheaders') else meta.get_all
                meta_length = meta_func("Content-Length")
                file_size = None
                if meta_length:
                    file_size = int(meta_length[0])
                print("Downloading: {0} Bytes: {1} \n".format(url, file_size))

                file_size_dl = 0
                block_sz = 8192
                while True:
                    buffer = u.read(block_sz)
                    if not buffer:
                        break

                    file_size_dl += len(buffer)
                    f.write(buffer)

                    status = "{0:16}".format(file_size_dl)
                    if file_size:
                        status += "   [{0:6.2f}%]".format(file_size_dl * 100 / file_size)
                    status += chr(13)
                    print(status, end="")
                print()
            unzip_file_7z(filename)
        if os.path.exists(filename):
            print("La descarga de la última versión ya existe en el directorio \n")
    else:
        print("No es el archivo correcto a descargar: ", filename)
        indexado=indexado+1
        asset2 = data2[indexado]['assets']
        propiedad2= asset2[0]
        url3= propiedad2['browser_download_url']
        filename = url3.split('/')[-1]
        print("Nombre del siguiente posible archivo a descargar: ", filename)
        
    return filename



if __name__ == "__main__":  # Only run if this file is called directly
    print("Testing with: ")
    print(url2)
    #url = "http://download.thinkbroadband.com/10MB.zip"
    filename = download_file(url2, url3)
    print("Nombre Archivo: \n")
    print(filename)
    #unzip_file_7z(filename)



print("Fin \n")
