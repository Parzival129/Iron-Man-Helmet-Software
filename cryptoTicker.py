import time
from systemFunctions import speak, draw_text, turnOffJarvis, turnOnJarvis, recordAudio
import requests
import sys
import json

_showCrypto = False

def isRunning():
	return _showCrypto

def getPrice(crypto_currency, currency):
	bitstamp_api_url = "https://www.bitstamp.net/api/v2/ticker/" + crypto_currency.lower() + currency.lower()
	try:
		r = requests.get(bitstamp_api_url)
		return r.json()
	except:
		print ("Ran into problems from Bitstamp REST API")

def priceToText(crypto_currency, currency):
	data = getPrice(crypto_currency, currency)
	return '{}/{} {}\n24h HI {} LO {}'.format(crypto_currency, currency, data['last'], data['high'], data['low'])


def show_price(crypto, currency):
	draw_text(priceToText(crypto, currency))

def main():
	while isRunning():
		show_price("BTC", "USD")
		time.sleep(10)
		turnOnJarvis()
		return


if __name__ == "__main__":
	turnOffJarvis()
	_showCrypto = True
	main()


def stop():
	global _showCrypto
	_showCrypto = False

def start():
	time.sleep(5)
	turnOffJarvis()
	global _showCrypto
	_showCrypto = True
	main()
	stop()
	turnOnJarvis()
