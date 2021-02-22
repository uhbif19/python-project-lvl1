"""Pure math functions, which are required for our games."""


def is_prime(num: int) -> bool:
    """
    Super simple realization of prime checker.

    Args:
        num: number to check if it is prime
    """
    for possible_multiply in range(2, num):
        if num % possible_multiply == 0:
            return False
    return True
