def cmdSend(socket, cmd, encryptType):

    cmd += ':' + str(encryptType) + ':'
    socket.sendall(cmd.encode('utf-8'))
    return 0

def outputRecieved(socket):
    data = bytearray()
    msg = ''
    while not msg:
        recievedata = socket.recv(8192)
        if not recievedata:
            raise ConnectionError()
        data = data + recievedata
        if b'\0' in recievedata:
            msg = data.rstrip(b'\0')
    msg = msg.decode('utf-8')
    return msg

def getFile(socket):
    try:
        fN = socket.recv(8192).rstrip(b'\0').decode('utf-8')
        data = socket.recv(8192)

        return data, fN
    except:
        raise ConnectionError()

def sendFile(sock, file, fN):
    fN = fN + '\0'
    try:
        print('Sending the File: ')
        sock.sendall(fN.encode('utf-8'))
        print('Sending Data: ')
        sock.sendfile(file)
    except ( ConnectionError, BrokenPipeError ):
        raise ConnectionError()


