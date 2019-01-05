import socket


def valid_request(request):
    if request[0] == '+' or request[0] == '-' or request[0] == '*' or request[0] == '/':
        print("valid operator")
        print(request[0])
    else:
        return False
    comma_index = request.find(',')
    try:
        operand0 = int(request[1:comma_index])
    except ValueError:
        print("invalid operand present")
        return False

    try:
        operand1 =  int(request[comma_index + 1:])
    except ValueError:
        print("invalid operand present!")
        return False
    operand1 = int(request[comma_index + 1:])
    if request[0] == '/' and operand1 == 0:
        print("divide by 0 error")
        return False
    return True


def server_tcp():
    #server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #open socket
    #server_socket.bind(('127.0.0.1', 50001))
    #server_socket.listen(1)
    #this server socket is listening to it now, and we can now start processing requests.

    while True:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # open socket
        server_socket.bind(('127.0.0.1', 50002))
        server_socket.listen(1)
        (client_socket, address) = server_socket.accept()

        #we can use client socket to interact with the client.
        received_request  = client_socket.recv(1024)
        received_request = received_request.decode()
        #check string for validity
        #tentative format example: "+100000,2"
        if valid_request(received_request) == False:
            client_socket.send("FAILURE! Result = -1, STATUS CODE 300".encode())
        else:
            comma_index = received_request.find(',')
            operator = received_request[0] #this will always be an operand.
            operand0 = int(received_request[1:comma_index])
            operand1 = int(received_request[comma_index+1:])
            #its true so we can perform operation:
            result = 0
            if operator == '+':
                result = operand0 + operand1
            elif operator == '-':
                result = operand0 - operand1
            elif operator == '*':
                result = operand0*operand1
            else:
                result = operand0/operand1

            result_str = ("Result = %d, STATUS CODE 200" % result)
            client_socket.send(result_str.encode())

        server_socket.close()
        client_socket.close()






if __name__ == '__main__':
    server_tcp()

