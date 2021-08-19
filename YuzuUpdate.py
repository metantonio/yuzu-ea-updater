from __future__ import ( division, absolute_import, print_function, unicode_literals )
import sys, tempfile, logging
import json, requests 
import http.client
import os

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

propiedadDos= asset[0]

#url2="https://atrevete.academy/blog/wp-content/uploads/2020/04/whatsapp-icon-design_23-2147900927-1.jpg"
url2= propiedadDos['browser_download_url']

def download_file(url, dest=None):
    """ 
    Download and save a file specified by url to dest directory,
    """
    u = urllib2.urlopen(url)

    scheme, netloc, path, query, fragment = urlparse.urlsplit(url)
    filename = os.path.basename(path)
    if not filename:
        filename = url2.split('/')[-1]
    if dest:
        filename = os.path.join(dest, filename)

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

    return filename

if __name__ == "__main__":  # Only run if this file is called directly
    print("Testing with: ")
    print(url2)
    #url = "http://download.thinkbroadband.com/10MB.zip"
    filename = download_file(url2)
    print("Nombre Archivo: \n")
    print(filename)



print("Comprobar porcentaje de descarga sea 100% \n")
print("Fin \n")