import os

print(os.getcwd())

os.chdir('/home/alisson/Área de Trabalho/python praticas/pratica24/texto')

texto=open('solidão.txt')

for line in texto:
    print(line, end='')

