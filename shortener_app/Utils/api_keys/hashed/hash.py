import hashlib


def hash(api_key: str) -> str:
    return hashlib.sha256(api_key.encode()).hexdigest()
