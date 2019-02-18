from random import getrandbits, randrange
from math import gcd

from utils import is_prime, multiplicative_inverse


def get_random_prime(length):
    while True:
        number = getrandbits(length)
        if is_prime(number):
            return number

def generate_keys(key_length):
    if key_length < 8:
        raise ValueError('Key length must not be < 8')
    try:
        p = q = get_random_prime(key_length // 2)
        while q == p:
            q = get_random_prime(key_length - key_length // 2)
        n = p * q
        phi_n = (p - 1) * (q - 1)
        while True:
            e = randrange(2, phi_n)
            if gcd(e, phi_n) == 1:
                d = multiplicative_inverse(e, phi_n)
                if d == e:
                    return generate_keys(key_length)  # must choose new p and q; prettier than a huge loop
                return e, d, n
    except ValueError:  # empty range for randrange()
        return generate_keys(key_length)  # since key_length is not < 8, this is guaranteed to terminate; just try again!

def crypt(message, key):
    return message ** key[0] % key[1]
