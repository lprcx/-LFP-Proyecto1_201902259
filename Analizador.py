from clases import token, error

class Analizador():
    def __init__(self):
        self.listatokens = []
        self.listaerrores = []
    
    def analizar(self, texto):
        self.listatokens = []
        self.listaerrores = []


        texto+="$"
        indice = 0
        linea = 1
        columna = 1
        buffer = ""
        estado = "qo"

        while indice < len(texto):
            caracter = texto[indice]
            if estado == "qo":
                if caracter =="<":
                    buffer = caracter
                    columna+=1
                    self.listatokens.append(token(buffer, "menor_que", linea, columna))
                    buffer=""
                    estado = "qo"
                elif caracter == ">":
                    buffer = caracter
                    columna+=1
                    self.listatokens.append(token(buffer, "mayor_que", linea, columna))
                    buffer=""
                    estado = "q5"
                elif caracter == "/":
                    buffer = caracter
                    columna+=1
                    self.listatokens.append(token(buffer, "diagonal", linea, columna))
                    buffer=""
                    estado = "qo"
                elif caracter == "=":
                    buffer = caracter
                    columna+=1
                    self.listatokens.append(token(buffer, "igual", linea, columna))
                    buffer=""
                    estado = "qo"
                elif caracter == "[":
                    buffer = caracter
                    columna+=1
                    estado = "q4"
                elif caracter == "\n":
                    linea+=1
                    columna=1
                elif caracter == " " or caracter=="\t":
                    columna+=1
                elif caracter.isalpha() and not (caracter.isdigit()):
                    buffer = caracter
                    columna+=1
                    estado = "q1"
                elif caracter.isdigit():
                    buffer = caracter
                    columna+=1
                    estado = "q2"
                elif caracter == "$":
                    buffer=caracter
                    columna+=1
                    self.listatokens.append(token(buffer, "<< EOF >>", linea, columna))
                    buffer=""
                    estado="qo"
                    print("Terminó de analizar")
            elif estado == "q1":
                if caracter.isalpha() and not (caracter.isdigit()):
                    buffer+=caracter
                    columna+=1
                    estado = "q1"
                else:
                    if buffer=="Operacion":
                        self.listatokens.append(token(buffer, "OPERACION", linea, columna))
                    elif buffer == "SUMA":
                        self.listatokens.append(token(buffer, "SUMA", linea, columna))
                    elif buffer == "RESTA":
                        self.listatokens.append(token(buffer, "RESTA", linea, columna))
                    elif buffer == "MULTIPLICACION":
                        self.listatokens.append(token(buffer, "MULTIPLICACION", linea, columna))
                    elif buffer == "DIVISION":
                        self.listatokens.append(token(buffer, "DIVISION", linea, columna))
                    elif buffer == "MOD":
                        self.listatokens.append(token(buffer, "MOD", linea, columna))
                    elif buffer == "POTENCIA":
                        self.listatokens.append(token(buffer, "POTENCIA", linea, columna))
                    elif buffer == "RAIZ":
                        self.listatokens.append(token(buffer, "RAIZ", linea, columna))
                    elif buffer == "INVERSO":
                        self.listatokens.append(token(buffer, "INVERSO", linea, columna))
                    elif buffer == "SENO":
                        self.listatokens.append(token(buffer, "SENO", linea, columna))
                    elif buffer == "COSENO":
                        self.listatokens.append(token(buffer, "COSENO", linea, columna))
                    elif buffer == "TANGENTE":
                        self.listatokens.append(token(buffer, "TANGENTE", linea, columna))
                    elif buffer == "Tipo":
                        self.listatokens.append(token(buffer, "Tipo", linea, columna))
                    elif buffer == "Numero":
                        self.listatokens.append(token(buffer, "Numero", linea, columna))
                    elif buffer == "Texto":
                        self.listatokens.append(token(buffer, "Texto", linea, columna))
                    elif buffer == "Funcion":
                        self.listatokens.append(token(buffer, "Funcion", linea, columna))
                    elif buffer == "ESCRIBIR":
                        self.listatokens.append(token(buffer, "ESCRIBIR", linea, columna))
                    elif buffer == "Titulo":
                        self.listatokens.append(token(buffer, "Titulo", linea, columna))
                    elif buffer == "Descripcion":
                        self.listatokens.append(token(buffer, "Descripcion", linea, columna))
                    elif buffer == "Contenido":
                        self.listatokens.append(token(buffer, "Contenido", linea, columna))
                    elif buffer == "Estilo":
                        self.listatokens.append(token(buffer, "Estilo", linea, columna))
                    elif buffer == "Color":
                        self.listatokens.append(token(buffer, "Color", linea, columna))
                    elif buffer == "Tamanio":
                        self.listatokens.append(token(buffer, "Tamanio", linea, columna))
                    elif buffer == "ROJO":
                        self.listatokens.append(token(buffer, "COLOR", linea, columna))
                    elif buffer == "VERDE":
                        self.listatokens.append(token(buffer, "COLOR", linea, columna))
                    elif buffer == "AMARILLO":
                        self.listatokens.append(token(buffer, "COLOR", linea, columna))
                    elif buffer == "CELESTE":
                        self.listatokens.append(token(buffer, "COLOR", linea, columna))
                    elif buffer == "ROSADO":
                        self.listatokens.append(token(buffer, "COLOR", linea, columna))
                    elif buffer == "NEGRO":
                        self.listatokens.append(token(buffer, "COLOR", linea, columna))
                    elif buffer == "BLANCO":
                        self.listatokens.append(token(buffer, "COLOR", linea, columna))
                    elif buffer == "ANARANJADO":
                        self.listatokens.append(token(buffer, "COLOR", linea, columna))
                    elif buffer == "NARANJA":
                        self.listatokens.append(token(buffer, "COLOR", linea, columna))
                    elif buffer == "CAFE":
                        self.listatokens.append(token(buffer, "COLOR", linea, columna))
                    elif buffer == "AZUL":
                        self.listatokens.append(token(buffer, "COLOR", linea, columna))
                    elif buffer == "GRIS":
                        self.listatokens.append(token(buffer, "COLOR", linea, columna))
                    elif buffer == "MORADO":
                        self.listatokens.append(token(buffer, "COLOR", linea, columna))
                    buffer=""
                    estado = "qo"
                    indice-=1
            elif estado == "q2":
                if caracter.isdigit():
                    buffer+=caracter
                    columna+=1
                    estado = "q2"
                elif caracter == ".":
                    buffer+=caracter
                    columna+=1
                    estado = "q3"
                else:
                    self.listatokens.append(token(buffer, "NUMERO", linea, columna))
                    buffer = ""
                    indice-=1
                    estado="qo"
            elif estado == "q3":
                if caracter.isdigit():
                    buffer+=caracter
                    columna+=1
                    estado = "q3"
                else:
                    self.listatokens.append(token(buffer, "NUMERO", linea, columna))
                    buffer = ""
                    indice-=1
                    estado="qo"
            elif estado == "q4":
                if caracter.isalpha() and not (caracter.isdigit()):
                    buffer+=caracter
                    columna+=1
                    estado = "q4"
                elif caracter == "]":
                    buffer+=caracter
                    columna+=1
                    if buffer == "[TEXTO]":
                        self.listatokens.append(token(buffer, "[TEXTO]", linea, columna))
                    elif buffer=="[TIPO]":
                        self.listatokens.append(token(buffer, "[TIPO]", linea, columna))
                    buffer = ""
                    indice-=1
                    estado="qo"
            elif estado == "q5":
                if caracter!="<":
                    buffer+=caracter
                    if caracter == "\n":
                        columna = 1
                        linea+=1
                    columna+=1
                    estado = "q5"
                else:
                    self.listatokens.append(token(buffer, "CONTENIDO", linea, columna))
                    buffer = ""
                    indice-=1
                    estado = "qo"
                    



            indice+=1


    def mostrar(self):
        print("tokens:")
        for t in self.listatokens:
            t.mostrartoken()
            print("")
        print("errores:")
        for e in self.listaerrores:
            e.mostrarerror()
            print("")
        print("tokens: ", str(len(self.listatokens)))
        print("errores: ", str(len(self.listaerrores)))
