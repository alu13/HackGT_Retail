import bs4
from Helper import get_webdriver


def search_oldnavy(*keywords):
    """
    Searchs old navy by the passed keywords
    :param keywords: search terms
    :return: a list of bs4 objects representing the articles of clothing
    """
    URL = "https://oldnavy.gap.com/browse/search.do?searchText="
    KEYWORD_STRING = "%20".join(keywords)
    URL += KEYWORD_STRING
    wd = get_webdriver()
    wd.get(URL)
    web_page = bs4.BeautifulSoup(wd.page_source, "lxml")
    print(web_page.head.title.text)
    articles = web_page.find_all("div", class_="product-card-grid__inner")
    return articles