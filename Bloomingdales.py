import bs4

from Helper import get_webdriver


def search_bloomingdales(*keywords):
    """
    This method searches bloomingdales given keywords
    :param keywords:    The keywords to search for
    :return:    BS4 list of all the items on the page that match the keywords
    """
    URL = "https://www.bloomingdales.com/shop/search?keyword="
    print(URL)
    KEYWORD_STRING = "+".join(keywords)
    URL += KEYWORD_STRING
    print(URL)
    wd = get_webdriver()
    wd.get(URL)
    web_page = bs4.BeautifulSoup(wd.page_source, "lxml")
    descriptions = web_page.find_all("div", class_="productDescription")
    wd.close()
    return descriptions