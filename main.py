import requests
import shutil

import getUrls

def getIconByUrl(url):
    faviconUrl = getUrls.getFaviconUrl(url)
    outpuFileName = faviconUrl.split("/")[-1]

    r = requests.get(faviconUrl, allow_redirects=True)
    open(outpuFileName, 'wb').write(r.content)


def getIconByName(name):
    url = getUrls.getUrlByWebsearch(name)
    getIconByUrl(url)

