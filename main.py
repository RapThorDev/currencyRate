#!/usr/bin/python3

from signal import pause
import requests
import os
from colors import bcolors

URL = 'https://api.exchangerate.host/latest'
RATES = False
ARGUMENTS = False


def _clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')

def _end():
	input("\nPress any key to continue...")
	_clear_screen()

def _calculate(source_currency, target_currency, value):
    return value / source_currency * target_currency

def main():
	_clear_screen()
	get_rates_from_url()
	if RATES:
		if ARGUMENTS:
			pass
		else:
			manual_exchange()
	
	_end()

def get_rates_from_url():
    global RATES
    print(f"[INFO] Get rates from {bcolors.OKBLUE}{URL}{bcolors.ENDC}", end='')
    response = requests.get(URL)
    data = response.json()
    if data['success']:
        print(bcolors.OKGREEN + " DONE" + bcolors.ENDC + "\n")
        RATES = data['rates']
    else:
        print(bcolors.FAIL + " FAIL" + bcolors.ENDC + "\n")

def manual_exchange():
	value = float(input("Value: ")) or 1.0
	source_currency = input("Source currency: ").upper() or 'EUR' 
	target_currency = input("Target currency: ").upper() or 'HUF'
	source_currency_rate = RATES[source_currency]
	target_currency_rate = RATES[target_currency]
	print(f"\n{value} {source_currency} = {_calculate(source_currency_rate,target_currency_rate,value)} {target_currency}")

if __name__ == "__main__":
	main()
