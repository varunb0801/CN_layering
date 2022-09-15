def textEncrypt(text, encryptType = None ):
    lis = ['p', 'c', 't', 'q']
    while (encryptType == None or encryptType not in lis):
        try :
            encryptType = input('enter the type of encryption you want. input: \np for plain \nc for caesar \nt for transpose\nq to quit\n')
        except:
            print('Input type does not exist. Try again')
            continue
        if (encryptType not in lis):
            print('Input type is not valid.')
        else:
            break
    
    if (encryptType == 'p'):
        return text, 'p'
    
    elif (encryptType == 'c'):

        res = ""

        for i in range(len(text)):
            curr = text[i]

            if( curr.isupper() ):
                res += chr((ord(curr) + 2 - 65) % 26 + 65)
            elif( curr.islower() ):
                res += chr((ord(curr) + 2 - 97) % 26 + 97)
            elif( curr.isnumeric() ):
                res += str((int(curr) + 2)%10)
            else:
                res += curr
        
        return res, 'c'
    
    elif (encryptType == 't'):
        return text[::-1], 't'
    
    elif (encryptType == 'q'):
        return None, 'q'

def textDecrypt(text, encryptType):

    if(encryptType == 'p'):
        return text

    elif(encryptType == 'c'):

        res = ''

        for i in range(len(text)):
            curr = text[i]

            if( curr.isupper() ):
                res += chr((ord(curr) + 24 - 65) % 26 + 65)
            elif( curr.islower() ):
                res += chr((ord(curr) + 24 - 97) % 26 + 97)
            elif( curr.isnumeric() ):
                res += str((int(curr) - 2)%10)
            else:
                res += curr

        return res

    elif(encryptType == 't'):
        return text[::-1]
