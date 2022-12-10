import time

import requests
from bs4 import BeautifulSoup


class Track:

    def __init__(self):
        self.FILE_NAME = 'url.txt'
        self.URL = self.open_link()
        self.SLEEP_TIME = 60
        self.HEADERS = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
        }
        self.complimentary = "Status updates beyond the United States are only available for select countries. For more information, review the list of eligible countries at https://www.usps.com/international/first-class-package-international-service.htm ."

    def open_link(self):
        with open(self.FILE_NAME, 'r') as f:
            return f.read()

    def get(self):
        return requests.get(self.URL, headers=self.HEADERS)

    def status(self):
        soup = BeautifulSoup(self.get().content, 'html.parser')
        return soup.find('p', class_='banner-content').text.strip().split(self.complimentary)[0]

    def run(self):
        while True:
            print(self.status())
            print("Sleeping for {} seconds".format(self.SLEEP_TIME))
            print("——————————————————————————————————————————")
            print()
            time.sleep(self.SLEEP_TIME)
