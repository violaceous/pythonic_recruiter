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

def _open_craigslist(link):
    browser = _get_browser()
    browser.implicitly_wait(3)
    browser.get(link)
    elements = browser.find_elements_by_css_selector('.i')
    links = []
    for element in elements:
        links.append(element.get_attribute('href'))
    browser.quit()
    return links

def _get_craigslist_contact_details(link):
    browser = _get_browser()
    browser.get(link)
    results = {}
    results['address'] = browser.find_element_by_css_selector('.anonemail').text
    return results

def _get_craigslist_post(link):
    browser = _get_browser()
    browser.get(link)
    details = {}
    details['link'] = link
    details['title'] = browser.title
    location = browser.find_element_by_css_selector('.postingtitle').text
    details['location'] = location[location.rfind('(') + 1 : location.rfind(')')]
    compensation = browser.find_element_by_css_selector('.bigattr').text
    details['compensation'] = compensation[compensation.find(':') + 2:]
    details['contact_link'] = browser.find_element_by_css_selector('#replylink').get_attribute('href')
    browser.quit()
    return details
    

    
