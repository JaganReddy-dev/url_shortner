import secrets
import string
from datetime import datetime, timezone

ALPHABET = string.ascii_uppercase + string.digits


def api_key_generator(length: int = 28) -> dict:
    for _ in range(10):
        key = "".join(secrets.choice(ALPHABET) for _ in range(length))
        if sum(c.isdigit() for c in key) >= 4:
            created_at = int(datetime.now(timezone.utc).timestamp())
            expires_at = created_at + 30 * 24 * 60 * 60
            obj = {
                "api_key": key,
                "created_at": created_at,
                "expires_at": expires_at,
            }
            return obj
    raise RuntimeError("API key generation failed")
