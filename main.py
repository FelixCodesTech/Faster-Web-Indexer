import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlunparse

startURL = "https://en.wikipedia.org/wiki/Alphabet_Inc."

def extractLinks(url):
    response = requests.get(url, timeout=1)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.startswith(('http', 'https')):
            href = href.strip('\'"')
            links.append(href)
    return url, links

def prepLinks(url, links):
    parsedURL = urlparse(url)
    preppedLinks = []
    for link in links:
        parsedLink = urlparse(link)

        if not parsedLink.netloc == parsedURL.netloc:
            preppedLink = parsedLink.netloc+parsedLink.path
            preppedLinks.append(preppedLink)

    return url, preppedLinks



url, links = extractLinks(startURL)
url, preppedLinks = prepLinks(url, links)
print(preppedLinks)