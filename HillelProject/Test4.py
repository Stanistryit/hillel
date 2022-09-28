from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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
