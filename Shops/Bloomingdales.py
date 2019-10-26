import re

import bs4
from selenium.webdriver.common.by import By

from Utilities.Helper import get_webdriver, waitForLoad


def search_bloomingdales(*keywords):
    """
    This method searches bloomingdales given keywords
    :param keywords:    The keywords to search for
    :return:    BS4 list of all the items on the page that match the keywords
    """
    URL = "https://www.bloomingdales.com/shop/search?keyword="
    KEYWORD_STRING = "+".join(keywords)
    URL += KEYWORD_STRING
    dataList = []
    wd = get_webdriver()
    wd.get(URL)
    waitForLoad(URL, wd, "productThumbnail", BySelector=By.CLASS_NAME)
    web_page = bs4.BeautifulSoup(wd.page_source, "lxml")
    descriptions = web_page.find_all("div", class_="productThumbnail")
    wd.close()
    for item in descriptions:
        data = {}
        try:
            data["name"] = re.sub(r'\n+?\s+?(\S)',r" | \1",
                                      item.find_all("div", class_="productDescription")[0].text.strip())
            data["price"] = item.find_all("div", class_="tnPrice")[0].text.strip()
            data["image"] = item.find_all("img")[0]["data-lazysrc"]
            url_postfix = item.find_all("a")[0]["href"]
            data["url"] = "https://www.bloomingdales.com" + url_postfix
        except:
            continue
        dataList.append(data)
    return dataList