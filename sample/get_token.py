import json
import credentials
from encrypt_payload import encrypt 
from base64 import b64encode, b64decode

payload = json.dumps({
    'USERNAME': credentials.userId,
    'PASSWORD': 'P;_H,vblu9wB-Mk]'
})

base64_cipher_text = encrypt(payload, credentials.publicKey)
print("base64 cipher text->", base64_cipher_text)
