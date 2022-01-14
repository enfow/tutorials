"""Define the calculator for importing whisky.

Author: Kyeongmin Woo
E-mail: wgm0601@gmail.com

Notes:
    - exchange rate: 1200 per dallor
    - tax rate: 0.95%
    - price * exchange_rate * (1 + tax rate)
"""
import argparse

EXCHANGE_RATE = 1200
TAX_RATE = 0.95

parser = argparse.ArgumentParser()
parser.add_argument("d", type=float, nargs="?", help="the original price with dollar")

args = parser.parse_args()
price_with_dollar = args.d

expected_price = round(price_with_dollar * EXCHANGE_RATE * (1 + TAX_RATE))

print(f"expected price: ₩{expected_price:,} (${price_with_dollar})")
