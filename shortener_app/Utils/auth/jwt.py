import jwt


def generate_jwt_token(payload: dict, secret: str) -> str:
    encoded = jwt.encode(payload, secret, algorithm="HS256")
    return encoded


def decode_jwt_token(token: str, secret: str) -> dict:
    decoded = jwt.decode(token, secret, algorithms=["HS256"])
    return decoded
