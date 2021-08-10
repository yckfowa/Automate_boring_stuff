from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import os
import wget
import time

keyword = input("Please enter the keyword you want to search: ")

driver = webdriver.Chrome('<Enter the path for your webdriver>')
driver.get("https://imgur.com") #imgur as example 

search_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[1]/div/div[1]/div[2]/div[4]/div/form/input")))
time.sleep(5)
search_field.send_keys(keyword + "\n")  #press enter immediate after input

# decide how many pages to scrape 
n_scrolls = 2
for i in range(1, n_scrolls):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

images = driver.find_elements_by_tag_name('img')
images = [image.get_attribute('src') for image in images]
print(f"Number of scraped images: {len(images)}")

path = os.getcwd()
path = os.path.join(path,  "imgur_photos")

os.mkdir(path)

counter = 0
for image in images:
    save_as = os.path.join(path, str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1

print("Process completed...")

driver.close()


