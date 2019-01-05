import socket

def client_tcp():
    while True:
        OC = input("Please type in your OC and numbers with the following format: operatorNumber1,Number2 For example,"
                   "a correct input looks like: +50,12 Another correct input is: /500,100")
        print("given input is %s" %OC)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('127.0.0.1',50002))
        client_socket.send(OC.encode())
        returned_string = client_socket.recv(1024).decode()
        print(returned_string)
        client_socket.close()


if __name__ == '__main__':
    client_tcp()

