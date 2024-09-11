with open("teste.txt", "r") as arquivo:
    texto = arquivo.read()

print(texto[::-1])
numero = float(texto[8]) * 1.5
print(str(numero))