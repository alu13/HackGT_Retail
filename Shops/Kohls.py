import bs4
from selenium.webdriver.common.by import By

from Utilities.Helper import get_webdriver, waitForLoad


def search_kohls(*keywords):
    """
    This method searches bloomingdales for the passed keywords
    :param keywords:    The keywords to search for
    :return:    The list of articles for the search terms
    """
    URL = "https://www.kohls.com/search.jsp?submit-search=web-regular&search="
    KEYWORD_STRING = "+".join(keywords)
    URL += KEYWORD_STRING
    dataList = []
    wd = get_webdriver()
    wd.get(URL)
    waitForLoad(URL, wd, "products_matrix", By.CLASS_NAME)
    web_page = bs4.BeautifulSoup(wd.page_source, "lxml")
    articles = web_page.find_all("li", class_="products_grid")
    wd.close()
    for item in articles:
        data = {}
        try:
            data["name"] = item.find_all("div", class_="prod_nameBlock")[0].text.strip()
            data["price"] = item.find_all("p", class_="prod_price_amount")[0].text.strip()
            data["image"] = item.find_all("img")[0]["data-herosrc"]
            data["url"] = "https://kohls.com" + item.find_all("a")[0]["href"].replace(" ", "%20")
        except:
            continue
        dataList.append(data)
    return dataList
