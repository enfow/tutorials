"""Simple argparse example."""

import argparse

parser = argparse.ArgumentParser(description='Simple Parser.')
parser.add_argument('--txt', type=str, help='input text to print')

args = parser.parse_args()
print(args.txt)
