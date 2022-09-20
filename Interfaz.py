import tkinter as tk
from tkinter import Label, Button, Entry
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu
from tkinter import filedialog
from Analizador import Analizador


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

menu = Menu(principal)
principal.config(menu=menu)

def abrirarchivo():
    ruta=filedialog.askopenfilename(title="Cargar Archivo", filetypes=(("Text files", "*.lfp"), ("all files", "*.*")))
    if ruta != "":
        archivo = open(ruta, "r")
        contenido = archivo.read()
        a = Analizador()
        a.analizar(contenido)
        a.mostrar()


fileMenu = Menu(menu)
fileMenu.add_command(label="Abrir", command=abrirarchivo)
fileMenu.add_command(label="Guardar")
fileMenu.add_command(label="Guardar Como")
fileMenu.add_command(label="Errores")
menu.add_cascade(label="Archivo", menu=fileMenu)

editMenu = Menu(menu)
editMenu.add_command(label="Manual de Usuario")
editMenu.add_command(label="Manual Técnico")
editMenu.add_command(label="Temas de Ayuda")
menu.add_cascade(label="Ayuda", menu=editMenu)


#botones
bot1 = Button(principal, text="Analizar", font="Arial 12", bg="#FFD8D4")
bot1.place(x=50, y= 100)
bot2 = Button(principal, text="Salir", font="Arial 12", bg="#FFD8D4")
bot2.place(x=150, y= 100)




principal.mainloop()





