import requests
from bs4 import BeautifulSoup
import datetime as dt

# crossfit.com main url
crossfit_com_url = "https://www.crossfit.com/"


def get_wod_by_date(date):
    """
    Get the date's wod.
    :param date: The date of WOD to get.
    :return: WOD content to string. [string]
    """
    if type(date) != dt.datetime:
        return ""

    response = requests.get(f'{crossfit_com_url}/{date.strftime("%y%m%d")}')
    if response.status_code != 200:
        return ""

    soup = BeautifulSoup(response.text, 'html.parser')
    return extract_wod(soup)


def extract_wod(soup):
    """
    Get Tag strings of wod from BeautifulSoup.
    :param soup: The BeautifulSoup for crossfit .com wod page.
    :return: Tag strings of wod [string]
    """
    article = soup.select('article > div > p')
    if len(article) == 0:
        return ""

    result = ""
    for p in article:
        result += str(p)

    return result
