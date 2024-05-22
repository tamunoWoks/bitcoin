import sys
import requests

if len(sys.argv) == 2:
    try:
        amount = float(sys.argv[1])
    except:
        sys.exit("Command-line argument is not a number")
else:
    sys.exit("Missing command-line argument")

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = r.json()
    btc = response["bpi"]["USD"]["rate-float"]
    total = btc * amount
    print(f"${total:,.4f}")
except requests.RequestException:
    sys.exit("Request Exception")
