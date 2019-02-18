from time import time
from matplotlib import pyplot
from random import randrange

from rsa import generate_keys, crypt
from crack import math_attack


def plot_crypt(max_seed_length, number_of_points):
    key_lengths = []
    encryption_times = []
    for i in range(number_of_points):
        print('Computing point', i + 1)
        e, _, n = generate_keys(randrange(4, max_seed_length))
        time_before = time()
        crypt(n - 1, (e, n))
        time_after = time()
        key_lengths.append(n.bit_length())
        encryption_times.append(time_after - time_before)

    pyplot.scatter(key_lengths, encryption_times)
    pyplot.title('Encryption Time vs. Key Length')
    pyplot.xlabel('Key Length (in bits)')
    pyplot.ylabel('Encryption Time (in seconds)')
    pyplot.show()

def plot_crack(max_seed_length, number_of_points):
    key_lengths = []
    encryption_times = []
    for i in range(number_of_points):
        print('Computing point', i + 1)
        e, d, n = generate_keys(randrange(4, max_seed_length))
        time_before = time()
        private_key = math_attack(e, n)
        time_after = time()
        if d != private_key:
            raise RuntimeError
        key_lengths.append(n.bit_length())
        encryption_times.append(time_after - time_before)

    pyplot.scatter(key_lengths, encryption_times)
    pyplot.title('Math Attack Time vs. Key Length')
    pyplot.xlabel('Key Length (in bits)')
    pyplot.ylabel('Encryption Time (in seconds)')
    pyplot.show()
