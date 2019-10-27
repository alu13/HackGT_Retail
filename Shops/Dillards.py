import bs4
import re
from selenium.webdriver.common.by import By


from Utilities.Helper import get_webdriver, waitForLoad

def search_dillards(*keywords):
    """
    Searchs old navy by the passed keywords
    :param keywords: search terms
    :return: a list of bs4 objects representing the articles of clothing
    """
    URL = "https://www.dillards.com/search-term/"
    KEYWORD_STRING = "+".join(keywords)
    URL += KEYWORD_STRING
    URL += "?"
    dataList = []
    wd = get_webdriver()
    wd.get(URL)
    waitForLoad(URL, wd, "result-tile-above", By.CLASS_NAME, timeout=5)
    web_page = bs4.BeautifulSoup(wd.page_source, "lxml")
    articles = web_page.find_all("div", class_="col-xs-4 result-tile")
    wd.close()
    for item in articles:
        data = {}
        try:
            data["name"] = item.find_all("span", class_="productName")[0].text.strip()
            prices = str(item.find_all(class_="price"))
            data["price"] = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", prices)[0]
            data["image"] = item.find_all("img")[0]["src"]
            data["url"] = "dillards.com" + item.find_all("a")[0]["href"]
        except:
            continue
        dataList.append(data)
    return dataList

article = "jeans"
price = 50
redjeans = search_dillards("red", "jeans")

def sort(arrOfDics):
    holder = arrOfDics
    for i in holder:
        total = 0
        if article.lower() in i["name"].lower():
            total += 100
        total -= abs(float(i["price"])-price)
        i["value"] = total
    shitRank = sorted(holder, key = lambda i: i['value'], reverse=True)
    for i in shitRank:
        print(i["name"])
        print(i["price"])
        print(i["value"])
sort(redjeans)
