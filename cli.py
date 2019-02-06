from rsa import generate_keys, crypt

import argparse
parser = argparse.ArgumentParser()
parsers = parser.add_subparsers(dest='command')
generate_keys_parser = parsers.add_parser('generate_keys')
generate_keys_parser.add_argument('key_length', type=int)
crypt_parser = parsers.add_parser('crypt', aliases=['encrypt', 'decrypt'])
crypt_parser.add_argument('key', type=int, nargs=2)
crypt_parser.add_argument('message', type=int)
args = parser.parse_args()

if args.command == 'generate_keys':
    print(generate_keys(args.key_length))
elif args.command == 'encrypt' or args.command == 'decrypt':
    print(crypt(args.message, args.key))
else:
    raise argparse.ArgumentTypeError('Invalid command')
