from random import getrandbits, randrange
from math import gcd

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, round(number ** 0.5)):
        if number % i == 0:
            return False
    return True

def get_random_prime(size):
    while True:
        number = getrandbits(size)
        if is_prime(number):
            return number

def multiplicative_inverse(x, n):
    for i in range(2, n):
        if i * x % n == 1:
            return i

def generate_keys(key_size):
    p = q = get_random_prime(key_size)
    while q == p:
        q = get_random_prime(key_size)
    n = p * q
    phi_n = (p-1) * (q-1)
    while True:
        e = randrange(2, phi_n)
        if gcd(e, phi_n) == 1:
            d = multiplicative_inverse(e, phi_n)
            return e, d, n

def crypt(message, key):
    return message ** key[0] % key[1]
