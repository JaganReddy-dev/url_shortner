import os
from dotenv import load_dotenv

load_dotenv()

xor_key = int(os.getenv("SECRET"), 16)


def xor_encrypt(data):
    xor_encrypted = ""
    obfuscated_id = data ^ int(xor_key)
    xor_encrypted += str(obfuscated_id)
    return xor_encrypted
