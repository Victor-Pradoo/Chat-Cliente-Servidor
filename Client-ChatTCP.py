
import socket #importa modulo socket

TCP_IP = '192.168.0.23' # endereço IP do servidor 
TCP_PORTA = 32070      # porta disponibilizada pelo servidor
TAMANHO_BUFFER = 1024

MENSAGEM  = input("Digite sua mensagem para o servidor: ")

# Criação de socket TCP do cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Conecta ao servidor em IP e porta especifica 
cliente.connect((TCP_IP, TCP_PORTA))

# envia mensagem para servidor 
cliente.send(MENSAGEM.encode('UTF-8'))

i =0
# recebe dados do servidor 
while i != 1:

    data = cliente.recv(TAMANHO_BUFFER).decode('UTF-8')
    if data == 'quit': #caso receba a mesagem quit, fecha conexão com o servidor.
        cliente.close()
        i = i + 1
    elif data != 'quit': 
        print ("Mensagem recebida:", data)
        data = input("Digite sua mensagem: ")
        cliente.send(data.encode('UTF-8'))

