import requests
import sys


def main():
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    else:
        get_price(n)

def get_price(n):
    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        if r.status_code == requests.codes.ok:
            results = r.json()
            btc = float(results["bpi"]["USD"]["rate_float"])
            price = btc * n
            print(f"${price:,.4f}")
    except requests.RequestException:
        print("request error")

main()