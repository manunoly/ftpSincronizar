#!/usr/bin/env python
__author__ = 'manuel'


import ftplib
import string
from datetime import datetime
import os
# Connection information
server = "****"
username = "iner@******"
password = "******"

# Directory and matching information
directory = ['/','/iner_cuenca','/iner_cuenca/Matus','/iner_cuenca/MULTITUD','/iner_cuenca/TIXAN','/iner_cuenca/ALAO','/iner_cuenca/URBINA','/metman/BALTRA']
directory = ['/']
arbol = []
filematch = '*.*'
# Establish the connection
try:
    ftp = ftplib.FTP(server)
    ftp.login(username, password)
    print 'Conectado '+datetime.now().strftime('%Y-%m-%d %H:%M:%S')
except:
    print "No se pudo conectar "+datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    exit()

dirRaiz = os.getcwd()

while directory:
    carpetas = []
    carpeta = ""
    ftp.cwd(directory[0])
    for dir in ftp.nlst():
    #        ftp.set_debuglevel(1)
        try:
            if "." not in dir:
                ftp.cwd(dir)
                ftp.cwd("/")
                ftp.cwd(directory[0])
                carpeta = dir
                carpetas.append(carpeta)
        except:
            continue
    armando = directory.pop(0)
    if armando != "/":
        armando = armando+"/"
    for direccion in carpetas:
        directory.append(armando+direccion)
        if armando+direccion not in arbol:
            arbol.append(armando+direccion)
    ftp.cwd("/")
    if directory.__len__()==0:
        break

for dir in arbol:
    if not os.path.isdir(dirRaiz+dir):
        if os.path.isfile(dirRaiz+dir):
            os.remove(dirRaiz+dir)
        os.makedirs(dirRaiz+dir)
        print "Creado Directorio " + dirRaiz+dir
ftp.close()
print arbol
