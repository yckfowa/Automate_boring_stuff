import requests
from bs4 import BeautifulSoup


url = input("Please enter the url to begin download: ")

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')

for link in soup.select('a'):
    print(link)