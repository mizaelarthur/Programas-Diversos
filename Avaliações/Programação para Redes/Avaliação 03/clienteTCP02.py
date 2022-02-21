import socket
import threading

Servidor = socket.gethostbyname('localhost')
PORTA = 6432

cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    login = input('Login: ')
    cliente.connect((Servidor,PORTA))
    print(f'Conectado!')
except:
    print(f'Erro ao conectar!')

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

def envio():
    while True:
        cliente.send(input().encode('utf-8'))

thread1 = threading.Thread(target=MensagemRecebida,args=()) 
thread2 = threading.Thread(target=envio,args=())

thread1.start()
thread2.start()
