from zope.interface import declarations
from Backend.abrirArchivo import abrirArchivo
from tkinter import Tk
import eel
import sys

from Backend.abrirArchivo import abrirArchivo


ruta=''
global mensaje


sys.path.append("..")
eel.init('Fonts', )


@eel.expose
def cargar():
    global ruta, mensaje
    ruta= abrirArchivo()
    if(ruta!=0):
        f = open (ruta,'r')
        mensaje = f.read()
        print(mensaje)
        f.close()
    return ruta

eel.start('index.html')
