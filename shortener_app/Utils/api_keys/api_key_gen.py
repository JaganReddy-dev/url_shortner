import secrets
import string
from datetime import datetime, timedelta, timezone

ALPHABET = string.ascii_uppercase + string.digits


def api_key_generator(length: int = 28) -> dict:
    for _ in range(10):
        key = "".join(secrets.choice(ALPHABET) for _ in range(length))
        if sum(c.isdigit() for c in key) >= 4:
            created_at = datetime.now(timezone.utc)
            expires_at = created_at + timedelta(days=30)
            obj = {
                "api_key": key,
                "created_at": created_at,
                "expires_at": expires_at,
            }
            return obj
    raise RuntimeError("API key generation failed")
