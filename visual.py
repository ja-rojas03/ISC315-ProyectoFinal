# from pyswip import Prolog, Query, Variable, Functor
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import tabs

window = Tk()
window.title("Calculadora de Dietas")
window.geometry("720x480")

tabControl = ttk.Notebook(window)

tabControl.grid(column=0, row=3)

# LABEL 1
lbl = Label(window, text="Calculadora de Dietas", font=("Arial Bold", 15))
lbl.grid(column=0, row=0)

#PARSER  TAB
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="Parser")
tabs.parserTab(tab1)

#RUN VISUAL
window.mainloop()