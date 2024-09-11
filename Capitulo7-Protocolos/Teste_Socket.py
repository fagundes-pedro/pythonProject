import socket

resp = "S"
while resp == "S":
    url = input("Digite o endereço desejado: ")
    ip = socket.gethostbyname(url)
    print("O IP referente ao endereço passado é: ", ip)
    resp = input("Digite <S> para verificar outro endereço: ").upper()
