import xml.etree.ElementTree as ET
import json
from pyswip import Prolog
from tkinter import scrolledtext
from tkinter import *
import views

prolog = Prolog()
prolog.consult("reglas.pl")
recetas = {}

def getList(array):
    pl = '['

    for item in array:
        if item == array[-1]:
            pl += str(item)
        else:
            pl += str(item) + ','
    
    pl += ']'

    return pl

def asserta(file):
    tree = ET.parse(file)
    root = tree.getroot()
    for elem in root:
        name = elem[0].text
        recetas[name] = elem[1].text # calories
        ingredients = []
        steps = []
        tools = []
        for ingredient in elem[2]:
            ingredients.append(ingredient.text)
        for step in elem[3]:
            steps.append(step.text)
        for tool in elem[4]:
            tools.append(tool.text)
        
        prolog.asserta("ingredientes(" + name + ", " + getList(ingredients) + ")")
        prolog.asserta("procedimientos(" + name + ", " + getList(steps) + ")")
        prolog.asserta("herramientas(" + name + ", " + getList(tools) + ")")

def contiene(ingrediente, window):
    salida = list(prolog.query("contiene_el_ingrediente(" + ingrediente.get() + ",Salida)"))
    views.printToScreen(salida,'platos',4, window)

def contiene_al_menos_tres(ingredientes,window):
    arr_ingredientes = ingredientes.get().split(',')
    items = len(arr_ingredientes)
    query =""
    if items == 2: 
        query = arr_ingredientes[0] + "," + arr_ingredientes[1]
    elif items == 3:
        query = arr_ingredientes[0] + "," + \
            arr_ingredientes[1] + "," + arr_ingredientes[2] 
    else:
        query = arr_ingredientes[0]

    test ="contiene_al_menos_tres([" + query + "],Salida)"
    print("TEST" + test)
    salida = list(prolog.query(test))

    views.printToScreen(salida, 'platos', 8, window)

def contiene_herramienta(herramienta,window):
    salida = list(prolog.query("contiene_herramienta(" + herramienta.get() + ",Salida)"))
    views.printToScreen(salida,'herramientas',13, window)

def no_tiene_herramienta(herramienta,window):
    salida = list(prolog.query("no_tiene_herramienta(" + herramienta.get() + ",Salida)"))
    views.printToScreen(salida, 'platos', 4, window)

def no_tiene_ingrediente(ingrediente,window):
    salida = list(prolog.query("no_tiene_ingrediente(" + ingrediente.get() + ",Salida)"))
    views.printToScreen(salida, 'platos', 9, window)

def no_tiene_ingrediente_ni_herramienta(ingrediente,herramienta,window):
    salida = list(prolog.query("no_tiene_ingrediente_ni_herramienta(" + ingrediente.get() + "," + herramienta.get() + ",Salida)"))
    views.printToScreen(salida, 'platos', 14, window)

def getRecetas():
    return recetas