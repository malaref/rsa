from rsa import generate_keys
from time import time
from matplotlib import pyplot
from MathematicalAttack import get_private_key

max_key_length = 10

key_lengths = list(range(4, max_key_length + 1))
encryption_times = []
for key_length in key_lengths:
    e, d, n = generate_keys(key_length)
    time_before = time()
    private_key = get_private_key(n,e)
    time_after = time()
    if d != private_key:
        raise RuntimeError
    encryption_times.append(time_after - time_before)

pyplot.plot(key_lengths, encryption_times)
pyplot.title('Math Attack Time vs. Key Length')
pyplot.xlabel('Key Length (in bits)')
pyplot.ylabel('Encryption Time (in seconds)')
pyplot.show()