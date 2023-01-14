import socket
from threading import Thread

nickname = input('Enter your nickname here')

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 5500

client.connect((ip_address,port))

def recieve():
    while True:
        try:
          message = client.recv(2048).decode('utf-8')
          if message == 'NICKNAME':
                client.send(nickname.encode('utf-8'))
          else :
             print(message)
        except:
            print('Sorry! an eror has occured')
            client.close()
            break

def write():
    while True:
        message = '{} : {}'.format(nickname,input(' '))
        client.send(message.encode('utf-8'))

recieve_Thread = Thread(target= recieve)
recieve_Thread.start()

write_Thread = Thread(target= write)
write_Thread.start()
