print("PROGRAM STARTED")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(
    ChromeDriverManager().install(),
    log_path=os.devnull   # 🔥 THIS suppresses GetHandleVerifier
)

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.google.com")

time.sleep(5)
driver.quit()