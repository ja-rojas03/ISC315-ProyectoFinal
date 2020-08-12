from pyswip import Prolog, Query, Variable, Functor
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
from tkinter.ttk import *
from tkinter import filedialog
import customParser
import reglas
import tab1
import tab2
import tab3
import tab4

prolog = Prolog()
prolog.consult("reglas.pl")

files = {}
xmlMesg = ''
xmlValid = False
dtdMesg = ''
dtdValid = False

def parserTab(content):
    tab1.validateView(content)

def rulesTab(content):
    tab2.allRulesView(content)

def moreRulesTab(content):
    tab3.lastThreeRulesView(content)

def dietTab(content):
    tab4.dietView(content)

### HELPER FUNCTIONS
def openFile(fileType, extension, txt):
    text = "Evaluando " + extension + "...."
    txt.delete("1.0", END)
    txt.insert(INSERT, text)
    file = filedialog.askopenfilename(initialdir="/", title="Select file",
                                      filetypes=((fileType, extension), ("jpeg files", "*.jpg")))
    if (extension == "*.xml"):
        files['xml'] = file
    else:
        files['dtd'] = file


def parseFiles(nombreArch, nombreDTD, txt):
    try:
        xmlMesg,xmlValid,dtdMesg,dtdValid = customParser.parser(nombreArch, nombreDTD)
    except:
        xmlMesg, xmlValid, dtdMesg, dtdValid = "Error in parser", False, "Error in parser", False
    text = "XML: " + xmlMesg + "\n" + "DTD: " + dtdMesg
    txt.delete("1.0", END)
    txt.insert(INSERT, text)
    reglas.asserta(files['xml'])

def printToScreen(salida,tipo,row,window):
    print('SALIDA',salida)
    if(tipo == 'Grasa Corporal'):
        txt = scrolledtext.ScrolledText(window, width=60, height=6)
        txt.grid(column=0, row=row)

        txt.insert(INSERT, tipo + ' : ' + str(salida['fat']) + '%' + '\n')
        txt.insert(INSERT, 'Calorias diarias para mantener el peso: ' + str(salida['calories']))
        txt.insert(INSERT, '\nRecetas con menos calorias: ' + str(salida['less_calories']))
        txt.insert(INSERT, '\nRecetas con la misma cantidad: ' + str(salida['same_calories']))
        txt.insert(INSERT, '\nRecetas con mas calorias: ' + str(salida['more_calories']))
        return

    if salida:
        txt = scrolledtext.ScrolledText(window, width=40, height=5)
        txt.grid(column=0, row=row)
        txt.insert(INSERT, tipo + ' disponibles:')
        txt.insert(INSERT, '\n-----------------\n')
        salida_dict = {}
        for a_dict in salida: 
            for k in a_dict:
                txt.insert(INSERT,a_dict[k] + '\n')
    else:
        txt = scrolledtext.ScrolledText(window, width=40, height=5)
        txt.grid(column=0, row=row)
        txt.insert(INSERT, "No hay " + tipo + " disponibles ✖")



