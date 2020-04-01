import os
import json
import random
import string
import subprocess
from base64 import b64encode, b64decode

def randomStringDigits(stringLength=6):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

def encrypt(payload, publicKey):
    keyFile = '/tmp/'+ randomStringDigits(8) + '.key' 
    inFile = '/tmp/'+ randomStringDigits(8) + '.json'
    outFile = '/tmp/'+ randomStringDigits(8) + '.data'

    with open(keyFile, "w") as file:
        file.write(publicKey)

    with open(inFile, 'w') as file:
        file.write(payload)

    subprocess.run(['openssl', 'rsautl', '-encrypt', '-in', inFile, '-out', outFile, '-inkey', keyFile, '-pubin'])
    os.remove(keyFile)
    os.remove(inFile)

    with open(outFile, 'rb') as file:
        encData = b64encode(file.read()).decode('utf-8') 

    os.remove(outFile)

    return encData
