# from pyswip import Prolog, Query, Variable, Functor
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
from tkinter.ttk import *
from tkinter import filedialog
import customParser

files = {}
xmlMesg = ''
xmlValid = False
dtdMesg = ''
dtdValid = False

def parserTab(tab1):
    #XML SECTION
    labelFrame = ttk.LabelFrame(tab1, text="Seleccione un XML")
    labelFrame.grid(column=0, row=5)

    btn = Button(labelFrame, text="Buscar XML", command=lambda: openFile("all XML", "*.xml", txt))
    btn.grid(column=1, row=13)

    txt = scrolledtext.ScrolledText(labelFrame, width=40, height=3)
    txt.grid(column=1, row=15)
    txt.insert(INSERT, "No hay XML insertado...")

    #DTD SECTION
    labelFrame = ttk.LabelFrame(tab1, text="Seleccione un DTD")
    labelFrame.grid(column=0, row=6)

    btn2 = Button(labelFrame, text="Buscar DTD", command=lambda: openFile("all DTD", "*.dtd", txt2))
    btn2.grid(column=1, row=15)

    txt2 = scrolledtext.ScrolledText(labelFrame, width=40, height=3)
    txt2.grid(column=1, row=17)
    txt2.insert(INSERT, "No hay DTD insertado...")

    #PARSER ACTION SECTION
    labelFrame = ttk.LabelFrame(tab1, text="Parse XML / DTD")
    labelFrame.grid(column=0, row=8)

    btn3 = Button(labelFrame, text="Parse", command=lambda: parseFiles(files['xml'], files['dtd'], txt3))
    btn3.grid(column=1, row=19)

    txt3 = scrolledtext.ScrolledText(labelFrame, width=40, height=3)
    txt3.grid(column=1, row=17)
    txt3.insert(INSERT, "Validar ..")

def rulesTab(tab2):
    labelFrame = ttk.LabelFrame(tab2, text="Seleccione una regla")
    labelFrame.grid(column=0, row=5)

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


