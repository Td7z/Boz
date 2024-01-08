import socket
import re

# Defina suas variÃ¡veis
NOME_DO_BOT = 'hawkinngx'
TOKEN = 'oauth:rdjdrtbvsumf3127zffe8xniwqcxvc'
CANAL = 'xxmarciano'

# Conecte-se ao servidor Twitch
HOST = 'irc.chat.twitch.tv'
PORTA = 6667

sock = socket.socket()
sock.connect((HOST, PORTA))
sock.send(f'PASS {TOKEN}\r\n'.encode('utf-8'))
sock.send(f'NICK {NOME_DO_BOT}\r\n'.encode('utf-8'))
sock.send(f'JOIN #{CANAL}\r\n'.encode('utf-8'))

# FunÃ§Ã£o para enviar mensagens ao chat
def enviar_mensagem(mensagem):
    sock.send(f'PRIVMSG #{CANAL} :{mensagem}\r\n'.encode('utf-8'))

# Loop principal para ouvir mensagens do chat
while True:
    resposta = sock.recv(2048).decode('utf-8')

    # LÃ³gica para identificar mensagens do chat
    if 'PING' in resposta:
        sock.send('PONG\r\n'.encode('utf-8'))
    elif 'PRIVMSG' in resposta:
        usuario = re.search(r'\w+', resposta).group(0)
        mensagem = re.search(r'PRIVMSG #\w+ :(.+)', resposta).group(1)
        
        print(f'{usuario}: {mensagem}')

        # Adicione sua lÃ³gica para responder a mensagens aqui

# Lembre-se de adicionar lÃ³gica para fechar a conexÃ£o quando necessÃ¡rio