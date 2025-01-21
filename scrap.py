import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time

def scrap_Site(website):
    print('Launching chrome browser')
    
    chrome_driver_path="chromedriver-linux64/chromedriver"
    options = webdriver.ChromeOptions()
    driver=webdriver.Chrome(service=Service(chrome_driver_path),options=options)
    
    try:
        driver.get(website)
        print('page loading')
        html = driver.page_source
        time.sleep(5)
        
        return html
    finally:
        driver.quit()
        
    