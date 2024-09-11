from socket import *

servidor = "localhost"
porta = 43210

obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.connect((servidor, porta))
saida = ""

while saida != "X":
    msg = input("Digite sua mensagem para o servidor: ")
    obj_socket.sendto(msg.encode(), (servidor,porta))
    dados, origem = obj_socket.recvfrom(65535)
    print("A resposta do servidor foi: ", dados.decode())
    saida = input("Digite <X> se deseja sair: ").upper()

obj_socket.close()
