import secrets
import string


def url_id_generator(url: str) -> str:
    alphabet = string.ascii_letters + string.digits
    while True:
        unique_id = "".join(secrets.choice(alphabet) for i in range(8))
        if (
            any(c.islower() for c in unique_id)
            and any(c.isupper() for c in unique_id)
            and sum(c.isdigit() for c in unique_id) >= 2
        ):
            return unique_id
