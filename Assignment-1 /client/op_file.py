import os

def writeFile(data, name):
    file = open(name, 'wb')
    file.write(data)
    file.close()
    return 0

def readFile(cmd):
    fP = cmd[4:]

    if os.path.isfile(fP):
        fN = os.path.basename(fP)
        file = open(fP, 'rb')
        return file, fN
    else:
        raise Exception('enter a valid file path')