import os # importação do modulo

library_log = "C:\\system\\LOG\\log.txt" # diretorio do arquivo de log.txt

os.makedirs(os.path.dirname(library_log),exist_ok=True) # código que verifica se o arquivo já está criado, caso não esteja, ele cria

def insert_log(value): # function que cria e escreve dados no .txt
    with open(library_log, "a") as create_library_log:
        create_library_log.write(f"{value}\n")
    