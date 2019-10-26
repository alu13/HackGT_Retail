import bs4

from Helper import get_webdriver


def search_kohls(*keywords):
    """
    This method searches bloomingdales for the passed keywords
    :param keywords:    The keywords to search for
    :return:    The list of articles for the search terms
    """
    URL = "https://www.kohls.com/search.jsp?submit-search=web-regular&search="
    KEYWORD_STRING = "+".join(keywords)
    URL += KEYWORD_STRING
    wd = get_webdriver()
    wd.get(URL)
    web_page = bs4.BeautifulSoup(wd.page_source, "lxml")
    print(web_page.head.title.text)
    articles = web_page.find_all("div",class_="products_matrix")
    wd.close()
    return articles[0].find_all("li")
