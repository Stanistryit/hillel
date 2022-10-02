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
SignIn = driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[2]/button[2]")
SignIn.click()
fpass = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-signin-modal/div[2]/app-signin-form/form/div[3]/button")
fpass.click()

# assert form name
time.sleep(2)  # sleep for 2 sec
assert "Restore access" in driver.page_source

driver.close()
