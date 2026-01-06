import os
from dotenv import load_dotenv

load_dotenv()
base62 = os.getenv("BASE62")


def encode_base62(num):
    if num == 0:
        return base62[0]

    base62_id = ""
    while num > 0:
        base62_id = base62[num % 62] + base62_id
        num //= 62

    return base62_id
