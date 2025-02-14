# wpHunter v1.0.0 (beta)

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
print('[+] https://twitter.com/cryptxe')
print('')

# read user agents from text file
def read_user_agents(file_path):
    with open(file_path, "r") as file:
        userAgents = file.read().splitlines()  # read lines and remove new line characters
        return userAgents

# select a random user agent from text file
def get_random_user_agent(userAgents):
    return random.choice(userAgents)

# make a request with the selected user agent
def make_request(url, userAgents):
    headers = {
        'User-Agent': get_random_user_agent(userAgents)
    }
    response = requests.get(url, headers=headers)
    return response

if __name__ == '__main__':
    # path to user agents file
    userAgentsFile = "userAgents.txt"

    # read user agents from text file
    userAgents = read_user_agents(userAgentsFile)

    # select a random user agent
    random_user_agent = get_random_user_agent(userAgents)
    print(f"Random User Agent: {random_user_agent}")
    print('')

    # make a request with the selected user agent
    # url = "https://www.google.com"
    # response = make_request(url, userAgents)

    # check the response
    # print(f"Response Status Code: {response.status_code}")
    # print(f"Response Content: {response.content}")

print('Please select the search engine you would like to scrape:')
print('')

print('1. Google')
print('2. Bing')
print('3. Yahoo')
print('4. DuckDuckGo')
print('5. Ask')
print('6. AOL')
print('')

searchEngineTarget = input()

if searchEngineTarget == '1':
    searchEngine = 'Google'
    searchEngineURL = 'https://www.google.com/search?q='
    searchEngineClass = 'g'

    print('')
    print('Enter your search query: ')
    searchQuery = input()

    print('')
    print('Enter the number of pages you would like to scrape: ')
    pagesToScrape = int(input())

    if pagesToScrape > 10:
        print('You can only scrape up to 10 pages.')
        sys.exit()
    elif pagesToScrape <= 1:
        print('You must scrape at least 1 page.')
        sys.exit()
    elif pagesToScrape == 1:
        print('Scraping 1 page...')
    elif pagesToScrape > 1:
        print('')
        print('Scraping ' + str(pagesToScrape) + ' pages...')

elif searchEngineTarget == '2':
    searchEngine = 'Bing'
    searchEngineURL = 'https://www.bing.com/search?q='
    searchEngineClass = 'b'

    print('')
    print('Enter your search query: ')
    searchQuery = input()

    print('')
    print('Enter the number of pages you would like to scrape: ')
    pagesToScrape = int(input())

    if pagesToScrape > 10:
        print('You can only scrape up to 10 pages.')
        sys.exit()
    elif pagesToScrape <= 1:
        print('You must scrape at least 1 page.')
        sys.exit()
    elif pagesToScrape == 1:
        print('Scraping 1 page...')
    elif pagesToScrape > 1:
        print('')
        print('Scraping ' + str(pagesToScrape) + ' pages...')
elif searchEngineTarget == '3':
    searchEngine = 'Yahoo'
    searchEngineURL = 'https://search.yahoo.com/search?p='
    searchEngineClass = 'y'

    print('')
    print('Enter your search query: ')
    searchQuery = input()

    print('')
    print('Enter the number of pages you would like to scrape: ')
    pagesToScrape = int(input())

    if pagesToScrape > 10:
        print('You can only scrape up to 10 pages.')
        sys.exit()
    elif pagesToScrape <= 1:
        print('You must scrape at least 1 page.')
        sys.exit()
    elif pagesToScrape == 1:
        print('Scraping 1 page...')
    elif pagesToScrape > 1:
        print('')
        print('Scraping ' + str(pagesToScrape) + ' pages...')

elif searchEngineTarget == '4':
    searchEngine = 'DuckDuckGo'
    searchEngineURL = 'https://duckduckgo.com/html/?q='
    searchEngineClass = 'd'

    print('')
    print('Enter your search query: ')
    searchQuery = input()

    print('')
    print('Enter the number of pages you would like to scrape: ')
    pagesToScrape = int(input())

    if pagesToScrape > 10:
        print('You can only scrape up to 10 pages.')
        sys.exit()
    elif pagesToScrape <= 1:
        print('You must scrape at least 1 page.')
        sys.exit()
    elif pagesToScrape == 1:
        print('Scraping 1 page...')
    elif pagesToScrape > 1:
        print('')
        print('Scraping ' + str(pagesToScrape) + ' pages...')

elif searchEngineTarget == '5':
    searchEngine = 'Ask'
    searchEngineURL = 'https://www.ask.com/web?q='
    searchEngineClass = 'a'

    print('')
    print('Enter your search query: ')
    searchQuery = input()

    print('')
    print('Enter the number of pages you would like to scrape: ')
    pagesToScrape = int(input())

    if pagesToScrape > 10:
        print('You can only scrape up to 10 pages.')
        sys.exit()
    elif pagesToScrape <= 1:
        print('You must scrape at least 1 page.')
        sys.exit()
    elif pagesToScrape == 1:
        print('Scraping 1 page...')
    elif pagesToScrape > 1:
        print('')
        print('Scraping ' + str(pagesToScrape) + ' pages...')

elif searchEngineTarget == '6':
    searchEngine = 'AOL'
    searchEngineURL = 'https://search.aol.com/aol/search?q='
    searchEngineClass = 'o'

    print('')
    print('Enter your search query: ')
    searchQuery = input()

    print('')
    print('Enter the number of pages you would like to scrape: ')
    pagesToScrape = int(input())

    if pagesToScrape > 10:
        print('You can only scrape up to 10 pages.')
        sys.exit()
    elif pagesToScrape <= 1:
        print('You must scrape at least 1 page.')
        sys.exit()
    elif pagesToScrape == 1:
        print('Scraping 1 page...')
    elif pagesToScrape > 1:
        print('')
        print('Scraping ' + str(pagesToScrape) + ' pages...')
else:
    print('Invalid search engine selection.')
    sys.exit()
