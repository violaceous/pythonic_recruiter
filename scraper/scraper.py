from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sqlite3

def _get_browser():
    profile = webdriver.FirefoxProfile()
    profile.set_preference(
        "general.useragent.override",
        "Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0"
    )
    browser = webdriver.Firefox(profile)
    return browser
    
################################################################################

def _open_craigslist(link):
    browser = _get_browser()
    browser.implicitly_wait(3)
    browser.get(link)
    elements = browser.find_elements_by_css_selector('.hdrlnk')
    browser.quit()
    return len(elements)

    
