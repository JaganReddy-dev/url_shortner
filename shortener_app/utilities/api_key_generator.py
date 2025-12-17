import secrets
import string


def api_key_generator() -> str:
    alphabet = string.ascii_letters + string.digits
    while True:
        api_key = "".join(secrets.choice(alphabet) for i in range(14))
        if (
            any(c.islower() for c in api_key)
            and any(c.isupper() for c in api_key)
            and sum(c.isdigit() for c in api_key) >= 3
        ):
            return api_key
