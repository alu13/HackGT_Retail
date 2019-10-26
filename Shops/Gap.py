import bs4
from selenium.webdriver.common.by import By

from Utilities.Helper import get_webdriver, waitForLoad


def search_gap(*keywords):
    """
    Searchs old navy by the passed keywords
    :param keywords: search terms
    :return: a list of bs4 objects representing the articles of clothing
    """
    URL = "https://www.gap.com/browse/search.do?searchText="
    KEYWORD_STRING = "%20".join(keywords)
    URL += KEYWORD_STRING
    dataList = []
    wd = get_webdriver()
    wd.get(URL)
    waitForLoad(URL, wd, "product-card-grid__inner", By.CLASS_NAME, timeout=5)
    web_page = bs4.BeautifulSoup(wd.page_source, "lxml")
    articles = web_page.find_all("div", class_="product-card-grid__inner")
    wd.close()
    for item in articles:
        data = {}
        try:
            data["name"] = item.find_all("div", class_="product-card__name")[0].text.strip()
            highlight_prices = item.find_all(class_="product-price__highlight")
            if len(highlight_prices) > 0:
                data["price"] = highlight_prices[0].text.strip()
            else:
                data["price"] = item.find_all("div", class_="product-card-price")[0].text.strip()
            data["image"] = "https://oldnavy.gap.com" + item.find_all("img",class_="product-card__image")[0]["src"]
            data["url"] = item.find_all("a", class_="product-card__link")[0]["href"]
        except:
            continue
        dataList.append(data)

    return dataList