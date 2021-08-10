from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import getpass

def main():

    recipient = input("Please enter the recipient's email address : ")
    subject = input("Enter the subject of the email: ")
    content = input("Please enter the content of the email")
    password1 = getpass.getpass(prompt= "Please Enter your password ")

    driver = webdriver.Chrome("<Enter the path of your webdriver>") #Enter your own path 
    driver.get("https://login.live.com") #outlook as example 

    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='loginfmt']")))
    username.clear()
    username.send_keys("<Enter your email address>") #Enter your own email adddress

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='idSIButton9']"))).click()

    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='passwd']")))
    password.clear()
    password.send_keys(password1) 
    
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='idSIButton9']"))).click()

    # bypass the stay signed in page
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='KmsiCheckboxField']"))).click()
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='idBtn_Back']"))).click()

    # click the nav-bar and click to access outlook
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "O365_MainLink_NavMenu"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "O365_AppTile_Mail"))).click()

    # redirect to compose
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "id__7"))).click()

    recipient_field = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CLASS_NAME, "ms-BasePicker-input")))
    recipient_field.send_keys(recipient)

    new_subject_field = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "ms-TextField-field")))
    new_subject_field.send_keys(subject)

    content_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ReadingPaneContainerId']/div/div/div/div[1]/div[2]/div[1]")))
    content_field.send_keys(content)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ReadingPaneContainerId']/div/div/div/div[1]/div[3]/div[2]/div[1]/div/span/button[1]"))).click()

    driver.close()

    print("Email sent!")
    

if __name__ == '__main__':
    main()