def is_prime(number):
    if number < 2:
        return False
    for i in range(2, round(number ** 0.5 + 0.5) + 1):
        if number % i == 0:
            return False
    return True


def multiplicative_inverse(x,
                           n):  # using the extended Euclidean algorithm, source: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Computing_multiplicative_inverses_in_modular_structures
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
