from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
from tkinter.ttk import *
from tkinter import filedialog
import reglas
import dieta


def dietView(content):


    labelFrame = ttk.LabelFrame(content, text="Formulario")
    labelFrame.grid(column=0, row=1)

    lbl_edad = Label(labelFrame, text="Digite su edad : ")
    lbl_edad.grid(column=0, row=1)

    edad = Entry(labelFrame)
    edad.grid(column=1, row=1)

    lbl_altura = Label(labelFrame, text="Digite su altura: ")
    lbl_altura.grid(column=0, row=2)

    altura = Entry(labelFrame)
    altura.grid(column=1, row=2)


    lbl_peso = Label(labelFrame, text="Digite su peso: ")
    lbl_peso.grid(column=0, row=3)

    peso = Entry(labelFrame)
    peso.grid(column=1, row=3)

    var = StringVar()
    R1 = Radiobutton(labelFrame, text="Masculino", variable=var, value="Masculino")
    R1.grid(column=0, row=6)

    R2 = Radiobutton(labelFrame, text="Femenino", variable=var, value="Femenino")
    R2.grid(column=0, row=7)

    btn = Button(labelFrame, text="Buscar", command=lambda: dieta.calcularGrasaCorporal(var.get(),peso.get(), edad.get(),altura.get(), labelFrame))
    btn.grid(column=0, row=8)



