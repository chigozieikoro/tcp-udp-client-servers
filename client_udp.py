import socket


def client_udp():
    while True:
        OC = input("Please type in your OC and numbers with the following format: operatorNumber1,Number2 For example,"
               "a correct input looks like: +50,12 Another correct input is: /500,100")
        print("given input is %s" % OC)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.sendto(OC.encode(), ('127.0.0.1', 50001))
        returnedMessage, serverAddress = client_socket.recvfrom(2048)

        print(returnedMessage.decode())
        client_socket.close()


if __name__ == '__main__':
    client_udp()