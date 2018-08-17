import os

path = r"C:\Users\Pichau\Desktop\PythonFiles"

#print(os.listdir(path))

def pesquisar(conteudo):
    for roots, dirs, files in os.walk(path): #duvida: sem roots dá error
        for file in files:
            if conteudo in file:
                print("Arquivo - %s Tipo:" % file, type(file))
        for dir in dirs:
            if conteudo in dir:
                print("Diretorio - %s Tipo:" % dir, type(dir))
   # for root in roots:
       # print("Raiz - %s" % roots)

pesquisar("foto")

