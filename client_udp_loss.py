import socket
import time

def client_udp():
    while True:
        message = None
        OC = input("Please type in your OC and numbers with the following format: operatorNumber1,Number2 For example,"
                   "a correct input looks like: +50,12 Another correct input is: /500,100")
        print("given input is %s" % OC)
        d = 0.1
        while True:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            client_socket.sendto(OC.encode(), ('127.0.0.1', 50003))
            client_socket.settimeout(d)
            try:
                message = client_socket.recv(2048)
                client_socket.close() #we've received the message, so we can close the socket now.
                break
            except socket.timeout:
                #if the socket does time out
                d = 2.0*d
                if d > 2.0:
                    client_socket.close()
                    raise TimeoutError("DEAD Server. Program can not proceed")
        print(message.decode())

if __name__ == '__main__':
    client_udp()










