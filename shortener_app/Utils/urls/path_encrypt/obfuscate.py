import math

MIN_7_CHAR = 62**6
MAX_7_CHAR = 62**7 - 1
RANGE_SIZE = MAX_7_CHAR - MIN_7_CHAR + 1


def obfuscate_counter(counter: int, prime: int = 2654435761):
    if math.gcd(prime, RANGE_SIZE) != 1:
        raise ValueError("Prime is not coprime with RANGE_SIZE")
    obfuscated = (counter * prime) % RANGE_SIZE
    return obfuscated + MIN_7_CHAR


def deobfuscate_counter(obfuscated_value: int, prime: int = 2654435761):
    adjusted_value = obfuscated_value - MIN_7_CHAR
    modular_inverse = pow(prime, -1, RANGE_SIZE)
    original_counter = (adjusted_value * modular_inverse) % RANGE_SIZE
    return original_counter
