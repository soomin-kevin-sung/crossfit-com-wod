from selenium import webdriver
from bs4 import BeautifulSoup


def get_beautifulsoup(url):
    """
    Get beautifulsoup for url.
    :param url: url to get beautifulsoup
    :return: beautifulsoup for url. [beautifulsoup]
    """
    driver = None
    result = None
    try:
        driver = webdriver.Chrome()
        driver.get(url)

        result = BeautifulSoup(driver.page_source, 'html.parser')
    finally:
        driver.quit()

    return result


def extract_wod_contents(soup):
    """
    Get Tag strings of wod from BeautifulSoup.
    :param soup: The BeautifulSoup for crossfit .com wod page.
    :return: Tag strings of wod [string]
    """

    articles = soup.select('article')
    if len(articles) == 0:
        return ""

    paragrphs = articles[0].select('div > p')
    if len(paragrphs) == 0:
        return ""

    result = '<p><h2>Today\'s workout</h2></p><br>'
    for p in paragrphs:
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
