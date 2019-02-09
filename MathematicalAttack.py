from Utils import is_prime
from Utils import multiplicative_inverse
import random
from math import gcd


def pollard_rho_factoring(n):
    if n % 2 == 0:
        return 2
    if is_prime(n):
        return 1  # This algorithm fails for a prime, thus return 1
    while True:
        # The algorithm may fail for some values of c, so I chose a random value between 2 and n-1,
        # then carry on the algorithm until convergence
        c = random.randint(2, n - 1)
        f = lambda x: x ** 2 + c
        x = y = 2
        d = 1
        while d == 1:
            x = f(x) % n
            y = f(f(y)) % n
            d = gcd((x - y) % n, n)
        if d != n:
            return d


def get_private_key(n, e):
    p = pollard_rho_factoring(n)
    q = n // p
    phi_n = (p - 1) * (q - 1)
    return multiplicative_inverse(e, phi_n)


if __name__ == "__main__":
    from rsa import generate_keys

    e, d, n = generate_keys(key_length=32)
    print('n = ' + str(n) + ' d = ' + str(d) + ' e = ' + str(e))
    private_key = get_private_key(n, e)
    print('generated_key = ' + str(private_key))
    if private_key == d:
        print("Horray")
    else:
        print("SHIT")
