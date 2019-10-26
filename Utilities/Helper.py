from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_webdriver() -> webdriver:
    """
    This method creates a selenium web driver
    :return: A webdriver object
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--enable-javascript")
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")
    wd = webdriver.Chrome("./Utilities/chromedriver", options=options)
    timeout = 30
    #wd.implicitly_wait(timeout)
    return wd

def waitForLoad(url, driver, locator, BySelector = By.TAG_NAME, timeout = 0):
    print("Waiting on: %s" %url)
    try:
        # Wait as long as required, or maximum of 5 sec for element to appear
        # If successful, retrieves the element
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((BySelector, locator)))
    except TimeoutException:
        print("Failed to load at %s" % url)
    print("Finished waiting for: %s" % url)