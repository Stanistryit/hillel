from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time

# START DRIVER
# driver = webdriver.Firefox('/home/dima/Завантаження/Hillel/geckodriver')
driver = webdriver.Firefox(service=Service('F:\\Hillel_Cours\\work\\geckodriver.exe'))
user = "guest"
password = "welcome2qauto"
driver.get("https://"+user+":"+password+"@"+"qauto2.forstudy.space/")
# LOGIN
signIn = driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[2]/button[2]")
signIn.click()
email = driver.find_element(By.ID, "signinEmail")
email.send_keys("testmailgroup1@yopmail.com")
password = driver.find_element(By.ID, "signinPassword")
password.send_keys("Test_group")
remember = driver.find_element(By.ID, "remember")
remember.click()
loginIn = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-signin-modal/div[3]/button[2]")
loginIn.click()

# assert alert "Wrong email or password"
time.sleep(2)  # sleep for 2 sec
assert "Wrong email or password" in driver.page_source

driver.close()
