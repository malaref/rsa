from rsa import generate_keys, crypt
from time import time
from random import randrange
from matplotlib import pyplot

max_key_length = 10

key_lengths = list(range(4, max_key_length + 1))
encryption_times = []
for key_length in key_lengths:
    e, _, n = generate_keys(key_length)
    random_message = randrange(1, n)
    time_before = time()
    crypt(random_message, (e, n))
    time_after = time()
    encryption_times.append(time_after - time_before)

pyplot.plot(key_lengths, encryption_times)
pyplot.title('Encryption Time vs. Key Length')
pyplot.xlabel('Key Length (in bits)')
pyplot.ylabel('Encryption Time (in seconds)')
pyplot.show()