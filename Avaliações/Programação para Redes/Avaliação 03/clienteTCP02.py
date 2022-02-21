import socket
import threading
#
# Parametros do Servidor
Servidor = socket.gethostbyname('localhost')
PORTA = 6432
#
# Parametros do cliente para conexão TCP via socket
cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#
# Parametro para tentar o login, caso falhe, exibe mensagem de erro
try:
    login = input('Login: ')
    cliente.connect((Servidor,PORTA))
    print(f'Conectado!')
except:
    print(f'Erro ao conectar!')
#
# Função para enviar o login inserido, caso solicitado pelo servidor, ao receber do servidor a
# mensagem login
def MensagemRecebida():
    while True:
        try:
            mensagem = cliente.recv(1024).decode('utf-8')
            if mensagem=='login':
                cliente.send(login.encode('utf-8'))
            else:
                print(mensagem)
        except:
            print('Sem conexão com o servidor')
#
# Parametro para envio das mensagens
def envio():
    while True:
        cliente.send(input().encode('utf-8'))
#
# Declaração das Threads
thread1 = threading.Thread(target=MensagemRecebida,args=()) 
thread2 = threading.Thread(target=envio,args=())
#
# Chamando a thread para rodar o programa por completo
thread1.start()
thread2.start()
