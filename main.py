from Backend.abrirArchivo import abrirArchivo
from tkinter import Tk
import eel
import sys

from Backend.abrirArchivo import abrirArchivo


ruta=''
global datos


sys.path.append("..")
eel.init('Fonts', )


@eel.expose
def cargar():
    global ruta, datos
    ruta= abrirArchivo()
    if(ruta!=0):
        print('Archivo cargado')
    return ruta

eel.start('index.html')
