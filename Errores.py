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
    <title>Reporte de Errores</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
  </head>
  <body>
    <div class="p-3 mb-2 text-white" style="background-color: #9779c7;"><h1>Errores</h1></div>
    <br>
    """

def tabla(listat):
    global texto
    texto+="""
    <table class="table table-dark table-hover table-bordered">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Caracter</th>
            <th scope="col">Descripción</th>
            <th scope="col">Tipo</th>
            <th scope="col">Línea</th>
            <th scope="col">Columna</th>
          </tr>
        </thead>
        <tbody class="table-primary">
    """
    for i in range(len(listat)):
        texto+="""
        <tr>
            <th scope="row">"""+ str(i+1)+"""</th>
            <td>"""+ listat[i].caracter +"""</td>
            <td>"""+ listat[i].descripcion +"""</td>
            <td>"""+ listat[i].tipo +"""</td>
            <td>"""+ str(listat[i].linea) +"""</td>
            <td>"""+ str(listat[i].columna) +"""</td>
          </tr>
        """
    texto+="""
    </tbody>
      </table>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
  </body>
</html>
    """

def crearreporte():
    global texto
    archivo = open("Errores.html", "w", encoding="UTF-8")
    archivo.write(texto)
    archivo.close()
    os.startfile("Errores.html")

def generarreporteerrores(listat):
    encabezado()
    tabla(listat)
    crearreporte()