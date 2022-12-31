from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

try:
    iv = int("7a56c473ba65e25d4f34c84fdea67952", 16)
    cipher = int("00f02c46d5027a70de09290e2f726d05", 16)
    key = input("Key: ")
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(cipher), AES.block_size)
    print("Message: ", plaintext)
except (ValueError, KeyError):
    print("ERROR!")
