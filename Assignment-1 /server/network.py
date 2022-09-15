import socket

def createListenSocket(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(100)
    return sock


def recieveMessage(sock):

    data = bytearray()
    msg = ''
    while not msg:
        recivedData = sock.recv(8192)
        if not recivedData:
            raise ConnectionError()
        data = data + recivedData
        if b':' in recivedData:
            msg = data.rstrip(b':')
    msg = msg.decode('utf-8')

    encryptionType = msg[-1]
    msg = msg[:-2]

    return msg, encryptionType


def handleClient(sock, address):
    try:
        msg, encryptionType = recieveMessage(sock)
        return msg, encryptionType
    except ( ConnectionError, BrokenPipeError ):
        return 'Error', 0
    
def messageSent(sock, msg):
    msg = str(msg) +'\0'
    try:
        sock.sendall(msg.encode('utf-8'))
        print("Outgoing Message...")
        return 0
    except ( ConnectionError, BrokenPipeError ):
        print('Error in Connection')
    finally:
        print('Connection is Closed')
        sock.close()

def sendFile(sock, file, fN):
    fN = fN + '\0'
    try:
        print('Sending FileName... ')
        sock.sendall(fN.encode('utf-8'))
        print('Outgoing Data... ')
        sock.sendfile(file)
    except ( ConnectionError, BrokenPipeError ):
        print('File cannot be sent')

def receiveFile(sock):
    try:
        print('File Name Recieved...')
        fN = sock.recv(8192).rstrip(b'\0').decode('utf-8')
        print('File Data Recieved...')
        data = sock.recv(8192)

        return data, fN
    except ( ConnectionError ):
        print('Error in Connection')
