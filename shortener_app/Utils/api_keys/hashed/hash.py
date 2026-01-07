import hashlib


def hash_api_key(api_key: str) -> str:
    return hashlib.sha256(api_key.encode()).hexdigest()


# print(hash("34B7Q0ZCW2ZGRKW4I23Z3HM9E502"))
