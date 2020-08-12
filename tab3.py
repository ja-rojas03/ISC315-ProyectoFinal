from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
from tkinter.ttk import *
import reglas


def lastThreeRulesView(content):
    labelFrame = ttk.LabelFrame(content, text="Seleccione una regla")
    labelFrame.grid(column=0, row=1)
    # QUEST 4
    lbl_1 = Label(labelFrame, text="Si no tengo X herramienta, ¿cuáles platos puedo hacer?")
    lbl_1.grid(column=0, row=1)
    lbl_1 = Label(labelFrame, text="Introduzca una herramienta", anchor='e', width=30)
    lbl_1.grid(column=0, row=2)

    herr = Entry(labelFrame)
    herr.grid(column=1, row=2)

    print('REEEEE', herr.get())

    btn_1 = Button(labelFrame, text="Buscar", command=lambda: reglas.no_tiene_herramienta(herr, labelFrame))
    btn_1.grid(column=1, row=3)

    # 5
    lbl_2 = Label(labelFrame, text="Si no tengo X ingrediente ¿qué plato puedo preparar?")
    lbl_2.grid(column=0, row=5)
    lbl_2 = Label(labelFrame, text="Introduzca un ingrediente: ")
    lbl_2.grid(column=0, row=6)

    ingred = Entry(labelFrame)
    ingred.grid(column=1, row=6)

    btn_2 = Button(labelFrame, text="Buscar", command=lambda: reglas.no_tiene_ingrediente(ingred, labelFrame))
    btn_2.grid(column=1, row=8)

    #6
    lbl_3 = Label(labelFrame, text="Si no tengo X ingrediente ni Y herramienta ¿qué plato puedo preparar?")
    lbl_3.grid(column=0, row=10)
    lbl_3 = Label(labelFrame, text="Introduzca un ingrediente: ")
    lbl_3.grid(column=0, row=11)
    lbl_4 = Label(labelFrame, text="Introduzca una herramienta: ")
    lbl_4.grid(column=0, row=12)

    hrrmnt = Entry(labelFrame)
    hrrmnt.grid(column=1, row=11)
    ngrdnt = Entry(labelFrame)
    ngrdnt.grid(column=1, row=12)

    btn_3 = Button(labelFrame, text="Buscar", command=lambda: reglas.no_tiene_ingrediente_ni_herramienta(hrrmnt,ngrdnt, labelFrame))
    btn_3.grid(column=1, row=13)



