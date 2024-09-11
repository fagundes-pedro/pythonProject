from socket import *

servidor = "localhost"
porta = 43210

msg = bytes(input("Digite algo para o servidor: "), 'utf-8')
obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.connect((servidor, porta))
obj_socket.send(msg)
resposta = obj_socket.recv(1024)
print("A resposta do servidor foi: ", resposta)
obj_socket.close()
