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

# assert title
time.sleep(2)  # sleep for 2 sec
assert "Hillel Qauto" in driver.title

driver.close()
