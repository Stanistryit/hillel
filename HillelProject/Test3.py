from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("incognito")
options.add_argument("headless")
# START DRIVER
# driver = webdriver.Chrome('/home/dima/Завантаження/Hillel/chromedriver', options=options)
driver = webdriver.Chrome(service=Service('F:\\Hillel_Cours\\work\\chromedriver'), options=options)
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
user = "guest"
password = "welcome2qauto"
driver.get("https://"+user+":"+password+"@"+"qauto2.forstudy.space/")

# Login in

SignIn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class$='signin']")))
SignIn.click()
email = driver.find_element(By.CSS_SELECTOR, "input[id$='Email']")
email.send_keys("testmailgroup1@yopmail.com")
password = driver.find_element(By.CSS_SELECTOR, "input[id$='Password']")
password.send_keys("Test_group1")
remember = driver.find_element(By.CSS_SELECTOR, "input[id^='rem']")
remember.click()
loginIn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class^='btn btn-p']")))
loginIn.click()
elem = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add car')]")))

# assert login in
import re
assert re.match(r'Add car', elem.text)
# assert elem.text == 'Add car'

# assert "My profile" in driver.page_source

driver.close()
