from selenium import webdriver

def get_webdriver() -> webdriver:
    """
    This method creates a selenium web driver
    :return: A webdriver object
    """
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--enable-javascript")
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")
    wd = webdriver.Chrome("./chromedriver", options=options)
    timeout = 30
    wd.implicitly_wait(timeout)
    return wd