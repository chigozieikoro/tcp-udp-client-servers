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


def server_udp():
    #server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #open socket
    #server_socket.bind(('127.0.0.1', 50001))
    #this server socket is listening to it now, and we can now start processing requests.

    while True:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # open socket
        server_socket.bind(('127.0.0.1', 50001))
        (message, address) = server_socket.recvfrom(2048)
        decoded_message = message.decode()
        if valid_request(decoded_message) == False:
            server_socket.sendto("FAILURE! Result = -1, STATUS CODE 300".encode(), address)
        else:
            comma_index = decoded_message.find(',')
            operator = decoded_message[0]  # this will always be an operand.
            operand0 = int(decoded_message[1:comma_index])
            operand1 = int(decoded_message[comma_index + 1:])
            # its true so we can perform operation:
            result = 0
            if operator == '+':
                result = operand0 + operand1
            elif operator == '-':
                result = operand0 - operand1
            elif operator == '*':
                result = operand0 * operand1
            else:
                result = operand0 / operand1

            result_str = ("Result = %d, STATUS CODE 200" % result)
            server_socket.sendto(result_str.encode(),address)

        server_socket.close()





if __name__ == '__main__':
    server_udp()