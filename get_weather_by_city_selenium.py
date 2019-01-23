from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium_headless_driver import get_headless_driver
import requests
import xmltodict

def get_url_for_city(city):
	# search for city
	#  load driver (without headless)
	# chromedriver = path of chrome driver
	# browser = webdriver.Chrome(chromedriver)
	browser = get_headless_driver()
	# call for url
	base_url = "http://www.bbc.com/weather"
	browser.get(base_url)

	try:
		browser.find_element_by_id('ls-c-search__input-label').send_keys(city)
		fastrack = WebDriverWait(browser, 10).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='location-list']/li[1]/a")))
		fastrack.click()
		return browser.current_url
	except Exception as e:
		print ("exception ", e)
	finally:
		browser.close()