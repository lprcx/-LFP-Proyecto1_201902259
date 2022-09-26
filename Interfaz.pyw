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
from Operacion import operacion
from Reporte import generarreporteoperaciones
import math
import os
scanner = Analizador()
operaciones = []


def ventanayuda():
    pass



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
    global operaciones
    if text_area.get(1.0, END)!="":
        scanner.analizar(text_area.get(1.0, END))
        if (len(scanner.listaerrores)==0):
            generarreportetokens(scanner.listatokens)
            obteneroperaciones(scanner.listatokens)
            generarreporteoperaciones(scanner.titulo, scanner.texto, operaciones)


def repoerrores():
    global scanner
    generarreporteerrores(scanner.listaerrores)

def obteneroperaciones(listatokens):
    global operaciones
    for i in range(len(listatokens)):
        if listatokens[i].tipo=="OPERACION" and listatokens[i+1].lexema=="=":
            print(listatokens[i+2].lexema)
            op = operacion(listatokens[i+2].lexema)
            contador = i+5
            t = listatokens[contador]
            while t.tipo=="Numero":
                if t.tipo == "Numero" and listatokens[contador+2].tipo=="NUMERO":
                    op.numeros.append(listatokens[contador+2].lexema)
                    print(listatokens[contador+2].lexema)
                    contador+=8
                else:
                    break
            if op.tipo=="SUMA":
                for n in op.numeros:
                    op.total+=float(n)
                print("Total: "+ str(op.total))
            elif op.tipo == "RESTA":
                op.total+=float(op.numeros[0])
                for i in range(1, len(op.numeros)):
                    op.total-=float(op.numeros[i])
                print("Total: "+ str(op.total))
            elif op.tipo == "MULTIPLICACION":
                op.total+=float(op.numeros[0])
                for i in range(1, len(op.numeros)):
                    op.total*=float(op.numeros[i])
                print("Total: "+ str(op.total))
            elif op.tipo == "DIVISION":
                op.total+=float(op.numeros[0])
                for i in range(1, len(op.numeros)):
                    op.total/=float(op.numeros[i])
                print("Total: "+ str(op.total))
            elif op.tipo == "POTENCIA":
                op.total+=float(op.numeros[0])
                for i in range(1, len(op.numeros)):
                    op.total= pow(float(op.numeros[i]),op.total)
                print("Total: "+ str(op.total))
            elif op.tipo == "RAIZ":
                op.total+=float(op.numeros[1])
                op.total= pow(op.total,float(1/float(op.numeros[0])))
                print("Total: "+ str(op.total))
            elif op.tipo == "INVERSO":
                op.total=1/float(op.numeros[0])
                print("Total: "+ str(op.total))
            elif op.tipo == "SENO":
                op.total=math.sin(math.radians(float(op.numeros[0])))
                print("Total: "+ str(op.total))
            elif op.tipo == "COSENO":
                op.total=math.cos(math.radians(float(op.numeros[0])))
                print("Total: "+ str(op.total))
            elif op.tipo == "TANGENTE":
                op.total=math.tan(math.radians(float(op.numeros[0])))
                print("Total: "+ str(op.total))
            elif op.tipo == "MOD":
                op.total+=float(op.numeros[0])
                for i in range(1, len(op.numeros)):
                    op.total%=float(op.numeros[i])
                print("Total: "+ str(op.total))

            operaciones.append(op)
                    

def guardarcomo():
    nombrearch=filedialog.asksaveasfilename(initialdir = "/",title = "Guardar como",filetypes = (("lfp files","*.lfp"),("todos los archivos","*.*")))
    if nombrearch!='':
        archi1=open(nombrearch+".lfp", "w", encoding="utf-8")
        archi1.write(text_area.get("1.0", tk.END))
        archi1.close()

def salir():
    principal.destroy()

def manualdeusuario():
    os.startfile("Documentacion\Manual de Usuario.pdf")

def temasdeayuda():
    os.startfile("Documentacion\Temas de ayuda.pdf")

def manualtecnico():
    os.startfile("Documentacion\Manual Técnico.pdf")


fileMenu = Menu(menu)
fileMenu.add_command(label="Abrir", command=abrirarchivo)
fileMenu.add_command(label="Guardar", command=guardarcomo)
fileMenu.add_command(label="Guardar Como", command = guardarcomo)
fileMenu.add_command(label="Errores", command=repoerrores)
menu.add_cascade(label="Archivo", menu=fileMenu)

editMenu = Menu(menu)
editMenu.add_command(label="Manual de Usuario", command= manualdeusuario)
editMenu.add_command(label="Manual Técnico", command=manualtecnico)
editMenu.add_command(label="Temas de Ayuda", command=temasdeayuda)
menu.add_cascade(label="Ayuda", menu=editMenu)

#botones
bot1 = Button(principal, text="Analizar", font="Arial 12", bg="#FFD8D4", command=analizar)
bot1.place(x=50, y= 100)
bot2 = Button(principal, text="Salir", font="Arial 12", bg="#FFD8D4", command=salir)
bot2.place(x=150, y= 100)

principal.mainloop()





