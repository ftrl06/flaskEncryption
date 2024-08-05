from Crypto.Cipher import AES
import base64
import hashlib
from .config import SECRET_KEY

class AESCipher:
    def __init__(self):
        self.bs = 32
        self.key = hashlib.sha256(SECRET_KEY.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = base64.b64encode(AES.new(self.key, AES.MODE_CBC).iv).decode('utf-8')
        cipher = AES.new(self.key, AES.MODE_CBC, iv.encode('utf-8'))
        return iv + base64.b64encode(cipher.encrypt(raw.encode())).decode('utf-8')

    def decrypt(self, enc):
        iv = base64.b64decode(enc[:24].encode('utf-8'))
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(base64.b64decode(enc[24:].encode('utf-8')))).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]
