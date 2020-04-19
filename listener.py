import socket
import time, sys

def clent_listener() -> None:
  try:
    SERVER_ADDRESS = '127.0.0.1'
    SERVER_PORT = 12000
    socket_instance = socket.socket()
    socket_instance.connect((SERVER_ADDRESS, SERVER_PORT))
    while True:
      try:
        try:
          server_msg = socket_instance.recv(1024)
          print(server_msg.decode())

        except Exception as e:
          print(f'Error handling server messages, closing conection: {e}')
          socket_instance.close()
      except KeyboardInterrupt:
        print ('Bye - cliente listener close')
        sys.exit()
        break

    socket_instance.close()
  except KeyboardInterrupt:
    print ('Bye - cliente listener close')
    sys.exit()
  except Exception as e:
    print(f'Error connecting to server socket {e}')


if __name__ == '__main__':
    clent_listener()
