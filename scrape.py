from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import os
import time
import ssl

def initialize():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.maximize_window()
        count=0
        for i in range(1, searchPage + 1):
            url = your_url + "&page=" + str(i)
            driver.get(url)
            data = driver.execute_script("return document.documentElement.outerHTML")
            print("Page " + str(i))

            scraper = BeautifulSoup(data, "lxml")

            img_container = scraper.find_all("img", {"class":"z_g_a z_g_b"})

            for j in range(0, len(img_container)-1):
                img_src = img_container[j].get("src")
                name = img_src.rsplit("/", 1)[-1]
                try:
                    urlretrieve(img_src, os.path.join(scrape_directory, os.path.basename(img_src)))
                    print("Scraped " + name)
                    count+=1
                except Exception as e:
                    print(e)
        driver.close()
    except Exception as e:
        print(e)

os.makedirs("images")
scrape_directory = "./images"
## Enter your url in this string
your_url = "https://www.shutterstock.com/search/indian+face?number_of_people=1&mreleased=true&image_type=photo"
#Number of pages
searchPage = 30
initialize()
print("Scraping complete.")
print("Images scraped=", count)
