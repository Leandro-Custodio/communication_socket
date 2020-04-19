import socket
import time, sys

def client() -> None:
  try:
    SERVER_ADDRESS = '127.0.0.1'
    SERVER_PORT = 12000
    socket_instance = socket.socket()
    socket_instance.connect((SERVER_ADDRESS, SERVER_PORT))
    while True:
      try:
        msg = input('Insider your message for client listener: ')
        if msg == 'exit':
          break
        socket_instance.send(msg.encode())
      except KeyboardInterrupt:
        print ('Bye - Client Close')
        sys.exit()
        break
    socket_instance.close()
  except Exception as e:
    print(f'Error connecting to server socket {e}')

if __name__ == '__main__':
    client()
