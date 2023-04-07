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


def extract_date_title(soup):
    """
    Get date title string.
    :param soup: The BeautifulSoup for crossfit .com wod page.
    :return: Title string of wod [string]
    """

    tags = soup.select('._day-text_1yolg_46')
    if len(tags) == 0:
        return "Not Loaded"

    day_text = tags[0].text

    tags = soup.select('._date-text_1yolg_69')
    if len(tags) == 0:
        return "Not Loaded"

    date_text = tags[0].text

    return f"{day_text} {date_text}"
