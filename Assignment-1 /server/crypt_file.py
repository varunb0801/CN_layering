def textEncrypt(text, encryptType = None ):
    
    if (encryptType == 'p'):
        return text
    
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
        
        return res
    
    elif (encryptType == 't'):
        return text[::-1]

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
