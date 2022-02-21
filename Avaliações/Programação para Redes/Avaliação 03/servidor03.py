import socket
import threading
#
# Parametros do Servidor
HOST = socket.gethostbyname('localhost')
PORTA = 6432
#
# Parametros para conexão TCP
servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
servidor.bind((HOST,PORTA))
servidor.listen()
#
# Listas Contendo Logins Permitidos e Lista para Armazenar logins ativos
usuarios = []
logins = ['mizael','marcelo']
#
#
# Criação da Função que irá enviar mensagem para todos do servidor
def MensagemGeral(mensagem):
    for usuario in usuarios:
        usuario.send(mensagem)
# Função que recebe mensagem, decodifica e envia para função MensagemGeral
def TrocaMensagem(usuario):
    while True:
        try:
            MensagemRecebida = usuario.recv(1024).decode('utf-8')
            MensagemGeral(f'{logins[usuarios.index(usuario)]} :{MensagemRecebida}'.encode('utf-8'))
        except:
            usuarioSaiu = usuarios.index(usuario)
            usuario.close()
            usuarios.remove(usuarios[usuarioSaiu])
            usuarioSaiuLogin = logins[usuarioSaiu]
            print(f'{usuarioSaiuLogin} Saiu.')
            MensagemGeral(f'{usuarioSaiuLogin} Saiu'.encode('utf-8'))
            logins.remove(usuarioSaiuLogin)
#
# Função para iniciar a conexão, verificando Login
def Conexao():
    while True:
        try:
            usuario, address = servidor.accept()
            usuarios.append(usuario)
            usuario.send('login'.encode('utf-8'))
            login = usuario.recv(1024).decode('utf-8')
            if login in logins:
                MensagemGeral(f'{login} Se juntou a sala!'.encode('utf-8'))
                user_thread = threading.Thread(target=TrocaMensagem,args=(usuario,))
                user_thread.start()
            else:
                print('Tentativa de Login falhou!!!')
                usuario.send('LoginFalhou'.encode('utf-8'))
        except:
            pass
#
# Chamando a função para iniciar o código
Conexao()
