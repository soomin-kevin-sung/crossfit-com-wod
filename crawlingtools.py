import requests
from bs4 import BeautifulSoup


def get_beautifulsoup(url):
    """
    Get beautifulsoup for url.
    :param url: url to get beautifulsoup
    :return: beautifulsoup for url. [beautifulsoup]
    """
    res = requests.get(url)
    if res.status_code != 200:
        return None

    return BeautifulSoup(res.text, 'html.parser')


def extract_wod_contents(soup):
    """
    Get Tag strings of wod from BeautifulSoup.
    :param soup: The BeautifulSoup for crossfit .com wod page.
    :return: Tag strings of wod [string]
    """
    article = soup.select('article > div > p')
    if len(article) == 0:
        return ""

    result = '<p><h2>Today\'s workout</h2></p><br>'
    for p in article:
        result += str(p)

    return result
