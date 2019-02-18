from time import time
from matplotlib import pyplot

from rsa import generate_keys, crypt
from crack import math_attack


def plot_crypt(max_key_length, trials):
    key_lengths = range(8, max_key_length + 1)
    encryption_times = []
    for key_length in key_lengths:
        print('Computing key length', key_length)
        key_length_time = 0
        for _ in range(trials):
            e, _, n = generate_keys(key_length)
            time_before = time()
            crypt(n - 1, (e, n))
            time_after = time()
            key_length_time += time_after - time_before
        encryption_times.append(key_length_time / trials)

    pyplot.plot(key_lengths, encryption_times)
    pyplot.title('Encryption Time vs. Key Length')
    pyplot.xlabel('Key Length (in bits)')
    pyplot.ylabel('Encryption Time (in seconds)')
    pyplot.show()

def plot_crack(max_key_length, trials):
    key_lengths = range(8, max_key_length + 1)
    crack_times = []
    for key_length in key_lengths:
        print('Computing key length', key_length)
        key_length_time = 0
        for _ in range(trials):
            e, d, n = generate_keys(key_length)
            time_before = time()
            private_key = math_attack(e, n)
            time_after = time()
            if d != private_key:
                raise RuntimeError
            key_length_time += time_after - time_before
        crack_times.append(key_length_time / trials)

    pyplot.plot(key_lengths, crack_times)
    pyplot.title('Math Attack Time vs. Key Length')
    pyplot.xlabel('Key Length (in bits)')
    pyplot.ylabel('Encryption Time (in seconds)')
    pyplot.show()
