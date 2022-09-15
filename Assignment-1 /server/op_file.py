import os
import subprocess


def handleCmd(command):

    if ( command.startswith('cd ') ):
        #checking if the path is a directory
        fP = command[3:]

        if os.path.isdir(fP):
            os.chdir(fP)
            return 'OK'
        else:
            return 'Directory Specified is not valid\nNOT OK'

    elif (command == 'ls'):
        res = subprocess.run(command, capture_output=True).stdout.decode('utf-8')
        return res

    elif (command == 'cwd'):
        res = subprocess.run('pwd', capture_output=True).stdout.decode('utf-8')
        return res
    
    elif ( command.startswith('dwd ') ):
        #checking if the path is a file
        fP = command[4:]
        
        if os.path.isfile(fP):
            fN = os.path.basename(fP)
            file = open(fP, 'rb')
            return file, fN
        else:
            return 'NOT OK'
    
    return 'Requested Command is not valid'

def writeFile(data, name):
    file = open(name, 'wb')
    file.write(data)
    file.close()
    print('File Write Successful')
    return 0