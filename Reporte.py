import os
texto = ""

def encabezado():
    global texto
    texto+="""
    
    <!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Reporte de Operaciones</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
  </head>
  <body>
    """

def titulo(t):
    global texto
    texto+="""<div class="p-3 mb-2 text-white" style="background-color: #9779c7;"><h1>"""+t+"""</h1></div>
    <br>"""

def descripcion(d):
    global texto
    texto+="""<div class="p-3 mb-2 text-white" style="background-color: #3a73af;"><h4>"""+d+"""</h4></div>
    <br>"""

def operacioneshtml(listao):
    global texto
    for o in listao:
        texto+="""<div class="card w-75">
      <div class="card-body">
        <h5 class="card-title">"""+o.tipo+"""</h5>
        <p class="card-text">"""
        if o.tipo == "SUMA":
            opt=""
            for i in range(len(o.numeros)):
                if i == len(o.numeros)-1:
                    opt+=str(o.numeros[i])
                else:
                    opt+=str(o.numeros[i])+"+"
            opt+="=" + str(o.total)
            texto+=opt+"""
            </p>
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
        </body>
        </html>
            """
        elif o.tipo == "RESTA":
            opt=""
            for i in range(len(o.numeros)):
                if i == len(o.numeros)-1:
                    opt+=str(o.numeros[i])
                else:
                    opt+=str(o.numeros[i])+"-"
            opt+="=" + str(o.total)
            texto+=opt+"""
            </p>
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
        </body>
        </html>
            """
        elif o.tipo == "MULTIPLICACION":
            opt=""
            for i in range(len(o.numeros)):
                if i == len(o.numeros)-1:
                    opt+=str(o.numeros[i])
                else:
                    opt+=str(o.numeros[i])+"*"
            opt+="=" + str(o.total)
            texto+=opt+"""
            </p>
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
        </body>
        </html>
            """
        elif o.tipo == "DIVISION":
            opt=""
            for i in range(len(o.numeros)):
                if i == len(o.numeros)-1:
                    opt+=str(o.numeros[i])
                else:
                    opt+=str(o.numeros[i])+"/"
            opt+="=" + str(o.total)
            texto+=opt+"""
            </p>
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
        </body>
        </html>
            """
        elif o.tipo == "POTENCIA":
            opt=str(o.numeros[1])+"^"+str(o.numeros[0])
            opt+="=" + str(o.total)
            texto+=opt+"""
            </p>
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
        </body>
        </html>
            """
        elif o.tipo == "RAIZ":
            opt=str(o.numeros[1])+"√"+str(o.numeros[0])
            opt+="=" + str(o.total)
            texto+=opt+"""
            </p>
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
        </body>
        </html>
            """
        elif o.tipo == "INVERSO":
            opt="1/"+str(o.numeros[0])
            opt+="=" + str(o.total)
            texto+=opt+"""
            </p>
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
        </body>
        </html>
            """
        elif o.tipo == "SENO":
            opt="sen("+str(o.numeros[0])+")"
            opt+="=" + str(o.total)
            texto+=opt+"""
            </p>
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
        </body>
        </html>
            """
        elif o.tipo == "COSENO":
            opt="cos("+str(o.numeros[0])+")"
            opt+="=" + str(o.total)
            texto+=opt+"""
            </p>
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
        </body>
        </html>
            """
        elif o.tipo == "TANGENTE":
            opt="tan("+str(o.numeros[0])+")"
            opt+="=" + str(o.total)
            texto+=opt+"""
            </p>
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
        </body>
        </html>
            """
        elif o.tipo == "MOD":
            opt=str(o.numeros[0])+"%"+str(o.numeros[1])
            opt+="=" + str(o.total)
            texto+=opt+"""
            </p>
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
        </body>
        </html>
            """

def crearreporte():
    global texto
    archivo = open("RESULTADOS_201902259.html", "w", encoding="UTF-8")
    archivo.write(texto)
    archivo.close()
    os.startfile("RESULTADOS_201902259.html")

def generarreporteoperaciones(ttitulo, ddescripcion, listao):
    encabezado()
    titulo(ttitulo)
    descripcion(ddescripcion)
    operacioneshtml(listao)
    crearreporte()