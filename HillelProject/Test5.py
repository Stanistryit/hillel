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
#Sign in button
SignIn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class$='signin']")))
SignIn.click()
#Frogot pass
fpass = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Forgot password')]")))
fpass.click()
time.sleep(2) # Без него находит кнопку Log in
elem = WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h4[class^='modal-title']"))).text
# print(elem)
# assert form name

assert elem == 'Restore access'

# assert "Restore access" in driver.page_source

driver.close()
