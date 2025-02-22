import validators
import requests, json
from bs4 import BeautifulSoup


def getRootUrl(url):
    slpitter = "/"
    splittedUrl = [e + slpitter for e in url.split(slpitter) if e]
    cleanedUrl = splittedUrl[:2]
    finalUrl = "/".join(cleanedUrl)

    if validators.url(finalUrl):
        return(finalUrl)
    else:
        print(f'Error: Cleaned url: {finalUrl} is not valid.')

def getFaviconUrl(url):
    rootUrl = getRootUrl(url)
    faviconUrl = rootUrl + "favicon.ico"
    if validators.url(faviconUrl):
        return(faviconUrl)
    else:
        print(f'Error: Favicon url: {faviconUrl} is not valid.')
