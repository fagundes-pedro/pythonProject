import json

dicionario = {
    "PE": ["PEDRO FAGUNDES", "29/03/2021", "ESCRITORIO"],
    "THAU": ["THAUANA FAGUNDES", "22/03/2021", "QUARTO"],
    "NABLA": ["NABLA FAGUNDES", "18/03/2021", "SALA"]
}

with open("bd.json", "w") as arquivo:
    json.dump(dicionario, arquivo)

with open("bd.json", "r") as arquivo:
    mostrar = json.load(arquivo)
    for chave, dados in mostrar.items():
        print(chave + " | " + str(dados))
