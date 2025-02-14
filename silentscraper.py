# silentscraper v1.0.0 (beta)

import requests
import random
import httpx
import time
import aiohttp
import aiofiles
import asyncio
import roundrobin
import scrapy
import sys
from bs4 import BeautifulSoup

print('')

print(' ____  _ _            _   ____                                 ')
print('/ ___|(_) | ___ _ __ | |_/ ___|  ___ _ __ __ _ _ __   ___ _ __ ')
print('\___ \| | |/ _ \  _ \| __\___ \ / __|  __/ _` |  _ \ / _ \  __|')
print(' ___) | | |  __/ | | | |_ ___) | (__| | | (_| | |_) |  __/ |   ')
print('|____/|_|_|\___|_| |_|\__|____/ \___|_|  \__,_| .__/ \___|_|   ')
print('                                              |_|              ')

print('Welcome to SilentScraper v1.0.0 (beta)')
print('[+] Tool created by cryptxe')
print('[+] contact: cryptxesec@gmail.com')
print('[+] https://github.com/savnyc')
print('[+] https://github.com/gl0ck18')
print('')

print('')
print('Enter your search query: ')
searchQuery = input()

print('')
print('Enter the number of pages you would like to scrape: ')
pagesToScrape = int(input())

# Function to read lines from a text file
def read_lines_from_file(file_path):
    with open(file_path, "r") as file:
        lines = file.read().splitlines()
    return lines

# Function to select a random item from a list
def get_random_item(items):
    return random.choice(items)

# Function to make a request with a random user agent and proxy
def make_request(url, user_agents, proxies):
    headers = {
        'User-Agent': get_random_item(user_agents)
    }
    proxy = get_random_item(proxies)
    proxies_dict = {
        'http': proxy,
        'https': proxy
    }
    response = requests.get(url, headers=headers, proxies=proxies_dict)
    return response

if __name__ == '__main__':
    # Paths to user agents and proxies files
    user_agents_file = "userAgents.txt"
    proxies_file = "proxyList.txt"

    # Read user agents and proxies from text files
    user_agents = read_lines_from_file(user_agents_file)
    proxies = read_lines_from_file(proxies_file)

    # Select a random user agent and proxy
    random_user_agent = get_random_item(user_agents)
    random_proxy = get_random_item(proxies)

    print('')
    print('')
    print(f"Random Proxy: {random_proxy}")
    print(f"Random User Agent: {random_user_agent}")
    print('Search Query: ' + searchQuery)
    print('Pages to Scrape: ' + str(pagesToScrape))
    print('')

    # Example URL to scrape
    url = "https://www.example.com"

    # Make a request with the selected user agent and proxy
    # response = make_request(url, user_agents, proxies)

    # Check the response
    # print(f"Response Status Code: {response.status_code}")
    # print(f"Response Content: {response.content}")

if pagesToScrape > 10:
    print('You can only scrape up to 10 pages.')
    sys.exit()
elif pagesToScrape < 1:
    print('You must scrape at least 1 page.')
    sys.exit()
elif pagesToScrape == 1:
    print('Scraping 1 page...')
elif pagesToScrape > 1:
    print('')
    print('Scraping ' + str(pagesToScrape) + ' pages...')

    print('')
    print('Enter your search query: ')
    searchQuery = input()

    print('')
    print('Enter the number of pages you would like to scrape: ')
    pagesToScrape = int(input())
