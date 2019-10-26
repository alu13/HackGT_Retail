import bs4

from Helper import get_webdriver

def search_dillards(*keywords):
    """
    This method searches dillards with the given keywords
    :param keywords:    The keywords to search for
    :return:    BS4 list of all the items on the page that match the keywords
    """
    URL = "https://www.dillards.com/search-term/"
    KEYWORD_STRING = "+".join(keywords)
    URL += KEYWORD_STRING
    URL += "?"
    wd = get_webdriver()
    wd.get(URL)
    web_page = bs4.BeautifulSoup(wd.page_source, "lxml")
    print(web_page)
    descriptions = web_page.find_all("span", class_="productName")
    wd.close()
    return descriptions
