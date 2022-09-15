import socket
import crypt_file, op_file, network

HOST = 'localhost'
PORT = 8000

if __name__ == '__main__':

    while True:

        try : 

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT))
            print('\nConnected to {}:{}'.format(HOST, PORT))

            command = input("Enter the command you wish to run, press q to quit\n")

            if command == 'q':
                break

            encryptcmd, encryptType = crypt_file.textEncrypt(command)

            if encryptType == 'q':
                break

            network.cmdSend(sock, encryptcmd, encryptType)

            if (command.startswith('dwd ')):

                file, fN = network.getFile(sock)
                decryptName = crypt_file.textDecrypt(fN, encryptType)

                if ('NOT OK' in fN):
                    print('Requested file not found.')
                    print('NOT OK')
                
                else:
                    op_file.writeFile(file, decryptName)
                    receivedOutput = network.outputRecieved(sock)
                    print(crypt_file.textDecrypt(receivedOutput, encryptType))

            elif( command.startswith('upd ')):
                try:
                    file, fN = op_file.readFile(command)

                    encryptedName = crypt_file.textEncrypt(fN, encryptType)[0]

                    network.sendFile(sock, file, encryptedName)

                    receivedOutput = network.outputRecieved(sock)
                    print(crypt_file.textDecrypt(receivedOutput, encryptType))
                except:
                    print('error in sending file\nNOT OK')
            else:
                receivedOutput = network.outputRecieved(sock)
                print(crypt_file.textDecrypt(receivedOutput, encryptType))
        
        except ConnectionError:
            print('Error in Socket')
            break
        finally :
            sock.close()
            print('Close the connection\n')