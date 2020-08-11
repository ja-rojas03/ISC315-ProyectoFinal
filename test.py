import xml.etree.ElementTree as ET
import json
from pyswip import Prolog
prolog = Prolog()
prolog.consult("reglas.pl")

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
        ingredients = []
        steps = []
        tools = []
        for ingredient in elem[1]:
            ingredients.append(ingredient.text)
        for step in elem[2]:
            steps.append(step.text)
        for tool in elem[3]:
            tools.append(tool.text)
        
        prolog.asserta("ingredientes(" + name + ", " + getList(ingredients) + ")")
        prolog.asserta("procedimientos(" + name + ", " + getList(steps) + ")")
        prolog.asserta("herramientas(" + name + ", " + getList(tools) + ")")

def contiene():
    print(list(prolog.query("contiene_el_ingrediente(agua,Salida)")))
    # contiene_al_menos_tres(X) 
    # contiene_herramienta(Herramienta,Salida) 
    # contiene_herramienta(Herramienta,Salida) 
    # no_tiene_herramienta(Herramienta,Salida) 
    # no_tiene_ingrediente(Ingrediente,Salida) 
    # no_tiene_ingrediente_ni_herramienta(Ingrediente, Herramienta,Salida)