from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("incognito")
# START DRIVER
# driver = webdriver.Chrome('/home/dima/Завантаження/Hillel/chromedriver', options=options)
driver = webdriver.Chrome(service=Service('F:\\Hillel_Cours\\work\\chromedriver'), options=options)
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
user = "guest"
password = "welcome2qauto"
driver.get("https://"+user+":"+password+"@"+"qauto2.forstudy.space/")

# LOGIN

SignIn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-outline-white header_signin']")))
SignIn.click()
email = driver.find_element(By.XPATH, "//input[@id='signinEmail']")
email.send_keys("testmailgroup1@yopmail.com")
password = driver.find_element(By.XPATH, "//input[@id='signinPassword']")
password.send_keys("Test_group")
remember = driver.find_element(By.XPATH, "//input[@id='remember']")
remember.click()
loginIn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]")))
loginIn.click()
elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Wrong email or password')]")))

# assert alert "Wrong email or password"

assert elem.text == 'Wrong email or password'

# assert "Wrong email or password" in driver.page_source

driver.close()
