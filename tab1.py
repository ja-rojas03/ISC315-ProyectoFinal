from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
from tkinter.ttk import *
from tkinter import filedialog
import views

def validateView(content):
    #XML SECTION
    labelFrame = ttk.LabelFrame(content, text="Seleccione un XML")
    labelFrame.grid(column=0, row=5)

    btn = Button(labelFrame, text="Buscar XML", command=lambda: views.openFile("all XML", "*.xml", txt))
    btn.grid(column=1, row=13)

    txt = scrolledtext.ScrolledText(labelFrame, width=40, height=3)
    txt.grid(column=1, row=15)
    txt.insert(INSERT, "No hay XML insertado...")

    #DTD SECTION
    labelFrame = ttk.LabelFrame(content, text="Seleccione un DTD")
    labelFrame.grid(column=0, row=6)

    btn2 = Button(labelFrame, text="Buscar DTD", command=lambda: views.openFile("all DTD", "*.dtd", txt2))
    btn2.grid(column=1, row=15)

    txt2 = scrolledtext.ScrolledText(labelFrame, width=40, height=3)
    txt2.grid(column=1, row=17)
    txt2.insert(INSERT, "No hay DTD insertado...")

    #PARSER ACTION SECTION
    labelFrame = ttk.LabelFrame(content, text="Parse XML / DTD")
    labelFrame.grid(column=0, row=8)

    btn3 = Button(labelFrame, text="Parse", command=lambda: views.parseFiles(views.files['xml'], views.files['dtd'], txt3))
    btn3.grid(column=1, row=19)

    txt3 = scrolledtext.ScrolledText(labelFrame, width=40, height=3)
    txt3.grid(column=1, row=17)
    txt3.insert(INSERT, "Validar...")