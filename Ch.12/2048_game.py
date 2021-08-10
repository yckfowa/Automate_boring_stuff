from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('<Enter you own path for webdriver')
driver.get("https://gabrielecirulli.github.io/2048/")

html_elem = driver.find_element_by_tag_name('html') # best way to send keys
game_over = driver.find_element_by_class_name("game-message")

while game_over.text == '':
    html_elem.send_keys(Keys.UP)
    time.sleep(2)
    html_elem.send_keys(Keys.RIGHT)
    html_elem.send_keys(Keys.DOWN)
    time.sleep(3)
    html_elem.send_keys(Keys.LEFT)

Score = driver.find_element_by_class_name('score-container')

print(f"Your Score: {Score.text}")

print('GAME OVER!!!')