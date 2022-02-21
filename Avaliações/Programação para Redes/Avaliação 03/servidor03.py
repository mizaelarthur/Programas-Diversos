import socket
import threading


HOST = socket.gethostbyname('localhost')
PORTA = 6432


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORTA))
server.listen()


clients = []
usernames = ['mizael','marcelo']



def globalMessage(message):
    for client in clients:
        client.send(message)

def handleMessages(client):
    while True:
        try:
            receiveMessageFromClient = client.recv(2048).decode('utf-8')
            globalMessage(f'{usernames[clients.index(client)]} :{receiveMessageFromClient}'.encode('utf-8'))
        except:
            clientLeaved = clients.index(client)
            client.close()
            clients.remove(clients[clientLeaved])
            clientLeavedUsername = usernames[clientLeaved]
            print(f'{clientLeavedUsername} has left the chat...')
            globalMessage(f'{clientLeavedUsername} has left us...'.encode('utf-8'))
            usernames.remove(clientLeavedUsername)


def initialConnection():
    while True:
        try:
            client, address = server.accept()
            print(f"New Connetion: {str(address)}")
            clients.append(client)
            client.send('login'.encode('utf-8'))
            username = client.recv(2048).decode('utf-8')
            #usernames.append(username)
            if username in usernames:
                globalMessage(f'{username} Se juntou a sala!'.encode('utf-8'))
                user_thread = threading.Thread(target=handleMessages,args=(client,))
                user_thread.start()
            else:
                print('Tentativa de Login falhou!!!')
                client.send('LoginFalhou'.encode('utf-8'))
        except:
            pass


initialConnection()
