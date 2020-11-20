import VigenereEncrypto
import VigenereDecrypto
while 1:
    b=int(input('请选择类型:（0：加密；1：解密:）'))
    if b==0:
        print("维吉尼亚加密")
        plainText = input ("请输入明文 : ")
        key = input ("请输入密钥 : ")
        plainTextToCipherText = VigenereEncrypto.VigenereEncrypto (plainText , key)
        print("加密后得到的暗文是 : " + plainTextToCipherText)
    else:
        print("维吉尼亚解密")
        cipherText = input ("请输入密文 : ")
        key = input ("请输入密钥 : ")
        cipherTextToPlainText = VigenereDecrypto.VigenereDecrypto (cipherText , key)
        print("解密后得到的明文是 : " + cipherTextToPlainText)