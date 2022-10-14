import socket #importa modulo socket
 
TCP_IP = '192.168.0.23' # endereço IP do servidor 
TCP_PORTA = 32070       # porta disponibilizada pelo servidor
TAMANHO_BUFFER = 1024     # definição do tamanho do buffer
 
# Criação de socket TCP
# SOCK_STREAM, indica que será TCP.
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# IP e porta que o servidor deve aguardar a conexão
servidor.bind((TCP_IP, TCP_PORTA))

#Define o limite de conexões. 
servidor.listen(1)

print("Servidor dispoivel na porta 5005 e escutando.....") 
# Aceita conexão 
conn, addr = servidor.accept()
print ('Endereço conectado:', addr)
while 1:
    #dados retidados da mensagem recebida
    data = conn.recv(TAMANHO_BUFFER).decode('UTF-8')
    if data == 'quit':
        servidor.close()
    elif data != 'quit': 
       print ("Mensagem recebida:", data)
       data = input("Digite sua mensagem: ")
       conn.send(data.encode('UTF-8'))  # envia dados recebidos em letra maiuscula


    

