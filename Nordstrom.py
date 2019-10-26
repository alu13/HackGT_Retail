import bs4
from Helper import get_webdriver

def search_nordstrom(*keywords):
    """
    This method searches bloomingdales for the passed keywords
    :param keywords:    The keywords to search for
    :return:    The list of articles for the search terms
    """
    URL = "https://shop.nordstrom.com/sr?origin=keywordsearch&keyword="
    KEYWORD_STRING = "%20".join(keywords)
    URL += KEYWORD_STRING
    wd = get_webdriver()
    wd.get(URL)
    web_page = bs4.BeautifulSoup(wd.page_source, "lxml")
    print(web_page.head.title.text)
    articles = web_page.find_all("article")
    return articles
