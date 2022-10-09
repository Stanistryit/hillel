from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time

# START DRIVER
# driver = webdriver.Chrome('/home/dima/Завантаження/Hillel/geckodriver')
driver = webdriver.Firefox(service=Service('F:\\Hillel_Cours\\work\\geckodriver.exe'))
user = "guest"
password = "welcome2qauto"
driver.get("https://"+user+":"+password+"@"+"qauto2.forstudy.space/")
SignIn = driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[2]/button[2]")
SignIn.click()
element = driver.find_element(By.CLASS_NAME, 'modal-title')
# assert form name
time.sleep(2)  # sleep for 2 sec
assert element.text == 'Log in'

driver.close()
