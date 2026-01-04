import secrets
import string

ALPHABET = string.ascii_uppercase + string.digits


def api_key_generator(length: int = 28) -> str:
    for _ in range(10):
        key = "".join(secrets.choice(ALPHABET) for _ in range(length))
        if sum(c.isdigit() for c in key) >= 4:
            return key
    raise RuntimeError("API key generation failed")
