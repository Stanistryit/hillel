from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
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

# assert title
time.sleep(2)  # sleep for 2 sec
assert "Hillel Qauto" in driver.title

driver.close()
