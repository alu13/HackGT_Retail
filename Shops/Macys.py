import re

import bs4
from selenium.webdriver.common.by import By

from Utilities.Helper import get_webdriver, waitForLoad


def search_macys(*keywords):
    """
    This method searches Macy's for the passed keywords
    :param keywords:    The keywords to search for
    :return:    The list of articles for the search terms
    """
    URL = "https://www.macys.com/shop/featured/"
    KEYWORD_STRING = "-".join(keywords)
    URL += KEYWORD_STRING
    dataList = []
    wd = get_webdriver()
    wd.get(URL)
    waitForLoad(URL, wd, "productThumbnailItem", By.CLASS_NAME)
    web_page = bs4.BeautifulSoup(wd.page_source, "lxml")
    articles = web_page.find_all("li", class_="productThumbnailItem")
    wd.close()
    for item in articles:
        data = {}
        try:
            productDesc = item.find_all("div", class_="productDescription")[0]
            data["name"] = re.sub(r'\n+?\s+?(\S)',r" | \1",
                                  productDesc.find_all("a")[0].text.strip())
            discountPrice = productDesc.find_all("span", class_="discount")
            if len(discountPrice) > 0:
                data["price"] = discountPrice[0].text.strip()
            else:
                data["price"] = productDesc.find_all("span", class_="regular")[0].text.strip()
            data["image"] = item.find_all("source")[0]["srcset"].replace(" ", "%20")
            data["url"] = "https://macys.com" + item.find_all("a")[0]["href"].replace(" ", "%20")
        except:
            continue
        dataList.append(data)
    return dataList
