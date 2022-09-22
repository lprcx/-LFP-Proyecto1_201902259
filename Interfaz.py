import tkinter as tk
from tkinter import END, Label, Button, Entry
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu
from tkinter import filedialog
from Analizador import Analizador
from tkinter import scrolledtext
from Tokens import generarreportetokens
from Errores import generarreporteerrores
scanner = Analizador()


def ventanayuda():
    principal.destroy()
    ayuda()


principal = None


principal = tk.Tk()
principal.title("Menú Principal")
principal.geometry("600x500")
principal.config(bg="#D4E6FF")
principal.resizable(0,0)

#label
tit1 = Label(principal, text="Menú de Archivo", font="Arial 12 bold", fg="black", bg="#D4E6FF")
tit1.place(x=20,y=40)


text_area = scrolledtext.ScrolledText(principal, wrap = tk.WORD, width = 60, height = 15, font = ("Arial",12))
text_area.grid(column = 0, pady = 160, padx = 20)
text_area.focus()

menu = Menu(principal)
principal.config(menu=menu)

def abrirarchivo():
    ruta=filedialog.askopenfilename(title="Cargar Archivo", filetypes=(("Text files", "*.lfp"), ("all files", "*.*")))
    if ruta != "":
        archivo = open(ruta, "r")
        contenido = archivo.read()
        text_area.insert(tk.INSERT, contenido)

def analizar():
    global scanner
    if text_area.get(1.0, END)!="":
        scanner.analizar(text_area.get(1.0, END))
        if (len(scanner.listaerrores)==0):
            generarreportetokens(scanner.listatokens)

def repoerrores():
    global scanner
    generarreporteerrores(scanner.listaerrores)

fileMenu = Menu(menu)
fileMenu.add_command(label="Abrir", command=abrirarchivo)
fileMenu.add_command(label="Guardar")
fileMenu.add_command(label="Guardar Como")
fileMenu.add_command(label="Errores", command=repoerrores)
menu.add_cascade(label="Archivo", menu=fileMenu)

editMenu = Menu(menu)
editMenu.add_command(label="Manual de Usuario")
editMenu.add_command(label="Manual Técnico")
editMenu.add_command(label="Temas de Ayuda")
menu.add_cascade(label="Ayuda", menu=editMenu)

#botones
bot1 = Button(principal, text="Analizar", font="Arial 12", bg="#FFD8D4", command=analizar)
bot1.place(x=50, y= 100)
bot2 = Button(principal, text="Salir", font="Arial 12", bg="#FFD8D4")
bot2.place(x=150, y= 100)

principal.mainloop()





