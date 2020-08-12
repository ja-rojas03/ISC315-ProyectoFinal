from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
from tkinter.ttk import *
import reglas

def allRulesView(content):
    ### QUESTION 1
    labelFrame = ttk.LabelFrame(content, text="Seleccione una regla")
    labelFrame.grid(column=0, row=1)
  
    lbl_ingrediente = Label(labelFrame, text="¿Cuáles platos se pueden preparar si tengo un ingrediente específico?")
    lbl_ingrediente.grid(column=0, row=1)
    lbl_ingrediente = Label(labelFrame, text="Introduca un ingrediente")
    lbl_ingrediente.grid(column=0, row=2)

    ingrediente = Entry(labelFrame)
    ingrediente.grid(column=1, row=2)

    btn = Button(labelFrame, text="Buscar", command=lambda: reglas.contiene(ingrediente,labelFrame))
    btn.grid(column=1, row=3)

    ### QUESTION 2
    lbl_ingrediente = Label(labelFrame, text="¿Cuáles platos se pueden preparar si tengo 3 ingredientes específicos?")
    lbl_ingrediente.grid(column=0, row=5)
    lbl_ingrediente = Label(labelFrame, text="Introduzca al menos 3 ingredientes (e.g: uno,dos,tres)")
    lbl_ingrediente.grid(column=0, row=6)

    ingredientes = Entry(labelFrame)
    ingredientes.grid(column=1, row=6)

    btn = Button(labelFrame, text="Buscar", command=lambda: reglas.contiene_al_menos_tres(ingredientes,labelFrame))
    btn.grid(column=1, row=7)

    ### QUESTION 3
    lbl_herramienta = Label(labelFrame, text="¿Cuáles platos implican usar una herramienta especifica?")
    lbl_herramienta.grid(column=0, row=10)
    lbl_herramienta = Label(labelFrame, text="Introduzca una herramienta")
    lbl_herramienta.grid(column=0, row=11)

    herramienta = Entry(labelFrame)
    herramienta.grid(column=1, row=11)

    btn = Button(labelFrame, text="Buscar", command=lambda: reglas.contiene_herramienta(herramienta,labelFrame))
    btn.grid(column=1, row=12)

