from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(service=Service('F:\\Hillel_Cours\\work\\geckodriver.exe'))
driver.get('https://mail.163.com/')