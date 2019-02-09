from rsa import generate_keys, crypt
from Utils import multiplicative_inverse


def get_original_text(cipher_text, e, d, n):
    padding_plain_text = 2
    dummy_cipher_text = padding_plain_text
    dummy_cipher_text = crypt(message=dummy_cipher_text, key=(e, n))
    dummy_cipher_text = dummy_cipher_text * cipher_text
    signed_message = crypt(message=dummy_cipher_text, key=(d, n))
    return signed_message * multiplicative_inverse(padding_plain_text, n)


if __name__ == "__main__":
    from rsa import generate_keys

    e, d, n = generate_keys(key_length=10)
    print('n = ' + str(n) + ' d = ' + str(d) + ' e = ' + str(e))
    original_message = 124852
    cipher_message = crypt(message=original_message, key=(e, n))
    cracked_message = get_original_text(cipher_message, e, d, n)
    if cracked_message == original_message:
        print('HORRAY')
    else:
        print('SHIT')
