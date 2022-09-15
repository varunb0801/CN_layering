import op_file, crypt_file, network
from socket import *

HOST = 'localhost'
PORT = 8000

if __name__ == '__main__':

    lis_socket = network.createListenSocket(HOST, PORT)
    address = lis_socket.getsockname()
    print('Listening on {}'.format(address))

    while True:

        Socket_client, address = lis_socket.accept()
        print('Connection from {}'.format(address))

        msg, encryptType = network.handleClient(Socket_client, address)

        if(msg == 'Error'):
            print('Connection Closed')
            continue

        decryptcmd = crypt_file.textDecrypt(msg, encryptType)
        print(decryptcmd)
        if( decryptcmd.startswith('dwd ') ):

            try:
                file, fileName = op_file.handleCmd(decryptcmd)
        
                encryptedName = crypt_file.textEncrypt(fileName, encryptType)

                network.sendFile(Socket_client, file, encryptedName)
                network.messageSent(Socket_client, crypt_file.textEncrypt('OK', encryptType))
            except ( ValueError ):
                network.messageSent(Socket_client, crypt_file.textEncrypt('NOT OK', encryptType))
            
        elif(decryptcmd.startswith('upd ')):

            try:
                data, fileName = network.receiveFile(Socket_client)

                decryptedName = crypt_file.textDecrypt(fileName, encryptType)

                op_file.writeFile(data, decryptedName)
                network.messageSent(Socket_client, crypt_file.textEncrypt('OK', encryptType))
            except:
                network.messageSent(Socket_client, crypt_file.textEncrypt('NOT OK', encryptType))

        else:
            output = op_file.handleCmd(decryptcmd)
            print(output)
            encryptedMessage = crypt_file.textEncrypt(output, encryptType)
            network.messageSent(Socket_client, encryptedMessage)