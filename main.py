import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlunparse
import csv
from datetime import date

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
            if not parsedLink.netloc.startswith("www"):
                preppedLink = parsedLink.netloc+parsedLink.path
                preppedLinks.append(preppedLink)

    return url, preppedLinks

def hashLinks(links):
    hashedLinks = []
    for link in links:
        hashedLink = str(hash(link))[:7]

        hashedLinks.append(hashedLink)

    return hashedLinks

def noteLinks(hashedLinks, preppedlinks):
    #first sort out duplicates (in both lists)
    hashedLinks = set(hashedLinks)
    # Create a new list with duplicates removed         - Yes this is untested, LOL
    filteredHashedLinks = []
    filteredPreppedLinks = []
    for i, x in enumerate(hashedLinks):
        if x not in filteredHashedLinks:
            filteredHashedLinks.append(x)
            filteredPreppedLinks.append(preppedlinks[i])

    with open('data.csv', mode='r+', newline='') as file:
        writer = csv.writer(file)
        for i in range(len(filteredHashedLinks)):
            if not filteredHashedLinks[i] in file:
                writer.writerow([filteredHashedLinks[i], filteredPreppedLinks[i], 0, str(date.today())])



url, links = extractLinks(startURL)
url, preppedLinks = prepLinks(url, links)
hashedLinks = hashLinks(preppedLinks)

noteLinks(hashedLinks, preppedLinks)