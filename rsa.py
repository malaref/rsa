from random import getrandbits, randrange
from math import gcd

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, round(number ** 0.5 + 0.5) + 1):
        if number % i == 0:
            return False
    return True

def get_random_prime(size):
    while True:
        number = getrandbits(size)
        if is_prime(number):
            return number

def multiplicative_inverse(x, n): # using the extended Euclidean algorithm, source: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Computing_multiplicative_inverses_in_modular_structures
    t, new_t = 0, 1
    r, new_r = n, x
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        return None
    if t < 0:
        t = t + n
    return t

def generate_keys(key_size):
    if key_size < 4:
        raise ValueError('Key size must not be < 4')
    try:
        p = q = get_random_prime(key_size)
        while q == p:
            q = get_random_prime(key_size)
        n = p * q
        phi_n = (p-1) * (q-1)
        while True:
            e = randrange(2, phi_n)
            if gcd(e, phi_n) == 1:
                d = multiplicative_inverse(e, phi_n)
                if d == e:
                    return generate_keys(key_size) # must choose new p and q; prettier than a huge loop
                return e, d, n
    except ValueError: # empty range for randrange()
        return generate_keys(key_size) # since key_size is not < 4, this is guaranteed to terminate; just try again!

def crypt(message, key):
    return message ** key[0] % key[1]
