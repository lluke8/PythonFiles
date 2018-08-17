import os
path = "."
def pesquisar(conteudo):
    for _, dirs, files in os.walk(path): 
        for file in files:
            if conteudo in file:
                print("Arquivo - %s Tipo:" % file, type(file))
        for dir in dirs:
            if conteudo in dir:
                print("Diretorio - %s Tipo:" % dir, type(dir))
                
pesquisar("foto")


