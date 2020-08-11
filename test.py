import xml.etree.ElementTree as ET
import json
from pyswip import Prolog
prolog = Prolog()
prolog.consult("reglas.pl")

tree = ET.parse('tests-data/testxml.xml')
root = tree.getroot()
recetas = {}

for elem in root:
    name = recetas[elem[0].text]
    ingredients = []
    steps = []
    tools = []
    for ingredient in elem[1]:
        ingredients.append(ingredient.text)
    for step in elem[2]:
        steps.append(step.text)
    for tool in elem[3]:
        tools.append(tool.text)
    
    prolog.asserta("ingredientes(" + name + ", " + ingredients + ")")
    prolog.asserta("procedimientos(" + name + ", " + steps + ")")
    prolog.asserta("herramientas(" + name + ", " + tools + ")")
