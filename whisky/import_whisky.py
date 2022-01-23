"""Define the calculator for importing whisky.

Author: Kyeongmin Woo
E-mail: wgm0601@gmail.com

Notes:
    - delivery fee: $30
    - exchange rate: 1200 per dallor
    - tax rate: 0.95%
    - (price * (1 + tax rate) + delivery fee) * exchange rate
"""
import argparse

DELIVER_FEE = 30
EXCHANGE_RATE = 1150
TAX_RATE = 0.92

parser = argparse.ArgumentParser()
parser.add_argument("d", type=float, nargs="?", help="the original price with dollar")

args = parser.parse_args()
price_with_dollar = args.d

expected_price = round(price_with_dollar * EXCHANGE_RATE)
expected_delivery_fee = round(DELIVER_FEE * EXCHANGE_RATE)
expected_tax = round(expected_price * TAX_RATE)

expected_sum = expected_price + expected_delivery_fee + expected_tax

print(
    f"expected sum: ₩{expected_sum:,} | expected price: ₩{expected_price:,} | expected delivery: ₩{expected_delivery_fee:,} | expected tax: ₩{expected_tax:,}"
)
