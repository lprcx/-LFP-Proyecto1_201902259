class token():
    def __init__(self, lexema, tipo, linea, columna):
        self.lexema = lexema
        self.tipo = tipo
        self.linea = linea
        self.columna = columna
    
    def mostrartoken(self):
        print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
        print("Lexema: ", self.lexema)
        print("Tipo: ", self.tipo)
        print("Linea: ", self.linea)
        print("Columna: ", self.columna)

class error():
    def __init__(self, caracter, descripcion, tipo, linea, columna):
        self.caracter = caracter
        self.descripcion = descripcion
        self.tipo = tipo
        self.linea = linea
        self.columna = columna
    
    def mostrarerror(self):
        print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
        print("Caracter: ", self.caracter)
        print("Descripción: ", self.descripcion)
        print("Tipo: ", self.tipo)
        print("Linea: ", self.linea)
        print("Columna: ", self.columna)