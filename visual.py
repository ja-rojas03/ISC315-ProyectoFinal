from pyswip import Prolog, Query, Variable, Functor
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import views

window = Tk()
window.title("Calculadora de Dietas")
window.geometry("720x700")

tabControl = ttk.Notebook(window)

tabControl.grid(column=0, row=3)

# LABEL 1
lbl = Label(window, text="Calculadora de Dietas", font=("Arial Bold", 15))
lbl.grid(column=0, row=0)

#PARSER  TAB
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="Parser")
views.parserTab(tab1)

#RULES  TAB
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Reglas")
views.rulesTab(tab2)

#RULES  TAB
tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text="Reglas")
views.moreRulesTab(tab3)

#DIET  TAB
tab4 = ttk.Frame(tabControl)
tabControl.add(tab4, text="Dieta")
views.dietTab(tab4)

#RUN VISUAL
window.mainloop()