from tkinter import Tk
import eel
import sys

ruta=''
global datos


sys.path.append("..")
eel.init('', )
eel.start('Fonts/index.html')

@eel.expose
def cargar():
    global ruta, datos
    if(ruta!=0):
        print('Archivo cargado')
    return ruta
