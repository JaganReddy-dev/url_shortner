import secrets
import string


def api_key_generator() -> str:
    alphabet = string.ascii_letters + string.digits
    while True:
        api_key = "".join(secrets.choice(alphabet) for i in range(28))
        if sum(c.isdigit() for c in api_key) >= 4:
            return api_key.upper()
