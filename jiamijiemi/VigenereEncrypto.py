def VigenereEncrypto (input , key) :
    ptLen = len(input)
    keyLen = len(key)
    quotient = ptLen // keyLen    #商
    remainder = ptLen % keyLen    #余
    out = ""
    for i in range (0 , quotient) :
        for j in range (0 , keyLen) :
            c = int((ord(input[i*keyLen+j]) - ord('a') + ord(key[j]) - ord('a')) % 26 + ord('a'))
            #global output
            out += chr (c)
    for i in range (0 , remainder) :
        c =  int((ord(input[quotient*keyLen+i]) - ord('a') + ord(key[i]) - ord('a')) % 26 + ord('a'))
        #global output
        out += chr (c)
    return out