from rsa import generate_keys, crypt
from mathematical_attack import get_private_key
from plot import plot_crypt, plot_crack

import argparse


parser = argparse.ArgumentParser()
parsers = parser.add_subparsers(dest='command')
generate_keys_parser = parsers.add_parser('generate_keys')
generate_keys_parser.add_argument('seed_length', type=int)
crypt_parser = parsers.add_parser('crypt', aliases=['encrypt', 'decrypt'])
crypt_parser.add_argument('key', type=int, nargs=2)
crypt_parser.add_argument('message', type=int)
crack_parser = parsers.add_parser('crack')
crack_parser.add_argument('key', type=int, nargs=2)
plot_parser = parsers.add_parser('plot')
plot_parser.add_argument('operation', type=str, choices=['crypt', 'crack'])
plot_parser.add_argument('max_seed_length', type=int)
plot_parser.add_argument('number_of_points', type=int)

args = parser.parse_args()

if args.command == 'generate_keys':
    print(generate_keys(args.seed_length))
elif args.command == 'encrypt' or args.command == 'decrypt':
    print(crypt(args.message, args.key))
elif args.command == 'crack':
    print(get_private_key(*args.key))
elif args.command == 'plot':
    if args.operation == 'crypt':
        plot_crypt(args.max_seed_length, args.number_of_points)
    if args.operation == 'crack':
        plot_crack(args.max_seed_length, args.number_of_points)
else:
    raise argparse.ArgumentTypeError('Invalid command')
