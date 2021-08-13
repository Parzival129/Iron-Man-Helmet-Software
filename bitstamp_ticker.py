import sys
import time
from pathlib import Path
from luma.core.render import canvas
from PIL import ImageFont
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306

serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)

def fetch_price(crypto_currency, fiat_currency):
    bitstamp_api = "https://www.bitstamp.net/api/v2/ticker/" + crypto_currency.lower() + fiat_currency.lower()
    try:
        r = requests.get(bitstamp_api)
        return r.json()
    except:
        print("Error fetching from Bitstamp API")


def get_price_text(crypto_currency, fiat_currency):
    data = fetch_price(crypto_currency, fiat_currency)
    return [
        '{}/{} {}'.format(crypto_currency, fiat_currency, data['last']),
        '24h Hi {} Lo {}'.format(data['high'], data['low'])
    ]


def show_price(device):
    # use custom font

    with canvas(device) as draw:
        rows = get_price_text("BTC", "USD")
        draw.text((0, 0), rows[0], fill="white")
        draw.text((0, 14), rows[1], fill="white")

        if device.height >= 64:
            rows = get_price_text("ETH", "USD")
            draw.text((0, 28), rows[0], fill="white")
            draw.text((0, 42), rows[1], fill="white")


def main():
    while True:
        show_price(device)
        time.sleep(5)


if __name__ == "__main__":
    try:
        #device = get_device()
        main()
    except KeyboardInterrupt:
        pass
