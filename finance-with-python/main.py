"""execute everything in this project.

Author: Kyeongmin Woo
Email: wgm0601@gmail.com
"""
import argparse

from src.reporter.dual_momentum import DualMomentum


parser = argparse.ArgumentParser()
parser.add_argument('exec', type=str, default="")
parser.add_argument('send_msg', type=bool, default=False)

args = parser.parse_args()

if args.exec == "dual_momentum":
    DualMomentum(save_dir="./img", send_msg=args.send_msg)

