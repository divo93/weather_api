from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = "./chromedriver"

WINDOW_SIZE = "1920,1080"

def get_headless_driver():
	chrome_options = Options()  
	chrome_options.add_argument("--headless")  
	chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
	chrome_options.binary_location = CHROME_PATH

	driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
	                          chrome_options=chrome_options
	                         )  
	driver.get("https://www.google.com")
	return driver
