from rsa import crypt
from utils import multiplicative_inverse


padding_plain_text = 2

cipher_text = int(input('Cipher text: '))
e, n = tuple(int(i) for i in input('Public key: ').split())
print('Sign this:', crypt(padding_plain_text, (e, n)) * cipher_text % n)
signed_message = int(input('Signed message: '))
print('Original message:', signed_message * multiplicative_inverse(padding_plain_text, n) % n)
