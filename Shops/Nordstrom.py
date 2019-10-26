
import bs4
from Utilities.Helper import get_webdriver, waitForLoad


def search_nordstrom(*keywords):
    """
    This method searches bloomingdales for the passed keywords
    :param keywords:    The keywords to search for
    :return:    A list of dictionary of {name, image, url, price}
    """
    URL = "https://shop.nordstrom.com/sr?origin=keywordsearch&keyword="
    KEYWORD_STRING = "%20".join(keywords)
    URL += KEYWORD_STRING
    dataList = []
    wd = get_webdriver()
    wd.get(URL)
    waitForLoad(URL, wd,  "article")
    web_page = bs4.BeautifulSoup(wd.page_source, "lxml")
    articles = web_page.find_all("article")
    wd.close()
    for item in articles:
        data = {}
        try:
            data["name"] = item.find_all("h3")[0].text
            data["price"] = item.find_all("div")[1].text
            data["image"] = item.find_all("img")[0]['src']
            data["url"] = "https://shop.nordstrom.com" + item.find_all("a")[0]['href']
        except:
            continue
        dataList.append(data)
    return dataList

