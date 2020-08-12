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

    lbl_sexo = Label(labelFrame, text="Seleccione su sexo: ")
    lbl_sexo.grid(column=0, row=4)

    sexo = StringVar()
    R1 = Radiobutton(labelFrame, text="Masculino", variable=sexo, value="Masculino")
    R1.grid(column=1, row=4)

    R2 = Radiobutton(labelFrame, text="Femenino", variable=sexo, value="Femenino")
    R2.grid(column=1, row=5)

    lbl_tmb = Label(labelFrame, text="Seleccione su actividad fisica: ")
    lbl_tmb.grid(column=0, row=6)

    tmb = StringVar()
    R1 = Radiobutton(labelFrame, text="Poco o ningún ejercicio", variable=tmb, value="1.2")
    R1.grid(column=0, row=7)

    R2 = Radiobutton(labelFrame, text="Ejercicio ligero (1 a 3 días a la semana)", variable=tmb, value="1.375")
    R2.grid(column=0, row=8)

    R3 = Radiobutton(labelFrame, text="Ejercicio moderado (3 a 5 días a la semana)", variable=tmb, value="1.55")
    R3.grid(column=0, row=9)

    R4 = Radiobutton(labelFrame, text="Deportista (6 -7 días a la semana)", variable=tmb, value="1.72")
    R4.grid(column=0, row=10)

    R5 = Radiobutton(labelFrame, text="Atleta (Entrenamientos mañana y tarde)", variable=tmb, value="1.9")
    R5.grid(column=0, row=11)

    btn = Button(labelFrame, text="Calcular", command=lambda: dieta.calcularGrasaCorporal(sexo.get(),peso.get(), edad.get(),altura.get(), tmb.get(),labelFrame))
    btn.grid(column=0, row=12)


