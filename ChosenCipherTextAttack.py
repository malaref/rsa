from random import randrange

from rsa import crypt
from Utils import multiplicative_inverse


def get_original_text(cipher_text, e, d, n):
    padding_plain_text = 2
    signed_message = crypt(crypt(message=padding_plain_text, key=(e, n)) * cipher_text,(d,n))
    return signed_message * multiplicative_inverse(padding_plain_text, n) % n


if __name__ == "__main__":
    from rsa import generate_keys

    e, d, n = generate_keys(key_length=10)
    print('n = ' + str(n) + ' d = ' + str(d) + ' e = ' + str(e))
    original_message = randrange(1, n)
    cipher_message = crypt(message=original_message, key=(e, n))
    cracked_message = get_original_text(cipher_message, e, d, n)
    if cracked_message == original_message:
        print('HORRAY')
    else:
        print('SHIT')
