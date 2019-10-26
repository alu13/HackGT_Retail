import bs4
from selenium.webdriver.common.by import By

from Utilities.Helper import get_webdriver, waitForLoad


def search_forever21(*keywords):
    """
    This method searches Forever21 for the passed keywords
    :param keywords:    The keywords to search for
    :return:    The list of articles for the search terms
    """
    URL = "https://www.forever21.com/us/shop/Search/#brm-search?request_type=search&search_type=keyword&q="
    KEYWORD_STRING = "%20".join(keywords)
    URL += KEYWORD_STRING
    dataList = []
    wd = get_webdriver()
    wd.get(URL)
    waitForLoad(URL, wd, "pi_container", By.CLASS_NAME)
    web_page = bs4.BeautifulSoup(wd.page_source, "lxml")
    articles = web_page.find_all("div", class_="pi_container")
    wd.close()
    for item in articles:
        data = {}
        try:
            data["name"] = item.find_all("p", class_="p_name")[0].text.strip()
            saleprice = item.find_all("p", class_="p_sale")
            if len(saleprice) > 0:
                data["price"] = saleprice[0].text.strip()
            else:
                data["price"] = item.find_all("p", class_="p_price")[0].text.strip()

            data["image"] = item.find_all("img", class_="product_image")[0]["src"]
            data["url"] = item.find_all("a")[0]["href"]
        except:
            continue
        dataList.append(data)
    return dataList
