from prime import is_prime

def test_prime(x, expected):
    if is_prime(x) != expected:
        print(f"Error, is_prime({x}) is supposed to be {expected}")